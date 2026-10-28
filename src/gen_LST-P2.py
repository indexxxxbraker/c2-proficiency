# gen_LST-P2.py · Generador de Listening Part 2 (sentence completion) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py y lst_audio.py en la misma carpeta (no modifica ninguno).
#
# QUE HACE
#   - Hoja de practica completa en PDF: frases 7-15 con hueco, hoja de respuestas y soluciones (transcripcion con
#     la respuesta resaltada, respuestas aceptadas, candidatos y formas que no valen, con su explicacion).
#   - MP3 con el mismo nombre: guion del examen (rubrica, 45 s de lectura, tono, monologo, 5 s, 'Now you will hear
#     Part Two again', tono, repeticion, 5 s, fin), voz neuronal con la velocidad de la hoja.
#   - Bloques sueltos para un simulacro (SIM): preguntas, hoja de respuestas, soluciones y eventos de audio.
#   - Verificacion automatica del contenido, del PDF y del audio (velocidad y reconocimiento de voz, que debe
#     reconocer cada respuesta tal cual).
#
# USO
#   python3 gen_LST-P2.py --demo [carpeta_salida]          -> hoja de ejemplo (contenido de la 01, como 99)
#   python3 gen_LST-P2.py mis_hojas.py [carpeta_salida]    -> mis_hojas.py define SPECS = [spec, ...]
#   Opciones: --no-audio · --no-asr
#   Por etapas (claude.ai corta cada comando a los 5 minutos; la sintesis queda en la cache):
#   python3 gen_LST-P2.py mis_hojas.py salida --num 03 --stage pdf | audio | asr1 | asr2 | asr3
#   (asr1-asr3 comprueban cada uno un tercio de los parrafos del monologo)
#   Desde otro script: importlib (ver gen_LST-P1.py); verify(spec), make(spec, carpeta), question_flowables(spec),
#   answer_sheet_flowables(spec), solutions_flowables(spec), audio_events(spec, standalone=False).
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num, subtitle, difficulty (1-4), wpm (160 en la 01 … 185 en la 04), lex (para LEX)
#   voice       voz del monologo (lst_audio.VOICES, no el narrador)
#   ctx         frase de la rubrica, tal como la lee el narrador: "You will hear a historian called … talking about …"
#   title       titulo que encabeza las frases (como en el cuadernillo del examen)
#   paragraphs  monologo en parrafos (3-4 minutos a la velocidad de la hoja); cada parrafo es un fragmento de audio
#   items       9 diccionarios (7-15):
#     n           7
#     sentence    frase del papel con el hueco marcado como ___ (ingles; reformula el audio)
#     key         respuestas aceptadas con la convencion de Cambridge: palabras opcionales entre parentesis y
#                 alternativas separadas por " / ", p. ej. "(seed) catalogues / (seed) catalogs"
#     evidence    fragmento literal del monologo que contiene la respuesta (se resalta en la transcripcion)
#     why         explicacion en espanol con citas {{…}} literales del monologo
#     wrong       respuestas que NO valen: [{"answer", "kind", "why"}]; kind = candidato (§6.3: se oye y no
#                 cumple la condicion de la frase), forma (§6.4: numero, encaje), sinónimo (§6.4: no es lo que se
#                 oye), ortografía (§6.5), incompleta (§6.4)
#     theory      secciones de LST_Teoria_v1
#     asr_ok      (opcional) homofonos que el reconocimiento de voz puede escribir en lugar de la clave sin que la
#                 voz este mal (bass/base): solo cuentan para la comprobacion del audio, nunca como respuesta
#   Marcado en textos en espanol: {{cita literal}} · [[ingles sin comprobar]] · [[!ingles en negrita]]
#
# QUE COMPRUEBA verify()
#   nueve items 7-15 · duracion estimada 3-4 min · respuestas de 1 a 3 palabras (hasta 5 con las opcionales) · que
#   alguna forma completa de la clave se oiga literalmente y dentro de su 'evidence' · orden de las respuestas en el
#   audio y al menos 25 palabras entre una y otra · que la frase no contenga la respuesta ni copie 6 o mas palabras
#   seguidas del audio · a/an delante del hueco · candidatos presentes en el audio · ninguna respuesta incorrecta
#   dentro del conjunto aceptado · al menos 6 items con candidatos · citas literales · teoria existente · marcado.
# QUE COMPRUEBA verify_audio()
#   velocidad real (±6 %) · parecido texto-reconocimiento de cada parrafo (>= 0,88) · que cada respuesta se
#   reconoce exactamente (sin esto, una palabra mal pronunciada por la voz sintetica pasaria desapercibida).
#
# A MANO
#   - Que ninguna respuesta fuera de la clave sea defendible: sinonimos que encajen, singular/plural (si la frase
#     admite los dos, la clave debe aceptar los dos o la frase debe forzar uno), variantes ortograficas registradas.
#   - Que la frase del papel identifique un solo candidato. Ingles britanico, registro, dificultad graduada.
#   - Revisar el PDF renderizado y escuchar el MP3.

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
import lst_audio as A  # noqa: E402

