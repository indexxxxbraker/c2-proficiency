# gen_SIM.py · Montaje de los simulacros (SIM-01 a SIM-06) · v1
# Proyecto C2 Proficiency. Usa c2_plantilla.py y los generadores de cada parte (no modifica ninguno).
#
# QUE HACE
#   Monta cada paper de un simulacro a partir de sus specs (sim/SIM-NN/specs_<paper>.py), con los bloques para
#   simulacros de cada generador: portada con instrucciones y tiempos, enunciados (una parte por pagina), hoja de
#   respuestas con el recuento total y soluciones de todas las partes.
#     rue  SIM-NN_RUE.pdf          Parts 1-7 (gen_UOE-P1..P4, gen_RDG-P5..P7)
#     wrt  SIM-NN_WRT.pdf          Part 1 + Part 2 con tres tareas (gen_WRT-P1, gen_WRT-P2)
#     lst  SIM-NN_LST.pdf + .mp3   Parts 1-4 con el guion completo del examen (gen_LST-P1..P4, lst_audio)
#     spk  SIM-NN_SPK.pdf + .mp3   test completo (gen_SPK)
#   Ademas genera, para la resolucion a ciegas, un PDF solo con la portada y los enunciados.
#
# USO
#   python3 src/gen_SIM.py rue sim/SIM-01                 verifica y genera sim/SIM-01/SIM-01_RUE.pdf
#   python3 src/gen_SIM.py rue sim/SIM-01 --ciegas DIR    ademas, DIR/SIM-01_RUE_enunciados.pdf
#   python3 src/gen_SIM.py verify rue sim/SIM-01          solo la verificacion de cada parte
#   (lo mismo con wrt; lst y spk tienen sus propias etapas, ver mas abajo)
#
# SPECS (sim/SIM-NN/specs_rue.py)
#   P1 ... P7   un spec por parte, con el formato del generador correspondiente (ver su cabecera); 'first'
#               se fija aqui (1, 9, 17, 25, 31, 37, 44) y 'num' y 'subtitle' se rellenan si faltan.

import importlib.util
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c2_plantilla import *  # noqa: E402,F401,F403
from c2_plantilla import _F, _font_path  # noqa: E402
from reportlab.lib.styles import ParagraphStyle  # noqa: E402

VERSION = "1"
DISCLAIMER = ("Material no oficial, sin afiliación con Cambridge University Press &amp; Assessment. "
              "Audio con voces sintéticas.")


def load(name):
    """Importa un generador por nombre de archivo (el guion impide un import normal)."""
    path = os.path.join(HERE, f"{name}.py")
    s = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def sim_id(sim_dir):
    sid = os.path.basename(os.path.normpath(sim_dir))
    if not re.fullmatch(r"SIM-\d\d", sid):
        raise ValueError(f"la carpeta tiene que llamarse SIM-NN: {sid}")
    return sid


def read_specs(sim_dir, paper):
    path = os.path.join(sim_dir, f"specs_{paper}.py")
    return runpy.run_path(path)


# ---------- Portada ----------
_cov_en = ParagraphStyle("sim_cov_en", parent=S["en"], fontSize=10.5, leading=15, spaceAfter=3)
_disc = ParagraphStyle("sim_disc", parent=S["small"], fontSize=8, leading=10.5)


def cover(sid, paper_title, subtitle, meta, instructions_en, rows, widths, how_to, notes=()):
    """Portada comun: bloque de titulo, instrucciones en ingles (como en el cuadernillo), tabla de partes y
    tiempos, como hacer el simulacro y el aviso de material no oficial."""
    out = title_block(f"{sid} · {paper_title}", paper_title, subtitle, meta)
    out += callout("clave", [Paragraph(x, _cov_en) for x in instructions_en], label="INSTRUCTIONS TO CANDIDATES")
    out.append(h2("Partes y tiempos"))
    out += table(rows, widths)
    out.append(h2("Cómo hacer el simulacro"))
    out += numbered(how_to)
    for n in notes:
        out.append(Paragraph(n, S["small"]))
    out += [Spacer(1, 10), Paragraph(DISCLAIMER, _disc)]
    return out


