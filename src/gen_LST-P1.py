# gen_LST-P1.py · Generador de Listening Part 1 (tres extractos, opcion multiple) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py y lst_audio.py en la misma carpeta (no modifica ninguno).
#
# QUE HACE
#   - Hoja de practica completa en PDF: preguntas 1-6, hoja de respuestas y soluciones (transcripcion con la
#     frase que da cada respuesta resaltada, por que es correcta la clave y por que falla cada distractor).
#   - MP3 con el mismo nombre: guion del examen (rubrica, 15 s de lectura por extracto, tono, extracto, 2 s,
#     tono, repeticion, 5 s), voces neuronales con la velocidad ajustada a la de la hoja.
#   - Bloques sueltos para un simulacro (SIM): preguntas, hoja de respuestas, soluciones y eventos de audio.
#   - Verificacion automatica: del contenido antes de generar; del PDF (restos de marcado) y del audio
#     (velocidad real y reconocimiento de voz de cada extracto) despues.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_LST-P1.py --demo [carpeta_salida]          -> hoja de ejemplo (contenido de la 01, como 99)
#   python3 gen_LST-P1.py mis_hojas.py [carpeta_salida]    -> mis_hojas.py define SPECS = [spec, ...]
#   Opciones: --no-audio (solo PDF) · --no-asr (sin reconocimiento de voz)
#   Por etapas (claude.ai corta cada comando a los 5 minutos y una hoja completa con reconocimiento de voz
#   tarda mas; la sintesis queda en la cache, asi que cada etapa reaprovecha la anterior):
#   python3 gen_LST-P1.py mis_hojas.py salida --num 03 --stage pdf      (verifica y genera el PDF)
#   python3 gen_LST-P1.py mis_hojas.py salida --num 03 --stage audio    (MP3 + velocidad de cada extracto)
#   python3 gen_LST-P1.py mis_hojas.py salida --num 03 --stage asr1     (asr2, asr3: un extracto por llamada)
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_lp1", "/ruta/gen_LST-P1.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, info = gen.verify(spec)
#   gen.make(spec, "/mnt/user-data/outputs")
#   story += gen.question_flowables(spec)          # para un SIM
#   events += gen.audio_events(spec, standalone=False)
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num         "03"
#   subtitle    "Hoja 03 · … · dificultad 3 de 4"                         (espanol)
#   difficulty  1-4
#   wpm         velocidad objetivo de los extractos (160 en la 01 … 185 en la 04)
#   lex         lexico para el modulo LEX (no se imprime; se usa en el resumen de cierre)
#   extracts    3 diccionarios:
#     ctx         frase introductoria, tal como la lee el narrador: "You hear two friends discussing …"
#     speakers    {"Woman": "Libby", "Man": "Ryan"}   etiqueta -> voz de lst_audio.VOICES (no el narrador)
#     turns       [("Woman", "texto"), …]              monologo: un solo turno
#     items       2 diccionarios:
#       n           1
#       type        uno de TYPES (los de §5.3 de la teoria)
#       stem        enunciado (ingles)
#       options     [A, B, C] (ingles)
#       key         "B"
#       evidence    ["frase literal"]  la frase (o frases) que da la respuesta; se resalta en la transcripcion
#       why         por que es correcta la clave; al menos una cita {{…}} del extracto
#       theory      secciones de LST_Teoria_v1 (ver THEORY)
#       distractors {"A": {"kinds": ["4.1"], "why": "… {{cita}} …"}, …}   los dos que no son la clave
#
#   Marcado en why (y en cualquier texto en espanol):
#     {{texto}}   -> cita literal del extracto, en serif; se comprueba que existe tal cual
#     [[texto]]   -> ingles en serif sin comprobar
#     [[!TEXTO]]  -> ingles en serif y negrita
#
# QUE COMPRUEBA verify()
#   tres extractos de dos preguntas, numeracion 1-6 · frase introductoria · voces validas, distintas del
#   narrador y sin repetirse entre extractos · al menos un dialogo · 140-200 palabras por extracto · 3 opciones
#   distintas · clave valida · dos distractores explicados con su tipo (§4.x) · citas y frases-respuesta
#   literales en su extracto · cada letra es clave entre 1 y 3 veces · la clave no es la opcion mas larga en mas
#   de dos preguntas · secciones de teoria existentes · marcado sin resolver.
# QUE COMPRUEBA verify_audio()
#   velocidad real de cada extracto (±6 % del objetivo) · parecido entre texto y reconocimiento de voz (>= 0,88) ·
#   que cada frase-respuesta se reconoce (>= 0,85).
#
# LO QUE EL GENERADOR NO PUEDE COMPROBAR (a mano)
#   - Que haya una sola respuesta defendible por pregunta y que ninguna dependa solo de la entonacion.
#   - Ingles britanico, registro C2, dificultad graduada entre hojas.
#   - Revisar el PDF renderizado y escuchar el MP3 antes de entregarlos.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
import lst_audio as A  # noqa: E402