VERSION = "1"
FIRST_ITEM = 7
N_ITEMS = 9
WPM_TOL = 0.06
MIN_GAP_WORDS = 25
MAX_COPY_RUN = 5
THEORY_DOC = "LST_Teoria_v1"
CODE = "LST-P2"
GAP = "___"

THEORY = {
    "2.1": "Habla conectada", "2.2": "Acentos del examen", "2.3": "Señales del discurso oral", "2.4": "Matización",
    "3.1": "Lo que se dice y lo que se da a entender", "3.2": "Voz propia y voces ajenas",
    "3.3": "La segunda idea manda", "6.1": "Part 2: la tarea", "6.2": "Los 45 segundos: predecir cada hueco",
    "6.3": "Varios candidatos para un mismo hueco", "6.4": "Qué se escribe", "6.5": "Ortografía",
    "6.6": "Part 2: caso resuelto", "9": "Rutina de autocorrección",
}
WRONG_KINDS = {"candidato": "6.3", "forma": "6.4", "sinónimo": "6.4", "ortografía": "6.5", "incompleta": "6.4"}

CITE_RE = re.compile(r"\{\{(.+?)\}\}")
VOWEL_EXC = ("uni", "use", "usu", "eu", "one", "once")       # empiezan por vocal y llevan 'a'
H_SILENT = ("hour", "honest", "honour", "heir")              # empiezan por h y llevan 'an'


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
    return _norm(" ".join(spec["paragraphs"]))


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def expand(key):
    """'(seed) catalogues / (seed) catalogs' -> ['seed catalogues', 'catalogues', 'seed catalogs', 'catalogs']"""
    out = []
    for alt in key.split(" / "):
        combos = [""]
        for part in re.split(r"(\([^)]+\))", alt.strip()):
            if part.startswith("("):
                combos = [c + part[1:-1] for c in combos] + combos
            else:
                combos = [c + part for c in combos]
        for c in combos:
            c = _norm(c)
            if c and c not in out:
                out.append(c)
    return out


def full_forms(key):
    """Una forma por alternativa, con todas las palabras opcionales (lo que se oye completo)."""
    return [_norm(alt.replace("(", "").replace(")", "")) for alt in key.split(" / ")]


def _words(s):
    return re.findall(r"[a-z0-9]+(?:[’'][a-z]+)?", s.lower().replace("’", "'"))


def _longest_common_run(a, b):
    best = 0
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                best = max(best, cur[j])
        prev = cur
    return best


def gap_html(n):
    pad = "&nbsp;" * 7
    return f'<u>{pad}<font name="EN-B" color="#A4243B">{n}</font>{pad}{pad}{pad}</u>'


# ---------- Estilos propios (sobre la plantilla, sin cambiarla) ----------
_rub = ParagraphStyle("p2_rubric", parent=S["en"], fontSize=10, leading=14)
_ttl = ParagraphStyle("p2_title", parent=S["en"], fontName="EN-B", fontSize=12.5, leading=16, textColor=NAVY,
                      alignment=1, spaceBefore=10, spaceAfter=8)
