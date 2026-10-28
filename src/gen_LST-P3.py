# gen_LST-P3.py · Generador de Listening Part 3 (entrevista o conversacion, opcion multiple de 4) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py y lst_audio.py en la misma carpeta (no modifica ninguno).
#
# QUE HACE
#   - Hoja de practica completa en PDF: preguntas 16-20, hoja de respuestas y soluciones (transcripcion con la
#     frase que da cada respuesta resaltada, por que es correcta la clave y por que falla cada distractor).
#   - MP3 con el mismo nombre: guion del examen (rubrica, 1 minuto de lectura, tono, entrevista, 5 s, 'Now you will
#     hear Part Three again', tono, repeticion, 5 s, fin), una voz neuronal distinta por hablante.
#   - Bloques sueltos para un simulacro (SIM): preguntas, hoja de respuestas, soluciones y eventos de audio.
#   - Verificacion automatica del contenido, del PDF y del audio (velocidad, reconocimiento de voz por tercios y
#     lista de diferencias entre el texto y lo que reconoce el ASR, para reformular lo que la voz deforma).
#
# USO
#   python3 gen_LST-P3.py --demo [carpeta_salida]          -> hoja de ejemplo (contenido de la 01, como 99)
#   python3 gen_LST-P3.py mis_hojas.py [carpeta_salida]    -> mis_hojas.py define SPECS = [spec, ...]
#   Opciones: --no-audio · --no-asr
#   Por etapas (claude.ai corta cada comando a los 5 minutos; la sintesis queda en la cache):
#   python3 gen_LST-P3.py mis_hojas.py salida --num 03 --stage pdf | audio | asr1 | asr2 | asr3
#   (asr1-asr3 comprueban cada uno un tercio de la grabacion, cortado por turnos)
#   Desde otro script: importlib (ver gen_LST-P1.py); verify(spec), make(spec, carpeta), question_flowables(spec),
#   answer_sheet_flowables(spec), solutions_flowables(spec), audio_events(spec, standalone=False).
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num, subtitle, difficulty (1-4), wpm (160 en la 01 … 185 en la 04), lex (para LEX; no se imprime)
#   ctx         rubrica tal como la lee el narrador: "You will hear part of an interview in which …"
#   speakers    {"Interviewer": "Ryan", "Clara": "Sonia"}   etiqueta -> voz de lst_audio.VOICES (no el narrador)
#   host        (opcional) etiqueta del presentador; sus turnos no cuentan como opinion en las preguntas de acuerdo
#   turns       [("Interviewer", "texto"), …]   cada turno es un fragmento de audio
#   items       5 diccionarios (16-20):
#     n           16
#     type        uno de TYPES ("Global" solo en la ultima pregunta)
#     stem        enunciado (ingles); puede ser una frase incompleta que completan las opciones
#     options     [A, B, C, D] (ingles)
#     key         "C"
#     speaker     (opcional) etiqueta o lista de etiquetas: la evidencia debe estar en sus turnos (§7.3)
#     evidence    ["frase literal", …]  dentro de un solo turno cada una; se resalta en la transcripcion
#     why         por que es correcta la clave; al menos una cita {{…}} literal
#     theory      secciones de LST_Teoria_v1 (ver THEORY)
#     distractors {"A": {"kinds": ["4.2"], "why": "… {{cita}} …"}, …}   los tres que no son la clave
#   Marcado en textos en espanol: {{cita literal}} · [[ingles sin comprobar]] · [[!ingles en negrita]]
#
# QUE COMPRUEBA verify()
#   cinco preguntas 16-20 · rubrica · 2-3 hablantes con voces validas, distintas y que no son el narrador · 3-4 min
#   a la velocidad de la hoja · 4 opciones distintas · clave valida · tres distractores con su tipo (§4.x) y su
#   explicacion · frases-respuesta literales y dentro de un turno (del hablante indicado, si lo hay) · preguntas en
#   el orden del audio (salvo la global) · acuerdo con evidencia de dos hablantes que no son el presentador · citas
#   literales · ninguna letra es clave mas de 2 veces y se usan al menos 3 · la clave no es la opcion mas larga en
#   mas de 2 preguntas · secciones de teoria existentes · marcado sin resolver.
# QUE COMPRUEBA verify_audio()
#   velocidad real de la grabacion y de cada voz (±6 %) · duracion 3-4 min (con margen) · parecido texto-ASR de
#   cada tercio (>= 0,88) · cada frase-respuesta reconocida (>= 0,85) · imprime las diferencias palabra a palabra.
#
# A MANO
#   - Una sola respuesta defendible por pregunta; actitudes deducidas de una frase concreta, nunca de la entonacion.
#   - Revisar las diferencias del ASR: las que repiten una deformacion de la voz se reformulan en el texto.
#   - Ingles britanico, registro C2, dificultad graduada. Revisar el PDF renderizado y escuchar el MP3.

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
import lst_audio as A  # noqa: E402