VERSION = "1"
FIRST_ITEM = 1
N_EXTRACTS = 3
LETTERS = "ABC"
WORDS_MIN, WORDS_MAX = 140, 200
WPM_TOL = 0.06
THEORY_DOC = "LST_Teoria_v1"
CODE = "LST-P1"

TYPES = ["Idea general", "Detalle", "Función", "Propósito", "Sentimiento", "Actitud y opinión",
         "Hablante y situación", "Acuerdo"]

THEORY = {
    "1.1": "Formato, tiempos y puntuación", "1.2": "Qué cambia respecto al C1", "1.3": "El guion del examen",
    "2.1": "Habla conectada", "2.2": "Acentos del examen", "2.3": "Señales del discurso oral",
    "2.4": "Matización", "3.1": "Lo que se dice y lo que se da a entender", "3.2": "Voz propia y voces ajenas",
    "3.3": "La segunda idea manda", "3.4": "Léxico de actitud en las opciones", "3.5": "Función y propósito",
    "3.6": "Acuerdo y desacuerdo entre hablantes", "4.1": "Eco léxico", "4.2": "Mencionado y descartado",
    "4.3": "Cierto, pero no responde", "4.4": "Voz equivocada", "4.5": "Grado y alcance",
    "4.6": "Relación lógica alterada", "4.7": "Expectativa frente a realidad", "4.8": "Plausible, pero ausente",
    "5.1": "Part 1: la tarea", "5.2": "Part 1: método", "5.3": "Part 1: tipos de pregunta",
    "5.4": "Part 1: caso resuelto", "9": "Rutina de autocorrección",
}
KINDS = {"4.1": "eco léxico", "4.2": "mencionado y descartado", "4.3": "no responde", "4.4": "voz equivocada",
         "4.5": "grado y alcance", "4.6": "lógica alterada", "4.7": "expectativa", "4.8": "ausente"}

CITE_RE = re.compile(r"\{\{(.+?)\}\}")
ORDW = ["One", "Two", "Three"]


# ---------- Ingles dentro del texto en espanol ----------
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


def _text(ex):
    return _norm(" ".join(t for _, t in ex["turns"]))


def _items(spec):
    return [it for ex in spec["extracts"] for it in ex["items"]]


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _is_dialogue(ex):
    return len(ex["speakers"]) > 1


# ---------- Estilos propios (sobre la plantilla, sin cambiarla) ----------
_rub = ParagraphStyle("p1_rubric", parent=S["en"], fontSize=10, leading=14)
_exh = ParagraphStyle("p1_exh", parent=S["en"], fontName="EN-B", fontSize=11, leading=14, textColor=NAVY,
                      spaceBefore=8, spaceAfter=1)
_ctx = ParagraphStyle("p1_ctx", parent=S["en"], fontName="EN-I", textColor=INK, spaceAfter=3)
_q = ParagraphStyle("p1_q", parent=S["en"], leftIndent=22, bulletIndent=0, bulletFontName="EN-B",
                    spaceBefore=5, spaceAfter=2)
_opt = ParagraphStyle("p1_opt", parent=S["en"], leftIndent=40, bulletIndent=22, bulletFontName="EN-B",
                      spaceAfter=1.5)
