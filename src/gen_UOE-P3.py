# gen_UOE-P3.py · Generador de Use of English Part 3 (word formation) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa (texto con la palabra base al margen, hoja de respuestas y soluciones),
#     identica a UOE-P3_Practica_01-06.
#   - Bloques sueltos para insertar la Part 3 en un simulacro (SIM): enunciado, hoja de respuestas
#     y soluciones por separado.
#   - Verificacion automatica de la hoja antes y despues de generar el PDF.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_UOE-P3.py --demo [carpeta_salida]        -> genera una hoja de ejemplo
#   python3 gen_UOE-P3.py mis_hojas.py [carpeta_salida]  -> mis_hojas.py define SPECS = [spec, ...]
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_p3", "/ruta/gen_UOE-P3.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, words = gen.verify(spec)
#   gen.build_sheet(spec, "/mnt/user-data/outputs/UOE-P3_Practica_07.pdf")
#   story += gen.question_flowables(spec)        # para un SIM
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num          "07"                       numero de hoja (para nombre, cabecera y pie)
#   subtitle     "Hoja 07 · ..."            subtitulo en espanol
#   changes      "hasta tres cambios por hueco"
#   title        "Titulo del texto"         en ingles
#   example      "EXTINCTION"               respuesta del ejemplo (0)
#   example_stem "EXTINCT"
#   text         [parrafo, parrafo, ...]    en ingles; cada hueco se escribe {numero|PALABRA_BASE},
#                                           p. ej. {0|EXTINCT}, {17|INTRODUCE}
#   items        8 diccionarios, uno por hueco, en orden:
#       n        17
#       stem     "INTRODUCE"
#       key      ["REINTRODUCTION"]          TODAS las formas aceptables (mayusculas; guion permitido)
#       type     "Sustantivo · prefijo re-"  tipo de hueco, en espanol
#       theory   ["6.4", "2.2"]              secciones de UOE-P3_Teoria_v1 (ver THEORY)
#       why      explicacion: que decide la forma
#       changes  cambios sobre la palabra base, contados
#       wrong    respuestas tentadoras que no valen (en mayusculas, para que se comprueben)
#
#   Marcado en why / changes / wrong (y en cualquier texto en espanol):
#       [[texto]]   -> ingles en serif (equivale a E("texto"))
#       [[!TEXTO]]  -> ingles en serif y negrita (equivale a EB("TEXTO"))
#   Tambien se pueden usar directamente las funciones E() y EB() del modulo.
#
# REGLAS DEL PROYECTO QUE EL GENERADOR NO PUEDE COMPROBAR (hay que hacerlas a mano)
#   - Que cada hueco tenga una sola respuesta defendible o que la clave recoja todas.
#   - Ingles britanico en el texto; la clave admite -ize, ortografia americana coherente y
#     dobles grafias de diccionario. La forma separada de un compuesto no puntua.
#   - Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
from reportlab.lib.enums import TA_RIGHT  # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth  # noqa: E402

VERSION = "1"
G = "__________"
GAP_RE = re.compile(r"\{(\d+)\|([A-Z]+)\}")
FIRST_ITEM = 17           # la Part 3 del examen va de la 17 a la 24
N_ITEMS = 8
WORDS_MIN, WORDS_MAX = 180, 300


# ---------- Ingles dentro del texto en espanol ----------
def E(s):
    return f'<font name="EN">{s}</font>'


def EB(s):
    return f'<font name="EN"><b>{s}</b></font>'


def markup(s):
    """[[!X]] -> EB(X); [[x]] -> E(x)."""
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)


# ---------- Secciones de UOE-P3_Teoria_v1 ----------
THEORY = {
    "1": "Formato y puntuación",
    "2.1": "Método en cuatro pasos",
    "2.2": "Categoría: diagnóstico por el entorno del hueco",
    "2.3": "Número y forma",
    "2.4": "Sentido positivo o negativo",
    "2.5": "Contar los cambios",
    "3.1": "Cambio vocálico y -th",
    "3.2": "Verbo y sustantivo con cambio de consonante o de vocal",
    "3.3": "Familias latinas",
    "3.4": "-ity y -ous con cambio de raíz",
    "3.5": "Participios irregulares usados como adjetivo",
    "4.1": "Sufijos nominales",
    "4.2": "Sufijos adjetivales",
    "4.3": "Formación de verbos",
    "4.4": "Sustantivos de persona",
    "4.5": "Adverbios",
    "5": "Sufijos rivales",
    "6.1": "Elegir el prefijo negativo",
    "6.2": "Pares con significado distinto",
    "6.3": "Negativos con sentido propio",
    "6.4": "Prefijos de grado, posición y relación",
    "7.1": "Sustantivos formados con partícula",
    "7.2": "Adjetivos compuestos",
    "7.3": "Partícula + verbo",
    "7.4": "Grafía",
    "8.1": "Duplicación de consonante",
    "8.2": "La e final",
    "8.3": "La y final",
    "8.4": "-able o -ible; -ance o -ence; -ant o -ent",
    "8.5": "Letras que se pierden o cambian dentro de la raíz",
}
THEORY_DOC = "UOE-P3_Teoria_v1"