# ---------- Reading and Use of English ----------
RUE_PARTS = [  # clave del spec, generador, primer item, titulo, puntos maximos, minutos orientativos
    ("P1", "gen_UOE-P1", 1, "Multiple-choice cloze", 8, 8),
    ("P2", "gen_UOE-P2", 9, "Open cloze", 8, 9),
    ("P3", "gen_UOE-P3", 17, "Word formation", 8, 8),
    ("P4", "gen_UOE-P4", 25, "Key word transformations", 12, 12),
    ("P5", "gen_RDG-P5", 31, "Multiple choice", 12, 18),
    ("P6", "gen_RDG-P6", 37, "Gapped text", 14, 17),
    ("P7", "gen_RDG-P7", 44, "Multiple matching", 10, 15),
]
RUE_ITEMS = {"P1": 8, "P2": 8, "P3": 8, "P4": 6, "P5": 6, "P6": 7, "P7": 10}


def _rue_prepare(sid, ns):
    specs = {}
    for key, gen, first, title, _, _ in RUE_PARTS:
        sp = ns[key]
        sp.setdefault("num", sid.replace("SIM-", "S"))
        sp.setdefault("subtitle", f"{sid} · Part {key[1]} · {title}")
        sp["first"] = first
        specs[key] = sp
    return specs


def rue_verify(sid, specs, mods):
    """verify() de cada parte. Devuelve (errores, lineas de informe)."""
    errs, lines = [], []
    for key, gen, first, title, _, _ in RUE_PARTS:
        m, sp = mods[key], specs[key]
        e, info = m.verify(sp)
        errs += [f"Part {key[1]}: {x}" for x in e]
        if hasattr(m, "warnings") and not e:
            for w in m.warnings(sp):
                lines.append(f"Part {key[1]} · aviso: {w}")
        lines.append(f"Part {key[1]} · {title}: {info}")
    return errs, lines


def rue_story(sid, specs, mods, with_answers=True):
    total_items = sum(RUE_ITEMS.values())
    rows = [["Part", "Tarea", "Preguntas", "Puntos", "Tiempo orientativo"]]
    for key, gen, first, title, pts, mins in RUE_PARTS:
        last = first + RUE_ITEMS[key] - 1
        rows.append([key[1], title, f"{first}–{last}", str(pts), f"{mins} min"])
    rows.append(["", "<b>Total</b>", f"<b>{total_items}</b>", f"<b>{sum(r[4] for r in RUE_PARTS)}</b>",
                 "<b>90 min</b> (con 3 de repaso)"])
    story = cover(
        sid, "Reading and Use of English", f"Simulacro {sid[-2:]} · paper 1 de 4",
        f"Parts 1–7 · {total_items} preguntas · 1 hora 30 minutos · sin diccionario",
        ["Time: <b>1 hour 30 minutes</b>.",
         "There are <b>seven</b> parts to the test. Answer <b>all</b> the questions.",
         "Write your answers on the answer sheet. Use capital letters for Parts 2, 3 and 4.",
         "Parts 1, 2, 3 and 7 carry one mark per question; Part 4 carries up to two marks per question; "
         "Parts 5 and 6 carry two marks per question."],
        rows, [14, 60, 30, 22, 44],
        ["Imprime el PDF o ten a mano papel para las respuestas. Pon un cronómetro de 90 minutos y no lo pares.",
         "Haz las siete partes en orden o en el que prefieras, pero apunta la hora al terminar cada una: los "
         "tiempos de la tabla son una referencia para repartir los 90 minutos.",
         "Escribe las respuestas en la hoja de respuestas (después de la Part 7). En las Parts 2, 3 y 4, en "
         "mayúsculas; la ortografía cuenta.",
         "Corrige con las soluciones y anota la puntuación de cada parte en la tabla final de la hoja de "
         "respuestas. Lee también las explicaciones de los aciertos dudosos."])
    for key, gen, first, title, _, _ in RUE_PARTS:
        story.append(PageBreak())
        story.append(Paragraph(f'<font color="#A4243B">Part {key[1]}</font>&nbsp;&nbsp;{title}', S["h1"]))
        story += mods[key].question_flowables(specs[key])
    if not with_answers:
        return story
    # hoja de respuestas
    story.append(PageBreak())
    story.append(Paragraph("Hoja de respuestas", S["h1"]))
    for key, gen, first, title, _, _ in RUE_PARTS:
        kw = {"big": False} if key == "P2" else {}
        story.append(KeepTogether(mods[key].answer_sheet_flowables(specs[key], heading=f"Part {key[1]} · {title}",
                                                                   **kw)))
    rows = [["Part", "Tarea", "Puntos"]]
    for key, gen, first, title, pts, _ in RUE_PARTS:
        rows.append([key[1], title, f"______ / {pts}"])
    rows.append(["", "<b>Total</b>", f"<b>______ / {sum(r[4] for r in RUE_PARTS)}</b>"])
    block = [h2("Puntuación total")] + table(rows, [16, 104, 50], zebra=False, extra=[
        ("TOPPADDING", (0, 1), (-1, -1), 7), ("BOTTOMPADDING", (0, 1), (-1, -1), 7)])
    block.append(Paragraph(
        "Referencia orientativa, no oficial: en los tests publicados, el aprobado con nota C2 (200 en la Cambridge "
        "English Scale) suele quedar en torno al 60 % de la puntuación bruta, unos 43 de 72 puntos; la conversión "
        "exacta cambia de un examen a otro.", S["small"]))
    story.append(KeepTogether(block))
    # soluciones
    story += solutions_start("Soluciones")
    for i, (key, gen, first, title, _, _) in enumerate(RUE_PARTS):
        if i:
            story.append(PageBreak())
        story += mods[key].solutions_flowables(specs[key], with_band=False, heading=f"Part {key[1]} · {title}")
    return story