_ihead = ParagraphStyle("p1_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)
_sol = ParagraphStyle("p1_sol", parent=S["body"], leftIndent=14, spaceAfter=5)
_trs = ParagraphStyle("p1_trs", parent=S["cell_en"], fontName="EN-B", fontSize=9.4, leading=13.6, textColor=NAVY)
_tr = ParagraphStyle("p1_tr", parent=S["cell_en"], fontSize=10, leading=14)


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def question_flowables(spec, with_title_block=False):
    """Rubrica y preguntas de los tres extractos."""
    a = _first(spec)
    out = []
    if with_title_block:
        out += title_block(f"{CODE} · Práctica {spec['num']}", "Three extracts", spec["subtitle"],
                           f"6 preguntas ({a}–{a + 5}) · 1 punto por pregunta · audio: "
                           f"{CODE}_Practica_{spec['num']}.mp3 · cada extracto suena dos veces, con las pausas "
                           "del examen · sin consultar la teoría")
    out.append(Paragraph(
        f"You will hear three different extracts. For questions {a}–{a + 5}, choose the answer (<b>A, B</b> or "
        "<b>C</b>) which fits best according to what you hear. There are two questions for each extract.", _rub))
    for i, ex in enumerate(spec["extracts"]):
        block = [Paragraph(f"Extract {ORDW[i]}", _exh), Paragraph(ex["ctx"], _ctx)]
        for it in ex["items"]:
            block.append(Paragraph(it["stem"], _q, bulletText=str(it["n"])))
            block += [Paragraph(o, _opt, bulletText=L) for L, o in zip(LETTERS, it["options"])]
        out.append(KeepTogether(block))
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    out = [h2(heading), p(
        "Marca una sola letra por pregunta. Al corregir, 1 punto por acierto; los errores no restan. En el examen "
        "en papel se responde en el cuadernillo y al final hay 5 minutos para pasar las respuestas a la hoja.")]
    rows = [["Nº", "A", "B", "C", "Puntos"]]
    for it in _items(spec):
        rows.append([str(it["n"]), "A", "B", "C", "&nbsp;&nbsp;&nbsp;&nbsp;/ 1"])
    rows.append(["", "", "", "<b>Total</b>", "&nbsp;&nbsp;&nbsp;&nbsp;<b>/ 6</b>"])
    out += table(rows, [20, 30, 30, 40, 50], zebra=False, en_cols=(1, 2, 3),
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 10), ("BOTTOMPADDING", (0, 1), (-1, -1), 10),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"), ("TEXTCOLOR", (1, 1), (3, -2), GREY)])
    return out


def _voices_line(ex):
    parts = []
    for lab, v in ex["speakers"].items():
        parts.append(f"{lab}: {v}, inglés {A.ACCENTS[A.VOICES[v][1]]}")
    return "Voces · " + " · ".join(parts)


def transcript_flowables(ex):
    """Transcripcion con las frases-respuesta en negrita y el numero de la pregunta volado."""
    marks = []
    for it in ex["items"]:
        for ev in it["evidence"]:
            marks.append((ev, it["n"]))
    rows = []
    for lab, txt in ex["turns"]:
        for ev, n in marks:
            if ev in txt:
                txt = txt.replace(ev, f"<b>{ev}</b><super><font size=7 color='#A4243B'>&nbsp;{n}</font></super>", 1)
        rows.append([Paragraph(lab, _trs), Paragraph(txt, _tr)] if _is_dialogue(ex) else [Paragraph(txt, _tr)])
    widths = [22 * mm, CONTENT_W - 22 * mm] if _is_dialogue(ex) else [CONTENT_W]
    t = Table(rows, colWidths=widths)
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
        "1 punto por acierto. Para cada extracto: la transcripción, con la frase que da cada respuesta en negrita "
        "y el número de la pregunta; después, por qué la clave es correcta y por qué falla cada distractor, con su "
        f"tipo (§4) y la cita que lo descarta. Los números de sección remiten a {THEORY_DOC}."))
    out.append(h2("Clave rápida") if not heading else h3("Clave rápida"))
    rows = [["Nº", "Clave", "Tipo de pregunta", "Distractores", "Teoría"]]
    for it in _items(spec):
        dis = " · ".join(f"{L} §{'/'.join(it['distractors'][L]['kinds'])}" for L in LETTERS if L != it["key"])
        rows.append([str(it["n"]), f"<b>{it['key']}</b>", it["type"], dis, " · ".join("§" + s for s in it["theory"])])
    out += table(rows, [12, 14, 38, 66, 40])
    for i, ex in enumerate(spec["extracts"]):
        head = [h2(f"Extract {ORDW[i]}") if not heading else h3(f"Extract {ORDW[i]}"),
                Paragraph(ex["ctx"], _ctx), Paragraph(_voices_line(ex), S["small"])]
        out.append(KeepTogether(head + transcript_flowables(ex)))
        for it in ex["items"]:
            block = [Paragraph(f"{it['n']} · {it['key']} · {it['type']}", _ihead),
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
def audio_extracts(spec):
    out = []
    for i, ex in enumerate(spec["extracts"]):
        out.append({"ctx": ex["ctx"], "wpm": spec["wpm"], "id": f"{CODE}-{spec['num']}-E{i + 1}",
                    "turns": [(ex["speakers"][lab], txt) for lab, txt in ex["turns"]]})
    return out


def audio_events(spec, standalone=True):
    """Eventos de lst_audio. standalone=True antepone la identificacion de la pista (hoja suelta)."""
    ev = A.opening(f"Proficiency Listening. Part One practice, number {A.n2w(int(spec['num']))}.") if standalone else []
    return ev + A.script_part1(audio_extracts(spec), first=_first(spec))


def build_audio(spec, out_path):
    return A.render(audio_events(spec), out_path)


def verify_audio(spec, report, asr=True):
    errs, lines = [], []
    for i, ex in enumerate(spec["extracts"]):
        r = report["recs"][f"{CODE}-{spec['num']}-E{i + 1}"]
        dev = r["wpm_speech"] / spec["wpm"] - 1
        line = (f"Extract {i + 1}: {r['words']} palabras · {r['total_s']} s · {r['wpm_speech']} ppm "
                f"(objetivo {spec['wpm']}) · rates {r['rates']}")
        if abs(dev) > WPM_TOL:
            errs.append(f"Extract {i + 1}: velocidad {r['wpm_speech']} ppm fuera de ±{WPM_TOL:.0%} de {spec['wpm']}")
        if asr:
            phrases = [ev for it in ex["items"] for ev in it["evidence"]]
            chk = A.check_recording(r["wav"], _text(ex), phrases)
            line += f" · ASR {chk['sim']}"
            bad = [f"«{f[:40]}» {s}" for f, s in chk["phrases"] if s < 0.85]
            if not chk["ok"]:
                errs.append(f"Extract {i + 1}: reconocimiento de voz {chk['sim']}; frases mal reconocidas: {bad}\n"
                            f"    ASR: {chk['asr']}")
        lines.append(line)
    return errs, lines


# ---------- Verificacion del contenido ----------
def verify(spec):
    errs = []
    exs = spec.get("extracts", [])
    if len(exs) != N_EXTRACTS:
        return [f"hacen falta {N_EXTRACTS} extractos (hay {len(exs)})"], {}
    if not isinstance(spec.get("wpm"), (int, float)) or not 140 <= spec["wpm"] <= 200:
        errs.append("wpm ausente o fuera de 140-200")
    a = _first(spec)
    items = _items(spec)
    if [it.get("n") for it in items] != list(range(a, a + 2 * N_EXTRACTS)):
        errs.append(f"numeración: se esperaban {a}–{a + 2 * N_EXTRACTS - 1}, dos por extracto")
    used, words_info = {}, []
    for i, ex in enumerate(exs, 1):
        if len(ex.get("items", [])) != 2:
            errs.append(f"extracto {i}: hacen falta dos preguntas")
        if not ex.get("ctx", "").startswith("You hear ") or not ex["ctx"].endswith("."):
            errs.append(f"extracto {i}: la frase introductoria debe empezar por 'You hear' y acabar en punto")
        for lab, v in ex.get("speakers", {}).items():
            if v not in A.VOICES or v == A.NARRATOR:
                errs.append(f"extracto {i}: voz no válida para '{lab}': {v}")
            if v in used and used[v] != i:
                errs.append(f"extracto {i}: la voz {v} ya se usa en el extracto {used[v]}")
            used[v] = i
        if _is_dialogue(ex) and len(set(ex["speakers"].values())) < len(ex["speakers"]):
            errs.append(f"extracto {i}: dos hablantes con la misma voz")
        for lab, _ in ex.get("turns", []):
            if lab not in ex.get("speakers", {}):
                errs.append(f"extracto {i}: hablante sin voz asignada: {lab}")
        if not _is_dialogue(ex) and len(ex["turns"]) != 1:
            errs.append(f"extracto {i}: un monólogo va en un solo turno")
        txt = _text(ex)
        w = A.count_words(txt)
        words_info.append(w)
        if not WORDS_MIN <= w <= WORDS_MAX:
            errs.append(f"extracto {i}: {w} palabras, fuera de {WORDS_MIN}–{WORDS_MAX}")
        if re.search(r"[\[\]{}<>]", txt):
            errs.append(f"extracto {i}: marcado en la transcripción")
        for it in ex.get("items", []):
            n = it.get("n", "?")
            for field in ("type", "stem", "options", "key", "evidence", "why", "theory", "distractors"):
                if not it.get(field):
                    errs.append(f"{n}: falta el campo '{field}'")
            if it.get("type") not in TYPES:
                errs.append(f"{n}: tipo de pregunta desconocido '{it.get('type')}'")
            if it.get("type") == "Acuerdo" and not _is_dialogue(ex):
                errs.append(f"{n}: una pregunta de acuerdo necesita un diálogo")
            opts = it.get("options", [])
            if len(opts) != 3 or len(set(opts)) != 3 or not all(o.strip() for o in opts):
                errs.append(f"{n}: hacen falta tres opciones distintas")
            for o in opts:
                if re.search(r"[\[\]{}<>]", o):
                    errs.append(f"{n}: marcado en una opción")
            key = it.get("key")
            if key not in LETTERS:
                errs.append(f"{n}: clave no válida '{key}'")
                continue
            for s in it.get("theory", []):
                if s not in THEORY:
                    errs.append(f"{n}: sección de teoría inexistente §{s}")
            for ev in it.get("evidence", []):
                if not any(ev in t for _, t in ex["turns"]):
                    errs.append(f"{n}: frase-respuesta no literal o repartida entre turnos: «{ev[:50]}»")
            if not CITE_RE.findall(it.get("why", "")):
                errs.append(f"{n}: la explicación de la clave no cita el extracto")
            dis = it.get("distractors", {})
            if set(dis) != set(LETTERS) - {key}:
                errs.append(f"{n}: distractores explicados {sorted(dis)}; se esperaban {sorted(set(LETTERS) - {key})}")
            texts = [("why", it.get("why", ""))] + [(f"distractor {L}", d.get("why", "")) for L, d in dis.items()]
            for L, d in dis.items():
                if not d.get("kinds") or any(k not in KINDS for k in d["kinds"]):
                    errs.append(f"{n}{L}: tipo de distractor ausente o desconocido {d.get('kinds')}")
            for field, t in texts:
                for c in CITE_RE.findall(t):
                    if _norm(c) not in txt:
                        errs.append(f"{n} ({field}): cita inexistente en el extracto: «{c[:50]}»")
                if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(t)):
                    errs.append(f"{n}: marcado sin resolver en '{field}'")
    if not any(_is_dialogue(ex) for ex in exs):
        errs.append("la hoja necesita al menos un diálogo")
    keys = "".join(it.get("key", "?") for it in items)
    for L in LETTERS:
        if not 1 <= keys.count(L) <= 3:
            errs.append(f"la letra {L} es clave {keys.count(L)} veces (entre 1 y 3)")
    longest = []
    for it in items:
        if it.get("key") in LETTERS and len(it.get("options", [])) == 3:
            lens = [len(o) for o in it["options"]]
            k = LETTERS.index(it["key"])
            if lens[k] == max(lens) and lens.count(max(lens)) == 1:
                longest.append(it["n"])
    if len(longest) > 2:
        errs.append(f"la clave es la opción más larga en {len(longest)} preguntas: {longest}")
    return errs, {"words": words_info, "keys": keys, "longest": longest}


