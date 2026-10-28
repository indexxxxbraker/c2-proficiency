# gen_UOE-P2.py · Generador de Use of English Part 2 (open cloze) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa (texto con 8 huecos, hoja de respuestas y soluciones), con el formato
#     de UOE-P2_Practica_01-10.
#   - Bloques sueltos para insertar la Part 2 en un simulacro (SIM): enunciado, hoja de respuestas
#     y soluciones por separado.
#   - Verificacion automatica de la hoja y de la clave antes y despues de generar el PDF.
#   - Listado de cada frase con cada respuesta aceptada, para revisar la clave a mano.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_UOE-P2.py --demo [carpeta_salida]          -> genera una hoja de ejemplo
#   python3 gen_UOE-P2.py mis_hojas.py [carpeta_salida]    -> mis_hojas.py define SPECS = [spec, ...]
#   python3 gen_UOE-P2.py --frases mis_hojas.py | --demo   -> solo imprime las frases con cada clave
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_p2", "/ruta/gen_UOE-P2.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, words = gen.verify(spec)
#   gen.build_sheet(spec, "/mnt/user-data/outputs/UOE-P2_Practica_11.pdf")
#   story += gen.question_flowables(spec)        # para un SIM
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num        "11"                       numero de hoja (para nombre, cabecera y pie)
#   subtitle   "Hoja 11 · ..."            subtitulo en espanol
#   title      "Titulo del texto"         en ingles
#   example    "AT"                       respuesta del ejemplo (0), una palabra
#   text       [parrafo, parrafo, ...]    en ingles; el ejemplo es {0} y cada hueco {numero}, p. ej. {9}
#   first      9                          opcional: primer numero (en el examen, 9)
#   items      8 diccionarios, uno por hueco, en orden:
#       n      9
#       key    ["ALTHOUGH", "THOUGH"]     TODAS las respuestas aceptables (una palabra, mayusculas)
#       type   "Subordinada concesiva"    tipo de hueco, en espanol
#       theory ["7"]                      secciones de UOE-P2_Teoria_v1 (claves de THEORY)
#       why    explicacion: que delata la palabra (y, si hay varias, por que valen todas)
#       wrong  respuestas tentadoras que no valen y por que
#
#   Marcado en type / why / wrong (y en cualquier texto en espanol):
#       [[texto]]   -> ingles en serif (equivale a E("texto"))
#       [[!texto]]  -> ingles en serif y negrita (equivale a EB("texto")). En 'wrong', las respuestas
#                      rechazadas se marcan asi: el verificador comprueba que ninguna este en la clave.
#   Tambien se pueden usar directamente las funciones E() y EB() del modulo.
#
# REGLAS DEL PROYECTO QUE EL GENERADOR NO PUEDE COMPROBAR (hay que hacerlas a mano)
#   - Que la clave recoja todas las respuestas aceptables y que ninguna otra sea defendible.
#     Ayuda: --frases imprime cada frase con cada respuesta de la clave; probar ademas las
#     alternativas plausibles (sinonimos, adverbios negativos antepuestos, modales en las inversiones).
#   - Que el ejemplo (0) no regale la respuesta de otro hueco (el verificador solo avisa si coincide).
#   - Ingles britanico en el texto. Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402

VERSION = "1"
G = "__________"
GAP_RE = re.compile(r"\{(\d+)\}")
FIRST_ITEM = 9            # la Part 2 del examen va de la 9 a la 16
N_ITEMS = 8
WORDS_MIN, WORDS_MAX = 180, 300
CODE = "UOE-P2"


# ---------- Ingles dentro del texto en espanol ----------
def E(s):
    return f'<font name="EN">{s}</font>'


def EB(s):
    return f'<font name="EN"><b>{s}</b></font>'


def markup(s):
    """[[!x]] -> EB(x); [[x]] -> E(x)."""
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)


