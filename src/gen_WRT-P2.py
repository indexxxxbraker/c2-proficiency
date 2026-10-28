# gen_WRT-P2.py · Generador de Writing Part 2 (article, letter, report, review) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa: enunciado con formato de examen (70 palabras como maximo), hoja de
#     autocorreccion con la rubrica de WRT-P2_Teoria_v1 §8 (Content propio de la Part 2; CA, O y L con los
#     codigos de WRT-P1_Teoria_v1 §9.1 leidos para cada genero) y soluciones: analisis del enunciado, puntos de
#     contenido, plan, modelo de 280-320 palabras comentado criterio por criterio y errores que costarian puntos.
#   - Bloques sueltos para los simulacros (SIM): la Part 2 con tres tareas a elegir (preguntas 2-4), la hoja de
#     autocorreccion (generica o de una tarea) y las soluciones de cada tarea.
#   - Verificacion automatica antes y despues de generar el PDF.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_WRT-P2.py --demo [carpeta_salida]          -> hoja de ejemplo (numerada 99)
#   python3 gen_WRT-P2.py mis_hojas.py [carpeta_salida]   -> mis_hojas.py define SPECS = [spec, ...]
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_w2", "/ruta/gen_WRT-P2.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, info = gen.verify(spec)
#   gen.make(spec, "/mnt/user-data/outputs")
#   # en un SIM:
#   story += gen.part2_flowables([spec_a, spec_b, spec_c])          # enunciado de la Part 2 (preguntas 2-4)
#   story += gen.answer_sheet_flowables(None)                       # autocorreccion generica
#   story += gen.solutions_flowables(spec_a, with_band=False, heading="Part 2 · pregunta 2 · Article")
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num        "01"
#   subtitle   "Hoja 01 · Article · revista de viajes · dificultad 1 de 3"           (espanol)
#   genre      "article" | "letter" | "report" | "review"
#   register   "formal" | "semiformal" | "neutro" | "vivo"   (letter: formal o semiformal; report: formal o neutro)
#   prompt     enunciado en ingles britanico SIN la orden final (el generador añade "Write your <genre>.");
#              con la orden, 70 palabras como maximo
#   analysis   [{"dato": uno de DATOS, "quote": cita literal del enunciado o "", "note": "..."}, ...]
#   points     2-3 diccionarios, ids P1, P2, P3 en orden:
#       id     "P1"
#       quote  cita literal del enunciado (se comprueba)
#       asks   que pide, en espanol (§2.2)
#       par    parrafo del modelo donde se trata (1..n)
#       model  cita literal del modelo dentro de ese parrafo (se comprueba)
#   plan       [{"par": 1, "content": "...", "points": ["P1"]}, ...]  una entrada por parrafo del modelo
#   model      {"title": str|None, "salutation": str|None,
#               "paras": [{"heading": str|None, "text": str}, ...],
#               "closing": str|None, "signature": str|None}
#              280-320 palabras contando todo (titulo, encabezados, saludo, despedida y firma)
#   comments   {"Content": {"text": "...", "theory": ["2.2"]}, "Communicative Achievement": {...},
#               "Organisation": {...}, "Language": {...}}   cada texto cita el modelo al menos una vez
#   errors     [{"error": "...", "why": "...", "codes": ["C1"], "theory": ["2.1"]}, ...]  al menos cuatro
#   shared_ok  frases que el modelo puede compartir con el enunciado (nombres, terminos del tema): opcional
#   lex        lexico para el modulo LEX (no se imprime; se usa en el resumen de cierre)
#
#   Marcado en los campos en espanol:
#     {{texto}}   -> cita literal del enunciado, en serif; se comprueba que existe tal cual
#     {{=texto}}  -> cita literal del modelo, en serif cursiva; se comprueba que existe tal cual
#     [[texto]]   -> ingles en serif sin comprobar
#     [[!TEXTO]]  -> ingles en serif y negrita
#   Teoria: secciones de WRT-P2 ("4.4") o de WRT-P1 con prefijo ("P1-8.3").
#
# RECUENTO DE PALABRAS
#   Como el contador del examen digital: cuenta todo lo escrito. Es palabra cada secuencia separada por espacios
#   que contiene al menos una letra o cifra (un compuesto con guion o una contraccion es una palabra).
#
# QUE COMPRUEBA verify()
#   campos completos · genero y registro compatibles · enunciado <= 70 palabras con la orden final · modelo
#   280-320 palabras · numero de parrafos · formato del genero (titulo en article, review y report; encabezado en
#   cada seccion del report; saludo, despedida y firma en la letter, sin titulo; pareja saludo-despedida; sin
#   punto tras Mr, Ms, Dr) · 2-3 puntos con su cita en el enunciado y su cita del modelo en el parrafo indicado ·
#   el plan coloca cada punto donde esta · analisis con citas reales · todas las citas existen · ninguna
#   secuencia de cinco palabras o mas copiada del enunciado (salvo shared_ok) · grafias americanas y -ize ·
#   contracciones en registro formal y en el report · codigos de rubrica y secciones de teoria · marcado
#   sin resolver.
#
# LO QUE EL GENERADOR NO PUEDE COMPROBAR (a mano)
#   - Que el modelo merezca la banda 5 y que el registro sea el adecuado; ingles britanico idiomatico.
#   - Que los datos reales (obras, autores, fechas) sean ciertos; dificultad graduada.
#   - Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402

