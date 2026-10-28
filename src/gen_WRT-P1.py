# gen_WRT-P1.py · Generador de Writing Part 1 (essay a partir de dos textos) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa: enunciado (dos textos de unas 100 palabras), hoja de autocorrección con la
#     rubrica de WRT-P1_Teoria_v1 §9 y soluciones (ideas clave de cada texto, relacion entre los textos, plan,
#     essay modelo comentado criterio por criterio y errores que costarian puntos).
#   - Bloques sueltos para insertar la Part 1 en un simulacro (SIM): enunciado, hoja de autocorrección y
#     soluciones por separado.
#   - Verificacion automatica antes y despues de generar el PDF.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_WRT-P1.py --demo [carpeta_salida]          -> hoja de ejemplo (el caso de la teoria, como 99)
#   python3 gen_WRT-P1.py mis_hojas.py [carpeta_salida]   -> mis_hojas.py define SPECS = [spec, ...]
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_w1", "/ruta/gen_WRT-P1.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, info = gen.verify(spec)
#   gen.make(spec, "/mnt/user-data/outputs")
#   story += gen.question_flowables(spec)          # para un SIM
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num         "04"
#   subtitle    "Hoja 04 · Tema · relación · dificultad 2 de 4"            (espanol)
#   texts       [{"title": "...", "text": "..."}, {"title": "...", "text": "..."}]   ingles britanico, 90-110
#               palabras cada uno (el titulo no cuenta)
#   relation    {"type": uno de RELATIONS, "axis": "eje del debate", "contact": "punto de contacto"}
#   key_points  4 diccionarios, en este orden de id: T1·1, T1·2, T2·1, T2·2
#       id      "T1·1"
#       source  cita literal del texto correspondiente (se comprueba)
#       idea    la idea clave con palabras propias, en espanol
#       par     parrafo del modelo donde aparece
#       model   cita literal del modelo, dentro de ese parrafo (se comprueba)
#   stance      {"type": uno de STANCES, "text": "postura del modelo, en espanol"}
#   scheme      "integrado" o "bloques"
#   plan        [{"par": 1, "content": "...", "ideas": ["T1·1", "propia"]}, ...]  una entrada por parrafo
#   model       [parrafo, parrafo, ...]  essay modelo, 4-5 parrafos, 240-280 palabras, sin contracciones
#   own_ideas   ["... {{=cita del modelo}} ...", ...]  al menos una
#   comments    {"Content": {"text": "...", "theory": ["3.1"]}, "Communicative Achievement": {...},
#                "Organisation": {...}, "Language": {...}}   cada texto cita el modelo al menos una vez
#   errors      [{"error": "...", "why": "...", "codes": ["C1"], "theory": ["3.1"]}, ...]  al menos cuatro;
#               codes = preguntas de la rubrica de autocorrección que fallarian (RUBRIC)
#   shared_ok   frases que el modelo puede compartir con los textos (terminos tecnicos, nombres): opcional
#   lex         lexico para el modulo LEX (no se imprime; se usa en el resumen de cierre)
#
#   Marcado en los campos en espanol:
#     {{texto}}   -> cita literal de uno de los dos textos, en serif; se comprueba que existe tal cual
#     {{=texto}}  -> cita literal del essay modelo, en serif cursiva; se comprueba que existe tal cual
#     [[texto]]   -> ingles en serif sin comprobar
#     [[!TEXTO]]  -> ingles en serif y negrita
#
# RECUENTO DE PALABRAS
#   Cuenta como palabra cada secuencia separada por espacios que contiene al menos una letra o cifra: un
#   compuesto con guion o una contraccion es una palabra; una raya suelta no cuenta.
#
# QUE COMPRUEBA verify()
#   campos completos · 90-110 palabras por texto y 240-280 en el modelo · 4-5 parrafos · cuatro ideas clave
#   en orden, con su cita en el texto que les corresponde y su cita del modelo en el parrafo indicado · el plan
#   tiene un parrafo por cada parrafo del modelo y coloca cada idea clave donde esta · todas las citas existen ·
#   ninguna secuencia de cuatro palabras o mas copiada de los textos en el modelo (salvo shared_ok) · grafias
#   americanas y terminaciones -ize · contracciones en el modelo · tipos de relacion, postura y esquema ·
#   codigos de la rubrica y secciones de teoria existentes · marcado sin resolver · con esquema
#   integrado, que al menos un parrafo del desarrollo combine ideas clave de los dos textos.
#
# LO QUE EL GENERADOR NO PUEDE COMPROBAR (a mano)
#   - Que las cuatro ideas clave sean de verdad las ideas clave y que el modelo merezca la banda 5.
#   - Que los datos reales de los textos sean ciertos; ingles britanico; registro; dificultad graduada.
#   - Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402

