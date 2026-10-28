# gen_LST-P4.py · Generador de Listening Part 4 (cinco monologos, dos tareas de emparejamiento) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py y lst_audio.py en la misma carpeta (no modifica ninguno).
#
# QUE HACE
#   - Hoja de practica completa en PDF: Task One (21-25) y Task Two (26-30) con la maqueta del examen, hoja de
#     respuestas y soluciones (transcripcion con las frases-respuesta resaltadas; para cada hablante, la clave de
#     cada tarea y por que fallan las opciones que roza; al final, por que sobran las tres opciones de cada lista).
#   - MP3 con el mismo nombre: guion del examen (rubrica de las dos tareas, 45 s de lectura, tono, los cinco
#     hablantes seguidos en una sola grabacion, 5 s, 'Now you will hear Part Four again', tono, repeticion, 5 s, fin).
#   - Bloques sueltos para un simulacro (SIM): preguntas, hoja de respuestas, soluciones y eventos de audio.
#   - Verificacion automatica del contenido, del PDF y del audio (velocidad por voz, reconocimiento de voz de cada
#     hablante y lista de diferencias entre el texto y el ASR, para reformular lo que la voz deforma).
#
# USO
#   python3 gen_LST-P4.py --demo [carpeta_salida]          -> hoja de ejemplo (contenido de la 01, como 99)
#   python3 gen_LST-P4.py mis_hojas.py [carpeta_salida]    -> mis_hojas.py define SPECS = [spec, ...]
#   Opciones: --no-audio · --no-asr
#   Por etapas (claude.ai corta cada comando a los 5 minutos; la sintesis queda en la cache):
#   python3 gen_LST-P4.py mis_hojas.py salida --num 03 --stage pdf | audio | asr1 | asr2 | asr3
#   (asr1: hablantes 1-2 · asr2: hablantes 3-4 · asr3: hablante 5)
#   Desde otro script: importlib (ver gen_LST-P1.py); verify(spec), make(spec, carpeta), question_flowables(spec),
#   answer_sheet_flowables(spec), solutions_flowables(spec), audio_events(spec, standalone=False).
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num, subtitle, difficulty (1-4), wpm (160 en la 01 … 185 en la 04), lex (para LEX; no se imprime)
#   ctx         "You will hear five short extracts in which people are talking about …"  (rubrica; narrador y papel)
#   tasks       2 diccionarios:
#     prompt      lo que sigue a "choose from the list (A–H)": "what prompted each speaker to …"
#     options     8 opciones (ingles), A-H
#     extras      {letra: explicacion}  las tres opciones que no son clave de nadie: por que sobran
#   speakers    5 diccionarios:
#     voice       voz de lst_audio.VOICES (no el narrador; sin repetir en la hoja)
#     text        el monologo (~35 s a la velocidad de la hoja), un solo fragmento de audio
#     items       2 diccionarios (Task One, Task Two):
#       n           21-25 en la tarea 1, 26-30 en la tarea 2
#       key         "C"
#       evidence    ["frase literal", …]  se resalta en la transcripcion
#       why         por que es correcta la clave; al menos una cita {{…}} literal del monologo
#       touched     {"F": {"kinds": ["4.2"], "why": "… {{cita}} …"}, …}  opciones que el hablante roza y no son
#                   su respuesta (al menos una); tipo segun §4 y explicacion
#       theory      secciones de LST_Teoria_v1
#   Marcado en textos en espanol: {{cita literal}} · [[ingles sin comprobar]] · [[!ingles en negrita]]
#
# QUE COMPRUEBA verify()
#   rubrica · cinco hablantes con voces validas y distintas, al menos dos hombres y dos mujeres y dos acentos ·
#   30-42 s por monologo a la velocidad de la hoja · dos tareas de 8 opciones distintas · numeracion 21-30 · claves
#   distintas dentro de cada tarea y las tres que sobran explicadas · las claves no siguen el orden alfabetico ni
#   coinciden entre tareas · ningun hablante con la misma letra en las dos tareas · frases-respuesta y citas
#   literales · cada respuesta con al menos una opcion rozada y explicada · teoria existente · marcado sin resolver.
#   Informa de cuantas opciones roza cada hablante, cuantas opciones sobrantes roza alguien y en cuantos hablantes
#   la respuesta de la tarea 2 llega antes que la de la tarea 1 (§8.1).
# QUE COMPRUEBA verify_audio()
#   velocidad real de cada voz (±6 %) · duracion de la grabacion · parecido texto-ASR de cada hablante (>= 0,88) ·
#   frases-respuesta reconocidas (>= 0,85) · imprime las diferencias palabra a palabra.
#
# A MANO
#   - Que cada opcion encaje entera con un solo hablante y que las que roza cada uno queden descartadas por una frase
#     concreta (nunca por la entonacion). Antecedente frente a desencadenante, esperado frente a inesperado (§8.3).
#   - Revisar las diferencias del ASR y reformular lo que la voz deforma. Revisar el PDF y escuchar el MP3.

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
import lst_audio as A  # noqa: E402