def rue(sim_dir, ciegas=None, only_verify=False):
    sid = sim_id(sim_dir)
    ns = read_specs(sim_dir, "rue")
    specs = _rue_prepare(sid, ns)
    mods = {key: load(gen) for key, gen, *_ in RUE_PARTS}
    errs, lines = rue_verify(sid, specs, mods)
    for ln in lines:
        print("  " + ln)
    if errs:
        raise ValueError(f"{sid} RUE:\n  - " + "\n  - ".join(errs))
    if only_verify:
        print(f"{sid} RUE · verificación sin errores")
        return None
    name = f"{sid}_RUE.pdf"
    path = os.path.join(sim_dir, name)
    build(path, rue_story(sid, specs, mods), f"{sid} · Reading and Use of English", name,
          title=f"{sid} · Reading and Use of English")
    left = check_pdf(path)
    if left:
        raise ValueError(f"{name}: restos de código en el PDF: {sorted(set(left))}")
    print(f"{name} · {pages(path)} páginas · verificación sin errores")
    if ciegas:
        os.makedirs(ciegas, exist_ok=True)
        q = os.path.join(ciegas, f"{sid}_RUE_enunciados.pdf")
        build(q, rue_story(sid, specs, mods, with_answers=False), f"{sid} · Reading and Use of English",
              f"{sid}_RUE_enunciados.pdf")
        print(f"enunciados para la resolución a ciegas: {q}")
    return path


# ---------- Writing ----------
GENRE_NAMES = {"article": "Article", "letter": "Letter", "report": "Report", "review": "Review"}


def wrt_verify(sid, ns, w1, w2):
    errs, lines = [], []
    e, info = w1.verify(ns["P1"])
    errs += [f"Part 1: {x}" for x in e]
    lines.append(f"Part 1 · Essay: {info}")
    tasks = ns["P2"]
    if len(tasks) != 3 or len({t["genre"] for t in tasks}) != 3:
        errs.append("Part 2: hacen falta tres tareas de géneros distintos")
    for i, t in enumerate(tasks, 2):
        e, info = w2.verify(t)
        errs += [f"Part 2 · pregunta {i}: {x}" for x in e]
        lines.append(f"Part 2 · pregunta {i} · {GENRE_NAMES[t['genre']]}: {info}")
    return errs, lines


