# gen_RDG-P5.py · Generador de Reading Part 5 (multiple choice, texto largo) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa: texto, preguntas 31-36, hoja de respuestas y soluciones (por que es
#     correcta la clave y por que falla cada distractor, citando el texto).
#   - Bloques sueltos para insertar la Part 5 en un simulacro (SIM): enunciado, hoja de respuestas y
#     soluciones por separado.
#   - Verificacion automatica antes y despues de generar el PDF.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_RDG-P5.py --demo [carpeta_salida]          -> genera una hoja de ejemplo (la 01, como hoja 99)
#   python3 gen_RDG-P5.py mis_hojas.py [carpeta_salida]   -> mis_hojas.py define SPECS = [spec, ...]
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_p5", "/ruta/gen_RDG-P5.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, info = gen.verify(spec)
#   gen.make(spec, "/mnt/user-data/outputs")
#   story += gen.question_flowables(spec)          # para un SIM
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num         "03"
#   subtitle    "Hoja 03 · Reseña cultural · dificultad 3 de 4"     (espanol)
#   intro       "an extract from a book about…"   completa la rubrica: "You are going to read …"
#   title       titulo del texto (ingles)
#   standfirst  entradilla opcional (ingles)
#   text        [parrafo, parrafo, …]  (ingles britanico; 700-900 palabras; 5-9 parrafos)
#   lex         lexico para el modulo LEX (no se imprime; se usa en el resumen de cierre)
#   items       6 diccionarios, en orden:
#     n           31
#     type        uno de TYPES
#     para        [3] o [4, 5] (parrafos, desde 1) o "global" (solo la ultima pregunta)
#     stem        enunciado (ingles)
#     options     [A, B, C, D] (ingles)
#     key         "C"
#     own         respuesta propia del metodo (§2.2), en espanol
#     why         por que es correcta la clave; al menos una cita {{…}} de los parrafos de 'para'
#     theory      secciones de RDG-P5_Teoria_v1 (ver THEORY)
#     distractors {"A": {"kinds": ["7.1"], "why": "… {{cita}} …"}, …}  los tres que no son la clave
#
#   Marcado en own / why (y en cualquier texto en espanol):
#     {{texto}}   -> cita literal del texto, en serif; se comprueba que existe tal cual
#     [[texto]]   -> ingles en serif sin comprobar (palabras de una opcion, glosas)
#     [[!TEXTO]]  -> ingles en serif y negrita
#
# QUE COMPRUEBA verify()
#   numeracion 31-36 · 4 opciones · clave valida · tres distractores explicados con su tipo (§7.x) ·
#   cada explicacion cita el texto · todas las citas existen literalmente · las citas de la clave estan en
#   los parrafos indicados · los pasajes siguen el orden de las preguntas · ninguna letra es clave mas de
#   dos veces · la clave no es la opcion mas larga en mas de dos preguntas · la clave no es la opcion con
#   mas palabras del pasaje en mas de dos preguntas · longitud del texto · secciones de teoria existentes ·
#   marcado sin resolver.
#
# LO QUE EL GENERADOR NO PUEDE COMPROBAR (a mano)
#   - Que haya una sola respuesta defendible por pregunta y que los datos reales del texto sean ciertos.
#   - Ingles britanico, registro C2, dificultad graduada entre hojas.
#   - Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402

VERSION = "1"
FIRST_ITEM = 31
N_ITEMS = 6
WORDS_MIN, WORDS_MAX = 700, 900
PARAS_MIN, PARAS_MAX = 5, 9
LETTERS = "ABCD"
THEORY_DOC = "RDG-P5_Teoria_v1"

TYPES = ["Detalle", "Opinión y actitud", "Implicación", "Significado en contexto", "Propósito",
         "Organización", "Referencia", "Global"]