VERSION = "1"
FIRST_ITEM = 21
N_SPEAKERS = 5
LETTERS = "ABCDEFGH"
WPM_TOL = 0.06
SEC_MIN, SEC_MAX = 30, 42          # por monologo
SPEAKER_PAUSE = 3                  # silencio entre hablantes dentro de la grabacion
THEORY_DOC = "LST_Teoria_v1"
CODE = "LST-P4"
TASKW = ["One", "Two"]

THEORY = {
    "2.1": "Habla conectada", "2.2": "Acentos del examen", "2.3": "Señales del discurso oral", "2.4": "Matización",
    "3.1": "Lo que se dice y lo que se da a entender", "3.2": "Voz propia y voces ajenas",
    "3.3": "La segunda idea manda", "3.4": "Léxico de actitud en las opciones", "3.5": "Función y propósito",
    "4.1": "Eco léxico", "4.2": "Mencionado y descartado", "4.3": "Cierto, pero no responde",
    "4.4": "Voz equivocada", "4.5": "Grado y alcance", "4.6": "Relación lógica alterada",
    "4.7": "Expectativa frente a realidad", "4.8": "Plausible, pero ausente",
    "8.1": "Part 4: la tarea", "8.2": "Dos tareas y dos audiciones", "8.3": "Trampas propias",
    "8.4": "Part 4: caso resuelto", "9": "Rutina de autocorrección",
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


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _all_text(spec):
    return _norm(" ".join(s["text"] for s in spec["speakers"]))


def word_diff(ref, hyp):
    import difflib
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes():
        if op != "equal":
            out.append(f"«{' '.join(ref[max(0, i1 - 1):i2 + 1])}» → «{' '.join(hyp[max(0, j1 - 1):j2 + 1])}»")
    return out


# ---------- Estilos propios (sobre la plantilla, sin cambiarla) ----------
_rub = ParagraphStyle("p4_rubric", parent=S["en"], fontSize=10, leading=14, spaceAfter=6)
_task = ParagraphStyle("p4_task", parent=S["en"], fontName="EN-B", fontSize=11, leading=14, textColor=NAVY,
                       spaceBefore=8, spaceAfter=2)
_tins = ParagraphStyle("p4_tins", parent=S["en"], fontSize=10, leading=13.6, spaceAfter=5)
_optc = ParagraphStyle("p4_opt", parent=S["cell_en"], fontSize=10, leading=13)
_optl = ParagraphStyle("p4_optl", parent=S["cell_en"], fontName="EN-B", fontSize=10, leading=13)
_spk = ParagraphStyle("p4_spk", parent=S["cell_en"], fontSize=10, leading=13, alignment=2)
_box = ParagraphStyle("p4_box", parent=S["cell_en"], fontName="EN-B", fontSize=8, leading=10, textColor=ACCENT)
_ihead = ParagraphStyle("p4_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)
_sol = ParagraphStyle("p4_sol", parent=S["body"], leftIndent=14, spaceAfter=4)
_trs = ParagraphStyle("p4_trs", parent=S["cell_en"], fontName="EN-B", fontSize=9.4, leading=13.6, textColor=NAVY)
_tr = ParagraphStyle("p4_tr", parent=S["cell_en"], fontSize=10, leading=14)


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def _range(spec, t):
    a = _first(spec) + 5 * t
    return a, a + 4


def task_instruction(spec, t, spoken=False):
    a, b = _range(spec, t)
    if spoken:
        return (f"For questions {A.n2w(a)} to {A.n2w(b)}, choose from the list (A to H) "
                f"{spec['tasks'][t]['prompt']}.")
    return f"For questions {a}–{b}, choose from the list (<b>A–H</b>) {spec['tasks'][t]['prompt']}."


def _task_table(spec, t):
    opts = spec["tasks"][t]["options"]
    a, _ = _range(spec, t)
    left = Table([[Paragraph(L, _optl), Paragraph(o, _optc)] for L, o in zip(LETTERS, opts)],
                 colWidths=[7 * mm, 98 * mm])
    left.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 2),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 3),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    rows = [[Paragraph(f"Speaker {k}", _spk), Paragraph(str(a + k - 1), _box)] for k in range(1, 6)]
    right = Table(rows, colWidths=[24 * mm, 14 * mm], rowHeights=[9.6 * mm] * 5)
    right.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (1, 0), (1, 0), 0.8, GREY),
                               ("BOX", (1, 1), (1, 1), 0.8, GREY), ("BOX", (1, 2), (1, 2), 0.8, GREY),
                               ("BOX", (1, 3), (1, 3), 0.8, GREY), ("BOX", (1, 4), (1, 4), 0.8, GREY),
                               ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                               ("LEFTPADDING", (1, 0), (1, -1), 2), ("RIGHTPADDING", (0, 0), (0, -1), 6)]))
    outer = Table([[left, right]], colWidths=[108 * mm, CONTENT_W - 108 * mm])
    outer.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (1, 0), (1, 0), 3),
                               ("LINEBEFORE", (1, 0), (1, 0), 0.5, RULE)]))
    return outer