VERSION = "1"
PROMPT_MAX = 70
MODEL_MIN, MODEL_MAX = 280, 320
LIFT_N = 5
THEORY_DOC = "WRT-P2_Teoria_v1"
GENRES = {"article": "Article", "letter": "Letter", "report": "Report", "review": "Review"}
REGISTERS = {"article": {"vivo", "neutro", "formal"}, "letter": {"formal", "semiformal"},
             "report": {"formal", "neutro"}, "review": {"vivo", "neutro"}}
PARS = {"article": (4, 6), "letter": (4, 6), "report": (4, 6), "review": (4, 6)}
DATOS = ["Contexto", "Papel", "Lector", "Propósito", "Registro", "Puntos"]
CRITERIA = ["Content", "Communicative Achievement", "Organisation", "Language"]

THEORY = {
    "1.1": "Formato y enunciado", "1.2": "Qué cambia respecto al C1", "1.3": "Cómo se puntúa",
    "1.4": "Las cuatro respuestas del handbook",
    "2.1": "Anatomía del enunciado", "2.2": "Los verbos de los puntos", "2.3": "Elegir entre tres tareas",
    "2.4": "Método, tiempo y recuento",
    "3.1": "La escala de registro", "3.2": "Títulos, encabezados y párrafos", "3.3": "Funciones transversales",
    "4.1": "Article: convenciones", "4.2": "Article: lector y registro", "4.3": "Article: estructura y presupuesto",
    "4.4": "Aperturas y cierres", "4.5": "Article: funciones y lenguaje", "4.6": "Calibración: G frente a H",
    "5.1": "Letter: convenciones", "5.2": "Formal y semiformal", "5.3": "Tres tipos de carta",
    "5.4": "Letter: funciones y lenguaje", "5.5": "Letter: calibración con la escala",
    "6.1": "Report: convenciones", "6.2": "Report: lector y papel", "6.3": "Report: estructura y presupuesto",
    "6.4": "Report: funciones y lenguaje", "6.5": "Calibración: la respuesta F",
    "7.1": "Review: convenciones", "7.2": "Review: lector y registro", "7.3": "Review: estructura",
    "7.4": "Review: funciones y lenguaje", "7.5": "Calibración: la respuesta E",
    "8.1": "Content en la Part 2", "8.2": "Communicative Achievement, Organisation y Language",
    "8.3": "Contraste con el handbook", "8.4": "Lista de comprobación final",
    # secciones de WRT-P1_Teoria_v1 que tambien se citan
    "P1-7.4": "Cohesión de nivel C2", "P1-8.1": "Qué separa la banda 3 de la 5", "P1-8.2": "Estructuras rentables",
    "P1-8.3": "Errores frecuentes del hispanohablante",
}

# ---------- Rubrica (WRT-P2_Teoria_v1 §8; CA, O y L con los codigos de WRT-P1_Teoria_v1 §9.1) ----------
CA1_BY_GENRE = {
    "article": "Article reconocible: título, apertura que engancha, cierre que no es de essay",
    "letter": "Carta reconocible: saludo y despedida emparejados, motivo al principio, cierre con petición",
    "report": "Report reconocible: título, introducción con propósito, encabezados, conclusión",
    "review": "Review reconocible: título, obra identificada al principio, evaluación y veredicto",
    None: "Género reconocible, con sus convenciones (§4.1, §5.1, §6.1, §7.1)",
}
CA5_BY_GENRE = {
    "article": "Engancha: apertura y cierre trabajan, y el caso sirve a una idea",
    "letter": "Consigue lo que busca: el lector sabe qué se le pide y por qué hacerlo",
    "report": "Orienta una decisión: el lector puede actuar con lo que lee",
    "review": "Juzga y recomienda: el lector sabe si la obra es para él",
    None: "Produce el efecto del género sobre su lector (§8.2)",
}
REG_NAME = {"formal": "formal", "semiformal": "semiformal", "neutro": "neutro", "vivo": "vivo"}


def rubric(genre=None, register=None):
    reg = f"Registro {REG_NAME[register]}, adecuado al lector y constante" if register else \
        "Registro adecuado al lector (§3.1) y constante"
    return [
        ("Content", [
            ("C1", "Todos los puntos del enunciado, también los detalles pequeños"),
            ("C2", "Cada punto con el desarrollo que pide su verbo"),
            ("C3", "Se entiende sin haber visto el enunciado"),
            ("C4", "Todo relevante; la tarea, bien leída")]),
        ("Communicative Achievement", [
            ("CA1", CA1_BY_GENRE[genre]),
            ("CA2", reg),
            ("CA3", "Cumple todos los propósitos del enunciado"),
            ("CA4", "Las ideas complejas se entienden a la primera"),
            ("CA5", CA5_BY_GENRE[genre])]),
        ("Organisation", [
            ("O1", "Cada párrafo o sección tiene una función y una frase que la anuncia"),
            ("O2", "Progresión lógica"),
            ("O3", "Cohesión variada y correcta"),
            ("O4", "El cierre responde a lo que abre el primer párrafo"),
            ("O5", "Patrones organizativos más allá de los conectores")]),
        ("Language", [
            ("L1", "Léxico menos común usado con precisión"),
            ("L2", "Estructuras complejas variadas y controladas"),
            ("L3", "Solo despistes; nada impide entender"),
            ("L4", "Una sola variedad de inglés; el enunciado reformulado, no copiado"),
            ("L5", "Natural y preciso, sin expresiones forzadas")]),
    ]