def check_pdf(path):
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            txt = "\n".join(pg.extract_text() or "" for pg in pdf.pages)
    except ImportError:
        from pypdf import PdfReader
        txt = "\n".join(pg.extract_text() or "" for pg in PdfReader(path).pages)
    return re.findall(r"\{\{|\}\}|\[\[|\]\]|<font|</?b>|<br|<super|&nbsp", txt)


def make(spec, out_dir="/mnt/user-data/outputs", audio=True, asr=True):
    """Verifica, genera PDF y MP3 y comprueba ambos. Devuelve (pdf, mp3); lanza ValueError si algo falla."""
    errs, info = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}:\n  - " + "\n  - ".join(errs))
    base = os.path.join(out_dir, f"{CODE}_Practica_{spec['num']}")
    pdf = build_sheet(spec, base + ".pdf")
    left = check_pdf(pdf)
    if left:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {left}")
    print(f"{CODE}_Practica_{spec['num']}.pdf · palabras por extracto {info['words']} · claves {info['keys']} · "
          f"clave más larga en {info['longest'] or 'ninguna'} · verificación sin errores")
    mp3 = None
    if audio:
        A.setup(asr=asr)
        mp3 = base + ".mp3"
        rep = build_audio(spec, mp3)
        aerrs, lines = verify_audio(spec, rep, asr=asr)
        for ln in lines:
            print("  " + ln)
        m, s = divmod(int(round(rep["duration_s"])), 60)
        print(f"{CODE}_Practica_{spec['num']}.mp3 · {m}:{s:02d} · narrador rate {rep['narrator_rate']:+d} %")
        if aerrs:
            raise ValueError(f"Hoja {spec['num']} (audio):\n  - " + "\n  - ".join(aerrs))
        spec["_audio_report"] = rep
    return pdf, mp3