_sent = ParagraphStyle("p2_sent", parent=S["en"], fontSize=10.6, leading=16, spaceAfter=11)
_ihead = ParagraphStyle("p2_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)
_sol = ParagraphStyle("p2_sol", parent=S["body"], leftIndent=14, spaceAfter=4)
_tr = ParagraphStyle("p2_tr", parent=S["cell_en"], fontSize=10, leading=14.2)


# ---------- Bloques reutilizables ----------
def question_flowables(spec, with_title_block=False):
    a = _first(spec)
    out = []
    if with_title_block:
        out += title_block(f"{CODE} · Práctica {spec['num']}", "Sentence completion", spec["subtitle"],
                           f"9 preguntas ({a}–{a + 8}) · 1 punto por pregunta · audio: {CODE}_Practica_{spec['num']}"
                           ".mp3 · el monólogo suena dos veces, con las pausas del examen · sin consultar la teoría")
    out.append(Paragraph(f"{spec['ctx']} For questions {a}–{a + 8}, complete the sentences with a word or short "
                         "phrase.", _rub))
    out.append(Paragraph(spec["title"], _ttl))
    for it in spec["items"]:
        out.append(Paragraph(it["sentence"].replace(GAP, gap_html(it["n"])), _sent))
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    out = [h2(heading), p(
        "Escribe las palabras que oyes, sin cambiarlas, y comprueba que encajan en la frase y que están bien "
        "escritas. 1 punto por respuesta correcta. En el examen en papel: mayúsculas, una letra por casilla.")]
    rows = [["Nº", "Respuesta", "Puntos"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), "", "&nbsp;&nbsp;&nbsp;&nbsp;/ 1"])
    rows.append(["", "<b>Total</b>", "&nbsp;&nbsp;&nbsp;&nbsp;<b>/ 9</b>"])
    out += table(rows, [16, 124, 30], zebra=False,
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 11), ("BOTTOMPADDING", (0, 1), (-1, -1), 11),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
                        ("LINEBELOW", (1, 1), (1, -2), 0.6, GREY)])
    return out


def transcript_flowables(spec):
    marks = [(it["evidence"], it["n"]) for it in spec["items"]]
    rows = []
    for para in spec["paragraphs"]:
        for ev, n in marks:
            if ev in para:
                para = para.replace(ev, f"<b>{ev}</b><super><font size=7 color='#A4243B'>&nbsp;{n}</font></super>", 1)
        rows.append([Paragraph(para, _tr)])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_EJ), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, 0), 8), ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
        ("LINEBEFORE", (0, 0), (0, -1), 1.8, GREY)]))
    return [t, Spacer(1, 6)]


def solutions_flowables(spec, with_band=True, heading=None):
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(
        "1 punto por respuesta correcta y bien escrita. La clave sigue la convención de Cambridge: las palabras "
        "entre paréntesis son opcionales y la barra separa alternativas. Debajo de cada respuesta van las que no "
        "valen: candidatos que se oyen pero no cumplen la condición de la frase (§6.3), formas que no encajan o "
        f"palabras que no se oyen (§6.4) y errores de ortografía (§6.5). Los números de sección remiten a {THEORY_DOC}."))
    out.append(h2("Clave rápida") if not heading else h3("Clave rápida"))
    rows = [["Nº", "Clave", "No vale", "Teoría"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), EB(it["key"]), E(" · ".join(w["answer"] for w in it["wrong"])),
                     " · ".join("§" + s for s in it["theory"])])
    out += table(rows, [12, 62, 64, 32])
    v = spec["voice"]
    out.append(KeepTogether([h2("Transcripción") if not heading else h3("Transcripción"),
                             Paragraph(f"Voz · {v}, inglés {A.ACCENTS[A.VOICES[v][1]]}", S["small"])]))
    out += transcript_flowables(spec)
    out.append(h2("Explicaciones") if not heading else h3("Explicaciones"))
    for it in spec["items"]:
        accepted = " · ".join(expand(it["key"]))
        filled = it["sentence"].replace(GAP, f"<b><u>{expand(it['key'])[0]}</u></b>")
        block = [Paragraph(f"{it['n']} · {E(it['key'])}", _ihead),
                 Paragraph(f"<b>Frase:</b> {E(filled)}", _sol),
                 Paragraph(f"<b>Se oye:</b> {E(it['evidence'])}", _sol),
                 Paragraph(f"<b>Se acepta:</b> {E(accepted)}", _sol),
                 Paragraph(markup(it["why"]), _sol)]
        for w in it["wrong"]:
            sec = WRONG_KINDS[w["kind"]]
            block.append(Paragraph(f"<b>No vale</b> {E(w['answer'])} ({w['kind']} §{sec}). {markup(w['why'])}", _sol))
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