CODES = {c: q for _, qs in rubric() for c, q in qs}

QUOTE_RE = re.compile(r"\{\{(=?)(.+?)\}\}")
AMERICAN = re.compile(
    r"\b(colors?|colored|favor|favors|favored|favoring|favorite\w*|favorabl\w*|honor|honors|honored|honoring|"
    r"honorable|labor|labors|labored|laboring|neighbor\w*|behavior\w*|humor|humored|rumors?|harbor\w*|"
    r"flavor\w*|savor\w*|vigor|rigor|endeavor\w*|odors?|valor|armor\w*|center\w*|theaters?|liters?|fibers?|"
    r"defense|offense|traveled|traveling|traveler\w*|canceled|canceling|labeled|labeling|modeled|modeling|"
    r"judgment\w*|programs?|catalogs?|analyz\w*|paralyz\w*|fulfill|fulfills|enroll|enrolls|skeptic\w*|gray|"
    r"aging|practiced|practicing|jewelry|pajamas|mustache|math)\b", re.I)
IZE_OK = {"size", "prize", "seize", "capsize", "baize", "maize", "downsize", "oversize", "assize"}
CONTRACTION = re.compile(r"\b\w+(n’t|n't|’re|'re|’ve|'ve|’ll|'ll|’m|'m|’d|'d)\b", re.I)
SALUT_UNKNOWN = re.compile(r"^Dear (Sir or Madam|Editor|Sir/Madam),?$")
SALUT_NAMED = re.compile(r"^Dear (Mr|Ms|Mrs|Miss|Dr|Professor) [A-Z][\w’'-]+,?$")
SALUT_FIRST = re.compile(r"^Dear [A-Z][\w’'-]+,?$")
CLOSE_FORMAL_UNKNOWN = {"Yours faithfully"}
CLOSE_FORMAL_NAMED = {"Yours sincerely"}
CLOSE_SEMI = {"Yours sincerely", "Kind regards", "Best wishes", "Warm regards", "With best wishes", "Best regards"}


# ---------- Ingles dentro del texto en espanol ----------
def E(s):
    return f'<font name="EN">{s}</font>'


def EI(s):
    return f'<font name="EN"><i>{s}</i></font>'


def EB(s):
    return f'<font name="EN"><b>{s}</b></font>'


def markup(s):
    """{{=cita del modelo}} -> EI; {{cita del enunciado}} y [[x]] -> E; [[!X]] -> EB."""
    s = QUOTE_RE.sub(lambda m: EI(m.group(2)) if m.group(1) else E(m.group(2)), s)
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)


def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


def wc(s):
    return len([w for w in s.split() if re.search(r"[A-Za-z0-9]", w)])


def _tokens(s):
    return re.findall(r"[a-z0-9’']+", s.lower().replace("’", "'"))


def shared_runs(a, b, n):
    ta, tb = _tokens(a), _tokens(b)
    grams = {tuple(tb[i:i + n]) for i in range(len(tb) - n + 1)}
    return sorted({" ".join(ta[i:i + n]) for i in range(len(ta) - n + 1) if tuple(ta[i:i + n]) in grams})


def instruction(spec):
    return f"Write your {spec['genre']}."


def prompt_words(spec):
    return wc(spec["prompt"] + " " + instruction(spec))


def model_parts(spec):
    """Todas las piezas del modelo en orden de lectura: (tipo, texto)."""
    m = spec["model"]
    out = []
    if m.get("title"):
        out.append(("title", m["title"]))
    if m.get("salutation"):
        out.append(("salutation", m["salutation"]))
    for pa in m["paras"]:
        if pa.get("heading"):
            out.append(("heading", pa["heading"]))
        out.append(("para", pa["text"]))
    if m.get("closing"):
        out.append(("closing", m["closing"]))
    if m.get("signature"):
        out.append(("signature", m["signature"]))
    return out


def model_words(spec):
    return sum(wc(t) for _, t in model_parts(spec))


def par_words(spec):
    return [wc((pa.get("heading") or "") + " " + pa["text"]) for pa in spec["model"]["paras"]]


def _theory(secs):
    out = []
    for s in secs:
        if s.startswith("P1-"):
            out.append(f"WRT-P1 §{s[3:]} {THEORY[s]}")
        else:
            out.append(f"§{s} {THEORY[s]}")
    return " · ".join(out)


def _tref(secs):
    return " · ".join(("WRT-P1 §" + s[3:]) if s.startswith("P1-") else ("§" + s) for s in secs)


# ---------- Estilos propios de la hoja (sobre la plantilla, sin cambiarla) ----------
_rub = ParagraphStyle("w2_rubric", parent=S["en"], fontSize=10.5, leading=15)
_num = ParagraphStyle("w2_num", parent=S["en"], fontName="EN-B", fontSize=16, leading=19, textColor=ACCENT)
_task = ParagraphStyle("w2_task", parent=S["en"], fontSize=10.8, leading=16.2, spaceAfter=6)
_mtitle = ParagraphStyle("w2_mtitle", parent=S["en"], fontName="EN-B", fontSize=12, leading=16, textColor=NAVY,
                         spaceAfter=6)
_mhead = ParagraphStyle("w2_mhead", parent=S["en"], fontName="EN-B", fontSize=10.5, leading=14, textColor=NAVY,
                        spaceBefore=4, spaceAfter=2)