def stage(spec, out_dir, what, idx=None):
    """Generacion por etapas, para entornos que cortan cada comando a los 5 minutos (claude.ai):
    'pdf' verifica y genera el PDF · 'audio' genera el MP3 y guarda el informe en la cache ·
    'asr' comprueba un extracto (idx = 1, 2 o 3) con reconocimiento de voz. Devuelve True si todo va bien."""
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
        print(f"{CODE}_Practica_{spec['num']}.pdf · palabras {info['words']} · claves {info['keys']} · "
              f"clave más larga en {info['longest'] or 'ninguna'} · restos {left or 'ninguno'}")
        return not left
    if what == "audio":
        A.setup(asr=False)
        rep = build_audio(spec, base + ".mp3")
        json.dump(rep, open(rep_path, "w"), default=str)
        m, s = divmod(int(round(rep["duration_s"])), 60)
        print(f"{CODE}_Practica_{spec['num']}.mp3 · {m}:{s:02d} · narrador {rep['narrator_rate']:+d} %")
        errs, lines = verify_audio(spec, rep, asr=False)
        print("\n".join("  " + ln for ln in lines + errs))
        return not errs
    if what == "asr":
        A.setup(asr=True)
        rep = json.load(open(rep_path))
        one = dict(spec, extracts=[spec["extracts"][idx - 1]])
        r = rep["recs"][f"{CODE}-{spec['num']}-E{idx}"]
        rep1 = {"recs": {f"{CODE}-{spec['num']}-E1": r}}
        errs, lines = verify_audio(one, rep1, asr=True)
        print(f"  Extract {idx}: " + lines[0].split(": ", 1)[1])
        print("\n".join("  " + e for e in errs))
        return not errs
    raise ValueError(what)