THEORY = {
    "1.1": "La tarea", "1.2": "Qué cambia respecto al C1", "1.3": "Tipos de pregunta",
    "2.1": "Primera lectura: el mapa del texto", "2.2": "Del enunciado al pasaje",
    "2.3": "Contrastar las opciones", "2.4": "Tiempo y dudas",
    "3.1": "Inferencia legítima y sobreinterpretación", "3.2": "De dónde sale una inferencia",
    "3.3": "Narradores y personajes", "3.4": "Significado en contexto",
    "4.1": "La voz del autor frente a las voces citadas", "4.2": "Marcadores de postura",
    "4.3": "Ironía, understatement y concesión", "4.4": "Léxico de actitud en las opciones",
    "5.1": "Para qué sirve un fragmento", "5.2": "Verbos de función en las opciones",
    "5.3": "Referencia y cohesión", "5.4": "Preguntas globales",
    "6.1": "Grados de paráfrasis", "6.2": "Lo concreto del texto, lo abstracto de la opción",
    "6.3": "Polaridad y negación", "6.4": "Grado y alcance",
    "6.5": "Falsos amigos y matices que engañan al hispanohablante",
    "7.1": "Eco léxico", "7.2": "Cierto, pero no responde", "7.3": "Alcance excesivo o insuficiente",
    "7.4": "Voz equivocada", "7.5": "Relación lógica alterada", "7.6": "Medio cierto",
    "7.7": "Plausible, pero ausente", "7.8": "Pasaje vecino",
    "8": "Caso completo",
}
KINDS = {"7.1": "eco léxico", "7.2": "no responde", "7.3": "alcance", "7.4": "voz", "7.5": "lógica",
         "7.6": "medio cierto", "7.7": "ausente", "7.8": "pasaje vecino"}

CITE_RE = re.compile(r"\{\{(.+?)\}\}")
STOP = set("""a an the and or but nor so yet for of to in on at by with from into onto upon as than then that
this these those it its it’s is are was were be been being has have had do does did not no can could may
might must shall should will would he she they we you i me him her them us my his their our your who whom
which what when where why how about more most less very much many some any all each every one ones only
also just such other own same too over under again further once here there both few s t""".split())


# ---------- Ingles dentro del texto en espanol ----------
def E(s):
    return f'<font name="EN">{s}</font>'


def EB(s):
    return f'<font name="EN"><b>{s}</b></font>'


def markup(s):
    """{{cita}} y [[x]] -> E(x); [[!X]] -> EB(X)."""
    s = CITE_RE.sub(lambda m: E(m.group(1)), s)
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)


def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


# ---------- Estilos propios de la hoja (sobre la plantilla, sin cambiarla) ----------
_rub = ParagraphStyle("p5_rubric", parent=S["en"], fontSize=10, leading=14)
_ttl = ParagraphStyle("p5_title", parent=S["en"], fontName="EN-B", fontSize=13, leading=17, textColor=NAVY,
                      spaceBefore=4, spaceAfter=3)
_stand = ParagraphStyle("p5_stand", parent=S["en"], fontName="EN-I", textColor=GREY, spaceAfter=9)
_txt = ParagraphStyle("p5_txt", parent=S["en"], leading=15.4, spaceAfter=7.5)
_q = ParagraphStyle("p5_q", parent=S["en"], leftIndent=22, bulletIndent=0, bulletFontName="EN-B",
                    spaceBefore=6, spaceAfter=3)
_opt = ParagraphStyle("p5_opt", parent=S["en"], leftIndent=40, bulletIndent=22, bulletFontName="EN-B",
                      spaceAfter=2)
