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
    else:
        raise SystemExit(f"paper desconocido: {paper}")