def question_flowables(spec, with_title_block=False):
    a = _first(spec)
    out = []
    if with_title_block:
        out += title_block(f"{CODE} · Práctica {spec['num']}", "Multiple matching", spec["subtitle"],
                           f"10 preguntas ({a}–{a + 9}) · 1 punto por pregunta · audio: {CODE}_Practica_{spec['num']}"
                           ".mp3 · los cinco hablantes suenan seguidos y la serie entera se repite, con las pausas del "
                           "examen · sin consultar la teoría")
    out.append(Paragraph(f"{spec['ctx']} While you listen, you must complete both tasks.", _rub))
    for t in range(2):
        out.append(KeepTogether([Paragraph(f"TASK {TASKW[t].upper()}", _task),
                                 Paragraph(task_instruction(spec, t), _tins), _task_table(spec, t), Spacer(1, 6)]))
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    a = _first(spec)
    out = [h2(heading), p(
        "Una letra por casilla; en cada tarea, cada letra se usa una sola vez y sobran tres. 1 punto por acierto; "
        "los errores no restan. En el examen en papel se responde en el cuadernillo y al final hay 5 minutos para "
        "pasar las respuestas a la hoja.")]
    rows = [["Hablante", "Nº", "Task One", "Nº", "Task Two", "Puntos"]]
    for k in range(5):
        rows.append([f"Speaker {k + 1}", str(a + k), "", str(a + 5 + k), "", "&nbsp;&nbsp;&nbsp;&nbsp;/ 2"])
    rows.append(["", "", "", "", "<b>Total</b>", "&nbsp;&nbsp;&nbsp;&nbsp;<b>/ 10</b>"])
    out += table(rows, [28, 14, 36, 14, 36, 42], zebra=False, en_cols=(0,),
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 11), ("BOTTOMPADDING", (0, 1), (-1, -1), 11),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"), ("LINEBELOW", (2, 1), (2, -2), 0.6, GREY),
                        ("LINEBELOW", (4, 1), (4, -2), 0.6, GREY)])
    return out


def _voice_desc(v):
    return f"{v}, inglés {A.ACCENTS[A.VOICES[v][1]]}"


def transcript_flowables(spec):
    rows = []
    for k, sp in enumerate(spec["speakers"], 1):
        txt = sp["text"]
        for it in sp["items"]:
            for ev in it["evidence"]:
                if ev in txt:
                    txt = txt.replace(ev, f"<b>{ev}</b><super><font size=7 color='#A4243B'>&nbsp;{it['n']}</font>"
                                          "</super>", 1)
        rows.append([Paragraph(f"Speaker {k}", _trs), Paragraph(txt, _tr)])
    t = Table(rows, colWidths=[22 * mm, CONTENT_W - 22 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_EJ), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, 0), 7), ("BOTTOMPADDING", (0, -1), (-1, -1), 7),
        ("LINEBEFORE", (0, 0), (0, -1), 1.8, GREY)]))
    return [t, Spacer(1, 6)]