_ihead = ParagraphStyle("p5_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)
_sol = ParagraphStyle("p5_sol", parent=S["body"], leftIndent=14, spaceAfter=5)


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _range(spec):
    a = _first(spec)
    return f"{a}–{a + N_ITEMS - 1}"


def _para_label(it):
    if it["para"] == "global":
        return "el texto completo"
    ps = it["para"]
    if len(ps) == 1:
        return f"párrafo {ps[0]}"
    return "párrafos " + ", ".join(str(x) for x in ps[:-1]) + f" y {ps[-1]}"


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def question_flowables(spec, with_title_block=False):
    """Rubrica, texto y preguntas. Con with_title_block=True antepone el bloque de titulo de la hoja."""
    out = []
    if with_title_block:
        out += title_block(f"RDG-P5 · Práctica {spec['num']}", "Multiple choice", spec["subtitle"],
                           f"6 preguntas ({_range(spec)}) · 2 puntos por pregunta · tiempo orientativo: "
                           "18 minutos · sin consultar la teoría")
    out.append(Paragraph(
        f"You are going to read {spec['intro']}. For questions {_range(spec)}, choose the answer "
        "(<b>A, B, C</b> or <b>D</b>) which you think fits best according to the text. Mark your answers "
        "on the answer sheet.", _rub))
    out += [Spacer(1, 4), Paragraph(spec["title"], _ttl)]
    if spec.get("standfirst"):
        out.append(Paragraph(spec["standfirst"], _stand))
    out += [Paragraph(par, _txt) for par in spec["text"]]
    out.append(Spacer(1, 6))
    qs = []
    for it in spec["items"]:
        qs.append(Paragraph(it["stem"], _q, bulletText=str(it["n"])))
        qs += [Paragraph(o, _opt, bulletText=L) for L, o in zip(LETTERS, it["options"])]
    out.append(KeepTogether(qs))  # las seis preguntas siempre juntas, en la misma pagina
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    out = [h2(heading), p(
        "Marca una sola letra por pregunta. Al corregir, 2 puntos por acierto; los errores no restan. Anota "
        "también el tiempo empleado: el objetivo en el examen son unos 18 minutos.")]
    rows = [["Nº", "A", "B", "C", "D", "Puntos"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), "A", "B", "C", "D", "&nbsp;&nbsp;&nbsp;&nbsp;/ 2"])
    rows.append(["", "", "", "", "<b>Total</b>", f"&nbsp;&nbsp;&nbsp;&nbsp;<b>/ {2 * N_ITEMS}</b>"])
    out += table(rows, [16, 26, 26, 26, 36, 40], zebra=False, en_cols=(1, 2, 3, 4),
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 10), ("BOTTOMPADDING", (0, 1), (-1, -1), 10),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
                        ("TEXTCOLOR", (1, 1), (4, -2), GREY)])
    out.append(p("Tiempo empleado: ________ minutos."))
    return out


