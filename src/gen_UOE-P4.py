# gen_UOE-P4.py · Generador de Use of English Part 4 (key word transformations) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa (rubrica, ejemplo, 6 items, hoja de respuestas y soluciones) con el
#     formato de UOE-P4_Practica_01-08.
#   - Bloques sueltos para insertar la Part 4 en un simulacro (SIM): enunciado, hoja de respuestas
#     y soluciones por separado.
#   - Verificacion automatica de la hoja antes y despues de generar el PDF.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_UOE-P4.py --demo [carpeta_salida]        -> genera una hoja de ejemplo
#   python3 gen_UOE-P4.py mis_hojas.py [carpeta_salida]  -> mis_hojas.py define SPECS = [spec, ...]
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_p4", "/ruta/gen_UOE-P4.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, lex = gen.verify(spec)
#   gen.build_sheet(spec, "/mnt/user-data/outputs/UOE-P4_Practica_09.pdf")
#   story += gen.question_flowables(spec)        # para un SIM
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num        "09"                        numero de hoja (para nombre, cabecera y pie)
#   subtitle   "Hoja 09 · ..."             subtitulo en espanol
#   first      25                          opcional; primer numero de pregunta (por defecto 25)
#   example    {"s1": ..., "keyword": ..., "s2": "... {G} ...", "answer": "EN MAYUSCULAS"}
#              "shown" opcional: texto del hueco del ejemplo (por defecto, answer en minusculas)
#   items      6 diccionarios, uno por pregunta, en orden:
#       n        25
#       s1       "First sentence."                         en ingles
#       keyword  "UNTIL"                                   palabra clave, en mayusculas
#       s2       "Not {G} realise how much..."             {G} marca el hueco (uno solo)
#       key      ["UNTIL THE WATER {_|HAD} RECEDED DID WE"]
#                TODAS las respuestas aceptables, en mayusculas. La primera expansion del primer
#                patron es la respuesta principal. Alternativas: {A|B|C}; "_" = opcion vacia.
#                Ej.: "IS {HIGH|ABOUT|_} TIME YOU {GOT|HAD}" -> 6 respuestas.
#       halves   ("until the water (had) receded", "did we")   las dos mitades puntuables
#       theory   ["3.1"]                                   secciones de UOE-P4_Teoria_v1 (ver THEORY)
#       why      explicacion breve
#       wrong    [("RESPUESTA TENTADORA", "por que no vale"), ...]
#                El generador anade solo el recuento si se sale de 3-8 palabras y el aviso si no
#                usa la palabra clave; el motivo puede quedar vacio en esos casos.
#       lex      ["set foot in"]                           opcional: lexico que no esta en la teoria
#                                                          (se lista al generar, para el modulo LEX)
#
#   Marcado en why / halves / motivos de wrong (y en cualquier texto en espanol):
#       [[texto]]   -> ingles en serif (equivale a E("texto"))
#       [[!TEXTO]]  -> ingles en serif y negrita (equivale a EB("TEXTO"))
#
# RECUENTO DE PALABRAS (reglas de Cambridge)
#   Toda contraccion cuenta como dos palabras (DIDN'T, I'D, IT'S, WE'LL...). CANNOT cuenta como una.
#   El genitivo (SISTER'S, CRITICS') cuenta como una. Las palabras con guion cuentan como una.
#
# REGLAS DEL PROYECTO QUE EL GENERADOR NO PUEDE COMPROBAR (hay que hacerlas a mano)
#   - Que la clave recoja todas las respuestas aceptables y que ninguna otra sea defendible.
#   - Que la respuesta conserve el significado (nada anadido ni perdido) y encaje con la frase 2.
#   - Ingles britanico en las frases.
#   - Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import itertools
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
from reportlab.platypus import KeepTogether  # noqa: E402

VERSION = "1"
FIRST_ITEM = 25           # la Part 4 del examen va de la 25 a la 30
N_ITEMS = 6
WORDS_MIN, WORDS_MAX = 3, 8
GAP = "_" * 34
ACC_HEX = "#" + ACCENT.hexval()[2:]
GREY_HEX = "#" + GREY.hexval()[2:]


# ---------- Ingles dentro del texto en espanol ----------
def E(s):
    return f'<font name="EN">{s}</font>'


def EB(s):
    return f'<font name="EN"><b>{s}</b></font>'