def solutions_flowables(spec, with_band=True, heading=None):
    H2 = h2 if not heading else h3
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(
        "1 punto por acierto. Después de la clave rápida va la transcripción, con la frase que da cada respuesta en "
        "negrita y el número de la pregunta. Para cada hablante se explica la clave de cada tarea y por qué no valen "
        "las opciones que roza, con su tipo (§4) y la cita que las descarta. Al final, por qué sobran las tres "
        f"opciones restantes de cada lista. Los números de sección remiten a {THEORY_DOC}."))
    out.append(H2("Clave rápida"))
    rows = [["Hablante", "Task One", "Task Two"]]
    for k, sp in enumerate(spec["speakers"], 1):
        cells = []
        for t, it in enumerate(sp["items"]):
            cells.append(f"<b>{it['n']} · {it['key']}</b>&nbsp;&nbsp;"
                         + E(spec["tasks"][t]["options"][LETTERS.index(it["key"])]))
        rows.append([f"Speaker {k}"] + cells)
    out += table(rows, [24, 73, 73])
    out += [H2("Transcripción"), Paragraph(
        "Voces · " + " · ".join(f"{k}: {_voice_desc(sp['voice'])}" for k, sp in enumerate(spec["speakers"], 1)),
        S["small"])]
    out += transcript_flowables(spec)
    exp_head = H2("Explicaciones")
    for k, sp in enumerate(spec["speakers"], 1):
        block = [exp_head] if k == 1 else []
        i1, i2 = sp["items"]
        block.append(Paragraph(f"Speaker {k} · {i1['n']} {i1['key']} · {i2['n']} {i2['key']}", _ihead))
        for t, it in enumerate(sp["items"]):
            opts = spec["tasks"][t]["options"]
            block.append(Paragraph(f"<b>Task {TASKW[t]} · {it['key']}</b>&nbsp;&nbsp;{E(opts[LETTERS.index(it['key'])])}"
                                   f"<br/><b>Correcta.</b> {markup(it['why'])}", _sol))
            for L in sorted(it["touched"]):
                d = it["touched"][L]
                kinds = ", ".join(f"{KINDS[x]} §{x}" for x in d["kinds"])
                block.append(Paragraph(f"<b>No es {L}</b>&nbsp;&nbsp;{E(opts[LETTERS.index(L)])} "
                                       f"<b>({kinds}).</b> {markup(d['why'])}", _sol))
        th = []
        for it in sp["items"]:
            th += [s_ for s_ in it["theory"] if s_ not in th]
        block.append(p("<b>Teoría:</b> " + " · ".join(f"§{s_} {THEORY[s_]}" for s_ in th)))
        out.append(KeepTogether(block + [Spacer(1, 4)]))
    blk = [H2("Opciones que sobran")]
    for t, task in enumerate(spec["tasks"]):
        blk.append(Paragraph(f"<b>Task {TASKW[t]}</b>", _ihead))
        for L in sorted(task["extras"]):
            blk.append(Paragraph(f"<b>{L}</b>&nbsp;&nbsp;{E(task['options'][LETTERS.index(L)])}<br/>"
                                 f"{markup(task['extras'][L])}", _sol))
    out.append(KeepTogether(blk))
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
    turns = []
    for sp in spec["speakers"]:
        if turns:
            turns.append(("_pause", SPEAKER_PAUSE))
        turns.append((sp["voice"], sp["text"]))
    return turns


def audio_events(spec, standalone=True):
    rubric = ["Part Four consists of two tasks.", spec["ctx"], "Look at Task One. " + task_instruction(spec, 0, True),
              "Now look at Task Two. " + task_instruction(spec, 1, True), "While you listen, you must complete both tasks."]
    ev = A.opening(f"Proficiency Listening. Part Four practice, number {A.n2w(int(spec['num']))}.") \
        if standalone else []
    return ev + A.script_part(4, rubric, 45, audio_turns(spec), spec["wpm"], rec_id=_rec_id(spec))


def build_audio(spec, out_path):
    return A.render(audio_events(spec), out_path)


ASR_GROUPS = {1: [1, 2], 2: [3, 4], 3: [5]}


def verify_audio(spec, report, asr=True, part=None):
    errs, lines = [], []
    r = report["recs"][_rec_id(spec)]
    m, s = divmod(int(round(r["total_s"])), 60)
    lines.append(f"Grabación: {r['words']} palabras · {m}:{s:02d} · {r['wpm_speech']} ppm (objetivo {spec['wpm']}) · "
                 f"por voz {r['wpm_by_voice']}")
    for v, w in r["wpm_by_voice"].items():
        if abs(w / spec["wpm"] - 1) > WPM_TOL:
            errs.append(f"voz {v}: {w} ppm fuera de ±{WPM_TOL:.0%} de {spec['wpm']}")
    lo, hi = N_SPEAKERS * SEC_MIN + 4 * SPEAKER_PAUSE, N_SPEAKERS * SEC_MAX + 4 * SPEAKER_PAUSE
    if not lo <= r["total_s"] <= hi:
        errs.append(f"duración {r['total_s']} s fuera de {lo}-{hi} s")
    if asr:
        for k in (ASR_GROUPS[part] if part else range(1, 6)):
            sp = spec["speakers"][k - 1]
            wav = A.synth([(sp["text"], sp["voice"], r["rates"][sp["voice"]])])[0]
            phrases = [ev for it in sp["items"] for ev in it["evidence"]]
            chk = A.check_recording(wav, sp["text"], phrases)
            bad = [f"«{f[:45]}» {sc}" for f, sc in chk["phrases"] if sc < 0.85]
            diffs = word_diff(A.norm_words(sp["text"]), A.norm_words(chk["asr"]))
            lines.append(f"Speaker {k} ({sp['voice']}, {A.duration(wav):.1f} s): ASR {chk['sim']} · frases-respuesta "
                         f"{len(phrases) - len(bad)}/{len(phrases)} · diferencias {len(diffs)}")
            lines += ["    " + d for d in diffs]
            if not chk["ok"]:
                errs.append(f"speaker {k}: parecido {chk['sim']}; frases mal reconocidas {bad}\n    ASR: {chk['asr']}")
    return errs, lines