def solutions_flowables(spec, with_band=True, heading=None):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 5 · Multiple choice' dentro de un simulacro)."""
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(
        "2 puntos por acierto. Cada solución indica el pasaje, una respuesta propia como la que pide el método "
        f"(§2.2), por qué la clave es correcta y por qué falla cada distractor, con su tipo (§7) y la cita del "
        f"texto que lo descarta. Los números de sección remiten a {THEORY_DOC}."))
    out.append(h2("Clave rápida") if not heading else h3("Clave rápida"))
    rows = [["Nº", "Clave", "Tipo de pregunta", "Distractores", "Teoría"]]
    for it in spec["items"]:
        dis = " · ".join(f"{L} §{'/'.join(it['distractors'][L]['kinds'])}"
                         for L in LETTERS if L != it["key"])
        rows.append([str(it["n"]), f"<b>{it['key']}</b>", it["type"], dis,
                     " · ".join("§" + s for s in it["theory"])])
    out += table(rows, [12, 14, 38, 66, 40])
    out.append(h2("Explicación por pregunta") if not heading else h3("Explicación por pregunta"))
    for it in spec["items"]:
        block = [Paragraph(f"{it['n']} · {it['key']} · {it['type']}", _ihead),
                 p(f"<b>Pregunta:</b> {E(it['stem'])}"),
                 p(f"<b>Pasaje:</b> {_para_label(it)}. <b>Respuesta propia:</b> {markup(it['own'])}")]
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
    """Hoja de practica completa: texto y preguntas, hoja de respuestas (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"RDG-P5 · Práctica {n}", f"RDG-P5_Practica_{n}.pdf", title=f"RDG-P5 · Práctica {n}")
    return out_path


# ---------- Verificacion ----------
def _content_words(s):
    return {w for w in re.findall(r"[a-z’']+", s.lower()) if len(w) > 3 and w not in STOP}


def verify(spec):
    """Comprobaciones de formato y coherencia. Devuelve (errores, info)."""
    errs = []
    paras = [_norm(x) for x in spec["text"]]
    full = " ".join(paras)
    a = _first(spec)
    items = spec["items"]
    if [it.get("n") for it in items] != list(range(a, a + N_ITEMS)):
        errs.append(f"numeración de las preguntas: se esperaban {a}–{a + N_ITEMS - 1}")
    words = len(full.split())
    if not WORDS_MIN <= words <= WORDS_MAX:
        errs.append(f"longitud del texto fuera de {WORDS_MIN}–{WORDS_MAX} palabras: {words}")
    if not PARAS_MIN <= len(paras) <= PARAS_MAX:
        errs.append(f"número de párrafos fuera de {PARAS_MIN}–{PARAS_MAX}: {len(paras)}")

    last_para, longest, lexical, keys = 0, [], [], []
    for i, it in enumerate(items):
        n = it.get("n", "?")
        for field in ("type", "para", "stem", "options", "key", "own", "why", "theory", "distractors"):
            if not it.get(field):
                errs.append(f"{n}: falta el campo '{field}'")
        if it.get("type") not in TYPES:
            errs.append(f"{n}: tipo de pregunta desconocido '{it.get('type')}'")
        opts = it.get("options", [])
        if len(opts) != 4 or not all(o.strip() for o in opts):
            errs.append(f"{n}: hacen falta cuatro opciones no vacías")
        if len(set(opts)) != len(opts):
            errs.append(f"{n}: opciones repetidas")
        key = it.get("key")
        if key not in LETTERS:
            errs.append(f"{n}: clave no válida '{key}'")
            continue
        keys.append(key)
        for s in it.get("theory", []):
            if s not in THEORY:
                errs.append(f"{n}: sección de teoría inexistente §{s}")
        # pasaje y orden
        para = it.get("para")
        if para == "global":
            if i != len(items) - 1:
                errs.append(f"{n}: solo la última pregunta puede ser global")
            scope = full
        else:
            if not all(isinstance(x, int) and 1 <= x <= len(paras) for x in para):
                errs.append(f"{n}: párrafos fuera de rango {para}")
                continue
            if min(para) < last_para:
                errs.append(f"{n}: el pasaje ({para}) va antes que el de la pregunta anterior")
            last_para = max(last_para, min(para))
            scope = " ".join(paras[x - 1] for x in para)
        # citas
        key_cites = CITE_RE.findall(it.get("why", ""))
        if not key_cites:
            errs.append(f"{n}: la explicación de la clave no cita el texto")
        for c in key_cites:
            if _norm(c) not in full:
                errs.append(f"{n}: cita inexistente en la clave: «{c}»")
            elif para != "global" and _norm(c) not in scope:
                errs.append(f"{n}: la cita de la clave «{c[:40]}» no está en los párrafos {para}")
        dis = it.get("distractors", {})
        expected = set(LETTERS) - {key}
        if set(dis) != expected:
            errs.append(f"{n}: distractores explicados {sorted(dis)}; se esperaban {sorted(expected)}")
        for L, d in dis.items():
            if not d.get("kinds") or any(k not in KINDS for k in d["kinds"]):
                errs.append(f"{n}{L}: tipo de distractor ausente o desconocido {d.get('kinds')}")
            cites = CITE_RE.findall(d.get("why", ""))
            if not cites:
                errs.append(f"{n}{L}: la explicación no cita el texto")
            for c in cites:
                if _norm(c) not in full:
                    errs.append(f"{n}{L}: cita inexistente: «{c}»")
        # marcado sin resolver
        texts = [("own", it.get("own", "")), ("why", it.get("why", ""))]
        texts += [(f"distractor {L}", d.get("why", "")) for L, d in dis.items()]
        for field, txt in texts:
            if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(txt)):
                errs.append(f"{n}: marcado sin resolver en '{field}'")
        for o in opts:
            if re.search(r"[\[\]{}<>]", o):
                errs.append(f"{n}: marcado en una opción: {o[:30]}")
        # longitud y parecido lexico de la clave
        k = LETTERS.index(key)
        lens = [len(o) for o in opts]
        if lens[k] == max(lens) and lens.count(max(lens)) == 1:
            longest.append(n)
        sw = _content_words(scope)
        ov = [len(_content_words(o) & sw) for o in opts]
        if ov[k] == max(ov) and ov.count(max(ov)) == 1:
            lexical.append(n)

    for L in LETTERS:
        if keys.count(L) > 2:
            errs.append(f"la letra {L} es clave {keys.count(L)} veces (máximo 2)")
    if len(longest) > 2:
        errs.append(f"la clave es la opción más larga en {len(longest)} preguntas: {longest}")
    if len(lexical) > 2:
        errs.append(f"la clave es la opción con más palabras del pasaje en {len(lexical)} preguntas: {lexical}")
    info = {"words": words, "paras": len(paras), "keys": "".join(keys), "longest": longest, "lexical": lexical}
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
    return re.findall(r"\{\{|\}\}|\[\[|\]\]|<font|</?b>|<br", txt)


def make(spec, out_dir="/mnt/user-data/outputs"):
    """Verifica, genera y comprueba el PDF. Devuelve la ruta; lanza ValueError si algo falla."""
    errs, info = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}:\n  - " + "\n  - ".join(errs))
    path = build_sheet(spec, os.path.join(out_dir, f"RDG-P5_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    print(f"RDG-P5_Practica_{spec['num']}.pdf · {info['words']} palabras · {info['paras']} párrafos · "
          f"claves {info['keys']} · clave más larga en {info['longest'] or 'ninguna'} · "
          f"clave con más eco léxico en {info['lexical'] or 'ninguna'} · verificación sin errores")
    return path


# ---------- Hoja de ejemplo (contenido de RDG-P5_Practica_01, numerada como 99) ----------
DEMO = {
    "num": "99",
    "subtitle": "Hoja de prueba del generador (contenido de RDG-P5_Practica_01)",
    "intro": "an article about memory",
    "title": "In defence of forgetting",
    "standfirst": "Why a memory that lets things go may be smarter than one that keeps everything",
    "text": [
        "Most of us treat forgetting as a small humiliation: the name that slips away mid-introduction, the "
        "misplaced keys, the reason we walked into the kitchen. We apologise for it, joke about it and, past a "
        "certain age, begin quietly to worry about it. The assumption behind all this embarrassment is that "
        "memory exists to store things, and that every lapse is a failure of storage, a leak in a vessel that "
        "ought to be watertight. It is an assumption that a growing number of neuroscientists now regard as "
        "not merely mistaken but back to front.",

        "The idea that forgetting is a defect has a long and respectable pedigree. In the 1880s the German "
        "psychologist Hermann Ebbinghaus spent months memorising lists of nonsense syllables and testing "
        "himself at intervals, and the curve he plotted – steep loss within the first hours, then a long, "
        "slow decline – became one of the founding images of experimental psychology. For more than a century "
        "afterwards, the curve was read as a portrait of decay: something to be flattened, resisted and, if "
        "possible, abolished. Memory techniques, brain-training apps and a small industry of supplements have "
        "all been sold on the same promise, that with enough effort we might keep everything we put in.",

        "Yet the rare individuals who come closest to that ideal are not obviously to be envied. The Russian "
        "neuropsychologist Alexander Luria spent some thirty years studying a man, known in his writings as "
        "S., who could reproduce long tables of numbers years after studying them for only a few minutes. S. "
        "made a living on the stage as a memory performer, but he found ordinary life surprisingly hard. He "
        "struggled to recognise people whose faces kept changing with their expressions, and he could make "
        "little of poetry or of any text that asked him to move beyond the literal, because each word summoned "
        "a vivid image that crowded out the sense of the whole. His difficulty, in other words, was not too "
        "little memory but too much.",

        "Fiction had arrived at the same idea by another route. In a short story published in 1942, Jorge "
        "Luis Borges imagined a young man who, after being thrown from a horse, could forget nothing at all: "
        "every leaf on every tree, every shape of every cloud. Borges’s narrator suspects that this prodigy "
        "was not very capable of thought, since thinking requires us to overlook differences, to generalise, "
        "to abstract. It is a striking intuition, and one that laboratory science was slow to take up.",

        "The case was set out with particular clarity in 2017, when two neuroscientists at the University of "
        "Toronto, Blake Richards and Paul Frankland, argued that the purpose of memory is not to preserve "
        "information faithfully but to help us make good decisions. From that angle, forgetting earns its "
        "keep in two ways. First, the world changes: a memory of where food could be found last year, or of a "
        "route that has since been closed, is worse than useless if it overrides fresher information. Second, "
        "and less obviously, clinging to every detail of past experience makes it harder to extract the "
        "general pattern. A brain that remembered each individual dog it had ever met, down to the last "
        "whisker, might be slower to recognise a new one as a dog at all.",

        "Researchers who build artificial intelligence will recognise the problem. A system trained too "
        "closely on its examples learns them by heart, quirks and all, and then performs poorly on anything "
        "new, a failure known as overfitting. One standard remedy is, in effect, a form of deliberate "
        "forgetting: during training, parts of the network are randomly switched off, so that no single "
        "pathway can hold on to too much detail. That engineers, working on quite different problems, should "
        "have arrived at something resembling the brain’s own untidiness is, at the very least, suggestive.",

        "None of this means that every lapse is a blessing in disguise. Forgetting caused by disease is a "
        "different matter altogether, and anyone who has watched dementia take hold of a parent would find "
        "the cheerful language of ‘adaptive forgetting’ hard to stomach. Nor does the research suggest that we "
        "should stop writing things down. What it does suggest is that the healthy brain is not a filing "
        "cabinet with a faulty lock but something closer to an editor, constantly deciding what is worth "
        "keeping and what can safely be let go.",

        "That may be some consolation the next time a name escapes us at a party. The lapse is not "
        "necessarily a sign that the machinery is failing; it may simply mean that the machinery has judged, "
        "rightly or wrongly, that this particular name was not worth the space. We are, it turns out, built "
        "to forget, and we would be considerably worse off if we were not.",
    ],
    "lex": ["back to front", "a long and respectable pedigree", "earn its keep", "a blessing in disguise",
            "hard to stomach", "crowd out", "quirks and all", "overfitting"],
    "items": [
        {"n": 31, "type": "Opinión y actitud", "para": [1],
         "stem": "What does the writer suggest about the usual attitude to forgetting in the first paragraph?",
         "options": ["It reflects an exaggerated fear of growing old.",
                     "It rests on a mistaken idea of what memory is for.",
                     "It is shared by most of the scientists who study memory.",
                     "It has more to do with embarrassment than with genuine concern."],
         "key": "B",
         "own": "La actitud de siempre parte de una idea equivocada: que la memoria sirve para almacenarlo todo.",
         "why": "El párrafo atribuye la vergüenza a un supuesto ({{The assumption behind all this embarrassment "
                "is that memory exists to store things}}) y lo descalifica en la última frase: {{not merely "
                "mistaken but back to front}}. La opción resume ese supuesto como una idea equivocada sobre "
                "para qué sirve la memoria.",
         "theory": ["4.1", "6.1"],
         "distractors": {
             "A": {"kinds": ["7.1", "7.3"],
                   "why": "Recoge {{past a certain age, begin quietly to worry about it}}, que es solo una de las "
                          "reacciones que enumera el párrafo. El texto no dice que ese temor sea exagerado ni que "
                          "explique la actitud general."},
             "C": {"kinds": ["7.4"],
                   "why": "Invierte la postura de los científicos, que consideran esa idea {{not merely mistaken "
                          "but back to front}}. Además, el texto habla de {{a growing number of neuroscientists}}, "
                          "no de la mayoría (§6.4)."},
             "D": {"kinds": ["7.6"],
                   "why": "La vergüenza sí aparece ({{all this embarrassment}}), pero también la preocupación "
                          "real ({{begin quietly to worry about it}}), así que la comparación no se sostiene."},
         }},
        {"n": 32, "type": "Propósito", "para": [2],
         "stem": "The writer refers to the work of Ebbinghaus in order to",
         "options": ["show how a scientific finding came to be seen as evidence of a flaw.",
                     "cast doubt on the methods of early experimental psychology.",
                     "explain why memory techniques tend to be ineffective.",
                     "illustrate how quickly people forget meaningless information."],
         "key": "A",
         "own": "Para mostrar cómo una curva del olvido se leyó durante un siglo como prueba de un defecto que "
                "había que corregir.",
         "why": "El párrafo abre con la idea que va a ilustrar ({{The idea that forgetting is a defect has a long "
                "and respectable pedigree}}), y Ebbinghaus es su origen: su curva {{was read as a portrait of "
                "decay}}, algo que había que combatir. El verbo [[was read]] indica que al autor le interesa la "
                "interpretación del hallazgo, no el hallazgo en sí.",
         "theory": ["5.1", "5.2"],
         "distractors": {
             "B": {"kinds": ["7.7"],
                   "why": "El autor no critica el método: describe el experimento sin reservas y lo presenta "
                          "como {{one of the founding images of experimental psychology}}."},
             "C": {"kinds": ["7.5", "7.7"],
                   "why": "El texto dice que esos productos {{have all been sold on the same promise}}: relaciona "
                          "la promesa comercial con la lectura de la curva, pero no afirma que no funcionen."},
             "D": {"kinds": ["7.2"],
                   "why": "Es cierto que la curva muestra una pérdida rápida ({{steep loss within the first "
                          "hours}}), pero ese es el contenido del ejemplo, no su función en el argumento (§5.1)."},
         }},
        {"n": 33, "type": "Implicación", "para": [3],
         "stem": "What point does the writer make about S. in the third paragraph?",
         "options": ["His gift was accompanied by a talent for the arts.",
                     "His abilities were exaggerated for the sake of performance.",
                     "His memory left him unable to earn a living.",
                     "His memory interfered with his ability to grasp meaning."],
         "key": "D",
         "own": "Recordar tanto le impedía entender: los detalles tapaban el sentido.",
         "why": "S. {{could make little of poetry or of any text that asked him to move beyond the literal}}, "
                "porque cada palabra evocaba una imagen que {{crowded out the sense of the whole}}. La última "
                "frase lo resume: {{not too little memory but too much}}. La opción abstrae el caso concreto "
                "(§6.2).",
         "theory": ["3.2", "6.2"],
         "distractors": {
             "A": {"kinds": ["7.1"],
                   "why": "Junta {{on the stage}} y {{poetry}}, pero sobre la poesía el texto dice lo contrario: "
                          "S. no la entendía."},
             "B": {"kinds": ["7.1", "7.7"],
                   "why": "Toma {{memory performer}} y le añade una sospecha que el texto no plantea. Luria "
                          "comprobó que S. recordaba las tablas {{years after studying them for only a few "
                          "minutes}}."},
             "C": {"kinds": ["7.3"],
                   "why": "Lo contradice {{S. made a living on the stage}}. Que {{he found ordinary life "
                          "surprisingly hard}} no significa que no pudiera ganarse la vida."},
         }},
        {"n": 34, "type": "Opinión y actitud", "para": [4, 5],
         "stem": "How does the writer present Borges’s story in the fourth paragraph?",
         "options": ["as a fanciful idea that the evidence has failed to support",
                     "as more persuasive than the scientific work that followed it",
                     "as an imaginative insight that science later came to support",
                     "as an exaggerated version of the case that Luria documented"],
         "key": "C",
         "own": "Como una intuición literaria acertada, a la que la ciencia llegó más tarde.",
         "why": "Borges llegó a la misma idea {{by another route}}, y el autor la valora como {{a striking "
                "intuition}}. La ciencia tardó en asumirla ({{laboratory science was slow to take up}}), pero "
                "el párrafo siguiente muestra que acabó haciéndolo: {{The case was set out with particular "
                "clarity in 2017}}.",
         "theory": ["4.2", "5.2"],
         "distractors": {
             "A": {"kinds": ["7.5"],
                   "why": "Invierte la relación: la ciencia no ha refutado la intuición, sino que ha acabado "
                          "dándole forma ({{The case was set out with particular clarity in 2017}})."},
             "B": {"kinds": ["7.3"],
                   "why": "La expresión {{a striking intuition}} es un elogio, pero el texto no compara el cuento con la "
                          "investigación ni dice que convenza más."},
             "D": {"kinds": ["7.7"],
                   "why": "El texto no relaciona el cuento con el caso de Luria ni lo considera exagerado: dice "
                          "que la ficción llegó a la idea {{by another route}}, es decir, por su cuenta."},
         }},
        {"n": 35, "type": "Significado en contexto", "para": [5],
         "stem": "What does the writer mean by saying that forgetting ‘earns its keep’?",
         "options": ["It saves the brain energy that can then be used elsewhere.",
                     "It becomes more valuable as people grow older.",
                     "It is the price we pay for being able to decide quickly.",
                     "It is useful enough to justify its place in memory."],
         "key": "D",
         "own": "Que el olvido sirve para algo y por eso merece existir.",
         "why": "[[Earn one’s keep]] es «ganarse el sustento, justificar lo que uno cuesta». El contexto lo "
                "explica enseguida: el olvido aporta dos ventajas ({{forgetting earns its keep in two ways}}), "
                "porque el mundo cambia y porque recordar cada detalle {{makes it harder to extract the "
                "general pattern}}.",
         "theory": ["3.4"],
         "distractors": {
             "A": {"kinds": ["7.7"],
                   "why": "Lee la expresión en clave de ahorro, pero el texto no menciona la energía: las dos "
                          "ventajas que enumera sirven para decidir mejor ({{help us make good decisions}})."},
             "B": {"kinds": ["7.7", "7.1"],
                   "why": "Nada en el párrafo relaciona las ventajas del olvido con la edad, que solo aparece en "
                          "el primero, a propósito de la preocupación ({{past a certain age}})."},
             "C": {"kinds": ["7.5"],
                   "why": "El olvido no es el coste de decidir rápido, sino lo que permite decidir bien "
                          "({{help us make good decisions}}). Presentarlo como un precio contradice la propia "
                          "expresión, que habla de un beneficio."},
         }},
        {"n": 36, "type": "Global", "para": "global",
         "stem": "What is the writer’s main purpose in the article?",
         "options": ["to reassure readers that memory loss in later life need not worry them",
                     "to challenge the belief that forgetting is simply a failure of memory",
                     "to describe recent progress in the treatment of memory disorders",
                     "to compare the workings of human memory with those of machines"],
         "key": "B",
         "own": "Desmontar la idea de que olvidar es un fallo: olvidar forma parte del buen funcionamiento de "
                "la memoria.",
         "why": "El primer párrafo presenta la idea que se va a discutir (cada olvido sería {{a failure of "
                "storage}}) y el último da la conclusión: {{We are, it turns out, built to forget}}. Todo lo "
                "intermedio (Luria, Borges, Richards y Frankland, la inteligencia artificial) son pruebas al "
                "servicio de esa tesis.",
         "theory": ["5.4", "2.1"],
         "distractors": {
             "A": {"kinds": ["7.3"],
                   "why": "El autor deja fuera la enfermedad ({{Forgetting caused by disease is a different "
                          "matter altogether}}), y el consuelo final se limita a olvidos cotidianos, como un "
                          "nombre en una fiesta."},
             "C": {"kinds": ["7.7"],
                   "why": "El texto no habla de tratamientos: la demencia solo aparece para excluirla del "
                          "argumento ({{anyone who has watched dementia take hold of a parent}})."},
             "D": {"kinds": ["7.3"],
                   "why": "La comparación con la inteligencia artificial ocupa un solo párrafo y es un apoyo más, "
                          "que el autor presenta con cautela ({{at the very least, suggestive}})."},
         }},
    ],
}


if __name__ == "__main__":
    import runpy
    if len(sys.argv) < 2:
        print("Uso: python3 gen_RDG-P5.py --demo | mis_hojas.py [carpeta_salida]")
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
