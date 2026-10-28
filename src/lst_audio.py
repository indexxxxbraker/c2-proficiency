# lst_audio.py · Motor de audio del Listening · v1
# Proyecto C2 Proficiency. Lo usan gen_LST-P1.py, gen_LST-P2.py, los generadores de las Parts 3 y 4 y los
# simulacros (SIM). No depende de c2_plantilla.py.
#
# QUE HACE
#   - Sintetiza voz con edge-tts (voces neuronales en-GB, en-IE, en-AU, en-NZ, en-US) y guarda cada fragmento
#     en una cache, de modo que regenerar una hoja no vuelve a llamar al servicio si el texto no cambia.
#   - Ajusta la velocidad de cada voz hasta las palabras por minuto pedidas (la velocidad por defecto cambia
#     mucho de una voz a otra) y la mide despues de recortar los silencios.
#   - Monta el MP3 con el guion del examen: narrador, rubricas, tonos, tiempos de lectura y pausas; cada
#     grabacion suena dos veces y la repeticion es identica a la primera audicion.
#   - Verifica el audio con reconocimiento de voz (faster-whisper): transcribe cada grabacion y comprueba que
#     se parece al texto y que se reconocen las frases que dan las respuestas (y, en la Part 2, las claves).
#
# NOTAS TECNICAS (contenedor de claude.ai)
#   - setup() instala edge-tts y faster-whisper con pip (--break-system-packages) y anade el certificado del
#     proxy (/etc/ssl/certs/ca-certificates.crt) al bundle de certifi, que el proxy intercepta SSL.
#   - ffmpeg siempre con -nostdin.
#
# USO DESDE UN GENERADOR
#   import lst_audio as A
#   A.setup()
#   ev = A.script_part1(extracts)            # o A.script_part(...) para las Parts 2, 3 y 4
#   rep = A.render(ev, "/mnt/user-data/outputs/LST-P1_Practica_01.mp3")
#   chk = A.check_recording(rep["recs"]["E1"]["wav"], texto, frases)
#
# EVENTOS DEL GUION (listas de diccionarios; se pueden concatenar para un simulacro completo)
#   say(texto)                        el narrador lee una linea
#   pause(segundos)                   silencio
#   tone()                            el tono que abre cada audicion
#   rec(id, turns, wpm, label)        una grabacion; turns = [(voz, texto), ("_pause", segundos), ...]
#                                     la misma id repetida reutiliza el mismo audio (segunda audicion)
#   mark(etiqueta)                    marca en la linea de tiempo (no suena)

import asyncio
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys

VERSION = "1"
SR = 24000
CACHE = os.environ.get("LST_CACHE", "/home/claude/lst_cache")

VOICES = {  # id: (voz de edge-tts, variedad, sexo)
    "Thomas": ("en-GB-ThomasNeural", "en-GB", "M"),     # narrador
    "Ryan": ("en-GB-RyanNeural", "en-GB", "M"),
    "Sonia": ("en-GB-SoniaNeural", "en-GB", "F"),
    "Libby": ("en-GB-LibbyNeural", "en-GB", "F"),
    "Connor": ("en-IE-ConnorNeural", "en-IE", "M"),
    "Emily": ("en-IE-EmilyNeural", "en-IE", "F"),
    "William": ("en-AU-WilliamMultilingualNeural", "en-AU", "M"),
    "Natasha": ("en-AU-NatashaNeural", "en-AU", "F"),
    "Mitchell": ("en-NZ-MitchellNeural", "en-NZ", "M"),
    "Molly": ("en-NZ-MollyNeural", "en-NZ", "F"),
    "Andrew": ("en-US-AndrewNeural", "en-US", "M"),
    "Brian": ("en-US-BrianNeural", "en-US", "M"),
    "Emma": ("en-US-EmmaNeural", "en-US", "F"),
    "Ava": ("en-US-AvaNeural", "en-US", "F"),
}
NARRATOR = "Thomas"
ACCENTS = {"en-GB": "británico", "en-IE": "irlandés", "en-AU": "australiano", "en-NZ": "neozelandés",
           "en-US": "norteamericano"}
NARRATOR_WPM = 150
TURN_GAP = 0.4          # silencio entre turnos de un dialogo
WPM_TOL = 0.04          # tolerancia del ajuste de velocidad
ASR_MODEL = "small.en"  # base.en confunde palabras que la voz pronuncia bien ('sudden' -> 'southern')

NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
       "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
       "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six",
       "twenty-seven", "twenty-eight", "twenty-nine", "thirty"]
ORD = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}


# ---------- Entorno ----------
def setup(asr=True):
    """Instala lo necesario y anade el certificado del proxy a certifi (idempotente)."""
    pkgs = ["edge-tts"] + (["faster-whisper", "num2words"] if asr else [])
    for pkg, mod in zip(pkgs, [p.replace("-", "_") for p in pkgs]):
        try:
            __import__(mod)
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", pkg, "--break-system-packages", "-q"],
                           check=True)
    import certifi
    ca, sys_ca, marker = certifi.where(), "/etc/ssl/certs/ca-certificates.crt", "# LST_PROXY_CA"
    if os.path.exists(sys_ca) and marker not in open(ca).read():
        with open(ca, "a") as f:
            f.write("\n" + marker + "\n" + open(sys_ca).read())
    os.makedirs(CACHE, exist_ok=True)


def _ff(*args):
    subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", *args], check=True)


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def count_words(text):
    return len(re.findall(r"[A-Za-z0-9]+(?:[’'\-.][A-Za-z0-9]+)*", text))


# ---------- Eventos ----------
def say(text):
    return {"t": "say", "text": text}


def pause(s):
    return {"t": "pause", "s": float(s)}


def tone():
    return {"t": "tone"}


def rec(rec_id, turns, wpm, label=""):
    return {"t": "rec", "id": rec_id, "turns": turns, "wpm": wpm, "label": label}


def mark(label):
    return {"t": "mark", "label": label}


# ---------- Sintesis ----------
def _key(*parts):
    return hashlib.sha1("|".join(str(p) for p in parts).encode()).hexdigest()[:16]


async def _synth_async(jobs):
    import edge_tts
    sem = asyncio.Semaphore(4)

    async def one(text, voice, rate, out):
        async with sem:
            for attempt in range(5):
                try:
                    await edge_tts.Communicate(text, VOICES[voice][0], rate=f"{rate:+d}%").save(out)
                    if os.path.getsize(out) > 1000:
                        return
                except Exception:
                    if attempt == 4:
                        raise
                await asyncio.sleep(2 * (attempt + 1))
            raise RuntimeError(f"edge-tts no devolvio audio para: {text[:40]}")

    await asyncio.gather(*(one(*j) for j in jobs))


def synth(items):
    """items: [(texto, voz, rate)] -> [wav]. Cada wav esta recortado (sin silencio al principio ni al final),
    normalizado en sonoridad y a 24 kHz mono. Usa la cache."""
    todo, outs = [], []
    for text, voice, rate in items:
        k = _key(VOICES[voice][0], rate, text)
        mp3, wav = os.path.join(CACHE, k + ".mp3"), os.path.join(CACHE, k + ".wav")
        outs.append(wav)
        if not os.path.exists(wav) and not os.path.exists(mp3):
            todo.append((text, voice, rate, mp3))
    if todo:
        asyncio.run(_synth_async(todo))
    trim = ("silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
            "silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
            "loudnorm=I=-19:TP=-2:LRA=11")
    for (text, voice, rate), wav in zip(items, outs):
        if not os.path.exists(wav):
            _ff("-i", wav[:-4] + ".mp3", "-af", trim, "-ar", str(SR), "-ac", "1", "-c:a", "pcm_s16le", wav)
    return outs


def calibrate(texts, voice, target_wpm):
    """Busca el rate de edge-tts que da target_wpm para estos textos (medido sin silencios exteriores).
    Devuelve (rate, wavs, wpm_medido)."""
    words = sum(count_words(t) for t in texts)
    rate = 0
    for _ in range(4):
        wavs = synth([(t, voice, rate) for t in texts])
        wpm = words / sum(duration(w) for w in wavs) * 60
        if abs(wpm / target_wpm - 1) <= WPM_TOL:
            break
        rate = max(-40, min(40, int(round((1 + rate / 100) * target_wpm / wpm * 100 - 100))))
    return rate, wavs, wpm


def _silence(sec):
    path = os.path.join(CACHE, f"sil_{sec:.3f}.wav")
    if not os.path.exists(path):
        _ff("-f", "lavfi", "-i", f"anullsrc=r={SR}:cl=mono", "-t", f"{sec:.3f}", "-c:a", "pcm_s16le", path)
    return path