VERSION = "1"
TEXT_MIN, TEXT_MAX = 90, 110
MODEL_MIN, MODEL_MAX = 240, 280
PARS_MIN, PARS_MAX = 4, 5
LIFT_N = 4
THEORY_DOC = "WRT-P1_Teoria_v1"
KP_IDS = ["T1·1", "T1·2", "T2·1", "T2·2"]
RELATIONS = ["Opuestos", "Complementarios", "Mismo diagnóstico, distinta solución",
             "Mismo objetivo, distinto diagnóstico"]
STANCES = ["Elegir", "Matizar", "Superar"]
SCHEMES = {"integrado": "esquema integrado por ejes (§7.2)", "bloques": "esquema por bloques (§7.1)"}
CRITERIA = ["Content", "Communicative Achievement", "Organisation", "Language"]

THEORY = {
    "1.1": "Formato y enunciado", "1.2": "Qué cambia respecto al C1", "1.3": "Cómo se puntúa",
    "1.4": "Las cuatro respuestas del handbook",
    "2.1": "Cinco pasos", "2.2": "Tiempo y recuento",
    "3.1": "Qué es una idea clave", "3.2": "Cómo localizarlas", "3.3": "La relación entre los textos",
    "3.4": "La ficha de lectura",
    "4.1": "Palabras clave frente a fragmentos copiados", "4.2": "Técnicas de reformulación",
    "4.3": "Verbos de atribución", "4.4": "Comprimir sin deformar",
    "5.1": "Evaluar no es decir si se está de acuerdo", "5.2": "Formas de evaluar un argumento",
    "5.3": "Conceder y matizar", "5.4": "Evaluar los dos textos",
    "6.1": "Qué cuenta como idea propia", "6.2": "Tres posturas posibles", "6.3": "Registro y primera persona",
    "7.1": "Esquema por bloques", "7.2": "Esquema integrado por ejes", "7.3": "Introducción y conclusión",
    "7.4": "Cohesión de nivel C2", "7.5": "Presupuesto de palabras",
    "8.1": "Qué separa la banda 3 de la 5", "8.2": "Estructuras rentables",
    "8.3": "Errores frecuentes del hispanohablante",
    "9.1": "Los cuatro criterios en preguntas", "9.2": "De las respuestas a una nota",
    "9.3": "Lista de comprobación final",
    "10": "Caso completo",
}

# Rubrica de autocorreccion de WRT-P1_Teoria_v1 §9.1 (version abreviada para la hoja)
RUBRIC = [
    ("Content", [
        ("C1", "Las cuatro ideas clave, comprensibles sin tener los textos delante"),
        ("C2", "Las ideas de los dos textos, evaluadas con razones"),
        ("C3", "Al menos una idea propia y una postura clara"),
        ("C4", "Todo relevante, sin digresiones ni malas interpretaciones")]),
    ("Communicative Achievement", [
        ("CA1", "Essay reconocible: introducción, desarrollo argumentado y conclusión"),
        ("CA2", "Registro neutro-formal constante"),
        ("CA3", "Resume, evalúa y opina"),
        ("CA4", "Las ideas complejas se entienden a la primera"),
        ("CA5", "Resumen, evaluación y opinión integrados; el texto convence")]),
    ("Organisation", [
        ("O1", "Cada párrafo tiene una función y una frase que la anuncia"),
        ("O2", "Progresión lógica"),
        ("O3", "Cohesión variada y correcta"),
        ("O4", "La conclusión responde a la introducción"),
        ("O5", "Patrones organizativos más allá de los conectores")]),
    ("Language", [
        ("L1", "Léxico menos común usado con precisión"),
        ("L2", "Estructuras complejas variadas y controladas"),
        ("L3", "Solo despistes; nada impide entender"),
        ("L4", "Una sola variedad de inglés y nada copiado de los textos"),
        ("L5", "Natural y preciso, sin expresiones forzadas")]),
]
CODES = {c: crit for crit, qs in RUBRIC for c, _ in qs}