VERSION = "1"
FIRST_ITEM = 16
N_ITEMS = 5
LETTERS = "ABCD"
WPM_TOL = 0.06
SEC_MIN, SEC_MAX = 180, 240
THEORY_DOC = "LST_Teoria_v1"
CODE = "LST-P3"

TYPES = ["Idea general", "Detalle", "Inferencia", "Función", "Propósito", "Sentimiento", "Actitud y opinión",
         "Acuerdo", "Global"]

THEORY = {
    "2.1": "Habla conectada", "2.2": "Acentos del examen", "2.3": "Señales del discurso oral", "2.4": "Matización",
    "3.1": "Lo que se dice y lo que se da a entender", "3.2": "Voz propia y voces ajenas",
    "3.3": "La segunda idea manda", "3.4": "Léxico de actitud en las opciones", "3.5": "Función y propósito",
    "3.6": "Acuerdo y desacuerdo entre hablantes", "4.1": "Eco léxico", "4.2": "Mencionado y descartado",
    "4.3": "Cierto, pero no responde", "4.4": "Voz equivocada", "4.5": "Grado y alcance",
    "4.6": "Relación lógica alterada", "4.7": "Expectativa frente a realidad", "4.8": "Plausible, pero ausente",
    "7.1": "Part 3: la tarea", "7.2": "Part 3: método", "7.3": "Seguir a dos voces", "7.4": "Part 3: caso resuelto",
    "9": "Rutina de autocorrección",
}
KINDS = {"4.1": "eco léxico", "4.2": "mencionado y descartado", "4.3": "no responde", "4.4": "voz equivocada",
         "4.5": "grado y alcance", "4.6": "lógica alterada", "4.7": "expectativa", "4.8": "ausente"}

CITE_RE = re.compile(r"\{\{(.+?)\}\}")


# ---------- Utilidades ----------
def E(s):
    return f'<font name="EN">{s}</font>'


def EB(s):
    return f'<font name="EN"><b>{s}</b></font>'


def markup(s):
    s = CITE_RE.sub(lambda m: E(m.group(1)), s)
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)


def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


def _text(spec):
    return _norm(" ".join(t for _, t in spec["turns"]))


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _speaker_list(it):
    sp = it.get("speaker")
    return [] if not sp else ([sp] if isinstance(sp, str) else list(sp))


def word_diff(ref, hyp):
    """Diferencias palabra a palabra entre el texto y el ASR (ya normalizados): ['ref → asr', …]."""
    import difflib
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes():
        if op != "equal":
            out.append(f"«{' '.join(ref[max(0, i1 - 1):i2 + 1])}» → «{' '.join(hyp[max(0, j1 - 1):j2 + 1])}»")
    return out


# ---------- Estilos propios (sobre la plantilla, sin cambiarla) ----------
_rub = ParagraphStyle("p3_rubric", parent=S["en"], fontSize=10, leading=14, spaceAfter=8)
_q = ParagraphStyle("p3_q", parent=S["en"], leftIndent=22, bulletIndent=0, bulletFontName="EN-B",
                    spaceBefore=8, spaceAfter=2.5)
_opt = ParagraphStyle("p3_opt", parent=S["en"], leftIndent=40, bulletIndent=22, bulletFontName="EN-B",
                      spaceAfter=1.5)
_ihead = ParagraphStyle("p3_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)
_sol = ParagraphStyle("p3_sol", parent=S["body"], leftIndent=14, spaceAfter=5)
_trs = ParagraphStyle("p3_trs", parent=S["cell_en"], fontName="EN-B", fontSize=9.4, leading=13.6, textColor=NAVY)
_tr = ParagraphStyle("p3_tr", parent=S["cell_en"], fontSize=10, leading=14)
_ctx = ParagraphStyle("p3_ctx", parent=S["en"], fontName="EN-I", textColor=INK, spaceAfter=3)


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def rubric_text(spec):
    a = _first(spec)
    return (f"{spec['ctx']} For questions {a}–{a + 4}, choose the answer (<b>A, B, C</b> or <b>D</b>) which fits "
            "best according to what you hear.")


def question_flowables(spec, with_title_block=False):
    a = _first(spec)
    out = []
    if with_title_block:
        out += title_block(f"{CODE} · Práctica {spec['num']}", "Interview or conversation", spec["subtitle"],
                           f"5 preguntas ({a}–{a + 4}) · 1 punto por pregunta · audio: {CODE}_Practica_{spec['num']}"
                           ".mp3 · la grabación suena dos veces, con las pausas del examen · sin consultar la teoría")
    out.append(Paragraph(rubric_text(spec), _rub))
    for it in spec["items"]:
        block = [Paragraph(it["stem"], _q, bulletText=str(it["n"]))]
        block += [Paragraph(o, _opt, bulletText=L) for L, o in zip(LETTERS, it["options"])]
        out.append(KeepTogether(block))
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    out = [h2(heading), p(
        "Marca una sola letra por pregunta. Al corregir, 1 punto por acierto; los errores no restan. En el examen "
        "en papel se responde en el cuadernillo y al final hay 5 minutos para pasar las respuestas a la hoja.")]
    rows = [["Nº", "A", "B", "C", "D", "Puntos"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), "A", "B", "C", "D", "&nbsp;&nbsp;&nbsp;&nbsp;/ 1"])
    rows.append(["", "", "", "", "<b>Total</b>", "&nbsp;&nbsp;&nbsp;&nbsp;<b>/ 5</b>"])
    out += table(rows, [20, 26, 26, 26, 30, 42], zebra=False, en_cols=(1, 2, 3, 4),
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 10), ("BOTTOMPADDING", (0, 1), (-1, -1), 10),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"), ("TEXTCOLOR", (1, 1), (4, -2), GREY)])
    return out


