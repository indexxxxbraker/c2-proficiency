# gen_RDG-P7.py · Generador de Reading Part 7 (multiple matching) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa: preguntas 44-53 antes del texto (como en el examen), texto en 4-6
#     secciones, hoja de respuestas y soluciones (una linea del texto para cada elemento de la pregunta y,
#     si hay seccion tentadora, por que falla, con su tipo de RDG-P5 §7).
#   - Bloques sueltos para insertar la Part 7 en un simulacro (SIM): enunciado, hoja de respuestas y
#     soluciones por separado.
#   - Verificacion automatica antes y despues de generar el PDF.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_RDG-P7.py --demo [carpeta_salida]          -> hoja de ejemplo (la 01, numerada como 99)
#   python3 gen_RDG-P7.py mis_hojas.py [carpeta_salida]   -> mis_hojas.py define SPECS = [spec, ...]
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_p7", "/ruta/gen_RDG-P7.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, info = gen.verify(spec)
#   gen.make(spec, "/mnt/user-data/outputs")
#   story += gen.question_flowables(spec)          # para un SIM
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num         "03"
#   subtitle    "Hoja 03 · Extractos de un mismo texto · dificultad 3 de 4"   (espanol)
#   intro       "an article in which four novelists …"  completa la rubrica: "You are going to read …"
#   units       "sections" (por defecto), "novelists", "extracts"…: "choose from the {units} (A–D)"
#   lead        "In which section does the writer" / "Which novelist": frase comun que completan las preguntas
#   title       titulo del texto (ingles)
#   standfirst  entradilla opcional (ingles)
#   sections    [{"label": "A", "name": "Clare Hollis" (opcional), "text": "..." o ["parrafo", "parrafo"]}, …]
#               4-6 secciones con letras seguidas desde A; 650-800 palabras en total; ingles britanico
#   compound    numero de preguntas de dos o mas elementos (opcional; si consta, se comprueba)
#   lex         lexico para el modulo LEX (no se imprime; se usa en el resumen de cierre)
#   items       10 diccionarios, en orden:
#     n         44
#     prompt    "describes a decision that they now regret?"   (completa lead; minuscula inicial y ?)
#     key       "A"
#     elements  ["Decisión: {{cita}}.", "Arrepentimiento: {{cita}}."]   uno por elemento de la pregunta;
#               cada uno con al menos una cita {{…}} de la seccion clave
#     trap      opcional: {"letter": "C", "kinds": ["7.6"], "why": "… {{cita de C}} …"}
#               obligatorio en las preguntas de dos o mas elementos; kinds = tipos de RDG-P5 §7
#     theory    secciones de RDG-P7_Teoria_v1 (ver THEORY)
#
#   Marcado en elements / why (y en cualquier texto en espanol):
#     {{texto}}   -> cita literal, en serif; se comprueba que esta en la seccion que corresponde
#     [[texto]]   -> ingles en serif sin comprobar
#     [[!TEXTO]]  -> ingles en serif y negrita
#
# QUE COMPRUEBA verify()
#   numeracion 44-53 · 4-6 secciones, letras seguidas · longitud total y equilibrio entre secciones ·
#   cada seccion es clave de al menos una pregunta y de no mas de ceil(10/n)+1 · las claves no siguen el orden
#   del texto (ninguna racha no decreciente de mas de 4) ni repiten letra tres veces seguidas · cada elemento
#   cita la seccion clave · dos preguntas no se apoyan en la misma cita · la tentadora es otra seccion, con
#   tipo y cita de esa seccion · toda pregunta compuesta tiene tentadora · numero de compuestas (si consta) ·
#   eco lexico: la clave no es la seccion con mas palabras de la pregunta en mas de 3 preguntas ·
#   enunciados unicos y bien formados (con concordancia: 'Which person' + 3.a persona o pasado; 'In which
#   section does the writer' + forma base) · secciones de teoria existentes · marcado sin resolver.
#
# LO QUE EL GENERADOR NO PUEDE COMPROBAR (a mano)
#   - Que cada pregunta tenga una sola seccion defendible: leer cada pregunta contra TODAS las secciones.
#   - Que los datos reales del texto sean ciertos; ingles britanico; registro C2; dificultad graduada.
#   - Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402