# ---------- Estilos propios de la hoja (sobre la plantilla, sin cambiarla) ----------
TXT_FONT, TXT_SIZE, TXT_LEAD = "EN", 10.5, 17
STEM_W = 32 * mm
TXT_W = CONTENT_W - STEM_W
_txt = ParagraphStyle("p3_txt", fontName=TXT_FONT, fontSize=TXT_SIZE, leading=TXT_LEAD, textColor=INK)
_stem = ParagraphStyle("p3_stem", parent=_txt, fontName="EN-B", alignment=TA_RIGHT)
_ttl = ParagraphStyle("p3_title", fontName="EN-B", fontSize=12.5, leading=16, textColor=NAVY, spaceAfter=8)
_rub = ParagraphStyle("p3_rubric", parent=S["en"], fontSize=10, leading=14)
_ihead = ParagraphStyle("p3_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=4)


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _range(spec):
    a = _first(spec)
    return f"{a}–{a + N_ITEMS - 1}"


# ---------- Maquetacion del texto: una palabra base por linea ----------
def layout_lines(paragraphs):
    """Reparte el texto en lineas que caben en TXT_W, con un solo hueco por linea.
    Devuelve una lista de parrafos; cada uno es una lista de (texto_linea, palabra_base_o_None)."""
    out, limit = [], TXT_W - 6
    for par in paragraphs:
        tokens, stems = [], {}
        for tok in par.split():
            m = GAP_RE.search(tok)
            if m:
                tok = tok.replace(m.group(0), f"({m.group(1)}) {G}")
                stems[len(tokens)] = m.group(2)
            tokens.append(tok)
        lines, cur, cur_stem = [], [], None
        for i, tok in enumerate(tokens):
            tok_stem = stems.get(i)
            too_long = stringWidth(" ".join(cur + [tok]), TXT_FONT, TXT_SIZE) > limit
            if cur and (too_long or (tok_stem and cur_stem)):
                lines.append((" ".join(cur), cur_stem))
                cur, cur_stem = [], None
            cur.append(tok)
            if tok_stem:
                cur_stem = tok_stem
        if cur:
            lines.append((" ".join(cur), cur_stem))
        out.append(lines)
    return out


def text_block(paragraphs):
    rows, style = [], [
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]
    for p_i, lines in enumerate(layout_lines(paragraphs)):
        for l_i, (txt, stem) in enumerate(lines):
            rows.append([Paragraph(txt, _txt), Paragraph(stem or "", _stem)])
            if p_i > 0 and l_i == 0:
                style.append(("TOPPADDING", (0, len(rows) - 1), (-1, len(rows) - 1), 7))
    t = Table(rows, colWidths=[TXT_W, STEM_W])
    t.setStyle(TableStyle(style))
    return t


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def question_flowables(spec, with_title_block=False):
    """Rubrica, ejemplo y texto. Con with_title_block=True antepone el bloque de titulo de la hoja."""
    out = []
    if with_title_block:
        out += title_block(f"UOE-P3 · Práctica {spec['num']}", "Word formation", spec["subtitle"],
                           f"8 ítems (preguntas {_range(spec)}) · 1 punto por ítem · {spec['changes']}"
                           " · tiempo orientativo: 10 minutos · sin consultar la teoría")
    out.append(Paragraph(
        f"For questions {_range(spec)}, read the text below. Use the word given in <b>capitals</b> at the end of "
        "some of the lines to form a word that fits in the gap in the same line. There is an example at the "
        "beginning (0). Write your answers <b>IN CAPITAL LETTERS</b> on the answer sheet.", _rub))
    out.append(Paragraph(f"Example: (0) <b>{spec['example']}</b>", _rub))
    out += [Spacer(1, 6), Paragraph(spec["title"], _ttl), text_block(spec["text"])]
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    out = [h2(heading), p(
        "Escribe una sola palabra por hueco, en mayúsculas. Al corregir, marca 1 punto por acierto: la ortografía "
        "tiene que ser exacta, un compuesto con guion cuenta como una palabra y una respuesta doble vale 0.")]
    rows = [["Nº", "Palabra base", "Respuesta (en mayúsculas)", "Punto"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), it["stem"], "", "&nbsp;&nbsp;&nbsp;&nbsp;/ 1"])
    rows.append(["", "", "<b>Total</b>", f"&nbsp;&nbsp;&nbsp;&nbsp;<b>/ {N_ITEMS}</b>"])
    out += table(rows, [14, 36, 92, 28], en_cols=(1,), zebra=False,
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 10), ("BOTTOMPADDING", (0, 1), (-1, -1), 10),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE")])
    return out