def wrt_story(sid, ns, w1, w2, with_answers=True):
    p1, tasks = ns["P1"], ns["P2"]
    rows = [["Part", "Tarea", "Palabras", "Puntos", "Tiempo orientativo"],
            ["1", "Essay: resumir y evaluar dos textos (obligatoria)", "240–280", "20", "45 min"],
            ["2", "Una tarea a elegir entre tres: " + ", ".join(GENRE_NAMES[t["genre"]].lower() for t in tasks),
             "280–320", "20", "45 min"],
            ["", "<b>Total</b>", "", "<b>40</b>", "<b>90 min</b>"]]
    story = cover(
        sid, "Writing", f"Simulacro {sid[-2:]} · paper 2 de 4",
        "Part 1 obligatoria + una tarea de la Part 2 · 1 hora 30 minutos · sin diccionario",
        ["Time: <b>1 hour 30 minutes</b>.",
         "Part 1: answer the question. Write your answer in <b>240–280</b> words.",
         "Part 2: answer <b>one</b> question from questions 2–4. Write your answer in <b>280–320</b> words.",
         "Both parts carry equal marks."],
        rows, [14, 82, 24, 18, 32],
        ["Pon un cronómetro de 90 minutos. Lo razonable es dedicar unos 45 a cada parte, incluida la planificación "
         "y la revisión.",
         "Lee las tres tareas de la Part 2 antes de empezar y elige en un minuto: la que mejor sepas organizar, no "
         "la que trate el tema que más te guste (WRT-P2_Teoria_v1 §2.3).",
         "Escribe a mano o en un documento sin corrector; cuenta las palabras al final (en el examen digital todo "
         "cuenta: título, encabezados, saludo y firma).",
         "Corrige al día siguiente con la hoja de autocorrección y solo después lee los modelos. Las soluciones "
         "incluyen el análisis y un modelo de las tres tareas de la Part 2, también de las que no elegiste."])
    story.append(PageBreak())
    story.append(Paragraph('<font color="#A4243B">Part 1</font>&nbsp;&nbsp;Essay', S["h1"]))
    story += w1.question_flowables(p1, number="1")
    story.append(PageBreak())
    story.append(Paragraph('<font color="#A4243B">Part 2</font>&nbsp;&nbsp;Article, letter, report or review',
                           S["h1"]))
    story += w2.part2_flowables(tasks)
    if not with_answers:
        return story
    story.append(PageBreak())
    story.append(Paragraph("Hoja de autocorrección", S["h1"]))
    story += w1.answer_sheet_flowables(p1, heading="Part 1 · Essay")
    story.append(PageBreak())
    story += w2.answer_sheet_flowables(None, heading="Part 2 · La tarea elegida")
    story.append(KeepTogether([h2("Puntuación total")] + table(
        [["Part", "Puntos"], ["1 · Essay", "______ / 20"], ["2 · Tarea elegida (pregunta ___ )", "______ / 20"],
         ["<b>Total</b>", "<b>______ / 40</b>"]], [120, 50], zebra=False,
        extra=[("TOPPADDING", (0, 1), (-1, -1), 7), ("BOTTOMPADDING", (0, 1), (-1, -1), 7)])))
    story += solutions_start("Soluciones")
    story += w1.solutions_flowables(p1, with_band=False, heading="Part 1 · Essay")
    for i, t in enumerate(tasks, 2):
        story.append(PageBreak())
        story += w2.solutions_flowables(t, with_band=False,
                                        heading=f"Part 2 · pregunta {i} · {GENRE_NAMES[t['genre']]}")
    return story


def wrt(sim_dir, ciegas=None, only_verify=False):
    sid = sim_id(sim_dir)
    ns = read_specs(sim_dir, "wrt")
    w1, w2 = load("gen_WRT-P1"), load("gen_WRT-P2")
    ns["P1"].setdefault("num", sid.replace("SIM-", "S"))
    ns["P1"].setdefault("subtitle", f"{sid} · Part 1 · Essay")
    for i, t in enumerate(ns["P2"], 2):
        t.setdefault("num", sid.replace("SIM-", "S"))
        t.setdefault("subtitle", f"{sid} · Part 2 · pregunta {i}")
    errs, lines = wrt_verify(sid, ns, w1, w2)
    for ln in lines:
        print("  " + ln)
    if errs:
        raise ValueError(f"{sid} WRT:\n  - " + "\n  - ".join(errs))
    if only_verify:
        print(f"{sid} WRT · verificación sin errores")
        return None
    name = f"{sid}_WRT.pdf"
    path = os.path.join(sim_dir, name)
    build(path, wrt_story(sid, ns, w1, w2), f"{sid} · Writing", name, title=f"{sid} · Writing")
    left = check_pdf(path)
    if left:
        raise ValueError(f"{name}: restos de código en el PDF: {sorted(set(left))}")
    print(f"{name} · {pages(path)} páginas · verificación sin errores")
    if ciegas:
        os.makedirs(ciegas, exist_ok=True)
        q = os.path.join(ciegas, f"{sid}_WRT_enunciados.pdf")
        build(q, wrt_story(sid, ns, w1, w2, with_answers=False), f"{sid} · Writing", f"{sid}_WRT_enunciados.pdf")
        print(f"enunciados: {q}")
    return path