_mpar = ParagraphStyle("w2_mpar", parent=S["en"], leading=15.2, spaceAfter=6)
_mline = ParagraphStyle("w2_mline", parent=S["en"], leading=15.2, spaceAfter=2)
_ihead = ParagraphStyle("w2_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)
_PNUM = '<font name="Sans-B" color="#A4243B">{}</font>&nbsp;&nbsp;'


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def _task_block(spec, number):
    tb = Table([[Paragraph(str(number), _num),
                 [Paragraph(spec["prompt"], _task), Paragraph(f"<b>{instruction(spec)}</b>", _task)]]],
               colWidths=[12 * mm, CONTENT_W - 12 * mm])
    tb.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEABOVE", (0, 0), (-1, 0), 0.6, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return tb


def _closing_rule():
    line = Table([[""]], colWidths=[CONTENT_W], rowHeights=[2])
    line.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), 0.6, RULE)]))
    return line


def question_flowables(spec, with_title_block=False, number=2):
    """Rubrica de la Part 2 y una sola tarea (hoja de practica)."""
    out = []
    if with_title_block:
        out += title_block(f"WRT-P2 · Práctica {spec['num']}", GENRES[spec["genre"]], spec["subtitle"],
                           "Part 2 · 280–320 palabras · tiempo orientativo: 45 minutos · sin consultar la teoría")
    out.append(Paragraph("<b>Part 2</b>", _rub))
    out.append(Paragraph("Write an answer to the question below. Write your answer in <b>280–320</b> words in an "
                         "appropriate style.", _rub))
    out.append(Spacer(1, 8))
    out += [_task_block(spec, number), _closing_rule()]
    return out


def part2_flowables(specs, first_number=2):
    """Part 2 de un simulacro: tres tareas a elegir, numeradas 2-4."""
    if len(specs) != 3:
        raise ValueError("la Part 2 de un simulacro lleva tres tareas")
    if len({s["genre"] for s in specs}) != 3:
        raise ValueError("las tres tareas de la Part 2 deben ser de géneros distintos")
    last = first_number + 2
    out = [Paragraph("<b>Part 2</b>", _rub),
           Paragraph(f"Write an answer to <b>one</b> of the questions <b>{first_number}–{last}</b> in this part. "
                     "Write your answer in <b>280–320</b> words in an appropriate style.", _rub),
           Spacer(1, 8)]
    for i, sp in enumerate(specs):
        out.append(_task_block(sp, first_number + i))
    out.append(_closing_rule())
    return out


def answer_sheet_flowables(spec=None, heading="Hoja de autocorrección"):
    """Con spec: hoja de una tarea concreta. Con None: hoja generica para la tarea elegida en un SIM."""
    yn = '<font color="#5B6577">Sí · No</font>'
    genre = spec["genre"] if spec else None
    register = spec["register"] if spec else None
    out = [h2(heading), p(
        "Corrige al día siguiente, en frío: primero la rúbrica, sin mirar las soluciones; después, el plan y el "
        f"modelo. Preguntas completas en {THEORY_DOC} §8.1–8.2 y WRT-P1_Teoria_v1 §9.1.")]
    data = [["Dato", "Tu resultado"],
            ["Palabras (todo cuenta: título, encabezados, saludo, firma)", "________ (objetivo: 280–320)"],
            ["Tiempo empleado", "________ minutos (objetivo: unos 45)"]]
    if not spec:
        data.append(["Puntos del enunciado tratados con el desarrollo que piden", "________ / ____"])
    out += table(data, [100, 70], zebra=False,
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 1), (-1, -1), 2.5)])
    if spec:
        rows = [["Punto", "En el enunciado (¿tratado con el desarrollo que pide?)", "En tu texto"]]
        rows += [[pt["id"], E(pt["quote"]), yn] for pt in spec["points"]]
        out += table(rows, [16, 130, 24], zebra=False,
                     extra=[("TOPPADDING", (0, 1), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 1), (-1, -1), 2.5)])
    rows = [["Código", "Pregunta", ""]]
    shade = []
    for crit, qs in rubric(genre, register):
        rows.append([f"<b>{crit}</b>", "", ""])
        shade.append(len(rows) - 1)
        rows += [[c, q, yn] for c, q in qs]
    extra = [("BACKGROUND", (0, r), (-1, r), ZEBRA) for r in shade]
    extra += [("SPAN", (0, r), (-1, r)) for r in shade]
    extra += [("TOPPADDING", (0, 1), (-1, -1), 1.6), ("BOTTOMPADDING", (0, 1), (-1, -1), 1.6)]
    out += table(rows, [20, 126, 24], zebra=False, extra=extra)
    note = Paragraph(
        "<b>Content:</b> 5 si todo es sí · 4 un punto tratado de pasada o una digresión breve · 3 un punto omitido o "
        "dos fallos menores · 2 dos puntos omitidos o la tarea leída a medias · 1 tarea malinterpretada. "
        "<b>Communicative Achievement, Organisation y Language:</b> 5 las cinco sí · 4 sí a las cuatro primeras · "
        "3 falla una de las cuatro primeras · 2 fallan dos · 1 fallan tres o cuatro.", S["small"])
    sc = table([
        ["Content", "Communicative Achievement", "Organisation", "Language", "Total"],
        ["____ / 5", "____ / 5", "____ / 5", "____ / 5", "<b>____ / 20</b>"],
    ], [30, 46, 32, 30, 32], zebra=False, extra=[("TOPPADDING", (0, 1), (-1, -1), 6),
                                                 ("BOTTOMPADDING", (0, 1), (-1, -1), 6)])
    out.append(KeepTogether([note, Spacer(1, 3)] + sc))
    return out