def solutions_flowables(spec, with_band=True, heading=None):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 3 · Word formation' dentro de un simulacro)."""
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p("1 punto por acierto. La clave recoge todas las formas aceptables de cada hueco; basta con una. "
                 "Cada solución explica qué decide la forma, cuenta los cambios sobre la palabra base, señala las "
                 f"respuestas tentadoras que no valen y remite al apartado de {THEORY_DOC} que lo trabaja."))
    out.append(h2("Clave rápida") if not heading else h3("Clave rápida"))
    rows = [["Nº", "Clave", "Tipo de hueco", "Teoría"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), " / ".join(it["key"]), markup(it["type"]),
                     " · ".join("§" + s for s in it["theory"])])
    out += table(rows, [12, 50, 70, 38], en_cols=(1,))
    out.append(h2("Explicación por ítem") if not heading else h3("Explicación por ítem"))
    for it in spec["items"]:
        block = [Paragraph(f"{it['n']} · {E(' / '.join(it['key']))} · {markup(it['type'])}", _ihead),
                 p(f"<b>Por qué:</b> {markup(it['why'])}"),
                 p(f"<b>Cambios:</b> {markup(it['changes'])}"),
                 p(f"<b>No vale:</b> {markup(it['wrong'])}"),
                 p("<b>Teoría:</b> " + " · ".join(f"§{s} {THEORY[s]}" for s in it["theory"]))]
        out.append(KeepTogether(block + [Spacer(1, 4)]))
    return out