def audio_events(spec, standalone=True):
    a = _first(spec)
    rubric = [f"{spec['ctx']} For questions {A.n2w(a)} to {A.n2w(a + 8)}, complete the sentences with a word or "
              "short phrase."]
    turns = [(spec["voice"], para) for para in spec["paragraphs"]]
    ev = A.opening(f"Proficiency Listening. Part Two practice, number {A.n2w(int(spec['num']))}.") if standalone else []
    return ev + A.script_part(2, rubric, 45, turns, spec["wpm"], rec_id=_rec_id(spec))


def build_audio(spec, out_path):
    return A.render(audio_events(spec), out_path)


def _key_heard(key, hyp_words):
    """La respuesta se reconoce si alguna forma aceptada aparece tal cual (tolerando compuestos: deck hand/deckhand)."""
    hj = " " + " ".join(hyp_words) + " "
    hset = set(hyp_words)
    for form in expand(key):
        kw = A.norm_words(form)
        if not kw:
            continue
        if " " + " ".join(kw) + " " in hj or "".join(kw) in hset:
            return True
        if len(kw) == 1 and any(hyp_words[i] + hyp_words[i + 1] == kw[0] for i in range(len(hyp_words) - 1)):
            return True
    return False


def verify_audio(spec, report, asr=True, paragraphs=None):
    """Velocidad del monologo y, si asr, reconocimiento de los parrafos indicados (indices desde 1; None = todos)."""
    errs, lines = [], []
    r = report["recs"][_rec_id(spec)]
    dev = r["wpm_speech"] / spec["wpm"] - 1
    m, s = divmod(int(round(r["total_s"])), 60)
    lines.append(f"Monólogo: {r['words']} palabras · {m}:{s:02d} · {r['wpm_speech']} ppm (objetivo {spec['wpm']}) · "
                 f"rate {r['rates']}")
    if abs(dev) > WPM_TOL:
        errs.append(f"velocidad {r['wpm_speech']} ppm fuera de ±{WPM_TOL:.0%} de {spec['wpm']}")
    if not 180 <= r["total_s"] <= 250:
        errs.append(f"duración del monólogo {r['total_s']} s fuera de 3-4 min (con margen)")
    if asr:
        rate = r["rates"][spec["voice"]]
        idxs = paragraphs or range(1, len(spec["paragraphs"]) + 1)
        for i in idxs:
            para = spec["paragraphs"][i - 1]
            wav = A.synth([(para, spec["voice"], rate)])[0]
            its = [it for it in spec["items"] if it["evidence"] in para]
            keys = [it["key"] for it in its]
            chk = A.check_recording(wav, para)
            hw = A.norm_words(chk["asr"])
            missing = [it["key"] for it in its
                       if not _key_heard(it["key"], hw)
                       and not any(_key_heard(h, hw) for h in it.get("asr_ok", []))]
            lines.append(f"Párrafo {i}: ASR {chk['sim']} · respuestas {len(keys) - len(missing)}/{len(keys)}")
            if chk["sim"] < 0.88 or missing:
                errs.append(f"párrafo {i}: parecido {chk['sim']}; respuestas no reconocidas {missing}\n"
                            f"    ASR: {chk['asr']}")
    return errs, lines