VERSION = "1"
FIRST_ITEM = 44
N_ITEMS = 10
WORDS_MIN, WORDS_MAX = 650, 800
SEC_MIN, SEC_MAX = 4, 6
SEC_RATIO = (0.6, 1.5)
MAX_KEY_ECHO = 3
MAX_RUN = 4
THEORY_DOC = "RDG-P7_Teoria_v1"
LETTERS = "ABCDEF"

THEORY = {
    "1.1": "La tarea", "1.2": "Qué cambia respecto al C1", "1.3": "Cómo se formulan las preguntas",
    "2.1": "Las preguntas primero", "2.2": "Mapa rápido", "2.3": "Localizar", "2.4": "Comprobar y decidir",
    "2.5": "Orden de trabajo, tiempo y revisión",
    "3.1": "Qué se lee en el mapa y qué se salta", "3.2": "Anclas", "3.3": "Prever la paráfrasis",
    "3.4": "Señales de postura y de cambio",
    "4.1": "Preguntas de uno y de dos elementos", "4.2": "Lo que se pierde al comprobar",
    "4.3": "La sección tentadora", "4.4": "Desempatar entre dos secciones",
    "5.1": "Varias personas sobre un tema", "5.2": "Un texto dividido en secciones",
    "5.3": "Extractos de un mismo texto",
    "6": "Caso completo",
}
# Tipos de distractor de RDG-P5_Teoria_v1 §7 (la teoria de la Part 7 remite a ellos)
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
_rub = ParagraphStyle("p7_rubric", parent=S["en"], fontSize=10, leading=14)
_lead = ParagraphStyle("p7_lead", parent=S["en"], fontName="EN-B", spaceBefore=4, spaceAfter=4)
_q = ParagraphStyle("p7_q", parent=S["en"], leftIndent=22, bulletIndent=0, bulletFontName="EN-B", spaceAfter=3)
_ttl = ParagraphStyle("p7_title", parent=S["en"], fontName="EN-B", fontSize=13, leading=17, textColor=NAVY,
                      spaceBefore=4, spaceAfter=3)
_stand = ParagraphStyle("p7_stand", parent=S["en"], fontName="EN-I", textColor=GREY, spaceAfter=9)
_sec = ParagraphStyle("p7_sec", parent=S["en"], leading=15.4, leftIndent=20, bulletIndent=0,
                      bulletFontName="EN-B", bulletFontSize=11.5, spaceAfter=9)