def build_sheet(spec, out_path):
    """Hoja de practica completa: enunciado, hoja de respuestas (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"UOE-P3 · Práctica {n}", f"UOE-P3_Practica_{n}.pdf", title=f"UOE-P3 · Práctica {n}")
    return out_path


# ---------- Verificacion ----------
def verify(spec):
    """Comprobaciones de formato y coherencia antes de generar. Devuelve (errores, palabras_del_texto)."""
    errs = []
    a = _first(spec)
    expected = list(range(a, a + N_ITEMS))
    gaps = [m for par in spec["text"] for m in GAP_RE.finditer(par)]
    nums = [int(m.group(1)) for m in gaps]
    if nums != [0] + expected:
        errs.append(f"numeración de huecos en el texto: {nums}")
    stems_txt = {int(m.group(1)): m.group(2) for m in gaps}
    if stems_txt.get(0) != spec["example_stem"]:
        errs.append("la palabra base del ejemplo no coincide con example_stem")
    if spec["example"] == spec["example_stem"]:
        errs.append("el ejemplo no cambia la palabra base")
    if [it["n"] for it in spec["items"]] != expected:
        errs.append(f"ítems de la clave: se esperaban {expected}")
    for it in spec["items"]:
        n = it["n"]
        for field in ("stem", "key", "type", "theory", "why", "changes", "wrong"):
            if not it.get(field):
                errs.append(f"{n}: falta el campo '{field}'")
        if stems_txt.get(n) != it.get("stem"):
            errs.append(f"{n}: palabra base distinta en el texto y en la clave")
        for k in it.get("key", []):
            if not re.fullmatch(r"[A-Z]+(-[A-Z]+)*", k):
                errs.append(f"{n}: '{k}' no es una sola palabra en mayúsculas")
            if k == it.get("stem"):
                errs.append(f"{n}: una respuesta coincide con la palabra base")
        if len(set(it.get("key", []))) != len(it.get("key", [])):
            errs.append(f"{n}: formas repetidas en la clave")
        for s in it.get("theory", []):
            if s not in THEORY:
                errs.append(f"{n}: sección de teoría inexistente §{s}")
        wrong_txt = re.sub(r"<[^>]+>", "", markup(it.get("wrong", "")))
        cited = set(re.findall(r"\b[A-Z]{3,}(?:-[A-Z]+)*\b", wrong_txt))
        clash = cited & set(it.get("key", []))
        if clash:
            errs.append(f"{n}: forma de la clave citada como incorrecta: {clash}")
        for field in ("type", "why", "changes", "wrong"):
            txt = markup(it.get(field, ""))
            if re.search(r"\{E|EB\(|\[\[|\]\]", txt):
                errs.append(f"{n}: marcado sin resolver en '{field}'")
    for lines in layout_lines(spec["text"]):
        for txt, _ in lines:
            if txt.count(G) > 1:
                errs.append(f"dos huecos en una línea: {txt[:40]}…")
    words = len(GAP_RE.sub("X", " ".join(spec["text"])).split())
    if not WORDS_MIN <= words <= WORDS_MAX:
        errs.append(f"longitud del texto fuera de {WORDS_MIN}–{WORDS_MAX} palabras: {words}")
    return errs, words


def check_pdf(path):
    """Busca restos de codigo o de marcado en el texto del PDF ya generado."""
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            txt = "\n".join(pg.extract_text() or "" for pg in pdf.pages)
    except ImportError:
        from pypdf import PdfReader
        txt = "\n".join(pg.extract_text() or "" for pg in PdfReader(path).pages)
    return re.findall(r"\{E|EB\(|E\('|\{G\}|\{\d+\|[A-Z]+\}|\[\[|\]\]", txt)


def make(spec, out_dir="/mnt/user-data/outputs"):
    """Verifica, genera y comprueba el PDF. Devuelve la ruta; lanza ValueError si algo falla."""
    errs, words = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}: " + "; ".join(errs))
    path = build_sheet(spec, os.path.join(out_dir, f"UOE-P3_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    print(f"UOE-P3_Practica_{spec['num']}.pdf · {words} palabras · verificación sin errores")
    return path


# ---------- Hoja de ejemplo (contenido de UOE-P3_Practica_06, con el marcado [[ ]]) ----------
DEMO = {
    "num": "99",
    "subtitle": "Hoja de prueba del generador",
    "changes": "hasta tres cambios por hueco",
    "title": "The return of the beaver",
    "example": "EXTINCTION", "example_stem": "EXTINCT",
    "text": [
        "Beavers were hunted to {0|EXTINCT} in Britain some four hundred years ago, prized for their fur and for "
        "a scent gland used in medicine and perfume. Their {17|INTRODUCE}, first in fenced enclosures and more "
        "recently in the wild, has become one of the most closely watched experiments in British conservation.",
        "Supporters claim that the animals are {18|ARGUE} the most effective engineers in the natural world. "
        "Their dams slow the flow of rivers, creating ponds and wetlands that support a wealth of other wildlife "
        "and help to reduce flooding further downstream. In one study in south-west England, researchers recorded "
        "markedly lower peaks in river flow after heavy rain once beavers had settled in the area.",
        "Many farmers, however, regard the newcomers with deep {19|SUSPECT}. Dams can leave valuable fields "
        "{20|WATER} for months, and trees felled by beavers sometimes block drainage channels. Critics also point "
        "out that several of the wild {21|POPULATE} were established {22|LEGAL}, by enthusiasts who released "
        "animals without permission.",
        "Conservationists complain that the rules governing new releases are {23|NECESSARY} restrictive; "
        "farmers, that they are far too lax. For now, positions on both sides remain largely {24|COMPROMISE}, "
        "and the debate shows no sign of ending. The beavers, meanwhile, carry on building regardless.",
    ],
    "items": [
        {"n": 17, "stem": "INTRODUCE", "key": ["REINTRODUCTION"], "type": "Sustantivo · prefijo re-",
         "theory": ["6.4", "2.2"],
         "why": "[[Their]] + hueco + coma y verbo ([[has become]]): sustantivo singular. La frase anterior cuenta "
                "que los castores ya vivieron en Gran Bretaña: lo que se hace ahora es devolverlos.",
         "changes": "[[introduce]] → [[introduction]] ([[-tion]]) → [[reintroduction]] ([[re-]]): dos cambios.",
         "wrong": "[[!INTRODUCTION]] ignora que la especie ya había vivido allí; [[!REINTRODUCING]] no funciona "
                  "tras [[Their]] sin objeto."},
        {"n": 18, "stem": "ARGUE", "key": ["ARGUABLY"], "type": "Adverbio · e final",
         "theory": ["4.5", "8.2"],
         "why": "[[are]] + hueco + [[the most effective]]: delante de un superlativo, un adverbio que matiza la "
                "afirmación: [[arguably]], «se puede sostener que».",
         "changes": "[[argue]] → [[arguable]] ([[-able]], pierde la [[e]]) → [[arguably]]: dos cambios.",
         "wrong": "[[!ARGUABLE]] es adjetivo; *[[!ARGUEABLY]] conserva una [[e]] que se pierde."},
        {"n": 19, "stem": "SUSPECT", "key": ["SUSPICION"], "type": "Sustantivo · cambio interno",
         "theory": ["2.2"],
         "why": "[[regard … with deep]] + hueco: sustantivo; [[regard sb with suspicion]], «mirar con recelo».",
         "changes": "[[suspect]] → [[suspicion]]: la raíz pasa a [[suspic-]] y se añade [[-ion]].",
         "wrong": "[[!SUSPICIOUS]] es adjetivo; *[[!SUSPECTION]] no existe."},
        {"n": 20, "stem": "WATER", "key": ["WATERLOGGED"], "type": "Adjetivo · compuesto",
         "theory": ["7.2", "8.1"],
         "why": "[[leave valuable fields]] + hueco + [[for months]]: adjetivo predicativo. Campos encharcados.",
         "changes": "[[water]] → [[waterlog]] → [[waterlogged]] ([[-ed]], con doble [[g]]): dos cambios.",
         "wrong": "[[!WATERED]] es «regado»; [[!WATERY]] es «aguado»; *[[!WATERLOGED]] no duplica la [[g]]."},
        {"n": 21, "stem": "POPULATE", "key": ["POPULATIONS"], "type": "Sustantivo · plural",
         "theory": ["2.3"],
         "why": "[[several of the wild]] + hueco: [[several of]] exige plural, y [[were established]] lo confirma.",
         "changes": "[[populate]] → [[population]] → [[populations]]: dos cambios.",
         "wrong": "[[!POPULATION]] en singular no concuerda con [[several of]] ni con [[were]]."},
        {"n": 22, "stem": "LEGAL", "key": ["ILLEGALLY"], "type": "Adverbio · prefijo il-",
         "theory": ["6.1", "2.4"],
         "why": "[[were established]] + hueco: adverbio de modo. [[without permission]] fija el sentido negativo.",
         "changes": "[[legal]] → [[illegal]] ([[il-]]) → [[illegally]] ([[-ly]]): dos cambios.",
         "wrong": "[[!LEGALLY]] contradice [[without permission]]; *[[!ILEGALLY]] pierde una [[l]]."},
        {"n": 23, "stem": "NECESSARY", "key": ["UNNECESSARILY"], "type": "Adverbio · sentido",
         "theory": ["4.5", "2.4", "8.3"],
         "why": "[[are]] + hueco + [[restrictive]]: adverbio ante adjetivo. [[complain]] pide sentido negativo.",
         "changes": "[[necessary]] → [[unnecessary]] → [[unnecessarily]] ([[y]] → [[i]] + [[-ly]]): dos cambios.",
         "wrong": "[[!NECESSARILY]] da el sentido contrario; *[[!UNECESSARILY]] pierde una [[n]]."},
        {"n": 24, "stem": "COMPROMISE", "key": ["UNCOMPROMISING"], "type": "Adjetivo · prefijo un-",
         "theory": ["6.1", "2.4"],
         "why": "[[positions … remain largely]] + adjetivo. Nadie cede: posturas «intransigentes».",
         "changes": "[[compromise]] → [[compromising]] → [[uncompromising]] ([[un-]]): dos cambios.",
         "wrong": "[[!COMPROMISING]] es «comprometedor»; [[!COMPROMISED]] es «comprometido, dañado»."},
    ],
}


if __name__ == "__main__":
    import runpy
    if len(sys.argv) < 2:
        print(__doc__ or "Uso: python3 gen_UOE-P3.py --demo | mis_hojas.py [carpeta_salida]")
        sys.exit(1)
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "/mnt/user-data/outputs"
    os.makedirs(out_dir, exist_ok=True)
    if sys.argv[1] == "--demo":
        specs = [DEMO]
    else:
        ns = runpy.run_path(sys.argv[1], init_globals={"E": E, "EB": EB, "G": G})
        specs = ns.get("SPECS") or [ns["SPEC"]]
    for sp in specs:
        make(sp, out_dir)