# ---------- Listening ----------
# Etapas (la sintesis y el reconocimiento de voz son lentos; cada etapa reaprovecha la cache de lst_audio, que se
# fija con LST_CACHE=$PWD/.cache/lst):
#   --stage verify     contenido de las cuatro partes y voces sin repetir en el paper
#   --stage audio      MP3 completo con el guion del examen; guarda el informe en la cache y comprueba velocidades
#   --stage asr N      reconocimiento de voz de la parte N (1-4); en las Parts 2-4, --chunk K para un solo tramo
#   --stage pdf        PDF con el mapa del MP3 (necesita el informe de la etapa audio)
LST_PARTS = [  # clave, generador, titulo, items
    ("P1", "gen_LST-P1", "Three extracts", 6),
    ("P2", "gen_LST-P2", "Sentence completion", 9),
    ("P3", "gen_LST-P3", "Interview", 5),
    ("P4", "gen_LST-P4", "Multiple matching", 10),
]
LST_OPENING = [
    "Proficiency Listening. Mock test {n}.",
    "There are four parts to the test. You will hear each part twice. For each part of the test, there will be "
    "time for you to look through the questions and time for you to check your answers.",
    "Write your answers on the question paper. You will have five minutes at the end of the test to copy your "
    "answers onto the separate answer sheet.",
]


def _lst_voices(spec, key):
    if key == "P1":
        return [v for ex in spec["extracts"] for v in ex["speakers"].values()]
    if key == "P2":
        return [spec["voice"]]
    if key == "P3":
        return list(spec["speakers"].values())
    return [s["voice"] for s in spec["speakers"]]


def lst_load(sim_dir):
    sid = sim_id(sim_dir)
    ns = read_specs(sim_dir, "lst")
    mods = {key: load(gen) for key, gen, _, _ in LST_PARTS}
    specs = {key: ns[key] for key, *_ in LST_PARTS}
    return sid, specs, mods


def lst_verify(sid, specs, mods):
    import lst_audio as A
    errs, lines = [], []
    seen = {}
    for key, gen, title, _ in LST_PARTS:
        e, info = mods[key].verify(specs[key])
        errs += [f"Part {key[1]}: {x}" for x in e]
        lines.append(f"Part {key[1]} · {title}: {info}")
        for v in _lst_voices(specs[key], key):
            if v == A.NARRATOR:
                errs.append(f"Part {key[1]}: la voz del narrador ({v}) no puede ser un hablante")
            if v in seen and seen[v] != key:
                errs.append(f"la voz {v} se repite en las Parts {seen[v][1]} y {key[1]}")
            seen.setdefault(v, key)
    lines.append(f"Voces: {len(seen)} distintas · " + ", ".join(f"{v} ({k[1]})" for v, k in seen.items()))
    return errs, lines


def lst_events(sid, specs, mods):
    import lst_audio as A
    ev = [A.mark("Inicio")]
    for line in LST_OPENING:
        ev.append(A.say(line.format(n=A.n2w(int(sid[-2:])))))
        ev.append(A.pause(2))
    ev.append(A.pause(3))
    for key, *_ in LST_PARTS:
        ev += mods[key].audio_events(specs[key], standalone=False)
        ev.append(A.pause(2))
    ev.append(A.mark("Copiar respuestas"))
    ev += A.script_transfer(paper=True)
    ev.append(A.mark("Fin"))
    return ev


def _lst_report_path(sid):
    import lst_audio as A
    return os.path.join(A.CACHE, f"report_{sid}_LST.json")


def _mmss(t):
    m, s = divmod(int(round(t)), 60)
    return f"{m}:{s:02d}"