def markup(s):
    """[[!X]] -> EB(X); [[x]] -> E(x)."""
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)


# ---------- Secciones de UOE-P4_Teoria_v1 ----------
THEORY = {
    "1": "Formato y puntuación",
    "2": "Método en cuatro pasos",
    "3.1": "Inversión tras adverbiales negativos y restrictivos",
    "3.2": "Condicionales sin if",
    "3.3": "Pasiva impersonal y causativa",
    "3.4": "Cleft sentences y énfasis",
    "3.5": "Modales perfectos y grados de certeza",
    "3.6": "Wish, would rather, it’s high time, as if",
    "3.7": "Comparación y grado",
    "3.8": "Patrones verbales y verbos de reporte",
    "4": "Nominalización",
    "5.1": "Verbos comodín + sustantivo",
    "5.2": "Idioms frecuentes por palabra clave",
    "5.3": "Phrasal verbs y prepositional verbs",
    "5.4": "Frases preposicionales",
    "6": "Trampas típicas",
    "7": "Tabla de referencia por palabra clave",
}
THEORY_DOC = "UOE-P4_Teoria_v1"

# ---------- Estilos propios de la hoja (sobre la plantilla, sin cambiarla) ----------
_en_t = ParagraphStyle("p4_en_t", parent=S["en"], spaceAfter=2)
_key = ParagraphStyle("p4_key", parent=S["en"], fontName="EN-B", leftIndent=40, spaceAfter=2)
_num = ParagraphStyle("p4_num", parent=S["en"], fontName="EN-B")
_body_t = ParagraphStyle("p4_body_t", parent=S["body"], spaceAfter=2.5)
_sol_h = ParagraphStyle("p4_sol_h", parent=S["h3"], spaceBefore=8)


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _range(spec):
    a = _first(spec)
    return f"{a}–{a + N_ITEMS - 1}"


# ---------- Respuestas: normalizacion, recuento y alternativas ----------
_CONTR_END = ("N’T", "’D", "’LL", "’RE", "’VE", "’M")
_PRON_S = {"IT’S", "HE’S", "SHE’S", "THAT’S", "THERE’S", "WHAT’S", "WHO’S", "HERE’S", "LET’S", "WHERE’S"}


def norm(ans):
    """Mayusculas, apostrofo tipografico y espacios simples."""
    return re.sub(r"\s+", " ", ans.replace("'", "’")).strip().upper()


def word_count(ans):
    n = 0
    for w in norm(ans).replace(",", "").split():
        n += 2 if (w.endswith(_CONTR_END) or w in _PRON_S) else 1
    return n


def tokens(ans):
    return re.findall(r"[A-Z’\-]+", norm(ans))


def expand(pattern):
    """'IS {HIGH|_} TIME YOU {GOT|HAD}' -> lista de respuestas, en orden."""
    parts = re.split(r"(\{[^{}]*\})", pattern)
    choices = []
    for part in parts:
        if part.startswith("{") and part.endswith("}"):
            choices.append(["" if o.strip() == "_" else o.strip() for o in part[1:-1].split("|")])
        else:
            choices.append([part])
    out = []
    for combo in itertools.product(*choices):
        a = norm(" ".join(c for c in combo))
        if a not in out:
            out.append(a)
    return out


def all_keys(item):
    out = []
    for pat in item["key"]:
        for a in expand(pat):
            if a not in out:
                out.append(a)
    return out


def show_pattern(pattern):
    """Version legible de un patron: {A|B} -> (A / B); {A|_} -> [A]."""
    def rep(m):
        opts = [o.strip() for o in m.group(1).split("|")]
        real = [o for o in opts if o != "_"]
        if len(real) < len(opts):
            return "[" + " / ".join(real) + "]"
        return "(" + " / ".join(real) + ")"
    return norm(re.sub(r"\{([^{}]*)\}", rep, pattern))


def _count_label(answers):
    ns = sorted({word_count(a) for a in answers})
    return str(ns[0]) if len(ns) == 1 else f"{ns[0]}–{ns[-1]}"