def _voices_line(spec):
    parts = [f"{lab}: {v}, inglés {A.ACCENTS[A.VOICES[v][1]]}" for lab, v in spec["speakers"].items()]
    return "Voces · " + " · ".join(parts)


def transcript_flowables(spec):
    marks = [(ev, it["n"]) for it in spec["items"] for ev in it["evidence"]]
    rows = []
    for lab, txt in spec["turns"]:
        for ev, n in marks:
            if ev in txt:
                txt = txt.replace(ev, f"<b>{ev}</b><super><font size=7 color='#A4243B'>&nbsp;{n}</font></super>", 1)
        rows.append([Paragraph(lab, _trs), Paragraph(txt, _tr)])
    t = Table(rows, colWidths=[24 * mm, CONTENT_W - 24 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_EJ), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("TOPPADDING", (0, 0), (-1, 0), 7), ("BOTTOMPADDING", (0, -1), (-1, -1), 7),
        ("LINEBEFORE", (0, 0), (0, -1), 1.8, GREY)]))
    return [t, Spacer(1, 6)]


def solutions_flowables(spec, with_band=True, heading=None):
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(
        "1 punto por acierto. Primero la clave rápida; después, la transcripción completa con la frase que da cada "
        "respuesta en negrita y el número de la pregunta; por último, por qué la clave es correcta y por qué falla "
        f"cada distractor, con su tipo (§4) y la cita que lo descarta. Los números de sección remiten a {THEORY_DOC}."))
    out.append(h2("Clave rápida") if not heading else h3("Clave rápida"))
    rows = [["Nº", "Clave", "Tipo de pregunta", "Distractores", "Teoría"]]
    for it in spec["items"]:
        dis = " · ".join(f"{L} §{'/'.join(it['distractors'][L]['kinds'])}" for L in LETTERS if L != it["key"])
        rows.append([str(it["n"]), f"<b>{it['key']}</b>", it["type"], dis, " · ".join("§" + s for s in it["theory"])])
    out += table(rows, [12, 14, 34, 70, 40])
    out += [h2("Transcripción") if not heading else h3("Transcripción"), Paragraph(spec["ctx"], _ctx),
            Paragraph(_voices_line(spec), S["small"])]
    out += transcript_flowables(spec)
    exp_head = h2("Explicaciones") if not heading else h3("Explicaciones")
    for i, it in enumerate(spec["items"]):
        block = [exp_head] if i == 0 else []      # el titulo nunca queda solo al pie de una pagina
        block += [Paragraph(f"{it['n']} · {it['key']} · {it['type']}", _ihead),
                 p(f"<b>Pregunta:</b> {E(it['stem'])}")]
        for L, opt in zip(LETTERS, it["options"]):
            if L == it["key"]:
                verdict, expl = "Correcta.", it["why"]
            else:
                d = it["distractors"][L]
                kinds = ", ".join(f"{KINDS[k]} §{k}" for k in d["kinds"])
                verdict, expl = f"Falla ({kinds}).", d["why"]
            block.append(Paragraph(f"<b>{L}</b>&nbsp;&nbsp;{E(opt)}<br/><b>{verdict}</b> {markup(expl)}", _sol))
        block.append(p("<b>Teoría:</b> " + " · ".join(f"§{s} {THEORY[s]}" for s in it["theory"])))
        out.append(KeepTogether(block + [Spacer(1, 4)]))
    return out


def build_sheet(spec, out_path):
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"{CODE} · Práctica {n}", f"{CODE}_Practica_{n}.pdf", title=f"{CODE} · Práctica {n}")
    return out_path


# ---------- Audio ----------
def _rec_id(spec):
    return f"{CODE}-{spec['num']}"


def audio_turns(spec):
    return [(spec["speakers"][lab], txt) for lab, txt in spec["turns"]]


def audio_events(spec, standalone=True):
    a = _first(spec)
    rubric = [f"{spec['ctx']} For questions {A.n2w(a)} to {A.n2w(a + 4)}, choose the answer (A, B, C or D) which "
              "fits best according to what you hear."]
    ev = A.opening(f"Proficiency Listening. Part Three practice, number {A.n2w(int(spec['num']))}.") \
        if standalone else []
    return ev + A.script_part(3, rubric, 60, audio_turns(spec), spec["wpm"], rec_id=_rec_id(spec))