def lst_story(sid, specs, mods, rep, with_answers=True):
    """rep: informe de la etapa audio (para el mapa del MP3); None solo para los enunciados de la resolucion a
    ciegas, antes de tener el audio."""
    marks = [(t, lab) for t, kind, lab in rep["timeline"] if kind == "mark"] if rep else []
    start = {lab: t for t, lab in marks}
    when = (lambda lab: _mmss(start[lab])) if rep else (lambda lab: "—")
    rows = [["Part", "Tarea", "Preguntas", "Puntos", "En el MP3"]]
    first = 1
    for key, gen, title, n in LST_PARTS:
        rows.append([key[1], title, f"{first}–{first + n - 1}", str(n), when(f"Part {key[1]}")])
        first += n
    rows.append(["", "Copiar las respuestas en la hoja", "", "", when("Copiar respuestas")])
    rows.append(["", "<b>Total</b>", "<b>30</b>", "<b>30</b>", f"<b>{_mmss(rep['duration_s'])}</b>" if rep else ""])
    minutes = round(rep["duration_s"] / 60) if rep else 40
    story = cover(
        sid, "Listening", f"Simulacro {sid[-2:]} · paper 3 de 4",
        f"Parts 1–4 · 30 preguntas · unos {minutes} minutos · audio: {sid}_LST.mp3",
        ["Time: approximately <b>40 minutes</b>, including five minutes to copy your answers.",
         "There are <b>four</b> parts to the test. You will hear each part <b>twice</b>.",
         "Write your answers on the question paper as you listen. At the end of the test you will have five "
         "minutes to copy them onto the answer sheet.",
         "Each question carries one mark."],
        rows, [14, 74, 26, 20, 36],
        ["Ten delante solo los enunciados (las páginas siguientes). Reproduce el MP3 de principio a fin, sin pausar: "
         "las pausas para leer las preguntas y para revisar ya están en el audio, con el guion del examen.",
         "Responde en los enunciados mientras escuchas y, en los cinco minutos finales, pasa las respuestas a la hoja "
         "de respuestas (después de la Part 4). En la Part 2, escribe las palabras que oyes, sin cambiarlas.",
         "Corrige con las soluciones: incluyen la transcripción completa, con la frase que da cada respuesta "
         "resaltada.",
         "Si fallas una pregunta, vuelve a escuchar ese tramo con la transcripción delante; el mapa del MP3 está en "
         "esta página."],
        notes=["Voces sintéticas con acentos británico, irlandés, australiano, neozelandés y norteamericano; el "
               "narrador es siempre el mismo. Ninguna respuesta depende solo de la entonación."])
    if rep:
        story.append(h2("Mapa del MP3"))
        mrows = [["Minuto", "Tramo"]] + [[_mmss(t), lab] for t, lab in marks]
        story += table(mrows, [30, 140])
    for key, gen, title, _ in LST_PARTS:
        story.append(PageBreak())
        story.append(Paragraph(f'<font color="#A4243B">Part {key[1]}</font>&nbsp;&nbsp;{title}', S["h1"]))
        story += mods[key].question_flowables(specs[key])
    if not with_answers:
        return story
    story.append(PageBreak())
    story.append(Paragraph("Hoja de respuestas", S["h1"]))
    for key, gen, title, _ in LST_PARTS:
        story.append(KeepTogether(mods[key].answer_sheet_flowables(specs[key], heading=f"Part {key[1]} · {title}")))
    rows = [["Part", "Tarea", "Puntos"]]
    for key, gen, title, n in LST_PARTS:
        rows.append([key[1], title, f"______ / {n}"])
    rows.append(["", "<b>Total</b>", "<b>______ / 30</b>"])
    block = [h2("Puntuación total")] + table(rows, [16, 104, 50], zebra=False, extra=[
        ("TOPPADDING", (0, 1), (-1, -1), 7), ("BOTTOMPADDING", (0, 1), (-1, -1), 7)])
    block.append(Paragraph(
        "Referencia orientativa, no oficial: el aprobado con nota C2 suele quedar en torno al 60 % de la "
        "puntuación bruta, unos 18 de 30 puntos; la conversión exacta cambia de un examen a otro.", S["small"]))
    story.append(KeepTogether(block))
    story += solutions_start("Soluciones")
    for i, (key, gen, title, _) in enumerate(LST_PARTS):
        if i:
            story.append(PageBreak())
        story += mods[key].solutions_flowables(specs[key], with_band=False, heading=f"Part {key[1]} · {title}")
    return story