def _tone():
    path = os.path.join(CACHE, "tone_v2.wav")
    if not os.path.exists(path):
        _ff("-f", "lavfi", "-i", f"sine=frequency=880:sample_rate={SR}:duration=0.6",
            "-f", "lavfi", "-i", f"sine=frequency=1320:sample_rate={SR}:duration=0.6",
            "-filter_complex", "[0][1]amix=inputs=2:weights=1 0.35,volume=3.2,"
                               "afade=t=in:d=0.02,afade=t=out:st=0.35:d=0.25",
            "-ac", "1", "-c:a", "pcm_s16le", path)
    return path


def _concat(wavs, out):
    lst = out + ".txt"
    with open(lst, "w") as f:
        for w in wavs:
            f.write(f"file '{w}'\n")
    if out.endswith(".mp3"):
        _ff("-f", "concat", "-safe", "0", "-i", lst, "-ar", str(SR), "-ac", "1", "-c:a", "libmp3lame",
            "-b:a", "64k", out)
    else:
        _ff("-f", "concat", "-safe", "0", "-i", lst, "-c:a", "pcm_s16le", out)
    os.remove(lst)


def build_recording(turns, wpm):
    """Grabacion completa (wav) a partir de los turnos. Cada voz se calibra una vez con todos sus turnos."""
    by_voice = {}
    for v, t in turns:
        if v != "_pause":
            by_voice.setdefault(v, []).append(t)
    rates, measured, wav_of = {}, {}, {}
    for v, texts in by_voice.items():
        rate, wavs, got = calibrate(texts, v, wpm)
        rates[v], measured[v] = rate, round(got)
        for t, w in zip(texts, wavs):
            wav_of[(v, t)] = w
    pieces, speech = [], 0.0
    for i, (v, t) in enumerate(turns):
        if v == "_pause":
            pieces.append(_silence(float(t)))
            continue
        if pieces and turns[i - 1][0] != "_pause":
            pieces.append(_silence(TURN_GAP))
        pieces.append(wav_of[(v, t)])
        speech += duration(wav_of[(v, t)])
    out = os.path.join(CACHE, "rec_" + _key(wpm, json.dumps(turns)) + ".wav")
    if not os.path.exists(out):
        _concat(pieces, out)
    words = sum(count_words(t) for v, t in turns if v != "_pause")
    total = duration(out)
    return {"wav": out, "words": words, "speech_s": round(speech, 1), "total_s": round(total, 1),
            "wpm_speech": round(words / speech * 60), "wpm_total": round(words / total * 60),
            "rates": rates, "wpm_by_voice": measured, "voices": sorted(by_voice)}


def render(events, out_mp3):
    """Monta el MP3. Devuelve un informe: duracion, linea de tiempo y datos de cada grabacion."""
    narr_lines = [e["text"] for e in events if e["t"] == "say"]
    narr_rate = calibrate(narr_lines, NARRATOR, NARRATOR_WPM)[0] if narr_lines else 0
    narr_wav = dict(zip(narr_lines, synth([(t, NARRATOR, narr_rate) for t in narr_lines])))
    recs, pieces, timeline, t0 = {}, [], [], 0.0
    for e in events:
        if e["t"] == "mark":
            timeline.append((round(t0, 1), "mark", e["label"]))
            continue
        if e["t"] == "say":
            w, kind, lab = narr_wav[e["text"]], "say", e["text"][:60]
        elif e["t"] == "pause":
            w, kind, lab = _silence(e["s"]), "pause", f"{e['s']:g} s"
        elif e["t"] == "tone":
            w, kind, lab = _tone(), "tone", ""
        else:
            if e["id"] not in recs:
                recs[e["id"]] = build_recording(e["turns"], e["wpm"])
                recs[e["id"]]["label"] = e.get("label", "")
            w, kind, lab = recs[e["id"]]["wav"], "rec", e["id"]
        d = duration(w)
        timeline.append((round(t0, 1), kind, lab))
        pieces.append(w)
        t0 += d
    os.makedirs(os.path.dirname(os.path.abspath(out_mp3)), exist_ok=True)
    _concat(pieces, out_mp3)
    return {"mp3": out_mp3, "duration_s": round(duration(out_mp3), 1), "timeline": timeline, "recs": recs,
            "narrator_rate": narr_rate}