def build_audio(spec, out_path):
    return A.render(audio_events(spec), out_path)


def chunks(spec, k=3):
    """Reparte los turnos en k tercios de longitud parecida (indices de turno)."""
    words = [A.count_words(t) for _, t in spec["turns"]]
    total, acc, out = sum(words), 0, [[] for _ in range(k)]
    for i, w in enumerate(words):
        out[min(k - 1, int(acc / total * k))].append(i)
        acc += w
    return out


def _chunk_wav(spec, idxs, rates):
    turns = [spec["turns"][i] for i in idxs]
    wavs = A.synth([(t, spec["speakers"][lab], rates[spec["speakers"][lab]]) for lab, t in turns])
    pieces = []
    for w in wavs:
        if pieces:
            pieces.append(A._silence(A.TURN_GAP))
        pieces.append(w)
    out = os.path.join(A.CACHE, "chunk_" + A._key(*wavs) + ".wav")
    if not os.path.exists(out):
        A._concat(pieces, out)
    return out, _norm(" ".join(t for _, t in turns))


def verify_audio(spec, report, asr=True, part=None):
    """Velocidad y duracion; si asr, reconocimiento del tercio 'part' (1-3) o de los tres."""
    errs, lines = [], []
    r = report["recs"][_rec_id(spec)]
    m, s = divmod(int(round(r["total_s"])), 60)
    lines.append(f"Grabación: {r['words']} palabras · {m}:{s:02d} · {r['wpm_speech']} ppm (objetivo {spec['wpm']}) · "
                 f"por voz {r['wpm_by_voice']} · rates {r['rates']}")
    if abs(r["wpm_speech"] / spec["wpm"] - 1) > WPM_TOL:
        errs.append(f"velocidad {r['wpm_speech']} ppm fuera de ±{WPM_TOL:.0%} de {spec['wpm']}")
    for v, w in r["wpm_by_voice"].items():
        if abs(w / spec["wpm"] - 1) > WPM_TOL:
            errs.append(f"voz {v}: {w} ppm fuera de ±{WPM_TOL:.0%}")
    if not SEC_MIN <= r["total_s"] <= SEC_MAX + 15:
        errs.append(f"duración {r['total_s']} s fuera de 3-4 min (con margen)")
    if asr:
        parts = [part] if part else [1, 2, 3]
        for k in parts:
            idxs = chunks(spec)[k - 1]
            wav, text = _chunk_wav(spec, idxs, r["rates"])
            phrases = [ev for it in spec["items"] for ev in it["evidence"] if ev in text]
            chk = A.check_recording(wav, text, phrases)
            bad = [f"«{f[:45]}» {sc}" for f, sc in chk["phrases"] if sc < 0.85]
            diffs = word_diff(A.norm_words(text), A.norm_words(chk["asr"]))
            lines.append(f"Tercio {k} (turnos {idxs[0] + 1}-{idxs[-1] + 1}): ASR {chk['sim']} · frases-respuesta "
                         f"{len(phrases) - len(bad)}/{len(phrases)} · diferencias {len(diffs)}")
            lines += ["    " + d for d in diffs]
            if not chk["ok"]:
                errs.append(f"tercio {k}: parecido {chk['sim']}; frases mal reconocidas {bad}\n    ASR: {chk['asr']}")
    return errs, lines