def _wrong_reason(item, ans, reason):
    notes = []
    n = word_count(ans)
    if not WORDS_MIN <= n <= WORDS_MAX:
        notes.append(f"{n} palabras")
    if item["keyword"] not in tokens(ans):
        notes.append("no usa la palabra clave tal cual: el ítem vale 0")
    if reason:
        notes.append(markup(reason))
    return "; ".join(notes)


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def _q_block(num, s1, keyword, s2, shown=None):
    gap = f"<u>&nbsp;{shown}&nbsp;</u>" if shown else GAP
    inner = [Paragraph(s1, _en_t), Paragraph(keyword, _key), Paragraph(s2.replace("{G}", gap), S["en"])]
    t = Table([[Paragraph(str(num), _num), inner]], colWidths=[10 * mm, CONTENT_W - 10 * mm])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return KeepTogether([t, Spacer(1, 13)])


def question_flowables(spec, with_title_block=False):
    """Rubrica, ejemplo y los 6 items. Con with_title_block=True antepone el bloque de titulo de la hoja."""
    out = []
    if with_title_block:
        out += title_block(f"UOE-P4 · Práctica {spec['num']}", "Key word transformations", spec["subtitle"],
                           f"6 ítems (preguntas {_range(spec)}) · hasta 2 puntos por ítem · "
                           "tiempo orientativo: 12 minutos · sin consultar la teoría")
    out.append(en(f"For questions {_range(spec)}, complete the second sentence so that it has a similar meaning to "
                  "the first sentence, using the word given. <b>Do not change the word given.</b> You must use "
                  "between <b>three</b> and <b>eight</b> words, including the word given. Here is an example (0)."))
    ex = spec["example"]
    shown = ex.get("shown", ex["answer"].lower())
    out += [Spacer(1, 2), en("<b>Example:</b>"), _q_block(0, ex["s1"], ex["keyword"], ex["s2"], shown=shown),
            Paragraph(f"The gap can be filled by the words ‘{shown}’, so you write:", _en_t),
            en(f"<b>0</b>&nbsp;&nbsp;&nbsp;&nbsp;<b>{norm(ex['answer'])}</b>"),
            en("Write only the missing words IN CAPITAL LETTERS.")]
    line = Table([[""]], colWidths=[CONTENT_W], rowHeights=[2])
    line.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.6, RULE)]))
    out += [Spacer(1, 4), line, Spacer(1, 12)]
    for it in spec["items"]:
        out.append(_q_block(it["n"], it["s1"], it["keyword"], it["s2"]))
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    out = [h2(heading)]
    rows = [["Nº", "Respuesta (en mayúsculas)", "Puntos"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), "", "&nbsp;&nbsp;&nbsp;/ 2"])
    rows.append(["", "<b>Total</b>", f"&nbsp;&nbsp;&nbsp;/ {2 * N_ITEMS}"])
    out += table(rows, [14, 126, 30], zebra=False,
                 extra=[("TOPPADDING", (0, 1), (-1, -2), 9), ("BOTTOMPADDING", (0, 1), (-1, -2), 9),
                        ("LINEABOVE", (0, -1), (-1, -1), 0.8, NAVY)])
    return out


def _variants_line(it):
    parts = []
    for i, pat in enumerate(it["key"]):
        exps = expand(pat)
        if i == 0 and len(exps) == 1:
            continue
        parts.append(f"{EB(show_pattern(pat))} ({_count_label(exps)})")
    return " · ".join(parts)


def _item_solution(it):
    main = all_keys(it)[0]
    blk = [Paragraph(f'<font color="{ACC_HEX}">{it["n"]}</font>&nbsp;&nbsp;{EB(main)}&nbsp;&nbsp;'
                     f'<font name="Sans" color="{GREY_HEX}">({word_count(main)} palabras)</font>', _sol_h)]
    var = _variants_line(it)
    if var:
        blk.append(Paragraph(f"<b>También vale:</b> {var}", _body_t))
    h1_, h2_ = it["halves"]
    blk.append(Paragraph(f"<b>Mitades:</b> {E(markup(h1_))} &nbsp;|&nbsp; {E(markup(h2_))}", _body_t))
    blk.append(Paragraph(f"<b>Por qué:</b> {markup(it['why'])}", _body_t))
    wr = "; ".join(f"{E('*' + norm(a))} ({_wrong_reason(it, a, r)})" for a, r in it["wrong"])
    blk.append(Paragraph(f"<b>No puntúa:</b> {wr}.", _body_t))
    blk.append(Paragraph("Teoría: " + " · ".join(f"§{s} {THEORY[s]}" for s in it["theory"]), S["small"]))
    if it.get("lex"):
        blk.append(Paragraph("Léxico fuera de la teoría (para LEX): " + E(", ".join(it["lex"])), S["small"]))
    return KeepTogether(blk)