# ---------- Guiones del examen ----------
def n2w(n):
    return NUM[n] if 0 <= n < len(NUM) else str(n)


def opening(title):
    """Identificacion de la pista al principio del MP3 de una hoja suelta."""
    return [say(title), pause(2)]


def script_part1(extracts, first=1, part=1):
    """Part 1. extracts: [{'ctx': 'You hear …', 'turns': [(voz, texto), …], 'wpm': 160, 'id': 'E1'}] (tres).
    Guion: rubrica; por extracto, 15 s de lectura, tono, extracto, 2 s, tono, repeticion, 5 s."""
    a, b = first, first + 2 * len(extracts) - 1
    ev = [mark(f"Part {part}"), say(f"Now open your question paper and look at Part {ORD[part]}."), pause(5),
          say(f"You will hear three different extracts. For questions {n2w(a)} to {n2w(b)}, choose the answer "
              "(A, B or C) which fits best according to what you hear. There are two questions for each "
              "extract.")]
    ev.append(pause(2))
    for i, ex in enumerate(extracts):
        q = first + 2 * i
        rid = ex.get("id", f"P{part}E{i + 1}")
        ev += [mark(f"Extract {i + 1}"),
               say(f"Extract {ORD[i + 1]}. {ex['ctx']} Now look at questions {n2w(q)} and {n2w(q + 1)}."),
               pause(15), tone(), rec(rid, ex["turns"], ex["wpm"], f"Extract {i + 1}"), pause(2), tone(),
               rec(rid, ex["turns"], ex["wpm"], f"Extract {i + 1}"), pause(5)]
    ev += [say(f"That is the end of Part {ORD[part]}.")]
    return ev


def script_part(part, rubric, reading_s, turns, wpm, rec_id=None, extra_lines=()):
    """Parts 2, 3 y 4: rubrica, tiempo de lectura, tono, grabacion, 5 s, 'Now you will hear Part X again.',
    tono, repeticion, 5 s, 'That is the end of Part X.'
    rubric: lineas del narrador antes del tiempo de lectura (sin la de 'You now have…').
    reading_s: 45 o 60. turns: [(voz, texto) | ('_pause', s)]."""
    rid = rec_id or f"P{part}"
    reading = "1 minute" if reading_s == 60 else f"{n2w(reading_s) if reading_s <= 30 else 'forty-five'} seconds"
    ev = [mark(f"Part {part}"), say(f"Now turn to Part {ORD[part]}.")]
    ev += [say(line) for line in rubric] + [say(line) for line in extra_lines]
    ev += [say(f"You now have {reading} in which to look at Part {ORD[part]}."), pause(reading_s), tone(),
           rec(rid, turns, wpm, f"Part {part}"), pause(5), say(f"Now you will hear Part {ORD[part]} again."),
           tone(), rec(rid, turns, wpm, f"Part {part}"), pause(5), say(f"That is the end of Part {ORD[part]}.")]
    return ev


def script_transfer(paper=True):
    """Final de un simulacro: 5 minutos para pasar respuestas (papel) o 2 para revisar (digital)."""
    if paper:
        return [say("There will now be a pause of five minutes for you to copy your answers onto the separate "
                    "answer sheet. Be sure to follow the numbering of all the questions. I shall remind you "
                    "when there is one minute left, so that you are sure to finish in time."), pause(240),
                say("You have one more minute left."), pause(60), say("That is the end of the test.")]
    return [say("You now have two minutes to check your answers."), pause(120), say("That is the end of the test.")]


# ---------- Verificacion con reconocimiento de voz ----------
_MODEL = None


def _asr_model():
    global _MODEL
    if _MODEL is None:
        from faster_whisper import WhisperModel
        _MODEL = WhisperModel(ASR_MODEL, device="cpu", compute_type="int8")
    return _MODEL


def transcribe(wav):
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", wav, "-ar", "16000", "-ac", "1",
                          "-f", "s16le", "-"], capture_output=True, check=True).stdout
    audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768
    segs, _ = _asr_model().transcribe(audio, language="en", beam_size=5)
    return " ".join(s.text.strip() for s in segs)