# ---------- Verificacion del contenido ----------
def verify(spec):
    errs = []
    a = _first(spec)
    items = spec.get("items", [])
    if [it.get("n") for it in items] != list(range(a, a + N_ITEMS)):
        errs.append(f"numeración: se esperaban {a}–{a + N_ITEMS - 1}")
    if spec.get("voice") not in A.VOICES or spec.get("voice") == A.NARRATOR:
        errs.append(f"voz no válida: {spec.get('voice')}")
    for f in ("ctx", "title", "paragraphs", "subtitle"):
        if not spec.get(f):
            errs.append(f"falta '{f}'")
    if not spec.get("ctx", "").startswith("You will hear "):
        errs.append("ctx debe empezar por 'You will hear'")
    wpm = spec.get("wpm", 0)
    if not 140 <= wpm <= 200:
        errs.append("wpm ausente o fuera de 140-200")
    txt = _text(spec)
    low = txt.lower()
    nwords = A.count_words(txt)
    est = nwords / max(wpm, 1) * 60
    if not 180 <= est <= 240:
        errs.append(f"{nwords} palabras: {est:.0f} s estimados a {wpm} ppm, fuera de 3-4 min")
    if re.search(r"[\[\]{}<>]", txt):
        errs.append("marcado dentro del monólogo")
    twords = _words(txt)
    positions, with_cands = [], 0
    for it in items:
        n = it.get("n", "?")
        for f in ("sentence", "key", "evidence", "why", "wrong", "theory"):
            if not it.get(f):
                errs.append(f"{n}: falta el campo '{f}'")
        sent, key, ev = it.get("sentence", ""), it.get("key", ""), it.get("evidence", "")
        if sent.count(GAP) != 1:
            errs.append(f"{n}: la frase debe tener exactamente un hueco {GAP}")
        forms = expand(key)
        for fm in forms:
            nw = len(fm.split())
            if nw > 5:
                errs.append(f"{n}: respuesta demasiado larga «{fm}»")
        if forms and min(len(fm.split()) for fm in forms) > 3:
            errs.append(f"{n}: la forma más corta de la respuesta tiene más de 3 palabras")
        heard = [ff for ff in full_forms(key) if ff.lower() in low] + \
                [fm for fm in forms if fm.lower() in low]
        if not heard:
            errs.append(f"{n}: ninguna forma de la clave aparece literalmente en el monólogo")
        if ev not in txt:
            errs.append(f"{n}: evidence no literal: «{ev}»")
        elif not any(fm.lower() in ev.lower() for fm in forms):
            errs.append(f"{n}: la evidence no contiene ninguna forma de la clave")
        else:
            positions.append((n, len(_words(txt[:txt.index(ev)]))))
        # la frase no contiene la respuesta ni copia el audio
        content = [w for w in _words(forms[0] if forms else "") if len(w) > 3]
        if any(w in _words(sent) for w in content):
            errs.append(f"{n}: la frase del papel contiene la respuesta")
        run = _longest_common_run(_words(sent.replace(GAP, " ")), twords)
        if run > MAX_COPY_RUN:
            errs.append(f"{n}: la frase copia {run} palabras seguidas del monólogo (máximo {MAX_COPY_RUN})")
        # a / an delante del hueco
        before = sent.split(GAP)[0].rstrip().split(" ")[-1].lower() if GAP in sent else ""
        for fm in forms:
            w0 = fm.lower()
            starts_v = w0[0] in "aeiou" and not w0.startswith(VOWEL_EXC)
            starts_v = starts_v or w0.startswith(H_SILENT) or w0[0] in "8"
            if before == "a" and starts_v:
                errs.append(f"{n}: 'a' delante de «{fm}»")
            if before == "an" and not starts_v:
                errs.append(f"{n}: 'an' delante de «{fm}»")
        # respuestas que no valen
        acc = {fm.lower() for fm in forms}
        cands = 0
        for w in it.get("wrong", []):
            if w.get("kind") not in WRONG_KINDS:
                errs.append(f"{n}: tipo de respuesta incorrecta desconocido {w.get('kind')}")
            if w.get("answer", "").lower() in acc:
                errs.append(f"{n}: «{w.get('answer')}» está a la vez en la clave y en 'no vale'")
            if w.get("kind") == "candidato":
                cands += 1
                aw = A.norm_words(w["answer"])
                if " ".join(aw) not in " ".join(A.norm_words(txt)):
                    errs.append(f"{n}: el candidato «{w['answer']}» no se oye en el monólogo")
            if not w.get("why"):
                errs.append(f"{n}: falta la explicación de «{w.get('answer')}»")
        with_cands += cands > 0
        for s in it.get("theory", []):
            if s not in THEORY:
                errs.append(f"{n}: sección de teoría inexistente §{s}")
        texts = [it.get("why", "")] + [w.get("why", "") for w in it.get("wrong", [])]
        for t in texts:
            for c in CITE_RE.findall(t):
                if _norm(c) not in txt and _norm(c) not in sent:
                    errs.append(f"{n}: cita inexistente en el monólogo o en la frase: «{c[:50]}»")
            if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(t)):
                errs.append(f"{n}: marcado sin resolver")
    pos = [p_ for _, p_ in positions]
    if pos != sorted(pos):
        errs.append(f"las respuestas no siguen el orden del audio: {positions}")
    for (n1, p1), (n2, p2) in zip(positions, positions[1:]):
        if p2 - p1 < MIN_GAP_WORDS:
            errs.append(f"{n1}→{n2}: solo {p2 - p1} palabras entre respuestas (mínimo {MIN_GAP_WORDS})")
    if with_cands < 6:
        errs.append(f"solo {with_cands} ítems con candidatos (mínimo 6)")
    return errs, {"words": nwords, "est_s": round(est), "with_cands": with_cands}