QUOTE_RE = re.compile(r"\{\{(=?)(.+?)\}\}")
AMERICAN = re.compile(
    r"\b(colors?|colored|favor|favors|favored|favoring|favorite\w*|favorabl\w*|honor|honors|honored|honoring|"
    r"honorable|labor|labors|labored|laboring|neighbor\w*|behavior\w*|humor|humored|rumors?|harbor\w*|"
    r"flavor\w*|savor\w*|vigor|rigor|endeavor\w*|odors?|valor|armor\w*|center\w*|theaters?|liters?|fibers?|"
    r"defense|offense|traveled|traveling|traveler\w*|canceled|canceling|labeled|labeling|modeled|modeling|"
    r"judgment\w*|programs?|catalogs?|analyz\w*|paralyz\w*|fulfill|fulfills|enroll|enrolls|skeptic\w*|gray|"
    r"aging|practiced|practicing|jewelry|pajamas|mustache)\b", re.I)
IZE_OK = {"size", "prize", "seize", "capsize", "baize", "maize", "downsize", "oversize", "assize"}
CONTRACTION = re.compile(r"\b\w+(n’t|n't|’re|'re|’ve|'ve|’ll|'ll|’m|'m|’d|'d)\b", re.I)


# ---------- Ingles dentro del texto en espanol ----------
def E(s):
    return f'<font name="EN">{s}</font>'


def EI(s):
    return f'<font name="EN"><i>{s}</i></font>'


def EB(s):
    return f'<font name="EN"><b>{s}</b></font>'


def markup(s):
    """{{=cita del modelo}} -> EI; {{cita de los textos}} y [[x]] -> E; [[!X]] -> EB."""
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


# ---------- Estilos propios de la hoja (sobre la plantilla, sin cambiarla) ----------
_rub = ParagraphStyle("w1_rubric", parent=S["en"], fontSize=10.5, leading=15)
_num = ParagraphStyle("w1_num", parent=S["en"], fontName="EN-B", fontSize=16, leading=19, textColor=ACCENT)
_ttl = ParagraphStyle("w1_title", parent=S["en"], fontName="EN-B", fontSize=12, leading=16, textColor=NAVY,
                      spaceAfter=4)
_txt = ParagraphStyle("w1_txt", parent=S["en"], fontSize=10.8, leading=16.2, spaceAfter=0)
_essay = ParagraphStyle("w1_essay", parent=S["en"], leading=15.2, spaceAfter=6)
_ihead = ParagraphStyle("w1_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)
_PNUM = '<font name="Sans-B" color="#A4243B">{}</font>&nbsp;&nbsp;'


def _model_words(spec):
    return wc(" ".join(spec["model"]))


def _theory(secs):
    return " · ".join(f"§{s} {THEORY[s]}" for s in secs)


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def question_flowables(spec, with_title_block=False, number="1"):
    """Rubrica, los dos textos y la orden final. Con with_title_block=True antepone el bloque de titulo."""
    out = []
    if with_title_block:
        out += title_block(f"WRT-P1 · Práctica {spec['num']}", "Essay", spec["subtitle"],
                           "Part 1 · 240–280 palabras · tiempo orientativo: 45 minutos · sin consultar la teoría")
    out.append(Paragraph(f"<b>Part {number}</b>", _rub))
    out.append(Paragraph(
        "Read the two texts below. Write an essay in which you summarise and evaluate the key points from both "
        "texts, using your own words as far as possible and including your own ideas.", _rub))
    out.append(Paragraph("Write your answer in <b>240–280</b> words.", _rub))
    out.append(Spacer(1, 8))
    for i, t in enumerate(spec["texts"], 1):
        tb = Table([[Paragraph(str(i), _num), [Paragraph(t["title"], _ttl), Paragraph(t["text"], _txt)]]],
                   colWidths=[12 * mm, CONTENT_W - 12 * mm])
        tb.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEABOVE", (0, 0), (-1, 0), 0.6, RULE),
            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ]))
        out.append(tb)
    line = Table([[""]], colWidths=[CONTENT_W], rowHeights=[2])
    line.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), 0.6, RULE)]))
    out += [line, Spacer(1, 6), Paragraph("<b>Write your essay.</b>", _rub)]
    return out