# ---------- Verificacion del contenido ----------
def verify(spec):
    errs = []
    a = _first(spec)
    items = spec.get("items", [])
    if [it.get("n") for it in items] != list(range(a, a + N_ITEMS)):
        errs.append(f"numeración: se esperaban {a}–{a + N_ITEMS - 1}")
    for f in ("ctx", "speakers", "turns", "subtitle"):
        if not spec.get(f):
            errs.append(f"falta '{f}'")
    if not spec.get("ctx", "").startswith("You will hear ") or not spec.get("ctx", "").endswith("."):
        errs.append("ctx debe empezar por 'You will hear' y acabar en punto")
    wpm = spec.get("wpm", 0)
    if not 140 <= wpm <= 200:
        errs.append("wpm ausente o fuera de 140-200")
    sp = spec.get("speakers", {})
    if not 2 <= len(sp) <= 3:
        errs.append(f"{len(sp)} hablantes (2 o 3)")
    if len(set(sp.values())) != len(sp):
        errs.append("dos hablantes con la misma voz")
    for lab, v in sp.items():
        if v not in A.VOICES or v == A.NARRATOR:
            errs.append(f"voz no válida para '{lab}': {v}")
    host = spec.get("host")
    if host and host not in sp:
        errs.append(f"host '{host}' no está entre los hablantes")
    turns = spec.get("turns", [])
    for lab, t in turns:
        if lab not in sp:
            errs.append(f"hablante sin voz asignada: {lab}")
        if re.search(r"[\[\]{}<>]", t):
            errs.append(f"marcado en un turno: «{t[:40]}»")
    if set(lab for lab, _ in turns) != set(sp):
        errs.append("algún hablante no interviene")
    for (l1, _), (l2, _) in zip(turns, turns[1:]):
        if l1 == l2:
            errs.append(f"dos turnos seguidos de {l1}: únelos")
    txt = _text(spec) if turns else ""
    nwords = A.count_words(txt)
    est = nwords / max(wpm, 1) * 60
    if not SEC_MIN <= est <= SEC_MAX:
        errs.append(f"{nwords} palabras: {est:.0f} s estimados a {wpm} ppm, fuera de 3-4 min")
    positions = []
    for it in items:
        n = it.get("n", "?")
        for field in ("type", "stem", "options", "key", "evidence", "why", "theory", "distractors"):
            if not it.get(field):
                errs.append(f"{n}: falta el campo '{field}'")
        if it.get("type") not in TYPES:
            errs.append(f"{n}: tipo de pregunta desconocido '{it.get('type')}'")
        if it.get("type") == "Global" and n != a + N_ITEMS - 1:
            errs.append(f"{n}: solo la última pregunta puede ser global")
        opts = it.get("options", [])
        if len(opts) != 4 or len(set(opts)) != 4 or not all(o.strip() for o in opts):
            errs.append(f"{n}: hacen falta cuatro opciones distintas")
        for o in opts + [it.get("stem", "")]:
            if re.search(r"[\[\]{}<>]", o):
                errs.append(f"{n}: marcado en el enunciado o en una opción")
        key = it.get("key")
        if key not in LETTERS:
            errs.append(f"{n}: clave no válida '{key}'")
            continue
        for s in it.get("theory", []):
            if s not in THEORY:
                errs.append(f"{n}: sección de teoría inexistente §{s}")
        who = _speaker_list(it)
        for w in who:
            if w not in sp:
                errs.append(f"{n}: hablante desconocido '{w}'")
        ev_speakers, first_pos = set(), None
        for ev in it.get("evidence", []):
            hits = [(i, lab) for i, (lab, t) in enumerate(turns) if ev in t]
            if not hits:
                errs.append(f"{n}: frase-respuesta no literal o repartida entre turnos: «{ev[:50]}»")
                continue
            if who and not any(lab in who for _, lab in hits):
                errs.append(f"{n}: la frase-respuesta «{ev[:40]}» no es de {who}")
            ev_speakers |= {lab for _, lab in hits}
            pos = txt.find(ev)
            first_pos = pos if first_pos is None else min(first_pos, pos)
        if it.get("type") == "Acuerdo" and len(ev_speakers - {host}) < 2:
            errs.append(f"{n}: una pregunta de acuerdo necesita evidencia de dos hablantes (no el presentador)")
        if first_pos is not None and it.get("type") != "Global":
            positions.append((n, first_pos))
        if not CITE_RE.findall(it.get("why", "")):
            errs.append(f"{n}: la explicación de la clave no cita la grabación")
        dis = it.get("distractors", {})
        if set(dis) != set(LETTERS) - {key}:
            errs.append(f"{n}: distractores explicados {sorted(dis)}; se esperaban {sorted(set(LETTERS) - {key})}")
        for L, d in dis.items():
            if not d.get("kinds") or any(k not in KINDS for k in d["kinds"]):
                errs.append(f"{n}{L}: tipo de distractor ausente o desconocido {d.get('kinds')}")
            if not d.get("why"):
                errs.append(f"{n}{L}: falta la explicación")
        texts = [("why", it.get("why", ""))] + [(f"distractor {L}", d.get("why", "")) for L, d in dis.items()]
        for field, t in texts:
            for c in CITE_RE.findall(t):
                if _norm(c) not in txt:
                    errs.append(f"{n} ({field}): cita inexistente en la grabación: «{c[:50]}»")
            if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(t)):
                errs.append(f"{n}: marcado sin resolver en '{field}'")
    if [p_ for _, p_ in positions] != sorted(p_ for _, p_ in positions):
        errs.append(f"las preguntas no siguen el orden del audio: {positions}")
    keys = "".join(it.get("key", "?") for it in items)
    if any(keys.count(L) > 2 for L in LETTERS) or len(set(keys)) < 3:
        errs.append(f"reparto de claves {keys}: ninguna letra más de 2 veces y al menos 3 letras distintas")
    longest = []
    for it in items:
        if it.get("key") in LETTERS and len(it.get("options", [])) == 4:
            lens = [len(o) for o in it["options"]]
            k = LETTERS.index(it["key"])
            if lens[k] == max(lens) and lens.count(max(lens)) == 1:
                longest.append(it["n"])
    if len(longest) > 2:
        errs.append(f"la clave es la opción más larga en {len(longest)} preguntas: {longest}")
    return errs, {"words": nwords, "est_s": round(est), "keys": keys, "longest": longest, "turns": len(turns)}


def check_pdf(path):
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            txt = "\n".join(pg.extract_text() or "" for pg in pdf.pages)
    except ImportError:
        from pypdf import PdfReader
        txt = "\n".join(pg.extract_text() or "" for pg in PdfReader(path).pages)
    return re.findall(r"\{\{|\}\}|\[\[|\]\]|<font|</?b>|<br|<super|&nbsp", txt)