def model_flowables(spec):
    out = []
    n = 0
    for kind, text in model_parts(spec):
        if kind == "title":
            out.append(Paragraph(text, _mtitle))
        elif kind == "heading":
            out.append(Paragraph(text, _mhead))
        elif kind == "para":
            n += 1
            out.append(Paragraph(_PNUM.format(n) + text, _mpar))
        else:
            out.append(Paragraph(text, _mline))
    return out


def solutions_flowables(spec, with_band=True, heading=None):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 2 · pregunta 3 · Report' dentro de un simulacro)."""
    H = h2 if not heading else h3
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(
        "Las soluciones analizan el enunciado, sitúan cada punto de contenido en el modelo y dan el plan y un "
        "modelo que apunta a la banda 5 en los cuatro criterios, comentado criterio por criterio. Al final, los "
        "errores que costarían puntos, con la pregunta de la rúbrica que fallaría. Las citas del enunciado van en "
        f"redonda y las del modelo, en cursiva. Los números de sección remiten a {THEORY_DOC}."))
    # analisis
    rows = [["Dato", "En el enunciado", "Consecuencia"]]
    for a in spec["analysis"]:
        rows.append([f"<b>{a['dato']}</b>", E(a["quote"]) if a.get("quote") else "—", markup(a["note"])])
    out.append(KeepTogether([H("Análisis del enunciado")] + table(rows, [24, 62, 84])))
    out.append(p("<b>Teoría:</b> " + _theory(["2.1", "3.1"])))
    # puntos
    rows = [["Punto", "En el enunciado", "Qué pide", "En el modelo"]]
    for pt in spec["points"]:
        rows.append([f"<b>{pt['id']}</b>", E(pt["quote"]), markup(pt["asks"]),
                     f"Párr. {pt['par']}: " + EI(pt["model"])])
    out.append(KeepTogether([H("Puntos de contenido")] + table(rows, [14, 48, 58, 50])))
    out.append(p("<b>Teoría:</b> " + _theory(["2.2", "8.1"])))
    # plan
    pw = par_words(spec)
    rows = [["Párrafo", "Contenido", "Puntos", "Palabras"]]
    for pl in spec["plan"]:
        rows.append([str(pl["par"]), markup(pl["content"]), ", ".join(pl["points"]) or "—", str(pw[pl["par"] - 1])])
    out.append(KeepTogether([H("Plan del modelo")] + table(rows, [18, 104, 26, 22])))
    # modelo
    out.append(CondPageBreak(110 * mm))
    out.append(H(f"{GENRES[spec['genre']]} modelo"))
    label = f"{model_words(spec)} PALABRAS (TODO INCLUIDO) · REGISTRO {spec['register'].upper()} · " \
            "BANDA OBJETIVO: 5 EN LOS CUATRO CRITERIOS"
    out += callout("ejemplo", model_flowables(spec), label=label)
    # comentario
    out.append(CondPageBreak(60 * mm))
    out.append(H("Comentario por criterio"))
    rows = [["Criterio", "Comentario"]]
    for c in CRITERIA:
        cm = spec["comments"][c]
        rows.append([f"<b>{c}</b> · 5", markup(cm["text"]) + " <i>Teoría: " + _tref(cm["theory"]) + ".</i>"])
    out += table(rows, [36, 134])
    # errores
    out.append(CondPageBreak(45 * mm))
    out.append(H("Errores que costarían puntos"))
    qmap = {c: q for _, qs in rubric(spec["genre"], spec["register"]) for c, q in qs}
    for i, er in enumerate(spec["errors"], 1):
        codes = ", ".join(f"{c} ({qmap[c]})" for c in er["codes"])
        block = [Paragraph(f"{i} · {markup(er['error'])}", _ihead),
                 p(markup(er["why"])),
                 p(f"<b>Falla:</b> {codes}. <b>Teoría:</b> {_theory(er['theory'])}.")]
        out.append(KeepTogether(block))
    return out