def answer_sheet_flowables(spec, heading="Hoja de autocorrección"):
    yn = '<font color="#5B6577">Sí · No</font>'
    out = [h2(heading), p(
        "Corrige al día siguiente, en frío. Primero marca la rúbrica sin mirar las soluciones; después compara tus "
        f"ideas clave con las de las soluciones y lee el modelo. Las preguntas completas están en {THEORY_DOC} §9.1.")]
    out += table([
        ["Dato", "Tu resultado"],
        ["Palabras", "________ (objetivo: 240–280)"],
        ["Tiempo empleado", "________ minutos (objetivo: unos 45)"],
        ["Ideas clave de las soluciones que estaban en tu essay", "________ / 4"],
    ], [92, 78], zebra=False, extra=[("TOPPADDING", (0, 1), (-1, -1), 3), ("BOTTOMPADDING", (0, 1), (-1, -1), 3)])
    rows = [["Código", "Pregunta", ""]]
    shade = []
    for crit, qs in RUBRIC:
        rows.append([f"<b>{crit}</b>", "", ""])
        shade.append(len(rows) - 1)
        rows += [[c, q, yn] for c, q in qs]
    extra = [("BACKGROUND", (0, r), (-1, r), ZEBRA) for r in shade]
    extra += [("SPAN", (0, r), (-1, r)) for r in shade]
    extra += [("TOPPADDING", (0, 1), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 1), (-1, -1), 2.2)]
    out += table(rows, [20, 126, 24], zebra=False, extra=extra)
    out.append(Paragraph(
        "<b>Content:</b> 5 si todo es sí · 4 un fallo menor · 3 dos fallos menores o una idea clave mal resumida · "
        "2 un texto sin evaluar o sin postura · 1 varias ideas clave omitidas o mal interpretadas. "
        "<b>Communicative Achievement, Organisation y Language:</b> 5 las cinco sí · 4 sí a las cuatro primeras · "
        "3 falla una de las cuatro primeras · 2 fallan dos · 1 fallan tres o cuatro.", S["small"]))
    out.append(Spacer(1, 4))
    sc = table([
        ["Content", "Communicative Achievement", "Organisation", "Language", "Total"],
        ["____ / 5", "____ / 5", "____ / 5", "____ / 5", "<b>____ / 20</b>"],
    ], [30, 46, 32, 30, 32], zebra=False, extra=[("TOPPADDING", (0, 1), (-1, -1), 8),
                                                 ("BOTTOMPADDING", (0, 1), (-1, -1), 8)])
    out.append(KeepTogether(sc))
    return out


def solutions_flowables(spec, with_band=True, heading=None):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 1 · Essay' dentro de un simulacro)."""
    H = h2 if not heading else h3
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(
        "Las soluciones dan las cuatro ideas clave con la frase del texto en que se apoyan, la relación entre los "
        "textos, el plan y un essay modelo que apunta a la banda 5 en los cuatro criterios, comentado criterio por "
        "criterio. Al final, los errores que costarían puntos, con la pregunta de la rúbrica que fallaría. Las citas "
        "de los textos van en redonda y las del modelo, en cursiva. Los números de sección remiten a "
        f"{THEORY_DOC}."))
    # ideas clave
    out.append(H("Ideas clave"))
    rows = [["Idea", "En el texto", "Con palabras propias", "En el modelo"]]
    for kp in spec["key_points"]:
        rows.append([f"<b>{kp['id']}</b>", E(kp["source"]), markup(kp["idea"]),
                     f"Párr. {kp['par']}: " + EI(kp["model"])])
    out += table(rows, [14, 54, 56, 46])
    rel = spec["relation"]
    out.append(p(f"<b>Relación entre los textos:</b> {rel['type'].lower()} (§3.3). <b>Eje del debate:</b> "
                 f"{markup(rel['axis'])} <b>Punto de contacto:</b> {markup(rel['contact'])}"))
    out.append(p("<b>Teoría:</b> " + _theory(["3.1", "3.3", "3.4"])))
    # plan
    st = spec["stance"]
    plan_block = [H("Plan del modelo"),
                  p(f"<b>Postura:</b> {st['type'].lower()} (§6.2). {markup(st['text'])} <b>Esquema:</b> "
                    f"{SCHEMES[spec['scheme']]}.")]
    rows = [["Párrafo", "Contenido", "Ideas"]]
    for pl in spec["plan"]:
        ideas = ", ".join("idea propia" if x == "propia" else x for x in pl["ideas"]) or "—"
        rows.append([str(pl["par"]), markup(pl["content"]), ideas])
    plan_block += table(rows, [18, 112, 40])
    out.append(KeepTogether(plan_block))
    # modelo
    out.append(CondPageBreak(110 * mm))
    out.append(H("Essay modelo"))
    paras = [Paragraph(_PNUM.format(i) + par, _essay) for i, par in enumerate(spec["model"], 1)]
    out += callout("ejemplo", paras, label=f"{_model_words(spec)} PALABRAS · BANDA OBJETIVO: 5 EN LOS CUATRO "
                                           "CRITERIOS")
    out.append(p("<b>Ideas propias del modelo:</b> " + " ".join(markup(x) for x in spec["own_ideas"])))
    # comentario
    out.append(CondPageBreak(60 * mm))
    out.append(H("Comentario por criterio"))
    rows = [["Criterio", "Comentario"]]
    for c in CRITERIA:
        cm = spec["comments"][c]
        rows.append([f"<b>{c}</b> · 5", markup(cm["text"]) + " <i>Teoría: " +
                     " · ".join("§" + s for s in cm["theory"]) + ".</i>"])
    out += table(rows, [36, 134])
    # errores
    out.append(CondPageBreak(45 * mm))
    out.append(H("Errores que costarían puntos"))
    for i, er in enumerate(spec["errors"], 1):
        codes = ", ".join(f"{c} ({CODES[c]})" for c in er["codes"])
        block = [Paragraph(f"{i} · {markup(er['error'])}", _ihead),
                 p(markup(er["why"])),
                 p(f"<b>Falla:</b> {codes}. <b>Teoría:</b> {_theory(er['theory'])}.")]
        out.append(KeepTogether(block))
    return out