_ihead = ParagraphStyle("p7_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)
_sol = ParagraphStyle("p7_sol", parent=S["body"], leftIndent=16, bulletIndent=4, spaceAfter=3)


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _range(spec):
    a = _first(spec)
    return f"{a}–{a + N_ITEMS - 1}"


def _labels(spec):
    return [s["label"] for s in spec["sections"]]


def _paras(sec):
    t = sec["text"]
    return [t] if isinstance(t, str) else list(t)


def _sec_text(sec):
    return _norm(" ".join(_paras(sec)))


def _sec_map(spec):
    return {s["label"]: _sec_text(s) for s in spec["sections"]}


def _units(spec):
    return spec.get("units", "sections")


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def question_flowables(spec, with_title_block=False):
    """Rubrica, preguntas (antes del texto, como en el examen) y texto en secciones.
    Con with_title_block=True antepone el bloque de titulo de la hoja."""
    out = []
    labs = _labels(spec)
    if with_title_block:
        out += title_block(f"RDG-P7 · Práctica {spec['num']}", "Multiple matching", spec["subtitle"],
                           f"10 preguntas ({_range(spec)}) · {len(labs)} secciones (A–{labs[-1]}), que pueden "
                           "repetirse · 1 punto por pregunta · tiempo orientativo: 18 minutos · sin consultar la "
                           "teoría")
    u = _units(spec)
    out.append(Paragraph(
        f"You are going to read {spec['intro']}. For questions {_range(spec)}, choose from the {u} "
        f"(<b>A–{labs[-1]}</b>). The {u} may be chosen more than once. Mark your answers on the answer sheet.",
        _rub))
    qs = [Paragraph(spec["lead"], _lead)]
    qs += [Paragraph(it["prompt"], _q, bulletText=str(it["n"])) for it in spec["items"]]
    out.append(KeepTogether(qs + [Spacer(1, 8)]))
    out.append(Paragraph(spec["title"], _ttl))
    if spec.get("standfirst"):
        out.append(Paragraph(spec["standfirst"], _stand))
    for sec in spec["sections"]:
        ps = _paras(sec)
        first = f"<b>{sec['name']}</b><br/>{ps[0]}" if sec.get("name") else ps[0]
        block = [Paragraph(first, _sec, bulletText=sec["label"])]
        block += [Paragraph(x, _sec) for x in ps[1:]]
        out.append(KeepTogether(block))
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    labs = _labels(spec)
    out = [h2(heading), p(
        "Marca una sola letra por pregunta; la misma letra puede repetirse. Al corregir, 1 punto por acierto; los "
        "errores no restan. Anota también el tiempo empleado: el objetivo en el examen son unos 18 minutos.")]
    rows = [["Nº"] + labs + ["Puntos"]]
    for it in spec["items"]:
        rows.append([str(it["n"])] + [f'<font color="#5B6577">{L}</font>' for L in labs]
                    + ["&nbsp;&nbsp;&nbsp;&nbsp;/ 1"])
    rows.append([""] * len(labs) + ['<font name="Sans"><b>Total</b></font>',
                                    f"&nbsp;&nbsp;&nbsp;&nbsp;<b>/ {N_ITEMS}</b>"])
    w = (CONTENT_W / mm - 16 - 34) / len(labs)
    out += table(rows, [16] + [w] * len(labs) + [34], zebra=False, en_cols=tuple(range(1, len(labs) + 1)),
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 9), ("BOTTOMPADDING", (0, 1), (-1, -1), 9),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE")])
    out.append(p("Tiempo empleado: ________ minutos."))
    return out


def _kinds_label(kinds):
    return ", ".join(f"{KINDS[k]}, RDG-P5 §{k}" for k in kinds)


def solutions_flowables(spec, with_band=True, heading=None):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 7 · Multiple matching' dentro de un simulacro)."""
    H = h2 if not heading else h3
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(
        "1 punto por acierto. Cada solución da una línea del texto para cada elemento de la pregunta y, cuando hay "
        "una sección tentadora, explica por qué falla y de qué tipo es (los tipos de distractor de RDG-P5 §7). Los "
        f"demás números de sección remiten a {THEORY_DOC}."))
    out.append(H("Clave rápida"))
    rows = [["Nº", "Clave", "Elementos", "Tentadora", "Teoría"]]
    for it in spec["items"]:
        tr = it.get("trap")
        trs = f"{tr['letter']} · " + ", ".join(KINDS[k] for k in tr["kinds"]) if tr else "—"
        rows.append([str(it["n"]), f"<b>{it['key']}</b>", str(len(it["elements"])), trs,
                     " · ".join("§" + s for s in it["theory"])])
    out += table(rows, [12, 16, 24, 40, 78])
    keys = [it["key"] for it in spec["items"]]
    rep = " · ".join(f"{L} {keys.count(L)}" for L in _labels(spec))
    out.append(p(f"<b>Reparto de claves:</b> {rep}. Cada sección es la respuesta de al menos una pregunta."))
    out.append(H("Explicación por pregunta"))
    names = {s["label"]: s.get("name") for s in spec["sections"]}
    for it in spec["items"]:
        k = it["key"]
        head = f"{it['n']} · {k}" + (f" · {names[k]}" if names.get(k) else "")
        block = [Paragraph(head, _ihead), p(f"<b>Pregunta:</b> {E(spec['lead'] + ' ' + it['prompt'])}")]
        els = it["elements"]
        if len(els) == 1:
            block.append(p(f"<b>En el texto:</b> {markup(els[0])}"))
        else:
            block.append(p(f"<b>Elementos ({len(els)}), cada uno con su línea:</b>"))
            block += [Paragraph(markup(e), _sol, bulletText=f"{i}.") for i, e in enumerate(els, 1)]
        tr = it.get("trap")
        if tr:
            block.append(p(f"<b>Tentadora: {tr['letter']}</b> ({_kinds_label(tr['kinds'])}). {markup(tr['why'])}"))
        block.append(p("<b>Teoría:</b> " + " · ".join(f"§{s} {THEORY[s]}" for s in it["theory"])))
        out.append(KeepTogether(block + [Spacer(1, 4)]))
    return out