def solutions_flowables(spec, with_band=True, heading=None, quick_key=False):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 4 · Key word transformations' dentro de un simulacro).
    quick_key=True antepone una tabla de clave rapida (util para corregir un simulacro)."""
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p("Corrige cada ítem por mitades: 1 punto por cada mitad correcta y bien escrita. Se acepta "
                 "cualquiera de las variantes indicadas; las respuestas fuera de 3–8 palabras o con la palabra "
                 "clave cambiada valen 0."))
    if quick_key:
        rows = [["Nº", "Clave", "Teoría"]]
        for it in spec["items"]:
            rows.append([str(it["n"]), " · ".join(show_pattern(k) for k in it["key"]),
                         " · ".join("§" + s for s in it["theory"])])
        out += table(rows, [12, 128, 30], en_cols=(1,))
    for it in spec["items"]:
        out.append(_item_solution(it))
    return out


def build_sheet(spec, out_path):
    """Hoja de practica completa: enunciado, hoja de respuestas (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"UOE-P4 · Práctica {n}", f"UOE-P4_Practica_{n}.pdf",
          title=f"UOE-P4 · Key word transformations · Práctica {n}")
    return out_path


# ---------- Verificacion ----------
def _half_ok(half, main):
    """La primera alternativa de cada mitad (sin parentesis) tiene que estar en la respuesta principal."""
    h = re.sub(r"\[\[!?|\]\]", "", half).split(" / ")[0]
    h = re.sub(r"\([^)]*\)", "", h)
    frags = [norm(f) for f in h.split("…") if f.strip()]
    return all(f in main for f in frags)


def verify(spec):
    """Comprobaciones de formato y coherencia antes de generar. Devuelve (errores, lexico_para_LEX)."""
    errs, lex = [], []
    a = _first(spec)
    expected = list(range(a, a + N_ITEMS))
    for field in ("num", "subtitle", "example", "items"):
        if not spec.get(field):
            errs.append(f"falta el campo '{field}' de la hoja")
    if errs:
        return errs, lex
    ex = spec["example"]
    exa = norm(ex.get("answer", ""))
    if ex.get("s2", "").count("{G}") != 1:
        errs.append("ejemplo: la frase 2 debe tener un solo {G}")
    if not WORDS_MIN <= word_count(exa) <= WORDS_MAX:
        errs.append(f"ejemplo: {word_count(exa)} palabras")
    if ex.get("keyword") not in tokens(exa):
        errs.append("ejemplo: la respuesta no contiene la palabra clave")
    if "shown" in ex and norm(ex["shown"]) != exa:
        errs.append("ejemplo: 'shown' no coincide con 'answer'")
    if [it.get("n") for it in spec["items"]] != expected:
        errs.append(f"numeración de ítems: se esperaban {expected}")
    for it in spec["items"]:
        n = it.get("n")
        for field in ("s1", "keyword", "s2", "key", "halves", "theory", "why", "wrong"):
            if not it.get(field):
                errs.append(f"{n}: falta el campo '{field}'")
        if any(not it.get(f) for f in ("keyword", "s2", "key", "halves")):
            continue
        kw = it["keyword"]
        if not re.fullmatch(r"[A-Z]+", kw):
            errs.append(f"{n}: la palabra clave debe ser una sola palabra en mayúsculas")
        if it["s2"].count("{G}") != 1:
            errs.append(f"{n}: la frase 2 debe tener un solo {{G}}")
        if re.search(rf"\b{kw}\b", it["s2"].replace("{G}", ""), re.I):
            errs.append(f"{n}: la palabra clave aparece fuera del hueco en la frase 2")
        keys = all_keys(it)
        for k in keys:
            if not re.fullmatch(r"[A-Z’\-, ]+", k):
                errs.append(f"{n}: '{k}' contiene caracteres no válidos (solo mayúsculas)")
            c = word_count(k)
            if not WORDS_MIN <= c <= WORDS_MAX:
                errs.append(f"{n}: '{k}' tiene {c} palabras")
            if kw not in tokens(k):
                errs.append(f"{n}: '{k}' no contiene la palabra clave {kw} sin cambios")
        if len(it["halves"]) != 2:
            errs.append(f"{n}: 'halves' debe tener dos mitades")
        else:
            for h in it["halves"]:
                if not _half_ok(h, keys[0]):
                    errs.append(f"{n}: la mitad '{h}' no aparece en la respuesta principal")
        for s in it.get("theory", []):
            if s not in THEORY:
                errs.append(f"{n}: sección de teoría inexistente §{s}")
        for w in it.get("wrong", []):
            if not (isinstance(w, (tuple, list)) and len(w) == 2):
                errs.append(f"{n}: cada 'wrong' debe ser (respuesta, motivo)")
                continue
            if norm(w[0]) in keys:
                errs.append(f"{n}: '{w[0]}' figura a la vez en la clave y en 'wrong'")
            if not _wrong_reason(it, w[0], w[1]):
                errs.append(f"{n}: falta el motivo de '{w[0]}'")
        texts = [it.get("why", "")] + list(it["halves"]) + [r for _, r in it.get("wrong", []) if isinstance(r, str)]
        for txt in texts:
            if re.search(r"\[\[|\]\]", re.sub(r"\[\[!?(.+?)\]\]", "", txt)):
                errs.append(f"{n}: marcado [[ ]] sin cerrar")
        lex += it.get("lex", [])
    return errs, lex