def _info_line(spec, info):
    return (f"{CODE}_Practica_{spec['num']}.pdf · {info['words']} palabras en {info['turns']} turnos "
            f"(~{info['est_s']} s) · claves {info['keys']} · clave más larga en {info['longest'] or 'ninguna'}")


def make(spec, out_dir="/mnt/user-data/outputs", audio=True, asr=True):
    errs, info = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}:\n  - " + "\n  - ".join(errs))
    base = os.path.join(out_dir, f"{CODE}_Practica_{spec['num']}")
    pdf = build_sheet(spec, base + ".pdf")
    left = check_pdf(pdf)
    if left:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {left}")
    print(_info_line(spec, info) + " · verificación sin errores")
    mp3 = None
    if audio:
        A.setup(asr=asr)
        mp3 = base + ".mp3"
        rep = build_audio(spec, mp3)
        aerrs, lines = verify_audio(spec, rep, asr=asr)
        print("\n".join("  " + ln for ln in lines))
        m, s = divmod(int(round(rep["duration_s"])), 60)
        print(f"{CODE}_Practica_{spec['num']}.mp3 · {m}:{s:02d} · narrador {rep['narrator_rate']:+d} %")
        if aerrs:
            raise ValueError(f"Hoja {spec['num']} (audio):\n  - " + "\n  - ".join(aerrs))
    return pdf, mp3


def stage(spec, out_dir, what, idx=None):
    """'pdf' | 'audio' | 'asr' con idx 1-3 (un tercio de la grabacion cada uno). Devuelve True si va bien."""
    import json
    base = os.path.join(out_dir, f"{CODE}_Practica_{spec['num']}")
    rep_path = os.path.join(A.CACHE, f"report_{CODE}_{spec['num']}.json")
    if what == "pdf":
        errs, info = verify(spec)
        if errs:
            print("\n".join(errs))
            return False
        build_sheet(spec, base + ".pdf")
        left = check_pdf(base + ".pdf")
        print(_info_line(spec, info) + f" · restos {left or 'ninguno'}")
        return not left
    if what == "audio":
        A.setup(asr=False)
        rep = build_audio(spec, base + ".mp3")
        json.dump(rep, open(rep_path, "w"), default=str)
        errs, lines = verify_audio(spec, rep, asr=False)
        m, s = divmod(int(round(rep["duration_s"])), 60)
        print(f"{CODE}_Practica_{spec['num']}.mp3 · {m}:{s:02d} · narrador {rep['narrator_rate']:+d} %")
        print("\n".join("  " + ln for ln in lines + errs))
        return not errs
    if what == "asr":
        A.setup(asr=True)
        rep = json.load(open(rep_path))
        errs, lines = verify_audio(spec, rep, asr=True, part=idx)
        print("\n".join("  " + ln for ln in lines[1:] + errs))
        return not errs
    raise ValueError(what)


# ---------- Hoja de ejemplo: contenido de LST-P3_Practica_01, numerada como 99 ----------
def _demo():
    import copy
    d = copy.deepcopy(DEMO_SPEC)
    d["num"], d["subtitle"] = "99", "Hoja de prueba del generador (contenido de LST-P3_Practica_01)"
    return d