_US_GB = {"color": "colour", "favorite": "favourite", "center": "centre", "theater": "theatre",
          "realize": "realise", "organize": "organise", "recognize": "recognise", "apologize": "apologise",
          "gray": "grey", "traveled": "travelled", "airplane": "aeroplane", "program": "programme",
          "practicing": "practising", "analyze": "analyse", "behavior": "behaviour", "neighbor": "neighbour",
          "humor": "humour", "honor": "honour", "labor": "labour", "meter": "metre", "meters": "metres",
          "centimeters": "centimetres", "kilometers": "kilometres", "defense": "defence", "license": "licence",
          "catalog": "catalogue", "catalogs": "catalogues", "dialog": "dialogue", "jewelry": "jewellery", "mold": "mould",
          "skeptical": "sceptical", "fiber": "fibre", "aluminum": "aluminium", "anesthetic": "anaesthetic",
          "cozy": "cosy", "coziness": "cosiness", "criticize": "criticise", "emphasize": "emphasise",
          "civilization": "civilisation", "pediatric": "paediatric", "maneuver": "manoeuvre",
          "plow": "plough"}


def norm_words(s):
    from num2words import num2words
    import unicodedata
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
    s = s.lower().replace("’", "'").replace("‘", "'")
    s = re.sub(r"(\d),(\d{3})", r"\1\2", s)
    s = re.sub(r"(\d+)%", r"\1 percent", s)

    def _year(m):  # 1937 -> nineteen thirty-seven; 1990s -> nineteen nineties
        y = num2words(int(m.group(1)), to="year")
        if m.group(2):
            y = y[:-1] + "ies" if y.endswith("y") else y + "s"
        return " " + y + " "
    s = re.sub(r"\b(1[1-9]\d\d|20\d\d)('?s)?\b", _year, s)
    s = re.sub(r"\d+(?:\.\d+)?", lambda m: " " + num2words(float(m.group()) if "." in m.group()
                                                             else int(m.group())) + " ", s)
    s = re.sub(r"[-–—/]", " ", s)
    for c, full in (("n't", " not"), ("'re", " are"), ("'ve", " have"), ("'ll", " will"), ("'m", " am")):
        s = s.replace(c, full)
    s = s.replace("ca not", "can not").replace("wo not", "will not")
    s = re.sub(r"[^a-z' ]", " ", s)
    words = [w.strip("'") for w in s.split()]
    return [_US_GB.get(w, w) for w in words if w and w != "and"]  # 'and' se omite: num2words lo mete o no


def phrase_score(phrase, hyp_words):
    """Mejor parecido (0-1) entre la frase y cualquier ventana de la transcripcion automatica."""
    p = norm_words(phrase)
    if not p:
        return 1.0
    best, n = 0.0, len(p)
    for size in range(max(1, n - 2), n + 3):
        for i in range(0, max(1, len(hyp_words) - size + 1)):
            r = difflib.SequenceMatcher(None, p, hyp_words[i:i + size]).ratio()
            best = max(best, r)
    return best


def check_recording(wav, text, phrases=(), exact=(), min_sim=0.88, min_phrase=0.85):
    """Transcribe la grabacion y la compara con el texto.
    phrases: frases que deben reconocerse (parecido >= min_phrase); exact: palabras que deben aparecer tal cual
    (claves de la Part 2). Devuelve un diccionario con 'ok' y los detalles."""
    hyp = transcribe(wav)
    hw, rw = norm_words(hyp), norm_words(text)
    sim = difflib.SequenceMatcher(None, rw, hw).ratio()
    ph = [(f, round(phrase_score(f, hw), 2)) for f in phrases]
    joined = " " + " ".join(hw) + " "
    ex = [(w, (" " + " ".join(norm_words(w)) + " ") in joined) for w in exact]
    ok = sim >= min_sim and all(s >= min_phrase for _, s in ph) and all(x for _, x in ex)
    return {"ok": ok, "sim": round(sim, 3), "phrases": ph, "exact": ex, "asr": hyp}


if __name__ == "__main__":
    if "--test" in sys.argv:
        setup()
        ev = opening("Audio engine test.") + [tone(), rec("T", [("Ryan", "Did you catch the final episode?"),
                                                                 ("Libby", "I did, and I'm still thinking about it.")],
                                                          160)]
        r = render(ev, "/home/claude/lst_test.mp3")
        print(json.dumps({k: v for k, v in r.items() if k != "timeline"}, indent=1, default=str))
        print(check_recording(r["recs"]["T"]["wav"], "Did you catch the final episode? I did, and I'm still "
                              "thinking about it."))