# ---------- Secciones de UOE-P2_Teoria_v1 (clave: (numero, titulo)) ----------
THEORY = {
    "1": ("1", "Formato y puntuación"),
    "2a": ("2", "Método · Diagnóstico por lo que rodea al hueco"),
    "2b": ("2", "Método · Cuando la pista está en otra frase"),
    "3": ("3", "Determinantes y cuantificadores"),
    "4": ("4", "Referencia y sustitución"),
    "5.1": ("5.1", "El auxiliar que falta"),
    "5.2": ("5.2", "Do enfático y elipsis"),
    "5.3": ("5.3", "Modales con usos de C2"),
    "6.1": ("6.1", "Preposición dependiente"),
    "6.2": ("6.2", "Partícula de phrasal verb"),
    "6.3": ("6.3", "Palabras gramaticales dentro de expresiones fijas"),
    "7": ("7", "Conectores y subordinadores"),
    "7.1": ("7.1", "Los que más caen en el C2"),
    "7.2": ("7.2", "La primera mitad de un conector compuesto"),
    "8": ("8", "Relativos y nominales"),
    "9.1": ("9.1", "Anteposición"),
    "9.2": ("9.2", "Otras formas concesivas enfáticas"),
    "9.3": ("9.3", "Qué cae en el hueco"),
    "10": ("10", "Estructuras de la Part 4 vistas desde el hueco"),
    "11": ("11", "Trampas típicas"),
    "12": ("12", "Tabla de referencia por palabra"),
}
THEORY_DOC = "UOE-P2_Teoria_v1"


def theory_label(keys):
    return " · ".join(f"{THEORY[k][0]} {THEORY[k][1]}" for k in keys)


# ---------- Estilos propios de la hoja (sobre la plantilla, sin cambiarla) ----------
_ttl = ParagraphStyle("p2_title", parent=S["en"], fontName="EN-B", fontSize=12, leading=16,
                      spaceBefore=4, spaceAfter=6)

INTRO_ONE = ("1 punto por acierto. Cada solución explica qué delata la palabra, señala las respuestas tentadoras "
             f"que no valen y remite al apartado de {THEORY_DOC} que lo trabaja.")
INTRO_MULTI = ("1 punto por acierto. En esta hoja hay huecos que admiten varias respuestas: vale cualquiera de las "
               "que recoge la clave, pero solo una por hueco (con dos respuestas, el hueco vale 0). Cada solución "
               "explica por qué valen todas las de la clave y por qué no valen otras que parecen posibles, y remite "
               f"al apartado de {THEORY_DOC}.")


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _range(spec):
    a = _first(spec)
    return f"{a}–{a + N_ITEMS - 1}"


def _multi(spec):
    return any(len(it["key"]) > 1 for it in spec["items"])


def gapped(par):
    """Parrafo con los huecos numerados; el numero y la raya no se separan al cortar la linea."""
    return GAP_RE.sub(lambda m: f"({m.group(1)})&nbsp;{G}", par)


def filled(par, spec, bold=False, choice=None):
    """Parrafo con las respuestas (la primera de cada clave, o la indicada en choice={n: palabra})."""
    keys = {it["n"]: it["key"][0] for it in spec["items"]}
    keys[0] = spec["example"]
    keys.update(choice or {})

    def rep(m):
        w = keys[int(m.group(1))].lower()
        before = par[:m.start()].rstrip()
        if before == "" or before.endswith((".", "?", "!")):
            w = w.capitalize()
        return f"<b>{w}</b>" if bold else w
    return GAP_RE.sub(rep, par)


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def question_flowables(spec, with_title_block=False):
    """Rubrica, ejemplo y texto. Con with_title_block=True antepone el bloque de titulo de la hoja."""
    out = []
    if with_title_block:
        out += title_block(f"{CODE} · Práctica {spec['num']}", "Open cloze", spec["subtitle"],
                           f"8 ítems (preguntas {_range(spec)}) · 1 punto por ítem · tiempo orientativo: 10 minutos"
                           " · sin consultar la teoría")
    out.append(en(f"For questions {_range(spec)}, read the text below and think of the word which best fits each "
                  "gap. Use only one word in each gap. There is an example at the beginning (0). "
                  "Write your answers IN CAPITAL LETTERS on the answer sheet."))
    out.append(en(f"<b>Example:</b> (0) {spec['example'].upper()}"))
    out += [Spacer(1, 4), Paragraph(spec["title"], _ttl)]
    out += [en(gapped(par)) for par in spec["text"]]
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas", big=True):
    """Hoja de respuestas. big=True usa el titulo grande (hoja suelta); big=False, h2 (simulacro)."""
    out = [Paragraph(heading, S["h1"]) if big else h2(heading), p(
        "Escribe una sola palabra por hueco, en mayúsculas. Al corregir, marca 1 punto por acierto: "
        "la ortografía tiene que ser exacta y una contracción o dos palabras valen 0.")]
    rows = [["Nº", "Respuesta (en mayúsculas)", "Punto"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), "", "/ 1"])
    rows.append(["Total", "", f"/ {N_ITEMS}"])
    out += table(rows, [22, 108, 40], zebra=True, extra=[
        ("TOPPADDING", (0, 1), (-1, -1), 10), ("BOTTOMPADDING", (0, 1), (-1, -1), 10),
        ("LINEABOVE", (0, -1), (-1, -1), 1, NAVY),
    ])
    return out