# ---------- Verificacion del contenido ----------
def _check_cites(errs, label, t, text):
    for c in CITE_RE.findall(t):
        if _norm(c) not in text:
            errs.append(f"{label}: cita inexistente: «{c[:50]}»")
    if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(t)):
        errs.append(f"{label}: marcado sin resolver")


def verify(spec):
    errs = []
    a = _first(spec)
    ctx = spec.get("ctx", "")
    if not ctx.startswith("You will hear five short extracts in which ") or not ctx.endswith("."):
        errs.append("ctx debe empezar por 'You will hear five short extracts in which' y acabar en punto")
    wpm = spec.get("wpm", 0)
    if not 140 <= wpm <= 200:
        errs.append("wpm ausente o fuera de 140-200")
    tasks, sps = spec.get("tasks", []), spec.get("speakers", [])
    if len(tasks) != 2 or len(sps) != N_SPEAKERS:
        return errs + ["hacen falta 2 tareas y 5 hablantes"], {}
    for t, task in enumerate(tasks):
        opts = task.get("options", [])
        if len(opts) != 8 or len(set(opts)) != 8 or not all(o.strip() for o in opts):
            errs.append(f"Task {TASKW[t]}: hacen falta 8 opciones distintas")
        if not task.get("prompt") or task["prompt"][0].isupper() or task["prompt"].endswith("."):
            errs.append(f"Task {TASKW[t]}: prompt en minúscula y sin punto final")
        for o in opts + [task.get("prompt", "")]:
            if re.search(r"[\[\]{}<>]", o):
                errs.append(f"Task {TASKW[t]}: marcado en una opción o en el prompt")
    voices = [s_.get("voice") for s_ in sps]
    if len(set(voices)) != 5:
        errs.append("voces repetidas en la hoja")
    for v in voices:
        if v not in A.VOICES or v == A.NARRATOR:
            errs.append(f"voz no válida: {v}")
    sexes = [A.VOICES[v][2] for v in voices if v in A.VOICES]
    if sexes.count("M") < 2 or sexes.count("F") < 2:
        errs.append("hacen falta al menos dos hombres y dos mujeres")
    if len({A.VOICES[v][1] for v in voices if v in A.VOICES}) < 2:
        errs.append("hacen falta al menos dos acentos")
    alltxt = _all_text(spec)
    keys = [[], []]
    words, touched_n, early2 = [], [], 0
    touched_letters = [set(), set()]
    for k, sp in enumerate(sps, 1):
        txt = _norm(sp.get("text", ""))
        if re.search(r"[\[\]{}<>]", txt):
            errs.append(f"speaker {k}: marcado en el monólogo")
        w = A.count_words(txt)
        words.append(w)
        est = w / max(wpm, 1) * 60
        if not SEC_MIN <= est <= SEC_MAX:
            errs.append(f"speaker {k}: {w} palabras, {est:.0f} s a {wpm} ppm (fuera de {SEC_MIN}-{SEC_MAX} s)")
        items = sp.get("items", [])
        if len(items) != 2:
            errs.append(f"speaker {k}: hacen falta dos ítems")
            continue
        pos = []
        for t, it in enumerate(items):
            n, exp_n = it.get("n"), a + 5 * t + k - 1
            lab = f"{exp_n}"
            if n != exp_n:
                errs.append(f"speaker {k}, Task {TASKW[t]}: número {n}, se esperaba {exp_n}")
            for f in ("key", "evidence", "why", "touched", "theory"):
                if not it.get(f):
                    errs.append(f"{lab}: falta el campo '{f}'")
            key = it.get("key")
            if key not in LETTERS:
                errs.append(f"{lab}: clave no válida '{key}'")
                continue
            keys[t].append(key)
            p0 = None
            for ev in it.get("evidence", []):
                if ev not in txt:
                    errs.append(f"{lab}: frase-respuesta no literal: «{ev[:50]}»")
                else:
                    p0 = txt.index(ev) if p0 is None else min(p0, txt.index(ev))
            pos.append(p0)
            if not CITE_RE.findall(it.get("why", "")):
                errs.append(f"{lab}: la explicación de la clave no cita el monólogo")
            _check_cites(errs, f"{lab} (clave)", it.get("why", ""), txt)
            for L, d in it.get("touched", {}).items():
                if L not in LETTERS or L == key:
                    errs.append(f"{lab}: opción rozada no válida '{L}'")
                if not d.get("kinds") or any(x not in KINDS for x in d["kinds"]):
                    errs.append(f"{lab}{L}: tipo de distractor ausente o desconocido {d.get('kinds')}")
                if not d.get("why"):
                    errs.append(f"{lab}{L}: falta la explicación")
                _check_cites(errs, f"{lab}{L}", d.get("why", ""), txt)
                touched_letters[t].add(L)
            touched_n.append(len(it.get("touched", {})))
            for s_ in it.get("theory", []):
                if s_ not in THEORY:
                    errs.append(f"{lab}: sección de teoría inexistente §{s_}")
        if None not in pos and pos[1] < pos[0]:
            early2 += 1
        if items[0].get("key") == items[1].get("key"):
            errs.append(f"speaker {k}: la misma letra en las dos tareas")
    extras_touched = 0
    for t, task in enumerate(tasks):
        ks = keys[t]
        if len(set(ks)) != 5:
            errs.append(f"Task {TASKW[t]}: claves repetidas {ks}")
        if ks == sorted(ks):
            errs.append(f"Task {TASKW[t]}: las claves siguen el orden alfabético {ks}")
        rest = set(LETTERS) - set(ks)
        if set(task.get("extras", {})) != rest:
            errs.append(f"Task {TASKW[t]}: extras {sorted(task.get('extras', {}))}; se esperaban {sorted(rest)}")
        for L, why in task.get("extras", {}).items():
            if not why:
                errs.append(f"Task {TASKW[t]} {L}: falta la explicación de por qué sobra")
            _check_cites(errs, f"Task {TASKW[t]} sobra {L}", why, alltxt)
        extras_touched += len(rest & touched_letters[t])
    if keys[0] == keys[1]:
        errs.append("las dos tareas tienen la misma secuencia de claves")
    return errs, {"words": words, "keys": ["".join(k_) for k_ in keys], "touched": touched_n,
                  "extras_touched": extras_touched, "task2_first": early2}


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
    return (f"{CODE}_Practica_{spec['num']}.pdf · palabras {info['words']} · claves {info['keys'][0]} / "
            f"{info['keys'][1]} · rozadas por ítem {info['touched']} · sobrantes rozadas {info['extras_touched']}/6 · "
            f"tarea 2 antes que la 1 en {info['task2_first']} hablantes")


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
    """'pdf' | 'audio' | 'asr' con idx 1-3 (hablantes 1-2, 3-4, 5). Devuelve True si va bien."""
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