def check_pdf(path):
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            txt = "\n".join(pg.extract_text() or "" for pg in pdf.pages)
    except ImportError:
        from pypdf import PdfReader
        txt = "\n".join(pg.extract_text() or "" for pg in PdfReader(path).pages)
    return re.findall(r"\{\{|\}\}|\[\[|\]\]|<font|</?b>|<br|<super|&nbsp|___", txt)


def make(spec, out_dir="/mnt/user-data/outputs", audio=True, asr=True):
    errs, info = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}:\n  - " + "\n  - ".join(errs))
    base = os.path.join(out_dir, f"{CODE}_Practica_{spec['num']}")
    pdf = build_sheet(spec, base + ".pdf")
    left = check_pdf(pdf)
    if left:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {left}")
    print(f"{CODE}_Practica_{spec['num']}.pdf · {info['words']} palabras (~{info['est_s']} s) · "
          f"{info['with_cands']} ítems con candidatos · verificación sin errores")
    mp3 = None
    if audio:
        A.setup(asr=asr)
        mp3 = base + ".mp3"
        rep = build_audio(spec, mp3)
        aerrs, lines = verify_audio(spec, rep, asr=asr)
        print("\n".join("  " + ln for ln in lines))
        m, s = divmod(int(round(rep["duration_s"])), 60)
        print(f"{CODE}_Practica_{spec['num']}.mp3 · {m}:{s:02d}")
        if aerrs:
            raise ValueError(f"Hoja {spec['num']} (audio):\n  - " + "\n  - ".join(aerrs))
    return pdf, mp3