def lst(sim_dir, stage="verify", n=None, chunk=None, ciegas=None):
    import json
    import lst_audio as A
    sid, specs, mods = lst_load(sim_dir)
    errs, lines = lst_verify(sid, specs, mods)
    if stage == "verify" or errs:
        for ln in lines:
            print("  " + ln)
        if errs:
            raise ValueError(f"{sid} LST:\n  - " + "\n  - ".join(errs))
        print(f"{sid} LST · verificación del contenido sin errores")
        return None
    rep_path = _lst_report_path(sid)
    if stage == "audio":
        A.setup(asr=False)
        mp3 = os.path.join(sim_dir, f"{sid}_LST.mp3")
        rep = A.render(lst_events(sid, specs, mods), mp3)
        json.dump(rep, open(rep_path, "w"), default=str)
        print(f"{sid}_LST.mp3 · {_mmss(rep['duration_s'])} · narrador {rep['narrator_rate']:+d} %")
        for t, kind, lab in rep["timeline"]:
            if kind == "mark":
                print(f"  {_mmss(t)}  {lab}")
        bad = []
        for key, *_ in LST_PARTS:
            e, ls = mods[key].verify_audio(specs[key], rep, asr=False)
            bad += [f"Part {key[1]}: {x}" for x in e]
            print("\n".join(f"  Part {key[1]} · {x}" for x in ls))
        if bad:
            raise ValueError("audio:\n  - " + "\n  - ".join(bad))
        return mp3
    if stage == "asr":
        A.setup(asr=True)
        rep = json.load(open(rep_path))
        key = f"P{n}"
        m, sp = mods[key], specs[key]
        if key == "P1":
            e, ls = m.verify_audio(sp, rep, asr=True)
        elif key == "P2":
            e, ls = m.verify_audio(sp, rep, asr=True, paragraphs=[chunk] if chunk else None)
        else:
            e, ls = m.verify_audio(sp, rep, asr=True, part=chunk)
        print("\n".join("  " + x for x in ls))
        if e:
            print("PROBLEMAS:\n  - " + "\n  - ".join(e))
        return not e
    if stage == "pdf":
        rep = json.load(open(rep_path))
        name = f"{sid}_LST.pdf"
        path = os.path.join(sim_dir, name)
        build(path, lst_story(sid, specs, mods, rep), f"{sid} · Listening", name, title=f"{sid} · Listening")
        left = check_pdf(path)
        if left:
            raise ValueError(f"{name}: restos de código en el PDF: {sorted(set(left))}")
        print(f"{name} · {pages(path)} páginas · verificación sin errores")
        if ciegas:
            os.makedirs(ciegas, exist_ok=True)
            q = os.path.join(ciegas, f"{sid}_LST_enunciados.pdf")
            build(q, lst_story(sid, specs, mods, rep, with_answers=False), f"{sid} · Listening",
                  f"{sid}_LST_enunciados.pdf")
            print(f"enunciados: {q}")
        return path
    raise ValueError(f"etapa desconocida: {stage}")


# ---------- Speaking ----------
# Necesita red: las fotos se descargan de Wikimedia Commons (y se vuelve a comprobar su licencia) y el MP3 del
# interlocutor se sintetiza con edge-tts. Specs: sim/SIM-NN/specs_spk.py define SPEC con el formato de gen_SPK.py.
def spk_story(sid, spec, rep, spk):
    n_min = round(rep["duration_s"] / 60)
    rows = [["Part", "Tarea", "En el examen", "En el MP3"]]
    mk = dict((lab, t) for t, lab in rep["marks"])
    rows += [["1", "Entrevista: cinco preguntas personales", "unos 2 min", _mmss(mk["Part 1 · Interview"])],
             ["2", "Tarea con fotos: un minuto sobre dos fotos y tres minutos de discusión hasta una decisión",
              "unos 4 min", _mmss(mk["Part 2 · Fase 1 (un minuto)"])],
             ["3", "Long turn de dos minutos con cada tarjeta, pregunta de seguimiento y discusión",
              "unos 10 min", _mmss(mk["Part 3 · Tarjeta A"])],
             ["", "<b>Total</b>", "<b>16 min</b> (en parejas)", f"<b>{_mmss(rep['duration_s'])}</b>"]]
    story = cover(
        sid, "Speaking", f"Simulacro {sid[-2:]} · paper 4 de 4",
        f"Test completo · unos {n_min} minutos con el MP3 {sid}_SPK.mp3 · grábate",
        ["The Speaking test has <b>three</b> parts and is taken in pairs, with two examiners.",
         "In this practice version, the interlocutor and your partner are on the recording. Answer when there is "
         "a pause: the silences are timed to the exam."],
        rows, [14, 92, 30, 34],
        [spk.M(x) for x in [
            "Ten delante solo el material del candidato (hoja de fotos y tarjetas, en las páginas siguientes). Las "
            "preguntas de la Part 1, las instrucciones de la Part 2 y las de la discusión solo se oyen.",
            "Pon a grabar el móvil y reproduce el MP3 de principio a fin, sin pausar. El [[Thank you]] del "
            "interlocutor marca el final de cada respuesta.",
            "Part 2: empiezas tú cada fase. El compañero interviene en momentos fijos y no te escucha (SPK_Teoria_v1 "
            "§1.4): reacciona a lo que dice cuando termine.",
            "Part 3: respondes las dos tarjetas y las dos preguntas de seguimiento, y luego las seis de la discusión.",
            "Al día siguiente, corrige con la hoja de autocorrección y solo después mira las soluciones (§8.1).",
        ]])
    story.append(h2("Mapa del MP3"))
    story += table([["Minuto", "Parte"]] + [[_mmss(t), lab] for t, lab in rep["marks"]], [30, 140])
    story.append(PageBreak())
    story += spk.visuals_flowables(spec)
    story.append(PageBreak())
    story += spk.cards_flowables(spec)
    story.append(PageBreak())
    story += spk.answer_sheet_flowables(spec)
    story += spk.solutions_flowables(spec, rep)
    return story