DEMO_SPEC = {
    "num": "01",
    "subtitle": "Hoja 01 · Entrevista con una invitada, opiniones explícitas · dificultad 1 de 4",
    "difficulty": 1,
    "wpm": 160,
    "ctx": "You will hear part of an interview with Clara Wainwright, a literary translator who translates novels "
           "from Swedish into English.",
    "speakers": {"Interviewer": "Ryan", "Clara": "Sonia"},
    "host": "Interviewer",
    "lex": ["drift into something", "of all things", "and that was that", "might as well", "show through",
            "on someone’s behalf", "keep someone awake", "untangle", "I won’t deny it", "a sense of rhythm"],
    "turns": [
        ("Interviewer",
         "My guest today is Clara Wainwright, whose translations of Scandinavian crime fiction have sold millions of "
         "copies. Clara, did you always know you wanted to be a translator?"),
        ("Clara",
         "I’d love to say it was a calling, but honestly, I drifted into it. I’d studied music, of all things, and I "
         "went to Stockholm for a year to play in an orchestra. I picked up the language because I had to, and when "
         "a friend at a publishing house needed someone to read a Swedish novel and tell her whether it was any "
         "good, I happened to be the only person she knew who could. I wrote a report, she asked me to translate a "
         "sample chapter, and that was that. Twenty years later, here I am."),
        ("Interviewer",
         "People often say that the best translation is one you don’t notice – that the reader should forget the "
         "book was ever written in another language. Is that what you aim for?"),
        ("Clara",
         "It’s what I was taught to aim for, and I’m less and less sure about it. Of course the English has to read "
         "naturally – nobody wants clumsy sentences. But if a novel is set in a small town in the north of Sweden, I "
         "don’t think the reader should come away feeling it might as well have been set in Yorkshire. Something of "
         "the original ought to show through. So no, I don’t want to be invisible. I’d rather readers knew that "
         "someone had made choices on their behalf."),
        ("Interviewer",
         "And which choices are the hardest? I imagine all those different words for snow…"),
        ("Clara",
         "Everyone imagines that! But vocabulary is the easy part – that’s what dictionaries are for. What really "
         "keeps me awake is the way people speak to each other. In Sweden, almost everyone uses first names and the "
         "informal word for ‘you’, whether they’re talking to a child or to the prime minister. English doesn’t work "
         "like that. So when a young police officer chats to her boss as if he were her brother, an English reader "
         "might think she’s being rude, when in Swedish it’s perfectly ordinary. I spend hours finding other ways to "
         "show how close or distant the characters are."),
        ("Interviewer",
         "Machine translation has improved enormously in the last few years. Does it worry you?"),
        ("Clara",
         "Not in the way you might think. I tried it once for a first draft, and I spent longer untangling the "
         "result than it would have taken me to start from scratch. For novels, I really don’t believe the machines "
         "are going to replace us. What does worry me is that some publishers may start handing translators machine "
         "output and calling the job ‘editing’ – at half the fee. That would be bad for translators, but it would "
         "also be bad for books."),
        ("Interviewer",
         "Finally, what would you say to someone who’d like to do what you do?"),
        ("Clara",
         "Most people expect me to say ‘go and live abroad’, and living in Sweden certainly helped me, I won’t deny "
         "it. But the mistake I see most often isn’t poor Swedish – it’s flat, awkward English. Your readers will "
         "never see the original; all they’ll ever see is your writing. So read as widely as you can in your own "
         "language, and write every day. You can always look up a word. You can’t look up a sense of rhythm."),
    ],
    "items": [
        {"n": 16, "type": "Detalle", "speaker": "Clara",
         "stem": "What does Clara say about how she became a translator?",
         "options": ["It came about largely by chance.",
                     "It was a natural next step after her university studies.",
                     "A friend persuaded her to give up her career in music.",
                     "She learnt Swedish because she wanted to translate from it."],
         "key": "A",
         "evidence": ["I drifted into it", "I happened to be the only person she knew who could"],
         "why": "Lo dice al principio, {{I drifted into it}}, y lo confirma la anécdota: la amiga necesitaba a alguien "
                "que leyera sueco y {{I happened to be the only person she knew who could}}. «Por casualidad» "
                "resume las dos frases sin repetir ninguna palabra.",
         "theory": ["7.1", "3.1"],
         "distractors": {
             "B": {"kinds": ["4.1"],
                   "why": "Recoge {{I’d studied music}}, pero lo que estudió no tenía nada que ver con la traducción, "
                          "y ella misma lo subraya: {{of all things}}."},
             "C": {"kinds": ["4.5"],
                   "why": "La amiga solo le pidió un informe sobre una novela ({{tell her whether it was any good}}). "
                          "Nadie la convence de dejar la música."},
             "D": {"kinds": ["4.6"],
                   "why": "Invierte el orden: aprendió sueco por necesidad, mientras tocaba en la orquesta "
                          "({{I picked up the language because I had to}}), y la traducción llegó después."}}},
        {"n": 17, "type": "Actitud y opinión", "speaker": "Clara",
         "stem": "What is Clara’s view of the idea that the best translation is one the reader does not notice?",
         "options": ["She thinks it matters more for crime fiction than for other kinds of novel.",
                     "She has come to have doubts about it.",
                     "She believes it is the only realistic goal for a translator.",
                     "She feels it has led to translations that sound unnatural."],
         "key": "B",
         "evidence": ["I’m less and less sure about it", "So no, I don’t want to be invisible."],
         "why": "Es lo que le enseñaron, pero {{I’m less and less sure about it}}, y lo cierra sin ambigüedad: "
                "{{So no, I don’t want to be invisible.}} La duda ha ido creciendo con los años: [[has come to]].",
         "theory": ["3.3", "3.2"],
         "distractors": {
             "A": {"kinds": ["4.8"],
                   "why": "La novela negra solo aparece cuando el entrevistador la presenta. Clara no compara géneros en ningún momento."},
             "C": {"kinds": ["4.4"],
                   "why": "Es lo que le enseñaron ({{It’s what I was taught to aim for}}), no lo que piensa ahora."},
             "D": {"kinds": ["4.1", "4.8"],
                   "why": "Recoge la idea de naturalidad ({{the English has to read naturally}}), pero Clara la da "
                          "por supuesta. No culpa a la invisibilidad de ninguna traducción poco natural."}}},
        {"n": 18, "type": "Detalle", "speaker": "Clara",
         "stem": "According to Clara, what is the most challenging aspect of translating from Swedish?",
         "options": ["finding English equivalents for specialised vocabulary",
                     "explaining police procedures to English readers",
                     "showing how close or distant characters are to one another",
                     "deciding which Swedish words to leave untranslated"],
         "key": "C",
         "evidence": ["What really keeps me awake is the way people speak to each other",
                      "I spend hours finding other ways to show how close or distant the characters are."],
         "why": "La señal {{What really keeps me awake is}} (§2.3) anuncia la respuesta: el trato entre los "
                "personajes. Lo resume al final: {{I spend hours finding other ways to show how close or distant the "
                "characters are.}}",
         "theory": ["2.3", "4.2"],
         "distractors": {
             "A": {"kinds": ["4.2"],
                   "why": "Lo menciona el entrevistador y ella lo descarta: {{vocabulary is the easy part}}."},
             "B": {"kinds": ["4.1"],
                   "why": "La policía aparece solo en el ejemplo ({{a young police officer chats to her boss}}), que "
                          "trata de cómo se hablan, no de procedimientos."},
             "D": {"kinds": ["4.8"],
                   "why": "Encaja con su idea de que {{Something of the original ought to show through}}, pero nunca "
                          "habla de dejar palabras en sueco."}}},
        {"n": 19, "type": "Actitud y opinión", "speaker": "Clara",
         "stem": "What concerns Clara about machine translation?",
         "options": ["It will soon translate novels as well as people can.",
                     "Correcting its errors takes longer than translating from scratch.",
                     "Publishers may use it as a way of paying translators less.",
                     "Readers will stop caring whether a book has been translated well."],
         "key": "C",
         "evidence": ["What does worry me is that some publishers may start handing translators machine output"],
         "why": "La señal {{What does worry me is}} da la respuesta: los editores podrían entregar a los traductores "
                "texto de máquina y llamarlo revisión, {{at half the fee}}.",
         "theory": ["2.3", "4.3"],
         "distractors": {
             "A": {"kinds": ["4.2"],
                   "why": "Lo descarta: {{I really don’t believe the machines are going to replace us}}."},
             "B": {"kinds": ["4.3"],
                   "why": "Es cierto según su experiencia ({{I spent longer untangling the result}}), pero lo cuenta "
                          "para explicar por qué la máquina no la preocupa como rival. No responde a qué le "
                          "preocupa."},
             "D": {"kinds": ["4.8"],
                   "why": "Dice que sería malo {{for books}}, no que los lectores vayan a dejar de valorar una "
                          "buena traducción."}}},
        {"n": 20, "type": "Detalle", "speaker": "Clara",
         "stem": "What advice does Clara give to people who want to become literary translators?",
         "options": ["Spend as long as possible in the country whose language they translate.",
                     "Get into the habit of checking every unfamiliar word.",
                     "Read the original aloud to get a feel for its rhythm.",
                     "Concentrate on improving their writing in their own language."],
         "key": "D",
         "evidence": ["So read as widely as you can in your own language, and write every day."],
         "why": "El error que más ve es {{flat, awkward English}}, y el consejo va a lo mismo: "
                "{{So read as widely as you can in your own language, and write every day.}}",
         "theory": ["3.3", "4.2", "7.2"],
         "distractors": {
             "A": {"kinds": ["4.2"],
                   "why": "Lo concede ({{living in Sweden certainly helped me, I won’t deny it}}) y lo deja de "
                          "lado con {{But}}: no es su consejo."},
             "B": {"kinds": ["4.1"],
                   "why": "Recoge {{You can always look up a word}}, que dice justo lo contrario: buscar palabras es "
                          "lo fácil."},
             "C": {"kinds": ["4.1", "4.8"],
                   "why": "Sale de {{a sense of rhythm}}, pero ese ritmo es el de la prosa inglesa del traductor. "
                          "Nunca propone leer el original en voz alta."}}},
    ],
}