def build_sheet(spec, out_path):
    """Hoja completa: enunciado, hoja de autocorrección (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"WRT-P1 · Práctica {n}", f"WRT-P1_Practica_{n}.pdf", title=f"WRT-P1 · Práctica {n}")
    return out_path


# ---------- Verificacion ----------
def _check_quotes(where, s, texts_full, model_full, errs):
    for is_model, q in QUOTE_RE.findall(s):
        q = _norm(q)
        if is_model and q not in model_full:
            errs.append(f"{where}: cita del modelo inexistente «{q[:50]}»")
        if not is_model and q not in texts_full:
            errs.append(f"{where}: cita de los textos inexistente «{q[:50]}»")


def _spelling(label, s, errs):
    for m in AMERICAN.finditer(s):
        errs.append(f"{label}: grafía americana «{m.group(0)}»")
    for w in re.findall(r"\b\w+iz(?:e|es|ed|ing|ation|ations)\b", s, re.I):
        if not w.lower().startswith(("size", "prize", "seiz")) and w.lower() not in IZE_OK:
            errs.append(f"{label}: «{w}» con -ize (el proyecto usa -ise)")


def verify(spec):
    """Comprobaciones de formato y coherencia. Devuelve (errores, info)."""
    errs = []
    for f in ("num", "subtitle", "texts", "relation", "key_points", "stance", "scheme", "plan", "model",
              "own_ideas", "comments", "errors"):
        if not spec.get(f):
            errs.append(f"falta el campo '{f}'")
    if errs:
        return errs, {}
    texts = spec["texts"]
    if len(texts) != 2 or not all(t.get("title") and t.get("text") for t in texts):
        return ["hacen falta dos textos con título"], {}
    tw = [wc(t["text"]) for t in texts]
    for i, w in enumerate(tw, 1):
        if not TEXT_MIN <= w <= TEXT_MAX:
            errs.append(f"texto {i} fuera de {TEXT_MIN}–{TEXT_MAX} palabras: {w}")
    model = [_norm(x) for x in spec["model"]]
    mw = _model_words(spec)
    if not MODEL_MIN <= mw <= MODEL_MAX:
        errs.append(f"modelo fuera de {MODEL_MIN}–{MODEL_MAX} palabras: {mw}")
    if not PARS_MIN <= len(model) <= PARS_MAX:
        errs.append(f"el modelo tiene {len(model)} párrafos (se esperaban {PARS_MIN}–{PARS_MAX})")
    for x in [t["title"] for t in texts] + [t["text"] for t in texts] + model:
        if re.search(r"[\[\]{}<>]", x):
            errs.append(f"marcado en un texto o en el modelo: {x[:40]}…")
    t_norm = [_norm(t["text"]) for t in texts]
    texts_full = " ".join(t_norm)
    model_full = " ".join(model)
    # relacion, postura, esquema
    if spec["relation"].get("type") not in RELATIONS:
        errs.append(f"tipo de relación desconocido '{spec['relation'].get('type')}'")
    for f in ("axis", "contact"):
        if not spec["relation"].get(f):
            errs.append(f"falta relation['{f}']")
    if spec["stance"].get("type") not in STANCES or not spec["stance"].get("text"):
        errs.append(f"postura no válida '{spec['stance'].get('type')}'")
    if spec["scheme"] not in SCHEMES:
        errs.append(f"esquema desconocido '{spec['scheme']}'")
    # ideas clave
    kps = spec["key_points"]
    if [k.get("id") for k in kps] != KP_IDS:
        errs.append(f"ideas clave: se esperaban {KP_IDS}")
    for k in kps:
        kid = k.get("id", "?")
        for f in ("source", "idea", "par", "model"):
            if not k.get(f):
                errs.append(f"{kid}: falta el campo '{f}'")
        if kid in KP_IDS:
            src_text = t_norm[0] if kid.startswith("T1") else t_norm[1]
            if _norm(k.get("source", "")) not in src_text:
                errs.append(f"{kid}: la cita «{k.get('source', '')[:40]}» no está en el texto {kid[1]}")
        par = k.get("par")
        if not isinstance(par, int) or not 1 <= par <= len(model):
            errs.append(f"{kid}: párrafo del modelo fuera de rango ({par})")
        elif _norm(k.get("model", "")) not in model[par - 1]:
            where = [i for i, m in enumerate(model, 1) if _norm(k.get("model", "")) in m]
            errs.append(f"{kid}: la cita del modelo no está en el párrafo {par}"
                        f"{' (está en ' + str(where) + ')' if where else ' (no existe)'}")
    # plan
    plan = spec["plan"]
    if [pl.get("par") for pl in plan] != list(range(1, len(model) + 1)):
        errs.append("el plan necesita una entrada por párrafo del modelo, en orden")
    else:
        for k in kps:
            par = k.get("par")
            placed = isinstance(par, int) and 1 <= par <= len(plan) and k.get("id") in plan[par - 1].get("ideas", [])
            if not placed:
                errs.append(f"{k.get('id')}: el plan no la coloca en el párrafo {par}")
        for pl in plan:
            for x in pl.get("ideas", []):
                if x not in KP_IDS + ["propia"]:
                    errs.append(f"plan, párrafo {pl['par']}: idea desconocida '{x}'")
    # esquema integrado: al menos un parrafo del desarrollo combina ideas clave de los dos textos (§7.2)
    if spec["scheme"] == "integrado" and isinstance(model, list):
        by_par = {}
        for k in kps:
            if isinstance(k.get("par"), int):
                by_par.setdefault(k["par"], set()).add(k.get("id", "??")[:2])
        if not any(v >= {"T1", "T2"} for v in by_par.values()):
            errs.append("esquema integrado, pero ningún párrafo combina ideas de los dos textos: el modelo va un "
                        "párrafo por texto, que es la variante del esquema por bloques (§7.1)")
    # ideas propias, comentarios, errores
    if not any(QUOTE_RE.search(x) and QUOTE_RE.search(x).group(1) for x in spec["own_ideas"]):
        errs.append("las ideas propias no citan el modelo")
    if sorted(spec["comments"]) != sorted(CRITERIA):
        errs.append(f"comentarios: se esperaban {CRITERIA}")
    else:
        for c in CRITERIA:
            cm = spec["comments"][c]
            if not cm.get("text") or not any(g == "=" for g, _ in QUOTE_RE.findall(cm["text"])):
                errs.append(f"comentario de {c}: no cita el modelo")
            for s in cm.get("theory", []):
                if s not in THEORY:
                    errs.append(f"comentario de {c}: sección de teoría inexistente §{s}")
            if not cm.get("theory"):
                errs.append(f"comentario de {c}: sin teoría")
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
    # todas las citas y el marcado
    fields = [("relación", spec["relation"]["axis"]), ("relación", spec["relation"]["contact"]),
              ("postura", spec["stance"]["text"])]
    fields += [(f"{k.get('id')} idea", k.get("idea", "")) for k in kps]
    fields += [(f"plan {pl.get('par')}", pl.get("content", "")) for pl in plan]
    fields += [("ideas propias", x) for x in spec["own_ideas"]]
    fields += [(f"comentario {c}", spec["comments"].get(c, {}).get("text", "")) for c in CRITERIA]
    fields += [(f"error {i}", er.get("error", "") + " " + er.get("why", ""))
               for i, er in enumerate(spec["errors"], 1)]
    for where, s in fields:
        _check_quotes(where, s, texts_full, model_full, errs)
        if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(s)):
            errs.append(f"{where}: marcado sin resolver")
    # copia, ortografia, contracciones
    # las frases de shared_ok se retiran de los dos lados antes de comparar (con marcadores distintos que nunca
    # coinciden), para que no generen coincidencias ni siquiera en el limite con la frase siguiente
    def _strip_ok(x, tag):
        for j, o in enumerate(spec.get("shared_ok", [])):
            x = re.sub(re.escape(_norm(o)), f" zz{tag}{j} ", x, flags=re.I)
        return x
    lifted = []
    for i, t in enumerate(t_norm, 1):
        for g in shared_runs(_strip_ok(model_full, "m"), _strip_ok(t, "t"), LIFT_N):
            lifted.append(f"texto {i}: «{g}»")
    if lifted:
        errs.append("secuencias copiadas en el modelo: " + "; ".join(lifted))
    for i, t in enumerate(texts, 1):
        _spelling(f"texto {i}", t["title"] + " " + t["text"], errs)
    _spelling("modelo", model_full, errs)
    for m in CONTRACTION.finditer(model_full):
        errs.append(f"modelo: contracción «{m.group(0)}»")
    tri = sum(len(shared_runs(model_full, t, 3)) for t in t_norm)
    info = {"texts": tw, "model": mw, "pars": [wc(x) for x in model], "tri": tri,
            "relation": spec["relation"]["type"], "stance": spec["stance"]["type"], "scheme": spec["scheme"]}
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
    path = build_sheet(spec, os.path.join(out_dir, f"WRT-P1_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    print(f"WRT-P1_Practica_{spec['num']}.pdf · textos {info['texts'][0]} y {info['texts'][1]} palabras · modelo "
          f"{info['model']} palabras ({'/'.join(str(x) for x in info['pars'])}) · {info['tri']} trigramas "
          f"compartidos con los textos · {info['relation'].lower()} · postura {info['stance'].lower()} · "
          f"esquema {info['scheme']} · verificación sin errores")
    return path


# ---------- Hoja de ejemplo (caso completo de WRT-P1_Teoria_v1 §10, numerada como 99) ----------
DEMO = {
    "num": "99",
    "subtitle": "Hoja de prueba del generador (caso completo de la teoría, §10)",
    "texts": [
        {"title": "Beyond the bookshelf",
         "text": "Public libraries were built for an age in which books were scarce and expensive, and that age has "
                 "passed. Loans of printed books have fallen steadily for two decades, and a library that measures "
                 "its worth by what it lends is measuring its own decline. If libraries are to survive, they must "
                 "become something more: places where people learn to use technology, find help with official "
                 "forms, attend talks and meet one another. The most successful branches have already made this "
                 "shift, and their visitor numbers show that the public will come when there is a reason to."},
        {"title": "The case for quiet",
         "text": "In the rush to reinvent libraries as lively community hubs, something valuable is in danger of "
                 "being lost. A library is one of the very few indoor public spaces where nobody is expected to buy "
                 "anything, and where a person may sit for hours undisturbed. For students without a desk at home, "
                 "or anyone who simply needs to think, that silence is not a luxury but a necessity. Filling the "
                 "building with events and activities may raise visitor numbers, but numbers are a poor measure of "
                 "value. A library that tries to be everything risks becoming merely another noisy room."},
    ],
    "relation": {"type": "Mismo objetivo, distinto diagnóstico",
                 "axis": "¿la biblioteca sobrevive reinventándose o protegiendo lo que ya ofrece?",
                 "contact": "el texto 1 usa las visitas como prueba de éxito ({{their visitor numbers show}}); el "
                            "texto 2 responde que no miden el valor ({{numbers are a poor measure of value}})."},
    "key_points": [
        {"id": "T1·1", "source": "a library that measures its worth by what it lends is measuring its own decline",
         "idea": "El préstamo, razón de ser de la biblioteca, está en declive porque los libros ya no escasean.",
         "par": 2, "model": "has been in long-term decline"},
        {"id": "T1·2", "source": "If libraries are to survive, they must become something more",
         "idea": "Para sobrevivir tiene que convertirse en un centro de servicios y encuentro; las que lo han hecho "
                 "atraen público.", "par": 2, "model": "only by offering new services"},
        {"id": "T2·1", "source": "that silence is not a luxury but a necessity",
         "idea": "Su valor está en ser un espacio público, gratuito y tranquilo, imprescindible para quien no tiene "
                 "otro sitio donde estudiar o pensar.", "par": 3, "model": "an undisturbed seat is indispensable"},
        {"id": "T2·2", "source": "numbers are a poor measure of value",
         "idea": "Llenarla de actividades puede subir las visitas, pero las visitas no miden el valor y el silencio "
                 "se pierde.", "par": 2, "model": "rising footfall is evidence of popularity, not of value"},
    ],
    "stance": {"type": "Superar", "text": "Las dos posturas defienden a quien no tiene alternativa, y un edificio "
                                          "con zonas separadas sirve a ambas."},
    "scheme": "integrado",
    "plan": [
        {"par": 1, "content": "Pregunta retórica y eje del debate", "ideas": []},
        {"par": 2, "content": "Eje «el éxito se mide en visitas»: diagnóstico del texto 1, válido; su prueba, "
                              "rebatida por el texto 2", "ideas": ["T1·1", "T1·2", "T2·2"]},
        {"par": 3, "content": "Eje «el silencio»: argumento del texto 2, convincente pero parcial; contraejemplo "
                              "propio", "ideas": ["T2·1", "propia"]},
        {"par": 4, "content": "Supuesto común a los dos textos y tercera vía", "ideas": ["propia"]},
    ],
    "model": [
        "What is a public library for? That libraries face an uncertain future is hardly in doubt; what remains "
        "contested is whether they will survive by reinventing themselves or by protecting what they already offer.",
        "Advocates of reinvention point out that book lending, once the core of a library’s work, has been in "
        "long-term decline, and conclude that only by offering new services – digital skills, practical advice, a "
        "programme of talks – can libraries remain relevant. The diagnosis is difficult to fault, and the thriving "
        "branches they cite suggest that the remedy works. Yet the opposing camp exposes a flaw in this reasoning: "
        "rising footfall is evidence of popularity, not of value. A building crowded with activities may draw more "
        "people through its doors while failing those who depend on it most.",
        "That critique rests on a compelling observation. Libraries are among the last public buildings in which no "
        "one is under any pressure to spend money, and for a student with no room of their own, an undisturbed seat "
        "is indispensable. Nevertheless, the defenders of silence risk mistaking one group of users for all of them. "
        "The pensioner who comes in for company, or the job-seeker who cannot complete an online application "
        "unaided, has an equally strong claim on the building.",
        "What both positions share, though neither states it, is the conviction that a library exists for people "
        "who have no alternative elsewhere. Seen in that light, the choice between hub and sanctuary is a false one. "
        "A silent floor above a lively one serves both constituencies, and it is this breadth of purpose, rather "
        "than any single function, that justifies keeping the doors open.",
    ],
    "own_ideas": ["Los usuarios que no buscan silencio ({{=The pensioner who comes in for company}}), el supuesto "
                  "común ({{=a library exists for people who have no alternative elsewhere}}) y la solución de "
                  "plantas separadas ({{=A silent floor above a lively one}})."],
    "comments": {
        "Content": {"text": "Las cuatro ideas clave están, y los dos textos se evalúan: {{=The diagnosis is difficult "
                            "to fault}} frente a {{=risk mistaking one group of users for all of them}}.",
                    "theory": ["3.1", "5.4"]},
        "Communicative Achievement": {"text": "Registro neutro-formal sin primera persona; las posturas aparecen "
                                              "como bandos ({{=Advocates of reinvention}}, {{=the opposing camp}}).",
                                      "theory": ["4.3", "6.3"]},
        "Organisation": {"text": "Esquema integrado; el párrafo 3 se engancha al 2 con {{=That critique}} y la "
                                 "conclusión responde a la pregunta inicial.", "theory": ["7.2", "7.4"]},
        "Language": {"text": "Léxico preciso ({{=difficult to fault}}, {{=footfall}}, {{=constituencies}}) e "
                             "inversión ({{=only by offering new services}} … can).", "theory": ["8.1", "8.2"]},
    },
    "errors": [
        {"error": "Resumir los ejemplos en lugar de la idea",
         "why": "Enumerar {{help with official forms}} y {{attend talks}} gasta palabras en apoyos y deja sin "
                "nombrar la idea: la biblioteca tiene que transformarse para sobrevivir.",
         "codes": ["C1"], "theory": ["3.1"]},
        {"error": "Copiar la frase central del texto 2",
         "why": "{{numbers are a poor measure of value}} reproducido tal cual no puntúa.",
         "codes": ["L4"], "theory": ["4.1"]},
        {"error": "Dar la razón a los dos textos sin explicar cómo encajan",
         "why": "Es una contradicción, no una postura.", "codes": ["C3", "CA5"], "theory": ["5.4", "6.2"]},
        {"error": "Evaluar con una preferencia personal",
         "why": "«Me gustan las bibliotecas tranquilas» no juzga la solidez de {{that silence is not a luxury but a "
                "necessity}}.", "codes": ["C2"], "theory": ["5.1"]},
    ],
    "lex": [],
}


if __name__ == "__main__":
    import runpy
    if len(sys.argv) < 2:
        print("Uso: python3 gen_WRT-P1.py --demo | mis_hojas.py [carpeta_salida]")
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