def build_sheet(spec, out_path):
    """Hoja de practica completa: preguntas y texto, hoja de respuestas (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"RDG-P7 · Práctica {n}", f"RDG-P7_Practica_{n}.pdf", title=f"RDG-P7 · Práctica {n}")
    return out_path


# ---------- Verificacion ----------
def _content_words(s):
    return {w for w in re.findall(r"[a-z’']+", s.lower()) if len(w) > 3 and w not in STOP}


IRREG_PAST = set("""had was felt found made took gave came saw knew thought became began left lost met said told
went won wrote got kept held heard led learnt spent understood brought bought chose fell forgot grew hid rose sold
sent set struck put let read""".split())
SKIP = {"once", "still", "never", "always", "not", "also", "only", "later", "now"}


def _agreement_error(lead, prompt):
    """Concordancia: 'Which person' + 3.a persona o pasado; 'In which section does the writer' + forma base."""
    words = [w for w in re.findall(r"[a-z’']+", prompt.lower())]
    w = next((x for x in words if not x.endswith("ly") and x not in SKIP), "")
    if re.search(r"\b(does|did|do)\b", lead):
        if (w.endswith("ed") and not w.endswith("eed")) or (w.endswith("s") and not w.endswith(("ss", "us"))):
            return f"tras '{lead}' el verbo va en forma base: «{w}»"
    elif lead.startswith("Which"):
        if w.endswith("ss") or not (w.endswith("s") or w.endswith("ed") or w in IRREG_PAST):
            return f"tras '{lead}' el verbo va en tercera persona o en pasado: «{w}»"
    return None


def _longest_nondecreasing(keys):
    best = cur = 1
    for a, b in zip(keys, keys[1:]):
        cur = cur + 1 if b >= a else 1
        best = max(best, cur)
    return best


def verify(spec):
    """Comprobaciones de formato y coherencia. Devuelve (errores, info)."""
    errs = []
    a = _first(spec)
    expected = list(range(a, a + N_ITEMS))
    items = spec["items"]
    secs = spec.get("sections", [])
    labs = [s.get("label") for s in secs]
    # secciones
    if not SEC_MIN <= len(secs) <= SEC_MAX:
        errs.append(f"número de secciones fuera de {SEC_MIN}–{SEC_MAX}: {len(secs)}")
    if labs != list(LETTERS[:len(secs)]):
        errs.append(f"letras de las secciones {labs}; se esperaban seguidas desde A")
    for f in ("num", "subtitle", "intro", "lead", "title"):
        if not spec.get(f):
            errs.append(f"falta el campo '{f}'")
    if errs:
        return errs, {}
    smap = _sec_map(spec)
    sw = {L: len(t.split()) for L, t in smap.items()}
    words = sum(sw.values())
    if not WORDS_MIN <= words <= WORDS_MAX:
        errs.append(f"longitud del texto fuera de {WORDS_MIN}–{WORDS_MAX} palabras: {words}")
    mean = words / len(secs)
    for L, w in sw.items():
        if not SEC_RATIO[0] * mean <= w <= SEC_RATIO[1] * mean:
            errs.append(f"sección {L} desequilibrada: {w} palabras (media {mean:.0f})")
    for s in secs:
        for x in _paras(s) + [s.get("name", "")]:
            if re.search(r"[\[\]{}<>]", x):
                errs.append(f"marcado en la sección {s['label']}: {x[:40]}…")
    # preguntas
    if [it.get("n") for it in items] != expected:
        errs.append(f"numeración de las preguntas: se esperaban {expected[0]}–{expected[-1]}")
    prompts = [it.get("prompt", "") for it in items]
    if len(set(prompts)) != len(prompts):
        errs.append("enunciados repetidos")
    for it in items:
        n, pr = it.get("n", "?"), it.get("prompt", "")
        if not pr or not pr.endswith("?") or not pr[0].islower():
            errs.append(f"{n}: el enunciado tiene que completar la frase común (minúscula inicial y '?')")
        if re.search(r"[\[\]{}<>]", pr):
            errs.append(f"{n}: marcado en el enunciado")
        agr = _agreement_error(spec.get("lead", ""), pr)
        if agr:
            errs.append(f"{n}: concordancia: {agr}")
        for f in ("key", "elements", "theory"):
            if not it.get(f):
                errs.append(f"{n}: falta el campo '{f}'")
        for s in it.get("theory", []):
            if s not in THEORY:
                errs.append(f"{n}: sección de teoría inexistente §{s}")
    keys = [it.get("key") for it in items]
    if any(k not in labs for k in keys):
        errs.append(f"claves no válidas: {keys}")
        return errs, {}
    # reparto
    cap = math.ceil(N_ITEMS / len(secs)) + 1
    for L in labs:
        c = keys.count(L)
        if c == 0:
            errs.append(f"la sección {L} no es la respuesta de ninguna pregunta")
        if c > cap:
            errs.append(f"la sección {L} es la clave {c} veces (máximo {cap})")
    for i in range(len(keys) - 2):
        if keys[i] == keys[i + 1] == keys[i + 2]:
            errs.append(f"la misma clave tres veces seguidas desde la {expected[i]}")
    run = _longest_nondecreasing(keys)
    if run > MAX_RUN:
        errs.append(f"las claves siguen el orden del texto: racha no decreciente de {run} ({''.join(keys)})")
    # elementos, citas y tentadoras
    used = []
    compound = traps = 0
    for it in items:
        n, k = it["n"], it["key"]
        els = it["elements"]
        if len(els) >= 2:
            compound += 1
        for i, e in enumerate(els, 1):
            cites = [_norm(c) for c in CITE_RE.findall(e)]
            if not cites:
                errs.append(f"{n}: el elemento {i} no cita el texto")
            for c in cites:
                if c not in smap[k]:
                    where = [L for L, t in smap.items() if c in t]
                    errs.append(f"{n}: cita del elemento {i} fuera de la sección clave {k}"
                                f"{' (está en ' + ', '.join(where) + ')' if where else ' (no existe)'}: «{c[:50]}»")
                for m_, c2 in used:
                    if m_ != n and (c in c2 or c2 in c):
                        errs.append(f"{n} y {m_} se apoyan en la misma cita: «{c[:50]}»")
                used.append((n, c))
        tr = it.get("trap")
        if tr:
            traps += 1
            L = tr.get("letter")
            if L not in labs or L == k:
                errs.append(f"{n}: sección tentadora no válida {L}")
                continue
            if not tr.get("kinds") or any(x not in KINDS for x in tr["kinds"]):
                errs.append(f"{n}: tipo de tentadora ausente o desconocido {tr.get('kinds')}")
            cites = [_norm(c) for c in CITE_RE.findall(tr.get("why", ""))]
            if not cites:
                errs.append(f"{n}: la explicación de la tentadora no cita el texto")
            for c in cites:
                if c not in smap[L]:
                    errs.append(f"{n}: cita de la tentadora fuera de la sección {L}: «{c[:50]}»")
        elif len(els) >= 2:
            errs.append(f"{n}: pregunta compuesta sin sección tentadora")
        texts = [("elements", e) for e in els] + ([("trap", tr["why"])] if tr else [])
        for field, t in texts:
            if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(t)):
                errs.append(f"{n}: marcado sin resolver en '{field}'")
    if spec.get("compound") is not None and compound != spec["compound"]:
        errs.append(f"preguntas compuestas: {compound}; consta {spec['compound']}")
    # eco lexico
    echo, trap_echo = [], []
    for it in items:
        pw = _content_words(it["prompt"])
        ov = {L: len(pw & _content_words(t)) for L, t in smap.items()}
        top = max(ov.values())
        if ov[it["key"]] == top and list(ov.values()).count(top) == 1 and top > 0:
            echo.append(it["n"])
        tr = it.get("trap")
        if tr and tr.get("letter") in ov and ov[tr["letter"]] >= ov[it["key"]]:
            trap_echo.append(it["n"])
    if len(echo) > MAX_KEY_ECHO:
        errs.append(f"la clave es la sección con más palabras de la pregunta en {len(echo)} preguntas "
                    f"(máximo {MAX_KEY_ECHO}): {echo}")
    info = {"words": words, "secs": len(secs), "sec_words": sw, "keys": "".join(keys),
            "share": {L: keys.count(L) for L in labs}, "compound": compound, "traps": traps, "echo": echo,
            "trap_echo": trap_echo, "run": run}
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
    return re.findall(r"\{\{|\}\}|\[\[|\]\]|<font|</?b>|</?i>|<br|&nbsp", txt)


def make(spec, out_dir="/mnt/user-data/outputs"):
    """Verifica, genera y comprueba el PDF. Devuelve la ruta; lanza ValueError si algo falla."""
    errs, info = verify(spec)
    if errs:
        raise ValueError(f"Hoja {spec.get('num')}:\n  - " + "\n  - ".join(errs))
    path = build_sheet(spec, os.path.join(out_dir, f"RDG-P7_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    share = " ".join(f"{L}{c}" for L, c in info["share"].items())
    print(f"RDG-P7_Practica_{spec['num']}.pdf · {info['words']} palabras en {info['secs']} secciones "
          f"({', '.join(str(w) for w in info['sec_words'].values())}) · claves {info['keys']} ({share}) · "
          f"{info['compound']} compuestas · {info['traps']} tentadoras "
          f"(con tanto eco como la clave o más en {info['trap_echo'] or 'ninguna'}) · "
          f"clave con más eco en {info['echo'] or 'ninguna'} · verificación sin errores")
    return path


# ---------- Hoja de ejemplo (contenido de RDG-P7_Practica_01, numerada como 99) ----------
DEMO = {'num': '99',
 'subtitle': 'Hoja de prueba del generador (contenido de RDG-P7_Practica_01)',
 'intro': 'an article in which four novelists talk about writing their second book',
 'units': 'novelists',
 'lead': 'Which novelist',
 'title': 'The difficult second book',
 'standfirst': 'Four writers look back on what happened after a successful debut.',
 'compound': 3,
 'sections': [{'label': 'A',
               'name': 'Clare Hollis',
               'text': 'When my first novel won a prize I had never expected even to be considered for, I was '
                       'convinced that I had about eighteen months before the world forgot my name. My agent, who '
                       'had seen this happen before, urged me to take a year off: to travel, to read, to do '
                       'anything but write. I ignored her and started the next book the following Monday. It was a '
                       'mistake, and one I would undo if I could. I spent a year producing two hundred pages that '
                       'were competent, airless and entirely without purpose, and in the end I threw every one of '
                       'them away. Looking back, I also think I took the prize far too much to heart. The judges '
                       'liked the book, certainly, but it came out in a thin year for debuts, and against stronger '
                       'competition it might well have sunk without trace. Knowing that has made me a good deal '
                       'calmer about whatever comes next. The second novel, when it finally came, took three '
                       'unhurried years and was the better for it.'},
              {'label': 'B',
               'name': 'Tomasz Brenner',
               'text': 'Journalists love the idea of the ‘difficult second novel’, and every interviewer asks me '
                       'about it. I think it is largely a myth, or at least a story that tells us more about the '
                       'publishing calendar than about writing. My second book was, if anything, easier than the '
                       'first. I had learned how long a novel takes, where it is likely to stall and what to do '
                       'when it does, and I no longer had to wonder whether I could finish one at all. Whatever '
                       'pressure I felt came from my bank manager rather than from my readers. The book that '
                       'nearly defeated me was the third, which I rewrote from scratch twice and which still feels '
                       'to me like a house with the scaffolding left up. The second was reviewed less kindly than '
                       'my debut; one critic said it read like the work of a man in a hurry. For a while I took '
                       'comments like that to heart. These days I leave reviews unread, not out of pride but '
                       'because I noticed that I had started writing for the critics rather than for my readers.'},
              {'label': 'C',
               'name': 'Ade Mensah',
               'text': 'My first novel came out when I was twenty-six, and for two years afterwards readers wrote '
                       'to ask when the next one would appear. Every letter was kind, and every letter added a '
                       'little to the weight I carried into my study each morning. The second book took seven '
                       'years. For long stretches of them I wrote nothing but short stories, which asked nothing '
                       'of me and which nobody was waiting for, and they were the only writing I enjoyed in that '
                       'period. Friends assumed I had given up writing altogether, and for a while I let them '
                       'think so. When I finally delivered a draft of the novel, my editor told me, very gently, '
                       'that I had chosen the wrong narrator: the story belonged to his sister. I rewrote it from '
                       'her point of view, a decision I have never regretted, and whatever is good in the finished '
                       'book I owe to that conversation. It was by far the hardest thing I have written, and it '
                       'remains the book I am proudest of.'},
              {'label': 'D',
               'name': 'Fiona Lockhart',
               'text': 'It is often said that first novels are disguised autobiography, and in my case that was '
                       'simply true: almost everything in my debut had happened to me or to someone I knew. When I '
                       'sat down to write the second, I found I had used my own life up; there was nothing left in '
                       'it that I could bear to put on the page. The new book was set in a Victorian shipyard, and '
                       'it demanded research, which I put off for months, telling myself that real novelists '
                       'invent rather than look things up. In the end I had no choice, and to my astonishment I '
                       'loved it: the archives, the old trade directories, the ledgers of a long-closed yard, '
                       'which handed me the novel’s best scene. Money was tight, since my advance had been modest, '
                       'so I took on book reviewing for a newspaper to pay the bills. I still read every review of '
                       'my own work, which my husband finds baffling. It is, I think, the better of my two books, '
                       'though I doubt that many readers would agree.'}],
 'lex': ['sink without trace',
         'take sth to heart',
         'if anything',
         'with the scaffolding left up',
         'airless (figurado)',
         'put sth off',
         'pay the bills',
         'use sth up',
         'owe sth to sb'],
 'items': [{'n': 44,
            'prompt': 'rejects a widely held assumption about second novels?',
            'key': 'B',
            'theory': ['3.3', '5.1'],
            'elements': ['La idea extendida la recoge ({{Journalists love the idea of the ‘difficult second '
                         'novel’}}) y la rechaza: {{I think it is largely a myth}}.'],
            'trap': {'letter': 'D',
                     'kinds': ['7.6'],
                     'why': 'También parte de una idea extendida sobre las primeras novelas ({{It is often said '
                            'that first novels are disguised autobiography}}), pero para darle la razón: {{in my '
                            'case that was simply true}}.'}},
           {'n': 45,
            'prompt': 'suggests that their early success owed something to circumstances?',
            'key': 'A',
            'theory': ['3.3', '4.2'],
            'elements': ['{{it came out in a thin year for debuts, and against stronger competition it might well '
                         'have sunk without trace}}. El grado coincide con [[owed something]]: el libro tenía '
                         'mérito ({{The judges liked the book, certainly}}), pero el momento ayudó.']},
           {'n': 46,
            'prompt': 'credits another person with improving the second book?',
            'key': 'C',
            'theory': ['3.3', '4.3'],
            'elements': ['{{my editor told me, very gently, that I had chosen the wrong narrator}}; {{whatever is '
                         'good in the finished book I owe to that conversation}}.'],
            'trap': {'letter': 'A',
                     'kinds': ['7.2'],
                     'why': 'Aparece otra persona con un consejo ({{My agent, who had seen this happen before, '
                            'urged me to take a year off}}), pero Hollis no lo siguió, así que no mejoró nada del '
                            'libro.'}},
           {'n': 47,
            'prompt': 'describes a decision that they now regret?',
            'key': 'A',
            'theory': ['4.1', '3.4'],
            'elements': ['Decisión: {{I ignored her and started the next book the following Monday}}.',
                         'Arrepentimiento actual: {{It was a mistake, and one I would undo if I could}}.'],
            'trap': {'letter': 'C',
                     'kinds': ['7.6'],
                     'why': 'Hay una decisión (reescribir la novela con otro narrador), pero con la polaridad '
                            'contraria: {{a decision I have never regretted}}. Cumple el primer elemento y niega '
                            'el segundo.'}},
           {'n': 48,
            'prompt': 'had exhausted their own experience as a source of material?',
            'key': 'D',
            'theory': ['3.3', '4.3'],
            'elements': ['{{I found I had used my own life up}}; {{there was nothing left in it that I could bear '
                         'to put on the page}}.'],
            'trap': {'letter': 'A',
                     'kinds': ['7.7'],
                     'why': 'Sus primeras páginas fracasaron ({{two hundred pages that were competent, airless and '
                            'entirely without purpose}}), pero no dice que se le acabara el material: lo atribuye '
                            'a haber empezado demasiado pronto. Hay que suponer la causa.'}},
           {'n': 49,
            'prompt': 'has stopped paying attention to what critics say?',
            'key': 'B',
            'theory': ['3.4', '4.2'],
            'elements': ['Antes sí ({{For a while I took comments like that to heart}}); ahora no: {{These days I '
                         'leave reviews unread}}.'],
            'trap': {'letter': 'D',
                     'kinds': ['7.1'],
                     'why': 'Habla de reseñas, pero para decir lo contrario: {{I still read every review of my own '
                            'work}}.'}},
           {'n': 50,
            'prompt': 'unexpectedly enjoyed a task they had been avoiding?',
            'key': 'D',
            'theory': ['4.1', '3.3'],
            'elements': ['Tarea evitada: {{it demanded research, which I put off for months}}.',
                         'Disfrute inesperado: {{to my astonishment I loved it}}.'],
            'trap': {'letter': 'C',
                     'kinds': ['7.5'],
                     'why': 'Los dos elementos están, pero no recaen sobre la misma tarea: lo que evitaba era la '
                            'novela, y lo que disfrutaba, los cuentos ({{they were the only writing I enjoyed in '
                            'that period}}).'}},
           {'n': 51,
            'prompt': 'found relief from the novel in another kind of writing?',
            'key': 'C',
            'theory': ['4.1', '4.3'],
            'elements': ['Otro tipo de escritura: {{I wrote nothing but short stories}}.',
                         'Como alivio: {{which asked nothing of me and which nobody was waiting for}}.'],
            'trap': {'letter': 'D',
                     'kinds': ['7.6'],
                     'why': 'También escribe otra cosa, pero por dinero, no como alivio: {{I took on book '
                            'reviewing for a newspaper to pay the bills}}.'}},
           {'n': 52,
            'prompt': 'found a later book more demanding than the second?',
            'key': 'B',
            'theory': ['4.3', '4.2'],
            'elements': ['{{The book that nearly defeated me was the third}}; además, {{My second book was, if '
                         'anything, easier than the first}}.'],
            'trap': {'letter': 'C',
                     'kinds': ['7.1'],
                     'why': 'Habla de dificultad, pero de la segunda novela, y en grado máximo: {{It was by far '
                            'the hardest thing I have written}}. Ningún libro posterior la supera.'}},
           {'n': 53,
            'prompt': 'feared that their reputation would not last?',
            'key': 'A',
            'theory': ['3.3'],
            'elements': ['{{I was convinced that I had about eighteen months before the world forgot my name}}.'],
            'trap': {'letter': 'C',
                     'kinds': ['7.2'],
                     'why': 'Siente presión, pero por las expectativas de los lectores, no por miedo a que lo '
                            'olviden: {{every letter added a little to the weight I carried into my study each '
                            'morning}}.'}}]}

if __name__ == "__main__":
    import runpy
    if len(sys.argv) < 2:
        print("Uso: python3 gen_RDG-P7.py --demo | mis_hojas.py [carpeta_salida]")
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