def _main():
    import runpy
    argv = sys.argv[1:]
    opt = {}
    for name in ("--num", "--stage"):
        if name in argv:
            i = argv.index(name)
            opt[name] = argv[i + 1]
            del argv[i:i + 2]
    args = [x for x in argv if not x.startswith("--no-")]
    flags = set(argv) - set(args)
    if not args:
        print(f"Uso: python3 gen_{CODE}.py --demo | mis_hojas.py [carpeta_salida] [--no-audio] [--no-asr]\n"
              "     por etapas: … --num 03 --stage pdf | audio | asr1 | asr2 | asr3")
        sys.exit(1)
    out_dir = args[1] if len(args) > 1 else "/mnt/user-data/outputs"
    os.makedirs(out_dir, exist_ok=True)
    specs = [_demo()] if args[0] == "--demo" else (runpy.run_path(args[0]).get("SPECS")
                                                   or [runpy.run_path(args[0])["SPEC"]])
    if "--num" in opt:
        specs = [sp for sp in specs if sp["num"] == opt["--num"]]
    for sp in specs:
        if "--stage" in opt:
            st = opt["--stage"]
            ok = stage(sp, out_dir, "asr", int(st[3:])) if st.startswith("asr") else stage(sp, out_dir, st)
            sys.exit(0 if ok else 2)
        make(sp, out_dir, audio="--no-audio" not in flags, asr="--no-asr" not in flags)


if __name__ == "__main__":
    _main()