def build_sheet(spec, out_path):
    """Hoja completa: enunciado, hoja de autocorreccion (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"WRT-P2 · Práctica {n}", f"WRT-P2_Practica_{n}.pdf", title=f"WRT-P2 · Práctica {n}")
    return out_path


# ---------- Verificacion ----------
def _check_quotes(where, s, prompt_full, model_full, errs):
    for is_model, q in QUOTE_RE.findall(s):
        q = _norm(q)
        if is_model and q not in model_full:
            errs.append(f"{where}: cita del modelo inexistente «{q[:50]}»")
        if not is_model and q not in prompt_full:
            errs.append(f"{where}: cita del enunciado inexistente «{q[:50]}»")


def _spelling(label, s, errs):
    for m in AMERICAN.finditer(s):
        errs.append(f"{label}: grafía americana «{m.group(0)}»")
    for w in re.findall(r"\b\w+iz(?:e|es|ed|ing|ation|ations)\b", s, re.I):
        if not w.lower().startswith(("size", "prize", "seiz")) and w.lower() not in IZE_OK:
            errs.append(f"{label}: «{w}» con -ize (el proyecto usa -ise)")


def _check_letter(spec, errs):
    m = spec["model"]
    sal, clo, sig = (m.get("salutation") or "").strip(), (m.get("closing") or "").strip(), m.get("signature")
    if m.get("title"):
        errs.append("letter: la carta no lleva título")
    if any(pa.get("heading") for pa in m["paras"]):
        errs.append("letter: la carta no lleva encabezados")
    if not sal or not clo or not sig:
        errs.append("letter: faltan saludo, despedida o firma")
        return
    if re.search(r"\b(Mr|Ms|Mrs|Dr)\.", sal + " " + sig):
        errs.append("letter: punto tras Mr, Ms o Dr (en británico, sin punto)")
    c = clo.rstrip(",")
    if SALUT_UNKNOWN.match(sal):
        if c not in CLOSE_FORMAL_UNKNOWN:
            errs.append(f"letter: «{sal}» pide «Yours faithfully», no «{c}»")
    elif SALUT_NAMED.match(sal) or SALUT_FIRST.match(sal):
        allowed = CLOSE_FORMAL_NAMED if spec["register"] == "formal" else CLOSE_SEMI
        if c not in allowed:
            errs.append(f"letter: «{sal}» en registro {spec['register']} no admite «{c}»")
        if spec["register"] == "formal" and SALUT_FIRST.match(sal) and not SALUT_NAMED.match(sal):
            errs.append("letter: saludo con nombre de pila en una carta formal")
    else:
        errs.append(f"letter: saludo no reconocido «{sal}»")
    if sal.endswith(",") != clo.endswith(","):
        errs.append("letter: puntuación distinta tras el saludo y tras la despedida")


def verify(spec):
    """Comprobaciones de formato y coherencia. Devuelve (errores, info)."""
    errs = []
    for f in ("num", "subtitle", "genre", "register", "prompt", "analysis", "points", "plan", "model", "comments",
              "errors"):
        if not spec.get(f):
            errs.append(f"falta el campo '{f}'")
    if errs:
        return errs, {}
    g, reg = spec["genre"], spec["register"]
    if g not in GENRES:
        return [f"género desconocido '{g}'"], {}
    if reg not in REGISTERS[g]:
        errs.append(f"registro '{reg}' no previsto para {g} ({sorted(REGISTERS[g])})")
    m = spec["model"]
    if not m.get("paras") or not all(pa.get("text") for pa in m["paras"]):
        return errs + ["el modelo necesita párrafos con texto"], {}
    prompt = _norm(spec["prompt"])
    paras = [_norm(pa["text"]) for pa in m["paras"]]
    model_full = " ".join(_norm(t) for _, t in model_parts(spec))
    # longitudes
    pw_ = prompt_words(spec)
    if pw_ > PROMPT_MAX:
        errs.append(f"enunciado de {pw_} palabras con la orden final (máximo {PROMPT_MAX})")
    mw = model_words(spec)
    if not MODEL_MIN <= mw <= MODEL_MAX:
        errs.append(f"modelo fuera de {MODEL_MIN}–{MODEL_MAX} palabras: {mw}")
    lo, hi = PARS[g]
    if not lo <= len(paras) <= hi:
        errs.append(f"el modelo tiene {len(paras)} párrafos (se esperaban {lo}–{hi})")
    for _, x in model_parts(spec):
        if re.search(r"[\[\]{}<>]", x):
            errs.append(f"marcado en el modelo: {x[:40]}…")
    if re.search(r"[\[\]{}<>]", spec["prompt"]):
        errs.append("marcado en el enunciado")
    # formato del genero
    if g in ("article", "review", "report") and not m.get("title"):
        errs.append(f"{g}: falta el título")
    if g in ("article", "review") and any(pa.get("heading") for pa in m["paras"]) and g == "review":
        errs.append("review: sin encabezados")
    if g == "report":
        if not all(pa.get("heading") for pa in m["paras"]):
            errs.append("report: cada sección necesita su encabezado")
        heads = [pa.get("heading", "") for pa in m["paras"]]
        if len(set(heads)) != len(heads):
            errs.append("report: encabezados repetidos")
    if g != "letter" and (m.get("salutation") or m.get("closing") or m.get("signature")):
        errs.append(f"{g}: saludo, despedida o firma fuera de una carta")
    if g == "letter":
        _check_letter(spec, errs)
    # analisis
    for a in spec["analysis"]:
        if a.get("dato") not in DATOS:
            errs.append(f"análisis: dato desconocido '{a.get('dato')}'")
        if a.get("quote") and _norm(a["quote"]) not in prompt + " " + instruction(spec):
            errs.append(f"análisis ({a.get('dato')}): la cita «{a['quote'][:40]}» no está en el enunciado")
        if not a.get("note"):
            errs.append(f"análisis ({a.get('dato')}): falta la nota")
    # puntos
    pts = spec["points"]
    if not 2 <= len(pts) <= 3:
        errs.append(f"el enunciado necesita dos o tres puntos ({len(pts)})")
    if [pt.get("id") for pt in pts] != [f"P{i}" for i in range(1, len(pts) + 1)]:
        errs.append("puntos: los ids deben ser P1, P2, P3 en orden")
    for pt in pts:
        pid = pt.get("id", "?")
        for f in ("quote", "asks", "par", "model"):
            if not pt.get(f):
                errs.append(f"{pid}: falta el campo '{f}'")
        if _norm(pt.get("quote", "")) not in prompt:
            errs.append(f"{pid}: la cita «{pt.get('quote', '')[:40]}» no está en el enunciado")
        par = pt.get("par")
        if not isinstance(par, int) or not 1 <= par <= len(paras):
            errs.append(f"{pid}: párrafo del modelo fuera de rango ({par})")
        elif _norm(pt.get("model", "")) not in paras[par - 1]:
            where = [i for i, x in enumerate(paras, 1) if _norm(pt.get("model", "")) in x]
            errs.append(f"{pid}: la cita del modelo no está en el párrafo {par}"
                        f"{' (está en ' + str(where) + ')' if where else ' (no existe)'}")
    # plan
    plan = spec["plan"]
    if [pl.get("par") for pl in plan] != list(range(1, len(paras) + 1)):
        errs.append("el plan necesita una entrada por párrafo del modelo, en orden")
    else:
        for pt in pts:
            par = pt.get("par")
            if not (isinstance(par, int) and 1 <= par <= len(plan) and pt.get("id") in plan[par - 1]["points"]):
                errs.append(f"{pt.get('id')}: el plan no lo coloca en el párrafo {par}")
        ids = {pt.get("id") for pt in pts}
        for pl in plan:
            for x in pl.get("points", []):
                if x not in ids:
                    errs.append(f"plan, párrafo {pl['par']}: punto desconocido '{x}'")
    # comentarios y errores
    if sorted(spec["comments"]) != sorted(CRITERIA):
        errs.append(f"comentarios: se esperaban {CRITERIA}")
    else:
        for c in CRITERIA:
            cm = spec["comments"][c]
            if not cm.get("text") or not any(gg == "=" for gg, _ in QUOTE_RE.findall(cm["text"])):
                errs.append(f"comentario de {c}: no cita el modelo")
            if not cm.get("theory"):
                errs.append(f"comentario de {c}: sin teoría")
            for s in cm.get("theory", []):
                if s not in THEORY:
                    errs.append(f"comentario de {c}: sección de teoría inexistente §{s}")
    if len(spec["errors"]) < 4:
        errs.append(f"hacen falta al menos cuatro errores comentados ({len(spec['errors'])})")
    for i, er in enumerate(spec["errors"], 1):
        for f in ("error", "why", "codes", "theory"):
            if not er.get(f):
                errs.append(f"error {i}: falta el campo '{f}'")
        for c in er.get("codes", []):
            if c not in CODES:
                errs.append(f"error {i}: código de rúbrica desconocido {c}")
        for s in er.get("theory", []):
            if s not in THEORY:
                errs.append(f"error {i}: sección de teoría inexistente §{s}")
    # citas y marcado
    prompt_full = prompt + " " + instruction(spec)
    fields = [(f"análisis {a.get('dato')}", a.get("note", "")) for a in spec["analysis"]]
    fields += [(f"{pt.get('id')} asks", pt.get("asks", "")) for pt in pts]
    fields += [(f"plan {pl.get('par')}", pl.get("content", "")) for pl in plan]
    fields += [(f"comentario {c}", spec["comments"].get(c, {}).get("text", "")) for c in CRITERIA]
    fields += [(f"error {i}", er.get("error", "") + " " + er.get("why", "")) for i, er in enumerate(spec["errors"], 1)]
    for where, s in fields:
        _check_quotes(where, s, prompt_full, model_full, errs)
        if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(s)):
            errs.append(f"{where}: marcado sin resolver")
    for pt in pts:
        _check_quotes(f"{pt.get('id')} model", "{{=" + pt.get("model", "") + "}}", prompt_full, model_full, errs)

    # copia del enunciado (las frases de shared_ok se retiran de los dos lados antes de comparar)
    def _strip_ok(x, tag):
        for j, o in enumerate(spec.get("shared_ok", [])):
            x = re.sub(re.escape(_norm(o)), f" zz{tag}{j} ", x, flags=re.I)
        return x
    lifted = shared_runs(_strip_ok(model_full, "m"), _strip_ok(prompt, "t"), LIFT_N)
    if lifted:
        errs.append("secuencias copiadas del enunciado en el modelo: " + "; ".join(f"«{x}»" for x in lifted))
    _spelling("enunciado", spec["prompt"], errs)
    _spelling("modelo", model_full, errs)
    if reg == "formal" or g == "report":
        for mm_ in CONTRACTION.finditer(model_full):
            errs.append(f"modelo: contracción «{mm_.group(0)}» en registro {reg} ({g})")
    info = {"prompt": pw_, "model": mw, "pars": par_words(spec), "genre": g, "register": reg,
            "contractions": len(CONTRACTION.findall(model_full)),
            "tri": len(shared_runs(model_full, prompt, 3))}
    return errs, info


def check_pdf(path):
    """Busca restos de codigo o de marcado en el texto del PDF ya generado."""
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            txt = "\n".join(pg.extract_text() or "" for pg in pdf.pages)
    except ImportError:
        from pypdf import PdfReader
        txt = "\n".join(pg.extract_text() or "" for pg in PdfReader(path).pages)
    return re.findall(r"\{\{|\}\}|\[\[|\]\]|<font|</?b>|</?i>|<br|&nbsp|&amp", txt)


def make(spec, out_dir="/mnt/user-data/outputs"):
    """Verifica, genera y comprueba el PDF. Devuelve la ruta; lanza ValueError si algo falla."""
    errs, info = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}:\n  - " + "\n  - ".join(errs))
    path = build_sheet(spec, os.path.join(out_dir, f"WRT-P2_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    print(f"WRT-P2_Practica_{spec['num']}.pdf · {info['genre']} {info['register']} · enunciado {info['prompt']} "
          f"palabras · modelo {info['model']} palabras ({'/'.join(str(x) for x in info['pars'])}) · "
          f"{info['contractions']} contracciones · {info['tri']} trigramas compartidos con el enunciado · "
          f"verificación sin errores")
    return path


# ---------- Hoja de ejemplo (el enunciado de WRT-P2_Teoria_v1 §2.1, numerada como 99) ----------
DEMO = {
    "num": "99",
    "subtitle": "Hoja de prueba del generador (enunciado de la teoría, §2.1)",
    "genre": "report", "register": "formal",
    "prompt": "The director of the international company you work for is considering replacing all face-to-face "
              "staff training with online courses. You have been asked to write a report for the director. Your "
              "report should briefly describe the training currently on offer, assess how well online courses "
              "would meet employees’ needs and recommend whether the change should go ahead.",
    "analysis": [
        {"dato": "Lector", "quote": "a report for the director", "note": "Un superior: registro formal."},
        {"dato": "Propósito", "quote": "recommend whether the change should go ahead",
         "note": "Todo desemboca en una recomendación."},
    ],
    "points": [
        {"id": "P1", "quote": "briefly describe the training currently on offer", "asks": "Hechos, en pocas frases.",
         "par": 2, "model": "two-day workshops"},
        {"id": "P2", "quote": "assess how well online courses would meet employees’ needs",
         "asks": "Un juicio matizado.", "par": 3, "model": "would serve some needs far better than others"},
        {"id": "P3", "quote": "recommend whether the change should go ahead", "asks": "Una recomendación clara.",
         "par": 4, "model": "a partial change"},
    ],
    "plan": [{"par": 1, "content": "Propósito y fuentes", "points": []},
             {"par": 2, "content": "La formación actual", "points": ["P1"]},
             {"par": 3, "content": "Ventajas y límites de lo online", "points": ["P2"]},
             {"par": 4, "content": "Recomendación", "points": ["P3"]}],
    "model": {
        "title": "Staff Training: Online or Face to Face?",
        "paras": [
            {"heading": "Introduction",
             "text": "The aim of this report is to assess whether the company’s training programme could be moved "
                     "entirely online, as has been proposed, and to recommend a course of action. It draws on "
                     "conversations with colleagues in three departments and on my own experience of both formats "
                     "over the past four years, during which I have attended most of the courses the company runs."},
            {"heading": "Current provision",
             "text": "Training is currently delivered in two-day workshops held at head office four times a year. "
                     "Most cover technical skills, such as the new accounting software, while a smaller number deal "
                     "with negotiation, presentations and team leadership. Attendance is compulsory for new staff "
                     "and voluntary for everyone else, and the sessions are generally well rated by those who "
                     "attend them."},
            {"heading": "The case for and against online courses",
             "text": "Online courses would serve some needs far better than others. Technical training lends "
                     "itself well to self-paced modules: staff could learn at their own speed, revisit difficult "
                     "material when they actually need it and avoid the cost and disruption of travelling to head "
                     "office. Courses built around interpersonal skills are a different matter. Negotiation and "
                     "leadership are learnt largely through practice and immediate feedback, and colleagues "
                     "consistently describe the role-plays and informal discussions as the most valuable part of "
                     "the workshops – precisely what a screen cannot easily reproduce."},
            {"heading": "Recommendation",
             "text": "I would therefore recommend a partial change rather than a complete one. Technical courses "
                     "should move online from next year, which would release a considerable part of the budget, "
                     "while the remaining workshops should continue in person, possibly in a shorter one-day "
                     "format. A review after twelve months would show whether the balance is right."},
        ]},
    "comments": {
        "Content": {"text": "Los tres puntos, con {{=two-day workshops}}, {{=would serve some needs far better than "
                            "others}} y {{=a partial change}}.", "theory": ["2.2"]},
        "Communicative Achievement": {"text": "Formal e impersonal; recomienda en primera persona: {{=I would "
                                              "therefore recommend}}.", "theory": ["6.2"]},
        "Organisation": {"text": "Encabezados con contenido y sección central con contraste: {{=a different "
                                 "matter}}.", "theory": ["6.3"]},
        "Language": {"text": "Precisión: {{=lends itself well to}}, {{=release a considerable part of the "
                             "budget}}.", "theory": ["6.4"]},
    },
    "errors": [
        {"error": "Ignorar [[briefly]]", "why": "Describir cada curso en detalle deja sin espacio el punto central.",
         "codes": ["C2"], "theory": ["2.2"]},
        {"error": "Recomendar sin matizar [[all]]", "why": "El enunciado habla de {{replacing all face-to-face "
                                                          "staff training}}: un sí parcial también es respuesta.",
         "codes": ["C4"], "theory": ["2.1"]},
        {"error": "Escribirlo como un essay", "why": "Sin título ni encabezados no es un report.",
         "codes": ["CA1"], "theory": ["6.1"]},
        {"error": "Contracciones", "why": "El lector es el director.", "codes": ["CA2"], "theory": ["3.1"]},
    ],
    "lex": [],
}


if __name__ == "__main__":
    import runpy
    if len(sys.argv) < 2:
        print("Uso: python3 gen_WRT-P2.py --demo | mis_hojas.py [carpeta_salida]")
        sys.exit(1)
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "/mnt/user-data/outputs"
    os.makedirs(out_dir, exist_ok=True)
    if sys.argv[1] == "--demo":
        specs = [DEMO]
    else:
        ns = runpy.run_path(sys.argv[1])
        specs = ns.get("SPECS") or [ns["SPEC"]]
    for sp in specs:
        make(sp, out_dir)