def solutions_flowables(spec, with_band=True, heading=None):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 2 · Open cloze' dentro de un simulacro)."""
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(INTRO_MULTI if _multi(spec) else INTRO_ONE))
    sub = h3 if heading else h2
    out.append(sub("Clave rápida"))
    rows = [["Nº", "Clave", "Tipo de hueco", "Teoría"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), E(" / ".join(it["key"])), markup(it["type"]), theory_label(it["theory"])])
    out += table(rows, [12, 52, 44, 62] if _multi(spec) else [12, 30, 52, 76])
    for i, it in enumerate(spec["items"]):
        block = [sub("Explicación por ítem")] if i == 0 else []
        block += [Paragraph(f'{it["n"]} · {E(" / ".join(it["key"]))}  '
                            f'<font color="#5B6577">·  {markup(it["type"])}</font>', S["h3"]),
                  p(("<b>Por qué valen:</b> " if len(it["key"]) > 1 else "<b>Por qué:</b> ") + markup(it["why"])),
                  p("<b>No vale:</b> " + markup(it["wrong"])),
                  Paragraph("<b>Teoría:</b> " + theory_label(it["theory"]), S["small"]),
                  Spacer(1, 4)]
        out.append(KeepTogether(block))
    return out


def build_sheet(spec, out_path):
    """Hoja de practica completa: enunciado, hoja de respuestas (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"{CODE} · Práctica {n}", f"{CODE}_Practica_{n}.pdf", title=f"{CODE} · Práctica {n}")
    return out_path


# ---------- Verificacion ----------
def _plain(s):
    return re.sub(r"<[^>]+>", "", s)


def verify(spec):
    """Comprobaciones de formato y de la clave antes de generar. Devuelve (errores, palabras_del_texto)."""
    errs = []
    a = _first(spec)
    expected = list(range(a, a + N_ITEMS))
    nums = [int(m.group(1)) for par in spec["text"] for m in GAP_RE.finditer(par)]
    if nums != [0] + expected:
        errs.append(f"numeración de huecos en el texto: {nums}")
    if not re.fullmatch(r"[A-Za-z]+", spec.get("example", "")):
        errs.append("el ejemplo (0) no es una sola palabra")
    for field in ("num", "subtitle", "title", "example", "text", "items"):
        if not spec.get(field):
            errs.append(f"falta el campo de hoja '{field}'")
    if [it.get("n") for it in spec.get("items", [])] != expected:
        errs.append(f"ítems de la clave: se esperaban {expected}")
    for it in spec.get("items", []):
        n = it.get("n")
        for field in ("key", "type", "theory", "why", "wrong"):
            if not it.get(field):
                errs.append(f"{n}: falta el campo '{field}'")
        if isinstance(it.get("key"), str) or isinstance(it.get("theory"), str):
            errs.append(f"{n}: 'key' y 'theory' tienen que ser listas")
            continue
        key = it.get("key", [])
        for k in key:
            if not re.fullmatch(r"[A-Z]+", k):
                errs.append(f"{n}: '{k}' no es una sola palabra en mayúsculas (sin guion, espacio ni apóstrofo)")
        if len(set(key)) != len(key):
            errs.append(f"{n}: respuestas repetidas en la clave")
        for s in it.get("theory", []):
            if s not in THEORY:
                errs.append(f"{n}: sección de teoría inexistente '{s}'")
        rejected = {w.strip("*").upper() for w in re.findall(r"\[\[!([^\]\s]+)\]\]", it.get("wrong", ""))}
        clash = rejected & set(key)
        if clash:
            errs.append(f"{n}: respuesta de la clave citada como incorrecta: {sorted(clash)}")
        for field in ("type", "why", "wrong"):
            if re.search(r"\[\[|\]\]", markup(it.get(field, ""))):
                errs.append(f"{n}: marcado sin resolver en '{field}'")
    for par in spec.get("text", []):
        if re.search(r"\{[^}]*[^\d}][^}]*\}", par):
            errs.append(f"marca de hueco mal escrita: {par[:40]}…")
    words = len(GAP_RE.sub("X", " ".join(spec.get("text", []))).split())
    if not WORDS_MIN <= words <= WORDS_MAX:
        errs.append(f"longitud del texto fuera de {WORDS_MIN}–{WORDS_MAX} palabras: {words}")
    return errs, words


def warnings(spec):
    """Avisos que no impiden generar, pero piden revisar a mano."""
    out = []
    ex = spec["example"].upper()
    for it in spec["items"]:
        if ex in it["key"]:
            out.append(f"el ejemplo (0) {ex} coincide con la clave del hueco {it['n']}: comprobar que no la regala")
    counts = {}
    for it in spec["items"]:
        counts.setdefault(" / ".join(it["key"]), []).append(it["n"])
    for k, ns in counts.items():
        if len(ns) > 1:
            out.append(f"la clave {k} se repite en los huecos {ns}: comprobar que son estructuras distintas")
    return out


def key_sentences(spec):
    """Cada frase con hueco, rellenada con cada respuesta de la clave. Devuelve [(n, palabra, frase)]."""
    out = []
    for par in spec["text"]:
        for sent in re.split(r"(?<=[.?!])\s+", par):
            for m in GAP_RE.finditer(sent):
                n = int(m.group(1))
                if n == 0:
                    continue
                it = next(i for i in spec["items"] if i["n"] == n)
                for w in it["key"]:
                    s = sent.replace("{0}", spec["example"].lower())
                    tag = "{" + str(n) + "}"
                    word = w.capitalize() if s.startswith(tag) else w.lower()
                    s = GAP_RE.sub("___", s.replace(tag, word))
                    out.append((n, w, s))
    return out


def check_pdf(path):
    """Busca restos de codigo o de marcado en el texto del PDF ya generado."""
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            txt = "\n".join(pg.extract_text() or "" for pg in pdf.pages)
    except ImportError:
        from pypdf import PdfReader
        txt = "\n".join(pg.extract_text() or "" for pg in PdfReader(path).pages)
    return re.findall(r"\{E|EB\(|E\('|\{G\}|\{\d+\}|\[\[|\]\]|&nbsp;", txt)


def make(spec, out_dir="/mnt/user-data/outputs"):
    """Verifica, genera y comprueba el PDF. Devuelve la ruta; lanza ValueError si algo falla."""
    errs, words = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}: " + "; ".join(errs))
    for w in warnings(spec):
        print(f"  aviso · hoja {spec['num']}: {w}")
    path = build_sheet(spec, os.path.join(out_dir, f"{CODE}_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    print(f"{CODE}_Practica_{spec['num']}.pdf · {words} palabras · verificación sin errores")
    return path


# ---------- Hoja de ejemplo (contenido de UOE-P2_Practica_09, con el marcado [[ ]]) ----------
DEMO = {
    "num": "99",
    "subtitle": "Hoja de prueba del generador",
    "title": "Alone across the Atlantic",
    "example": "AT",
    "text": [
        "{0} the age of twenty-three, with little money and even less experience, she bought a second-hand yacht and "
        "announced her intention to sail it single-handed across the Atlantic. {9} she had never sailed further than "
        "the mouth of the local estuary, she was convinced that she would succeed. No one in her family had ever "
        "crossed an ocean; {10} had any of her friends, and most of them tried to talk her out of it.",
        "Strange {11} it may seem, she later claimed that the first week was the hardest. Only when the coastline "
        "had disappeared behind her {12} she grasp the scale of what she had taken on, and for days she was too "
        "seasick to eat. The sea, she wrote in her log, behaved as {13} it had a will of its own, and a malicious "
        "one at that.",
        "Three weeks after setting out, she had {14} to reach the halfway point, and her supplies were running "
        "dangerously low. Exhausted {15} she was, she refused to radio for help. Not once, she insisted afterwards, "
        "{16} she seriously consider turning back. Forty-four days after leaving port, she sailed into harbour to a "
        "welcome she had never expected, and within a year she was planning a second voyage.",
    ],
    "items": [
        {"n": 9, "key": ["ALTHOUGH", "THOUGH", "WHILE", "WHILST"], "type": "Subordinada concesiva",
         "theory": ["7"],
         "why": "Oración subordinada antepuesta (sujeto + verbo, coma, oración principal) que expresa un contraste "
                "inesperado: no tenía experiencia y, aun así, estaba convencida. [[Although]] y [[though]] son "
                "equivalentes en esta posición; [[while]] y [[whilst]] también valen con valor concesivo "
                "(«aunque») al principio de la frase.",
         "wrong": "[[!whereas]] (contrapone dos hechos paralelos, no expresa concesión); [[!as]], [[!since]] o "
                  "[[!because]] (la relación no es de causa); [[!despite]] (no admite oración); [[!even]] (necesita "
                  "[[though]] o [[if]]); [[!if]] (con [[had never sailed]] se leería como condición)."},
        {"n": 10, "key": ["NOR", "NEITHER"], "type": "Adición negativa con inversión", "theory": ["5.2"],
         "why": "Tras una oración negativa ([[No one … had ever crossed]]), [[nor / neither]] + auxiliar + sujeto, "
                "con el verbo omitido: «tampoco lo había hecho ninguno de sus amigos». Las dos palabras son correctas.",
         "wrong": "[[!so]] (versión afirmativa: [[so had]] = «también»); [[!never]] o [[!hardly]] (provocan "
                  "inversión al adelantarse, pero no permiten omitir el verbo: *[[never had any of her friends]])."},
        {"n": 11, "key": ["AS", "THOUGH"], "type": "Anteposición concesiva", "theory": ["9.1"],
         "why": "Adjetivo al inicio + hueco + sujeto + verbo ([[it may seem]]): anteposición concesiva, «por extraño "
                "que parezca». En esta estructura valen [[as]] y [[though]].",
         "wrong": "[[!although]] (no admite anteposición: *[[Strange although it may seem]])."},
        {"n": 12, "key": ["DID", "COULD", "WOULD"], "type": "Inversión con auxiliar o modal", "theory": ["10"],
         "why": "[[Only when]] + oración, y en la principal inversión: hueco + sujeto + verbo en forma base "
                "([[grasp]]). [[Did]] presenta el hecho; [[could]], que solo entonces fue capaz de comprenderlo; "
                "[[would]], el futuro en el pasado propio de la narración.",
         "wrong": "[[!had]] (exigiría [[grasped]]); [[!can]] o [[!will]] (rompen el pasado); [[!might]] o "
                  "[[!should]] (no encajan con un hecho narrado). Explicación: UOE-P4_Teoria_v1, §3.1."},
        {"n": 13, "key": ["IF", "THOUGH"], "type": "As if / as though", "theory": ["10"],
         "why": "[[as if]] y [[as though]] + pasado irreal ([[had]]): «como si tuviera voluntad propia».",
         "wrong": "[[!although]] (*[[as although]]); [[!when]] ([[as when]] compara con un momento, no con una "
                  "situación imaginaria)."},
        {"n": 14, "key": ["YET", "STILL"], "type": "Had yet to / had still to", "theory": ["7.1"],
         "why": "[[had yet to]] y [[had still to]] + verbo = «todavía no había». Tres semanas después y sin "
                "provisiones, aún no había llegado a la mitad.",
         "wrong": "[[!now]], [[!only]] o [[!also]] (con [[had … to]] expresan obligación o suficiencia, que aquí "
                  "no tienen sentido); [[!never]] (*[[had never to reach]])."},
        {"n": 15, "key": ["AS", "THOUGH"], "type": "Anteposición concesiva", "theory": ["9.1"],
         "why": "Adjetivo al inicio + hueco + sujeto + [[was]]: «por agotada que estuviera». Con [[as]] podría "
                "leerse como causal, pero el contexto ([[refused to radio for help]]) es concesivo.",
         "wrong": "[[!although]] (*[[Exhausted although she was]])."},
        {"n": 16, "key": ["DID", "WOULD"], "type": "Inversión con auxiliar o modal", "theory": ["10"],
         "why": "[[Not once]] al inicio provoca inversión: hueco + sujeto + verbo en forma base ([[consider]]). "
                "[[Did]] presenta el hecho; [[would]], una negativa obstinada.",
         "wrong": "[[!could]] («ni una vez pudo plantearse») no encaja con [[insisted]]; [[!had]] exigiría "
                  "[[considered]]. Explicación: UOE-P4_Teoria_v1, §3.1."},
    ],
}


if __name__ == "__main__":
    import runpy
    args = sys.argv[1:]
    only_sentences = "--frases" in args
    args = [a for a in args if a != "--frases"]
    if not args:
        print("Uso: python3 gen_UOE-P2.py [--frases] --demo | mis_hojas.py [carpeta_salida]")
        sys.exit(1)
    if args[0] == "--demo":
        specs = [DEMO]
    else:
        ns = runpy.run_path(args[0], init_globals={"E": E, "EB": EB, "G": G})
        specs = ns.get("SPECS") or [ns["SPEC"]]
    if only_sentences:
        for sp in specs:
            print(f"--- Hoja {sp['num']}")
            for n, w, s in key_sentences(sp):
                print(f"  {n:>2} {w:<9}| {s}")
        sys.exit(0)
    out_dir = args[1] if len(args) > 1 else "/mnt/user-data/outputs"
    os.makedirs(out_dir, exist_ok=True)
    for sp in specs:
        make(sp, out_dir)