def stage(spec, out_dir, what, idx=None):
    """'pdf' | 'audio' | 'asr' con idx 1-3 (cada uno, un tercio de los parrafos). Devuelve True si va bien."""
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
        print(f"{CODE}_Practica_{spec['num']}.pdf · {info['words']} palabras (~{info['est_s']} s) · "
              f"{info['with_cands']} ítems con candidatos · restos {left or 'ninguno'}")
        return not left
    if what == "audio":
        A.setup(asr=False)
        rep = build_audio(spec, base + ".mp3")
        json.dump(rep, open(rep_path, "w"), default=str)
        errs, lines = verify_audio(spec, rep, asr=False)
        m, s = divmod(int(round(rep["duration_s"])), 60)
        print(f"{CODE}_Practica_{spec['num']}.mp3 · {m}:{s:02d}")
        print("\n".join("  " + ln for ln in lines + errs))
        return not errs
    if what == "asr":
        A.setup(asr=True)
        rep = json.load(open(rep_path))
        n = len(spec["paragraphs"])
        chunk = [i for i in range(1, n + 1) if (i - 1) * 3 // n == idx - 1]
        errs, lines = verify_audio(spec, rep, asr=True, paragraphs=chunk)
        print("\n".join("  " + ln for ln in lines[1:] + errs))
        return not errs
    raise ValueError(what)


# ---------- Hoja de ejemplo: contenido de LST-P2_Practica_01, numerada como 99 ----------
def _demo():
    import copy
    d = copy.deepcopy(DEMO_SPEC)
    d["num"], d["subtitle"] = "99", "Hoja de prueba del generador (contenido de LST-P2_Practica_01)"
    return d


DEMO_SPEC = {
    "num": "01",
    "subtitle": "Hoja 01 · Un candidato por hueco, sustantivos concretos · dificultad 1 de 4",
    "difficulty": 1,
    "wpm": 160,
    "voice": "Sonia",
    "ctx": "You will hear a historian called Claire Dunmore giving a talk about the lives of lighthouse keepers.",
    "title": "The lives of lighthouse keepers",
    "lex": ["rock station / shore station", "relief boat", "living quarters", "the best part of a year",
            "fall out (with someone)", "spare a thought for", "trim a wick", "highly prized"],
    "paragraphs": [
        "Good evening, everyone. When people find out that I study lighthouse keepers, they tend to picture a lonely "
        "old man with a beard, gazing out to sea. In reality, most keepers worked in teams of three, and the job had "
        "far more to do with routine than with romance. My own interest goes back to my grandfather. He wasn’t a "
        "keeper himself – people often assume he was – but a boatman, who spent thirty years taking supplies out to "
        "the rock stations off the west coast of Scotland and came home with stories about the men he met there.",
        "The keeper’s most important duty, of course, was the light itself. Before electricity arrived, the lamps "
        "burned paraffin, and every morning began with hours of trimming wicks and polishing lenses, because even a "
        "thin film of soot could cut the range of the beam by several miles. Visitors were often struck by the "
        "contrast between the lens room, which was spotless, and the living quarters, which were rather less so. "
        "Keepers were inspected regularly, and what the inspectors examined first wasn’t the kitchen or the "
        "bedrooms. It was the brass.",
        "Then there was the weather. On a rock station, the relief boat was meant to arrive every four weeks, but in "
        "winter it could be held up for a month or more. One keeper’s diary from 1937 describes the men living on "
        "porridge for every meal, and says that what they missed most wasn’t meat, or even fresh vegetables. It was "
        "tobacco, and several of them took to rolling cigarettes from dried tea leaves, with predictable results. "
        "Families weren’t allowed on the rock stations at all, which is why the shore stations, where wives "
        "and children could live alongside the keepers, were so highly prized.",
        "Isolation affected people in very different ways. Some keepers took up handicrafts – there are lovely "
        "examples of ships built inside bottles, and a surprising amount of knitting. But the pastime that comes up "
        "again and again in their letters is chess. Games were often played by post against keepers on other "
        "stations, and a single game could last the best part of a year.",
        "Living so close together, the men inevitably fell out from time to time, and the authorities had an "
        "interesting way of dealing with it. A nineteenth-century rule required keepers to write down any "
        "disagreement – not in their private letters, but in a special register that the inspectors read on every "
        "visit. The idea was to discourage quarrels, and by most accounts it worked, mainly because nobody wanted "
        "their arguments discussed at headquarters.",
        "Automation finally brought the profession to an end, and the last keepers left their stations in the late "
        "nineteen-nineties. Many of them found the change hard. One man I interviewed told me that what he missed "
        "wasn’t the sea, or even the solitude, but the clock: the fact that every hour of his day had had a purpose. "
        "As for the buildings, several have been turned into holiday cottages, and one, rather fittingly, has become "
        "a small museum, run by the grandchildren of its last keeper. So the next time you see a lighthouse on a "
        "postcard, spare a thought for the people who kept it shining, often in conditions most of us would find "
        "impossible.",
    ],
    "items": [
        {"n": 7, "sentence": "The speaker’s grandfather worked as a ___, taking provisions to remote lighthouses.",
         "key": "boatman", "evidence": "but a boatman",
         "why": "Corrige una idea extendida: {{He wasn’t a keeper himself – people often assume he was – but a "
                "boatman}}. La frase del papel ya anuncia el oficio con {{worked as a}}.",
         "wrong": [{"answer": "keeper", "kind": "candidato", "why": "Lo descarta: {{He wasn’t a keeper himself}}."},
                   {"answer": "boat man", "kind": "ortografía", "why": "Se escribe en una sola palabra."}],
         "theory": ["6.3", "3.3"]},
        {"n": 8, "sentence": "Until the arrival of electricity, the lamps ran on ___.",
         "key": "paraffin", "evidence": "the lamps burned paraffin",
         "why": "{{Before electricity arrived, the lamps burned paraffin}}: {{ran on}} reformula «quemaban».",
         "wrong": [{"answer": "kerosene", "kind": "sinónimo",
                    "why": "Es el nombre americano del mismo combustible, pero no es la palabra que se oye."},
                   {"answer": "parafin", "kind": "ortografía", "why": "Lleva doble f y una sola r: paraffin."}],
         "theory": ["6.4", "6.5"]},
        {"n": 9, "sentence": "The first thing inspectors checked on a visit was the ___.",
         "key": "brass", "evidence": "It was the brass",
         "why": "La negación descarta dos candidatos antes de dar la respuesta: {{what the inspectors examined first "
                "wasn’t the kitchen or the bedrooms. It was the brass}}.",
         "wrong": [{"answer": "kitchen", "kind": "candidato", "why": "Descartado: {{wasn’t the kitchen}}."},
                   {"answer": "lens room", "kind": "candidato",
                    "why": "Es lo que impresionaba a los visitantes ({{which was spotless}}), no lo que revisaban "
                           "primero los inspectores."}],
         "theory": ["6.3", "2.3"]},
        {"n": 10, "sentence": "A diary records that during a long delay, the keepers longed above all for ___.",
         "key": "tobacco", "evidence": "It was tobacco",
         "why": "La misma pauta: dos candidatos descartados y después la respuesta: {{what they missed most wasn’t "
                "meat, or even fresh vegetables. It was tobacco}}.",
         "wrong": [{"answer": "fresh vegetables", "kind": "candidato",
                    "why": "Descartado: {{or even fresh vegetables}}."},
                   {"answer": "porridge", "kind": "candidato",
                    "why": "Es lo que comían ({{living on porridge for every meal}}), no lo que echaban de menos."},
                   {"answer": "tobaco", "kind": "ortografía", "why": "Lleva doble c: tobacco."}],
         "theory": ["6.3", "6.5"]},
        {"n": 11, "sentence": "The ___ were popular postings because keepers’ families could live there.",
         "key": "shore stations", "evidence": "the shore stations",
         "why": "La condición de la frase (las familias) solo la cumplen las estaciones de costa: {{the shore stations, "
                "where wives and children could live alongside the keepers, were so highly prized}}. El verbo "
                "{{were}} del papel pide un plural.",
         "wrong": [{"answer": "rock stations", "kind": "candidato",
                    "why": "Allí las familias no podían vivir: {{Families weren’t allowed on the rock stations at "
                           "all}}."},
                   {"answer": "shore station", "kind": "forma",
                    "why": "Se oye en plural y la frase lo exige ({{were}})."}],
         "theory": ["6.3", "6.4"]},
        {"n": 12, "sentence": "The hobby that keepers refer to most frequently in their correspondence is ___.",
         "key": "chess", "evidence": "in their letters is chess",
         "why": "Después del contraste con {{But}}: {{the pastime that comes up again and again in their letters is "
                "chess}}. En el papel, {{correspondence}} reformula {{letters}}.",
         "wrong": [{"answer": "knitting", "kind": "candidato",
                    "why": "Aparece como ejemplo de manualidades, antes del contraste con {{But}}."},
                   {"answer": "handicrafts", "kind": "candidato",
                    "why": "Es lo que hacían algunos ({{Some keepers took up handicrafts}}), no lo que más se "
                           "menciona."}],
         "theory": ["6.3", "2.3"]},
        {"n": 13, "sentence": "Any argument between keepers had to be noted in a ___ that officials examined.",
         "key": "(special) register", "evidence": "in a special register",
         "why": "Descarta las cartas y da la respuesta: {{not in their private letters, but in a special register that the inspectors read on every "
                "visit}}. Se acepta con o sin {{special}}.",
         "wrong": [{"answer": "letters", "kind": "candidato",
                    "why": "Descartado ({{not in their private letters}}), y además no encaja tras {{a}}."},
                   {"answer": "registry", "kind": "sinónimo", "why": "No es la palabra que se oye."}],
         "theory": ["6.3", "6.4"]},
        {"n": 14, "sentence": "A former keeper told the speaker that, once he had left, it was the ___ he missed most.",
         "key": "clock", "evidence": "but the clock",
         "why": "Otra vez dos negaciones antes de la respuesta: {{what he missed wasn’t the sea, or even the solitude, "
                "but the clock}}.",
         "wrong": [{"answer": "sea", "kind": "candidato", "why": "Descartado: {{wasn’t the sea}}."},
                   {"answer": "solitude", "kind": "candidato", "why": "Descartado: {{or even the solitude}}."}],
         "theory": ["6.3", "2.3"]},
        {"n": 15, "sentence": "One former lighthouse is now a ___, managed by the family of the last keeper.",
         "key": "(small) museum", "evidence": "has become a small museum",
         "why": "Es el único edificio que gestiona la familia: {{one, rather fittingly, has become a small museum, run "
                "by the grandchildren of its last keeper}}. Se acepta con o sin {{small}}.",
         "wrong": [{"answer": "holiday cottage", "kind": "candidato",
                    "why": "Es el destino de otros faros ({{several have been turned into holiday cottages}}); no lo "
                           "gestiona la familia del último farero."}],
         "theory": ["6.3", "6.4"]},
    ],
}


if __name__ == "__main__":
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
        print("Uso: python3 gen_LST-P2.py --demo | mis_hojas.py [carpeta_salida] [--no-audio] [--no-asr]\n"
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