def spk(sim_dir, only_verify=False):
    sid = sim_id(sim_dir)
    spec = read_specs(sim_dir, "spk")["SPEC"]
    spec["num"] = sid[-2:]
    m = load("gen_SPK")
    pending = [ph["letter"] for ph in spec["p2"]["photos"] if not ph.get("file")]
    if pending:
        raise ValueError(f"{sid} SPK: fotos sin elegir en Commons: {pending} (ver 'busqueda' en specs_spk.py)")
    lines = m._say_lines

    def sim_lines(sp):   # el MP3 se identifica como simulacro, no como hoja de practica
        L = lines(sp)
        L["open"] = f"C2 Proficiency. Speaking. Mock test {m.NUMW[int(sp['num'])]}."
        return L
    m._say_lines = sim_lines
    if not os.environ.get("SPK_PHOTOS"):   # caché de fotos dentro del repositorio (ignorada por git)
        m.PHOTO_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".cache", "spk_photos")
    m.UA = "C2ProficiencySimulacros/1.0 (https://github.com/indexxxxbraker/c2-proficiency; educational)"
    fetch = m._fetch
    m._fetch = lambda url, timeout=60, tries=10: fetch(url, timeout, tries)   # Commons responde 429 a menudo
    for ph in spec["p2"]["photos"]:
        ph["_info"] = m.photo_info(ph["file"])
    errs, info = m.verify(spec)
    if errs:
        raise ValueError(f"{sid} SPK:\n  - " + "\n  - ".join(errs))
    print(f"{sid} SPK · contenido sin errores · {info}")
    if only_verify:
        return None
    mp3 = os.path.join(sim_dir, f"{sid}_SPK.mp3")
    rep = m.render_audio(spec, mp3)
    aerrs, ainfo = m.check_audio(spec, rep)
    print(f"{sid}_SPK.mp3 · {_mmss(rep['duration_s'])} · {ainfo}")
    if aerrs:
        raise ValueError("audio:\n  - " + "\n  - ".join(aerrs))
    name = f"{sid}_SPK.pdf"
    path = os.path.join(sim_dir, name)
    story = spk_story(sid, spec, rep, m)
    build(path, story, f"{sid} · Speaking", name, title=f"{sid} · Speaking")
    m._F = {k: _font_path(v) for k, v in _F.items()}   # comprobacion de glifos con las fuentes de fonts/
    perrs = m.check_pdf(path, story) + [f"resto de marcado: {x}" for x in check_pdf(path)]
    if perrs:
        raise ValueError(f"{name}:\n  - " + "\n  - ".join(perrs))
    print(f"{name} · {pages(path)} páginas · verificación sin errores")
    return path


# ---------- Comprobaciones del PDF ----------
def _pdf_text(path):
    import pdfplumber
    with pdfplumber.open(path) as pdf:
        return [pg.extract_text() or "" for pg in pdf.pages]


def pages(path):
    return len(_pdf_text(path))


def check_pdf(path):
    """Restos de marcado o de codigo en el texto del PDF."""
    txt = "\n".join(_pdf_text(path))
    return re.findall(r"\{\{|\}\}|\[\[|\]\]|<font|</?b>|</?i>|<br|&nbsp|&amp;|\{G\}|\{\d+\}|\{\d+\|[A-Z]+\}|EB\(|\{E",
                      txt)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Uso: python3 gen_SIM.py [verify] rue|wrt|lst|spk sim/SIM-NN [--ciegas DIR]")
        sys.exit(1)
    verify_only = args[0] == "verify"
    if verify_only:
        args = args[1:]
    paper, sim_dir = args[0], args[1]
    ciegas = args[args.index("--ciegas") + 1] if "--ciegas" in args else None
    if paper == "rue":
        rue(sim_dir, ciegas=ciegas, only_verify=verify_only)
    elif paper == "wrt":
        wrt(sim_dir, ciegas=ciegas, only_verify=verify_only)
    elif paper == "lst":
        st = args[args.index("--stage") + 1] if "--stage" in args else ("verify" if verify_only else "pdf")
        num = int(args[args.index("--stage") + 2]) if st == "asr" else None
        ch = int(args[args.index("--chunk") + 1]) if "--chunk" in args else None
        ok = lst(sim_dir, stage=st, n=num, chunk=ch, ciegas=ciegas)
        if ok is False:
            sys.exit(1)
    elif paper == "spk":
        spk(sim_dir, only_verify=verify_only)
    else:
        raise SystemExit(f"paper desconocido: {paper}")