# ---------- Hoja de ejemplo: contenido de LST-P4_Practica_01, numerada como 99 ----------
def _demo():
    import copy
    d = copy.deepcopy(DEMO_SPEC)
    d["num"], d["subtitle"] = "99", "Hoja de prueba del generador (contenido de LST-P4_Practica_01)"
    return d


DEMO_SPEC = {
    "num": "01",
    "subtitle": "Hoja 01 · Motivos y sorpresas, señales explícitas · dificultad 1 de 4",
    "difficulty": 1,
    "wpm": 160,
    "ctx": "You will hear five short extracts in which people are talking about learning a new language as adults.",
    "lex": ["slip away", "get someone going", "I hadn’t bargained for", "shattered", "it was X or no Y",
            "pompous", "take someone aback", "drain away", "that was that", "deflating", "in the slightest"],
    "tasks": [
        {"prompt": "why each speaker decided to learn a new language",
         "options": ["to meet a requirement at work",
                     "to keep a link with their family background",
                     "to read a favourite author in the original",
                     "to prepare for a move abroad",
                     "to keep their mind active in retirement",
                     "to take up a challenge from a friend",
                     "because of a memorable holiday",
                     "to talk to their partner’s relatives"],
         "extras": {
             "C": "Speaker 3 menciona a Murakami, pero como deseo para el futuro ({{I’d love to read Murakami in the "
                  "original one day}}), no como el motivo por el que empezó.",
             "G": "Speaker 1 lo descarta ({{People assume it was all those holidays in Italy that got me going}}), y "
                  "el viaje a Creta de Speaker 4 llega después de empezar, como consecuencia de la apuesta.",
             "H": "La familia griega de Speaker 4 es el antecedente: como todos hablan inglés, {{for years I never "
                  "bothered}}. Lo que le hizo empezar fue la apuesta."}},
        {"prompt": "what has surprised each speaker most about the experience",
         "options": ["how little native speakers care about grammar",
                     "how readily native speakers switch to English",
                     "how much they enjoy their lessons",
                     "how tiring it is to follow conversations",
                     "how unhelpful language-learning apps are",
                     "how quickly they forget what they have learnt",
                     "how much more confident they have become in general",
                     "how differently they behave when using the language"],
         "extras": {
             "A": "Speaker 2 dice lo contrario: {{they correct my grammar constantly}}.",
             "C": "Speaker 3 disfruta de las clases, pero no le sorprende: {{which I’d rather expected}}.",
             "E": "Speaker 1 habla bien de las aplicaciones: {{The apps were fine for vocabulary, actually.}}"}},
    ],
    "speakers": [
        {"voice": "Sonia",
         "text": "My grandmother came over from Naples in the fifties, and she never spoke much English, even at "
                 "home. When she died a few years ago, I realised that a whole side of the family was slipping away "
                 "from us, and I wanted my children to have some connection with it. People assume it was all those "
                 "holidays in Italy that got me going, but I’d been going there for years without learning a word. "
                 "The apps were fine for vocabulary, actually. What I hadn’t bargained for was how shattered I’d feel "
                 "after an hour of simply trying to keep up with people talking.",
         "items": [
             {"n": 21, "key": "B",
              "evidence": ["a whole side of the family was slipping away from us, and I wanted my children to have "
                           "some connection with it"],
              "why": "Tras la muerte de su abuela napolitana: {{a whole side of the family was slipping away from us, "
                     "and I wanted my children to have some connection with it}}.",
              "touched": {"G": {"kinds": ["4.2"],
                                "why": "Lo descarta: {{People assume it was all those holidays in Italy that got me "
                                       "going}}, pero había ido durante años {{without learning a word}}."}},
              "theory": ["8.1", "4.2"]},
             {"n": 26, "key": "D",
              "evidence": ["What I hadn’t bargained for was how shattered I’d feel after an hour of simply trying to "
                           "keep up with people talking."],
              "why": "La señal {{What I hadn’t bargained for}} (§2.3) introduce lo inesperado: acabar agotada "
                     "({{shattered}}) después de una hora intentando seguir una conversación.",
              "touched": {"E": {"kinds": ["4.2"],
                                "why": "Las aplicaciones le parecieron bien: {{The apps were fine for vocabulary, "
                                       "actually.}}"}},
              "theory": ["2.3", "8.1"]}]},
        {"voice": "Connor",
         "text": "I’d love to tell you it was a passion for French culture, but my company opened an office in Lyon, "
                 "and frankly it was French or no promotion. I didn’t have to move – I go over a couple of times a "
                 "month. I’d assumed people would switch to English the moment I stumbled, but in meetings they just "
                 "don’t, which is good for me. And they correct my grammar constantly. What really surprised me, "
                 "though, is that I’m a different person in French: far more formal, almost pompous. My colleagues "
                 "say I even stand differently.",
         "items": [
             {"n": 22, "key": "A",
              "evidence": ["it was French or no promotion"],
              "why": "Lo que de verdad le movió fue el trabajo: la empresa abrió una oficina en Lyon y {{it was French "
                     "or no promotion}}. La pasión por la cultura francesa la descarta él mismo con {{I’d love to "
                     "tell you}}.",
              "touched": {"D": {"kinds": ["4.2"],
                                "why": "No se ha mudado: {{I didn’t have to move}}."}},
              "theory": ["3.3", "4.2", "8.1"]},
             {"n": 27, "key": "H",
              "evidence": ["What really surprised me, though, is that I’m a different person in French"],
              "why": "Lo dice con todas las letras: {{What really surprised me, though, is that I’m a different person "
                     "in French}}, más formal y hasta pomposo.",
              "touched": {"B": {"kinds": ["4.7"],
                                "why": "Es lo que esperaba y no ocurrió: {{I’d assumed people would switch to English "
                                       "the moment I stumbled, but in meetings they just don’t}}."},
                          "A": {"kinds": ["4.1"],
                                "why": "Recoge [[grammar]], pero dice lo contrario: {{they correct my grammar "
                                       "constantly}}."}},
              "theory": ["2.3", "4.7", "8.3"]}]},
        {"voice": "Natasha",
         "text": "When I retired, I was determined not to spend my days in front of the television. I’d read that "
                 "learning a language is one of the best things you can do for an ageing brain, so I chose Japanese – "
                 "the hardest thing I could think of. I’d love to read Murakami in the original one day, but that’s a "
                 "long way off. The classes are great fun, which I’d rather expected. What did take me aback was how "
                 "quickly it all drains away: I spent three weeks at my sister’s without practising and came back "
                 "having forgotten half the characters I knew.",
         "items": [
             {"n": 23, "key": "E",
              "evidence": ["learning a language is one of the best things you can do for an ageing brain"],
              "why": "Al jubilarse no quería pasar el día delante del televisor, y había leído que {{learning a "
                     "language is one of the best things you can do for an ageing brain}}.",
              "touched": {"C": {"kinds": ["4.3"],
                                "why": "Leer a Murakami es un deseo para el futuro ({{that’s a long way off}}), no "
                                       "el motivo por el que empezó."}},
              "theory": ["8.1", "4.3"]},
             {"n": 28, "key": "F",
              "evidence": ["What did take me aback was how quickly it all drains away"],
              "why": "{{take me aback}} es «sorprender»: {{What did take me aback was how quickly it all drains "
                     "away}}. Tres semanas sin practicar y había olvidado la mitad de los caracteres.",
              "touched": {"C": {"kinds": ["4.7"],
                                "why": "Disfruta de las clases, pero contaba con ello: {{which I’d rather "
                                       "expected}}."}},
              "theory": ["2.3", "4.7", "8.3"]}]},
        {"voice": "Andrew",
         "text": "My wife’s family are Greek, but they all speak perfect English, so for years I never bothered. Then "
                 "at a dinner party a friend bet me fifty pounds that I couldn’t order a meal in Greek by the summer. "
                 "Well, I’m stubborn, so that was that. I won the bet, as it happens. It’s done wonders for my "
                 "confidence, I suppose, though I’d expected that. What I hadn’t expected was that in Crete, the "
                 "moment I opened my mouth, the waiters would answer in English. A bit deflating, after all that "
                 "effort.",
         "items": [
             {"n": 24, "key": "F",
              "evidence": ["a friend bet me fifty pounds that I couldn’t order a meal in Greek by the summer"],
              "why": "El desencadenante es la apuesta: {{a friend bet me fifty pounds that I couldn’t order a meal in "
                     "Greek by the summer}}. Y lo remata: {{so that was that}}.",
              "touched": {"H": {"kinds": ["4.3"],
                                "why": "La familia de su mujer es el antecedente, y justo lo contrario de un motivo: "
                                       "como todos hablan inglés, {{for years I never bothered}} (§8.3)."},
                          "G": {"kinds": ["4.6"],
                                "why": "El viaje a Creta vino después, cuando ya hablaba griego; no fue lo que le "
                                       "hizo empezar."}},
              "theory": ["8.3", "4.3"]},
             {"n": 29, "key": "B",
              "evidence": ["What I hadn’t expected was that in Crete, the moment I opened my mouth, the waiters would "
                           "answer in English."],
              "why": "{{What I hadn’t expected was that in Crete, the moment I opened my mouth, the waiters would answer "
                     "in English.}} Es la sorpresa, y además decepcionante: {{A bit deflating}}.",
              "touched": {"G": {"kinds": ["4.7"],
                                "why": "La confianza ganada no le sorprende: {{though I’d expected that}}."}},
              "theory": ["4.7", "8.3"]}]},
        {"voice": "Libby",
         "text": "We’re moving to Barcelona next spring for my husband’s job, so I signed up for Spanish classes "
                 "straight away – two evenings a week, and half an hour every morning before work. It isn’t for my "
                 "own job, by the way; I’ll carry on working remotely for a firm in London. Following conversations "
                 "is hard work, of course, but I knew it would be. The unexpected bonus has been how much bolder I’ve "
                 "become generally. If I can get through a phone call to a Spanish landlord, a presentation at work "
                 "doesn’t frighten me in the slightest.",
         "items": [
             {"n": 25, "key": "D",
              "evidence": ["We’re moving to Barcelona next spring for my husband’s job, so I signed up for Spanish "
                           "classes straight away"],
              "why": "Se muda: {{We’re moving to Barcelona next spring for my husband’s job, so I signed up for Spanish "
                     "classes straight away}}.",
              "touched": {"A": {"kinds": ["4.2"],
                                "why": "Lo descarta: {{It isn’t for my own job, by the way}}. El trabajo que origina "
                                       "la mudanza es el de su marido."}},
              "theory": ["8.1", "4.2"]},
             {"n": 30, "key": "G",
              "evidence": ["The unexpected bonus has been how much bolder I’ve become generally."],
              "why": "{{The unexpected bonus has been how much bolder I’ve become generally.}} El ejemplo lo "
                     "confirma: después de una llamada en español, una presentación no le da miedo.",
              "touched": {"D": {"kinds": ["4.7"],
                                "why": "Seguir conversaciones le cuesta, pero lo sabía: {{but I knew it would "
                                       "be}}."}},
              "theory": ["4.7", "8.3"]}]},
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