# ---------- Hoja de ejemplo: contenido de LST-P1_Practica_01, numerada como 99 ----------
def _demo():
    import copy
    d = copy.deepcopy(DEMO_SPEC)
    d["num"], d["subtitle"] = "99", "Hoja de prueba del generador (contenido de LST-P1_Practica_01)"
    return d


DEMO_SPEC = {
    "num": "01",
    "subtitle": "Hoja 01 · Detalle, opinión explícita y acuerdo · dificultad 1 de 4",
    "difficulty": 1,
    "wpm": 160,
    "lex": ["see the light of day", "break the spell", "how it was coming along", "mundane",
            "I’ll give them that", "make it (triunfar)", "more often than I’d care to admit", "late developer"],
    "extracts": [
        {"ctx": "You hear a novelist talking about writing her second book.",
         "speakers": {"Novelist": "Sonia"},
         "turns": [("Novelist",
                    "Everyone warns you about the second novel, and I assumed they were exaggerating. The first one "
                    "I’d written in the evenings, for nobody in particular, with no idea whether it would ever see "
                    "the light of day. The second came with a deadline, an advance and an editor who kept asking, "
                    "very politely, how it was coming along. I’d sit down at nine, and by eleven I’d have rewritten "
                    "the same paragraph four times. What finally broke the spell was rather mundane. I stopped "
                    "working at my desk, which had started to feel like a courtroom, and took a notebook to the café "
                    "round the corner, where nobody knew or cared what I was doing. The book I eventually handed in "
                    "is not the one I set out to write. It’s quieter, less ambitious on the surface. But I’d say it’s "
                    "more honest, and I’m prouder of it than I am of the first, which still surprises me.")],
         "items": [
             {"n": 1, "type": "Detalle",
              "stem": "What does the novelist say about writing her second book?",
              "options": ["It was hard to make progress because of the pressure she was under.",
                          "She regretted having accepted an advance for it.",
                          "It went better once she kept to a strict daily routine."],
              "key": "A",
              "evidence": ["by eleven I’d have rewritten the same paragraph four times"],
              "why": "La presión está enumerada ({{a deadline, an advance and an editor}}) y su efecto es que no "
                     "avanza: {{by eleven I’d have rewritten the same paragraph four times}}. La opción lo resume "
                     "sin repetir ninguna de esas palabras.",
              "theory": ["5.3", "3.1"],
              "distractors": {
                  "B": {"kinds": ["4.1"],
                        "why": "Recoge {{an advance}}, que es solo una parte de la presión. No dice que se arrepienta "
                               "de haberlo aceptado."},
                  "C": {"kinds": ["4.2"],
                        "why": "La rutina existía ({{I’d sit down at nine}}) y no funcionaba. Lo que la desbloqueó fue "
                               "cambiar de sitio: {{took a notebook to the café round the corner}}."}}},
             {"n": 2, "type": "Sentimiento",
              "stem": "How does she feel about the book she finally handed in?",
              "options": ["disappointed that it is less ambitious than she intended",
                          "anxious about how it will compare with her first novel",
                          "surprised by how proud she is of it"],
              "key": "C",
              "evidence": ["I’m prouder of it than I am of the first, which still surprises me"],
              "why": "Lo dice en la última frase: {{I’m prouder of it than I am of the first, which still surprises "
                     "me}}. La reacción final es la que cuenta (§3.3).",
              "theory": ["3.3", "5.3"],
              "distractors": {
                  "A": {"kinds": ["4.1", "4.2"],
                        "why": "Recoge {{less ambitious on the surface}}, pero la frase sigue con {{But I’d say it’s "
                               "more honest}}: la falta de ambición es solo aparente y no la lamenta."},
                  "B": {"kinds": ["4.8"],
                        "why": "Compara los dos libros, pero para decir que prefiere el segundo. No expresa ninguna "
                               "inquietud por la comparación: {{I’m prouder of it than I am of the first}}."}}},
         ]},
        {"ctx": "You hear two friends discussing a television documentary series.",
         "speakers": {"Woman": "Libby", "Man": "Ryan"},
         "turns": [
             ("Woman", "Did you catch the final episode of that ocean series last night?"),
             ("Man", "I did. Visually it was extraordinary – those shots of the squid at two thousand metres. I’ve no "
                     "idea how they managed it."),
             ("Woman", "Oh, the camera work’s never been the problem. It’s the narration I can’t stand. Every time "
                       "they show you something remarkable, there’s this booming voice telling you how remarkable it "
                       "is, as if you couldn’t work it out for yourself."),
             ("Man", "I suppose they’re aiming at a family audience."),
             ("Woman", "Children aren’t stupid, though. My nephew watched it with me, and he was the one who asked "
                       "why the squid glowed. The programme never bothered to explain."),
             ("Man", "Fair point. Mind you, they did finish with that section on the research team, which I thought "
                     "was the best bit. You actually got a sense of how the science gets done."),
             ("Woman", "Yes, I’ll give them that. Ten minutes of substance at the end of six hours.")],
         "items": [
             {"n": 3, "type": "Actitud y opinión",
              "stem": "What does the woman criticise about the series?",
              "options": ["the quality of the underwater filming",
                          "the narrator’s habit of stating the obvious",
                          "the decision to make it for a family audience"],
              "key": "B",
              "evidence": ["there’s this booming voice telling you how remarkable it is, as if you couldn’t work it "
                           "out for yourself"],
              "why": "{{It’s the narration I can’t stand}}: la voz cuenta lo que el espectador ya ve, {{telling you "
                     "how remarkable it is, as if you couldn’t work it out for yourself}}. Eso es decir lo obvio.",
              "theory": ["5.3", "3.2"],
              "distractors": {
                  "A": {"kinds": ["4.2"],
                        "why": "Lo menciona para descartarlo: {{the camera work’s never been the problem}}."},
                  "C": {"kinds": ["4.4"],
                        "why": "El público familiar es la explicación que propone él ({{I suppose they’re aiming at a "
                               "family audience}}). Ella no critica que vaya dirigida a familias, sino que trate a los "
                               "niños como si no entendieran: {{Children aren’t stupid, though}}."}}},
             {"n": 4, "type": "Acuerdo",
              "stem": "What do the two friends agree about?",
              "options": ["The series went on for longer than necessary.",
                          "Children would have enjoyed it more than adults.",
                          "The part about the scientists was worthwhile."],
              "key": "C",
              "evidence": ["which I thought was the best bit", "Yes, I’ll give them that"],
              "why": "Él: {{that section on the research team, which I thought was the best bit}}. Ella lo concede: "
                     "{{Yes, I’ll give them that}}. Es el único punto que suscriben los dos (§3.6).",
              "theory": ["3.6", "2.4"],
              "distractors": {
                  "A": {"kinds": ["4.4"],
                        "why": "Solo lo da a entender ella, con ironía: {{Ten minutes of substance at the end of six "
                               "hours}}. Él no dice nada parecido."},
                  "B": {"kinds": ["4.8"],
                        "why": "Hablan de un niño que vio la serie ({{My nephew watched it with me}}), pero nadie "
                               "compara cuánto la disfrutarían niños y adultos."}}},
         ]},
        {"ctx": "You hear a sports coach talking about working with young athletes.",
         "speakers": {"Coach": "Andrew"},
         "turns": [("Coach",
                    "When I started coaching, I thought my job was to spot talent. You watch a group of "
                    "twelve-year-olds, one of them is obviously quicker, stronger, better coordinated, and you pour "
                    "your energy into that child. It took me an embarrassingly long time to notice that the stars at "
                    "twelve were very rarely the ones still competing at eighteen. Often they’d simply grown early, "
                    "and once everyone else caught up, it turned out they’d never had to learn how to lose. The late "
                    "developers, on the other hand, had spent years being beaten and had worked out how to deal with "
                    "it. So these days I’m far more interested in how a youngster responds to a bad afternoon than in "
                    "how fast they run on a good one. I’m also much more careful about telling parents their child is "
                    "going to make it. I’ve said it before, and I’ve been wrong more often than I’d care to admit.")],
         "items": [
             {"n": 5, "type": "Detalle",
              "stem": "What point does the coach make about athletes who stand out at the age of twelve?",
              "options": ["They need more support than other children.",
                          "They often owe their early success to physical maturity.",
                          "They are frequently pushed too hard by their parents."],
              "key": "B",
              "evidence": ["Often they’d simply grown early"],
              "why": "{{Often they’d simply grown early}}: su ventaja era haber crecido antes que los demás, y "
                     "desaparecía {{once everyone else caught up}}.",
              "theory": ["5.3", "3.1"],
              "distractors": {
                  "A": {"kinds": ["4.4"],
                        "why": "Es lo que él pensaba al empezar ({{you pour your energy into that child}}), la idea "
                               "que ha abandonado."},
                  "C": {"kinds": ["4.1"],
                        "why": "Los padres aparecen más tarde y en otro contexto ({{telling parents their child is "
                               "going to make it}}). Nadie habla de presionar a los niños."}}},
             {"n": 6, "type": "Detalle",
              "stem": "What does the coach admit about his conversations with parents?",
              "options": ["He has been too optimistic in the past.",
                          "He finds their expectations difficult to deal with.",
                          "He now refuses to discuss their children’s prospects."],
              "key": "A",
              "evidence": ["I’ve said it before, and I’ve been wrong more often than I’d care to admit"],
              "why": "Ha dicho a padres que su hijo llegaría lejos y se ha equivocado: {{I’ve said it before, and I’ve "
                     "been wrong more often than I’d care to admit}}. Es decir, ha sido demasiado optimista.",
              "theory": ["5.3", "2.4"],
              "distractors": {
                  "B": {"kinds": ["4.8"],
                        "why": "Habla de sus propios errores, no de lo que esperan los padres."},
                  "C": {"kinds": ["4.5"],
                        "why": "Dice {{much more careful}}, no que se niegue a hablar del tema."}}},
         ]},
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
        print("Uso: python3 gen_LST-P1.py --demo | mis_hojas.py [carpeta_salida] [--no-audio] [--no-asr]\n"
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