def check_pdf(path):
    """Busca restos de codigo o de marcado en el texto del PDF ya generado."""
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            txt = "\n".join(pg.extract_text() or "" for pg in pdf.pages)
    except ImportError:
        from pypdf import PdfReader
        txt = "\n".join(pg.extract_text() or "" for pg in PdfReader(path).pages)
    return re.findall(r"\{E|EB\(|E\('|\{G\}|\{[A-Z_ ’]+\|[^}]*\}|\[\[|\]\]", txt)


def make(spec, out_dir="/mnt/user-data/outputs"):
    """Verifica, genera y comprueba el PDF. Devuelve la ruta; lanza ValueError si algo falla."""
    errs, lex = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}: " + "; ".join(errs))
    path = build_sheet(spec, os.path.join(out_dir, f"UOE-P4_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    n_keys = sum(len(all_keys(it)) for it in spec["items"])
    print(f"UOE-P4_Practica_{spec['num']}.pdf · {n_keys} respuestas aceptadas en la clave · verificación sin errores")
    if lex:
        print("  Léxico fuera de la teoría (anotar para LEX): " + "; ".join(lex))
    return path


# ---------- Hoja de ejemplo (contenido de UOE-P4_Practica_08, con el marcado [[ ]]) ----------
DEMO = {
    "num": "99",
    "subtitle": "Hoja de prueba del generador (contenido de UOE-P4_Practica_08)",
    "example": {"s1": "People say he is a brilliant cook.", "keyword": "SUPPOSED",
                "s2": "He {G} a brilliant cook.", "answer": "IS SUPPOSED TO BE"},
    "items": [
        {"n": 25, "s1": "It is common knowledge that the director and the producer don’t get on.",
         "keyword": "TERMS", "s2": "The director and the producer {G}.",
         "key": ["ARE KNOWN NOT TO BE ON GOOD TERMS", "ARE {_|WIDELY} KNOWN TO BE ON BAD TERMS"],
         "halves": ("are known", "not to be on good terms / to be on bad terms"),
         "theory": ["3.3", "7"],
         "why": "Pasiva impersonal ([[it is common knowledge that]] → [[are known]]) e idiom ([[not get on]] → "
                "[[not be on good terms]]). La negación va delante del infinitivo.",
         "wrong": [("ARE WELL KNOWN NOT TO BE ON GOOD TERMS", ""),
                   ("ARE KNOWN NOT TO BE ON SPEAKING TERMS", "exagera: significaría que ni se hablan")]},
        {"n": 26, "s1": "The remake is far inferior to the original film.",
         "keyword": "CANDLE", "s2": "The remake {G} the original film.",
         "key": ["{DOES NOT|DOESN’T|CAN’T|CANNOT} HOLD A CANDLE TO"],
         "halves": ("does not / can’t hold", "a candle to"),
         "theory": ["3.7"], "lex": ["not hold a candle to"],
         "why": "[[Not hold a candle to]] = ser muy inferior a algo. El idiom solo se usa en negativa, así que la "
                "negación es obligatoria.",
         "wrong": [("DOES NOT HOLD THE CANDLE TO", "el idiom lleva [[a]]"),
                   ("DOES NOT HOLD A CANDLE WITH", "preposición")]},
        {"n": 27, "s1": "I regret telling her what I thought of her new haircut.",
         "keyword": "KEPT", "s2": "I wish {G} her new haircut to myself.",
         "key": ["{I HAD|I’D} KEPT MY {OPINION OF|OPINION ABOUT|THOUGHTS ON|VIEWS ON}",
                 "{I HAD|I’D} KEPT WHAT I THOUGHT OF"],
         "halves": ("I had kept", "my opinion of"),
         "theory": ["3.6"], "lex": ["keep sth to oneself"],
         "why": "Lamento sobre el pasado → [[wish]] + past perfect. [[Keep sth to oneself]] = no decir algo; el "
                "[[to myself]] ya está fuera del hueco.",
         "wrong": [("I KEPT MY OPINION OF", "pasado simple: deseo sobre el presente"),
                   ("I HADN’T TOLD MY OPINION OF", "no encaja con [[to myself]]")]},
        {"n": 28, "s1": "If our deal with the bank collapses, we will have to find another investor.",
         "keyword": "THROUGH", "s2": "Should {G}, we will have to find another investor.",
         "key": ["OUR DEAL WITH THE BANK FALL THROUGH"],
         "halves": ("our deal with the bank", "fall through"),
         "theory": ["3.2", "5.3"],
         "why": "Condicional con [[should]] invertido: detrás va el sujeto y el infinitivo sin [[to]] y sin [[-s]]. "
                "[[Fall through]] = fracasar, no llegar a cerrarse un acuerdo o plan.",
         "wrong": [("OUR DEAL WITH THE BANK FALLS THROUGH", "tras [[should]] no va [[-s]]"),
                   ("OUR DEAL WITH THE BANK FELL THROUGH", "tras [[should]] va el infinitivo")]},
        {"n": 29, "s1": "Her success was due more to hard work than to talent.",
         "keyword": "MUCH", "s2": "Her success was {G} as of hard work.",
         "key": ["NOT SO MUCH {THE RESULT|A RESULT|A MATTER|THE PRODUCT} OF TALENT"],
         "halves": ("not so much", "the result of talent"),
         "theory": ["3.7"],
         "why": "[[Not so much X as Y]] = más Y que X. El orden se invierte respecto a la frase 1: lo que pesa menos "
                "([[talent]]) va primero. El [[of]] tras [[as]] obliga a usar un sustantivo seguido de [[of]].",
         "wrong": [("NOT SO MUCH THE RESULT OF HARD WORK", "invierte el sentido"),
                   ("NOT SO MUCH DUE TO TALENT", "no encaja con [[as of hard work]]")]},
        {"n": 30, "s1": "Although his story seemed unlikely, the teacher decided to believe him.",
         "keyword": "BENEFIT", "s2": "Although his story seemed unlikely, the teacher decided {G} doubt.",
         "key": ["TO GIVE HIM THE BENEFIT OF THE"],
         "halves": ("to give him", "the benefit of the"),
         "theory": ["5.1"],
         "why": "[[Give sb the benefit of the doubt]] = creer a alguien sin pruebas. El objeto ([[him]]) va entre "
                "el verbo y la expresión.",
         "wrong": [("TO GIVE THE BENEFIT OF THE", "falta [[him]]: cuesta una mitad"),
                   ("TO GIVE HIM A BENEFIT OF THE", "el idiom lleva [[the]]")]},
    ],
}


if __name__ == "__main__":
    import runpy
    if len(sys.argv) < 2:
        print("Uso: python3 gen_UOE-P4.py --demo | mis_hojas.py [carpeta_salida]")
        sys.exit(1)
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "/mnt/user-data/outputs"
    os.makedirs(out_dir, exist_ok=True)
    if sys.argv[1] == "--demo":
        specs = [DEMO]
    else:
        ns = runpy.run_path(sys.argv[1], init_globals={"E": E, "EB": EB})
        specs = ns.get("SPECS") or [ns["SPEC"]]
    for sp in specs:
        make(sp, out_dir)
