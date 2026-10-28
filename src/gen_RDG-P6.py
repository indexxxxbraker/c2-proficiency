# gen_RDG-P6.py · Generador de Reading Part 6 (gapped text) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa: texto base con 7 huecos (37-43), parrafos A-H (uno sobrante), hoja de
#     respuestas y soluciones (que une cada parrafo con lo de antes y con lo de despues, el parrafo tentador
#     cuando lo hay y por que el sobrante no entra en ningun hueco).
#   - Bloques sueltos para insertar la Part 6 en un simulacro (SIM): enunciado, hoja de respuestas y
#     soluciones por separado.
#   - Verificacion automatica antes y despues de generar el PDF.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_RDG-P6.py --demo [carpeta_salida]          -> hoja de ejemplo (la 01, numerada como 99)
#   python3 gen_RDG-P6.py mis_hojas.py [carpeta_salida]   -> mis_hojas.py define SPECS = [spec, ...]
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_p6", "/ruta/gen_RDG-P6.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, info = gen.verify(spec)
#   gen.make(spec, "/mnt/user-data/outputs")
#   story += gen.question_flowables(spec)          # para un SIM
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num         "03"
#   subtitle    "Hoja 03 · Ensayo argumentativo · dificultad 3 de 4"      (espanol)
#   intro       "an extract from a magazine article about…"  completa la rubrica: "You are going to read …"
#   title       titulo del texto (ingles)
#   standfirst  entradilla opcional (ingles)
#   text        lista en orden: parrafos del texto base (str) y huecos (int), p. ej.
#               ["parrafo", 37, "parrafo", 38, …, 43, "parrafo"]. Empieza y termina con parrafo; dos huecos
#               nunca van seguidos. Ingles britanico; 600-720 palabras en total.
#   paragraphs  {"A": "...", …, "H": "..."}: los 7 parrafos que faltan y el sobrante, 40-70 palabras cada uno
#   lex         lexico para el modulo LEX (no se imprime; se usa en el resumen de cierre)
#   items       7 diccionarios, en orden:
#     n         37
#     key       "F"
#     before    enlace con lo anterior: al menos una cita {{…}} del parrafo clave y otra del texto anterior
#     after     enlace con lo siguiente: al menos una cita {{…}} del parrafo clave y otra del texto posterior
#     trap      opcional: {"letter": "H", "why": "… {{cita}} …"}  parrafo tentador y por que falla
#     theory    secciones de RDG-P6_Teoria_v1 (ver THEORY)
#   extra       {"letter": "D", "rules_out": [{"gaps": [37], "why": "… {{cita}} …"}, …], "theory": ["5.1"]}
#               los grupos de rules_out tienen que cubrir los 7 huecos
#
#   Marcado en before / after / why (y en cualquier texto en espanol):
#     {{texto}}   -> cita literal del texto o de un parrafo, en serif; se comprueba que existe tal cual
#     [[texto]]   -> ingles en serif sin comprobar
#     [[!TEXTO]]  -> ingles en serif y negrita
#   "Texto anterior" a un hueco = parrafos base anteriores y parrafos clave de los huecos anteriores;
#   "texto posterior", lo mismo hacia delante.
#
# QUE COMPRUEBA verify()
#   numeracion 37-43 en el texto y en la clave · texto que empieza y termina con parrafo, sin huecos
#   seguidos · ocho parrafos A-H, siete claves distintas y el sobrante · longitud del texto base y de cada
#   parrafo · citas literales y en el lado correcto de cada enlace · parrafo tentador valido · el sobrante
#   descartado en los 7 huecos con cita · claves sin series alfabeticas · la clave no es el parrafo con mas
#   vocabulario en comun con sus vecinos en mas de 3 huecos · el sobrante comparte vocabulario con el texto ·
#   secciones de teoria existentes · marcado sin resolver.
#
# LO QUE EL GENERADOR NO PUEDE COMPROBAR (a mano)
#   - Que cada hueco tenga un solo parrafo defendible y que el sobrante no encaje en ninguno.
#   - Que los datos reales del texto sean ciertos; ingles britanico; registro C2; dificultad graduada.
#   - Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY.

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
from reportlab.lib.enums import TA_CENTER  # noqa: E402

VERSION = "1"
FIRST_ITEM = 37
N_ITEMS = 7
LETTERS = "ABCDEFGH"
BASE_MIN, BASE_MAX = 600, 720
PARA_MIN, PARA_MAX = 40, 70
MAX_KEY_ECHO = 3
THEORY_DOC = "RDG-P6_Teoria_v1"

THEORY = {
    "1.1": "La tarea", "1.2": "Qué cambia respecto al C1",
    "2.1": "Primera lectura del texto base", "2.2": "Ficha de cada párrafo", "2.3": "Doble encaje",
    "2.4": "Comprobación final y tiempo",
    "3.1": "Hilo narrativo", "3.2": "Hilo argumentativo", "3.3": "Textos mixtos", "3.4": "Progresión temática",
    "4.1": "Pistas hacia atrás", "4.2": "Pistas hacia delante", "4.3": "Conectores y adverbios de frase",
    "4.4": "Cadenas léxicas", "4.5": "Tiempo verbal y voz",
    "5.1": "Cómo se fabrica el sobrante", "5.2": "Trampas de encaje", "5.3": "Tabla de repaso",
    "6": "Caso completo",
}

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


def EI(s):
    return f'<font name="EN"><i>{s}</i></font>'


def markup(s):
    """{{cita}} y [[x]] -> E(x); [[!X]] -> EB(X)."""
    s = CITE_RE.sub(lambda m: E(m.group(1)), s)
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)


def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


# ---------- Estilos propios de la hoja (sobre la plantilla, sin cambiarla) ----------
_rub = ParagraphStyle("p6_rubric", parent=S["en"], fontSize=10, leading=14)
_ttl = ParagraphStyle("p6_title", parent=S["en"], fontName="EN-B", fontSize=13, leading=17, textColor=NAVY,
                      spaceBefore=4, spaceAfter=3)
_stand = ParagraphStyle("p6_stand", parent=S["en"], fontName="EN-I", textColor=GREY, spaceAfter=9)
_txt = ParagraphStyle("p6_txt", parent=S["en"], leading=15.4, spaceAfter=7.5)
_gap = ParagraphStyle("p6_gap", parent=S["en"], fontName="EN-B", alignment=TA_CENTER, textColor=ACCENT,
                      spaceBefore=2, spaceAfter=9)
_opt = ParagraphStyle("p6_opt", parent=_txt, leftIndent=20, bulletIndent=0, bulletFontName="EN-B",
                      bulletFontSize=11, spaceAfter=9)
_ihead = ParagraphStyle("p6_ihead", parent=S["h3"], fontName="Sans-B", fontSize=10.5, textColor=NAVY,
                        spaceBefore=6)


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _range(spec):
    a = _first(spec)
    return f"{a}–{a + N_ITEMS - 1}"


def _base(spec):
    return [x for x in spec["text"] if isinstance(x, str)]


def _opening(txt, n=7):
    """Primeras palabras de un parrafo; si la primera frase acaba antes, la frase entera."""
    w = txt.split()
    for i, x in enumerate(w[:n]):
        if i >= 2 and x.endswith((".", "?", "!")):
            return " ".join(w[:i + 1])
    if len(w) <= n:
        return txt
    return " ".join(w[:n]).rstrip(".,;:") + "…"


def _gaps_label(gaps):
    g = sorted(gaps)
    if len(g) == 1:
        return f"Hueco {g[0]}"
    if g == list(range(g[0], g[-1] + 1)) and len(g) > 2:
        return f"Huecos {g[0]}–{g[-1]}"
    return "Huecos " + ", ".join(str(x) for x in g[:-1]) + f" y {g[-1]}"


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def question_flowables(spec, with_title_block=False):
    """Rubrica, texto con huecos y parrafos A-H. Con with_title_block=True antepone el bloque de titulo."""
    out = []
    if with_title_block:
        out += title_block(f"RDG-P6 · Práctica {spec['num']}", "Gapped text", spec["subtitle"],
                           f"7 huecos ({_range(spec)}) · 8 párrafos (A–H), uno sobrante · 2 puntos por hueco · "
                           "tiempo orientativo: 18 minutos · sin consultar la teoría")
    out.append(Paragraph(
        f"You are going to read {spec['intro']}. Seven paragraphs have been removed from the extract. Choose "
        f"from the paragraphs <b>A–H</b> the one which fits each gap ({_range(spec)}). There is one extra "
        "paragraph which you do not need to use. Mark your answers on the answer sheet.", _rub))
    out += [Spacer(1, 4), Paragraph(spec["title"], _ttl)]
    if spec.get("standfirst"):
        out.append(Paragraph(spec["standfirst"], _stand))
    for x in spec["text"]:
        if isinstance(x, str):
            out.append(Paragraph(x, _txt))
        else:
            out.append(Paragraph(f"{x}&nbsp;&nbsp;______________________", _gap))
    opts = [Paragraph(spec["paragraphs"][L], _opt, bulletText=L) for L in LETTERS]
    out.append(KeepTogether([Spacer(1, 8)] + opts))  # los ocho parrafos siempre juntos
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    out = [h2(heading), p(
        "Marca una sola letra por hueco; cada letra se usa una vez como máximo. Al corregir, 2 puntos por "
        "acierto; los errores no restan. Anota también el tiempo empleado: el objetivo en el examen son unos "
        "18 minutos.")]
    rows = [["Nº"] + list(LETTERS) + ["Puntos"]]
    for it in spec["items"]:
        rows.append([str(it["n"])] + [f'<font color="#5B6577">{L}</font>' for L in LETTERS]
                    + ["&nbsp;&nbsp;&nbsp;&nbsp;/ 2"])
    rows.append([""] * 7 + ['<font name="Sans"><b>Total</b></font>', "", f"&nbsp;&nbsp;&nbsp;&nbsp;<b>/ {2 * N_ITEMS}</b>"])
    out += table(rows, [16] + [14] * 8 + [42], zebra=False, en_cols=tuple(range(1, 9)),
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 10), ("BOTTOMPADDING", (0, 1), (-1, -1), 10),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
                        ("SPAN", (7, -1), (8, -1))])
    out.append(p("Párrafo sobrante: ________ (no puntúa; sirve para comprobar). "
                 "Tiempo empleado: ________ minutos."))
    return out


def solutions_flowables(spec, with_band=True, heading=None):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 6 · Gapped text' dentro de un simulacro)."""
    H = h2 if not heading else h3
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p(
        "2 puntos por acierto. Cada solución explica qué une el párrafo con lo de antes (←) y con lo de después "
        "(→), con citas de los dos lados; cuando hay un párrafo tentador, por qué falla; y, al final, por qué "
        f"el sobrante no entra en ningún hueco. Los números de sección remiten a {THEORY_DOC}."))
    out.append(H("Clave rápida"))
    rows = [["Nº", "Clave", "Empieza", "Teoría"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), f"<b>{it['key']}</b>", _opening(spec["paragraphs"][it["key"]]),
                     " · ".join("§" + s for s in it["theory"])])
    x = spec["extra"]
    rows.append(["—", f"<b>{x['letter']}</b>",
                 _opening(spec["paragraphs"][x["letter"]]) + ' <font name="Sans-I">(sobrante)</font>',
                 " · ".join("§" + s for s in x.get("theory", ["5.1"]))])
    out += table(rows, [12, 14, 100, 44], en_cols=(2,))
    out.append(H("Explicación por hueco"))
    for it in spec["items"]:
        L = it["key"]
        head = [Paragraph(f"{it['n']} · {L} · " + EI(_opening(spec["paragraphs"][L], 9)), _ihead),
                p("<b>← Con lo anterior.</b> " + markup(it["before"]))]
        out.append(KeepTogether(head))  # el encabezado nunca queda solo al pie de una pagina
        out.append(p("<b>→ Con lo siguiente.</b> " + markup(it["after"])))
        if it.get("trap"):
            out.append(p(f"<b>Tentador: {it['trap']['letter']}.</b> " + markup(it["trap"]["why"])))
        out.append(p("<b>Teoría:</b> " + " · ".join(f"§{s} {THEORY[s]}" for s in it["theory"])))
        out.append(Spacer(1, 4))
    block = [H("El párrafo sobrante"),
             Paragraph(f"{x['letter']} · " + EI(_opening(spec["paragraphs"][x["letter"]], 9)), _ihead)]
    block += bullets([f"<b>{_gaps_label(r['gaps'])}.</b> " + markup(r["why"]) for r in x["rules_out"]])
    block.append(p("<b>Teoría:</b> " + " · ".join(f"§{s} {THEORY[s]}" for s in x.get("theory", ["5.1"]))))
    out.append(KeepTogether(block))
    return out


def build_sheet(spec, out_path):
    """Hoja de practica completa: texto y parrafos, hoja de respuestas (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"RDG-P6 · Práctica {n}", f"RDG-P6_Practica_{n}.pdf", title=f"RDG-P6 · Práctica {n}")
    return out_path


# ---------- Verificacion ----------
def _content_words(s):
    return {w for w in re.findall(r"[a-z’']+", s.lower()) if len(w) > 3 and w not in STOP}


def _scopes(spec):
    """Para cada hueco: (texto anterior, parrafo base inmediatamente anterior, texto posterior,
    parrafo base inmediatamente posterior). El texto anterior/posterior incluye las claves ya colocadas."""
    keys = {it["n"]: it["key"] for it in spec["items"]}
    seq = [x if isinstance(x, str) else spec["paragraphs"].get(keys.get(x), "") for x in spec["text"]]
    out = {}
    for i, x in enumerate(spec["text"]):
        if isinstance(x, int):
            prev_base = spec["text"][i - 1] if i > 0 and isinstance(spec["text"][i - 1], str) else ""
            next_base = spec["text"][i + 1] if i + 1 < len(spec["text"]) and isinstance(spec["text"][i + 1], str) else ""
            out[x] = (_norm(" ".join(seq[:i])), prev_base, _norm(" ".join(seq[i + 1:])), next_base)
    return out


def verify(spec):
    """Comprobaciones de formato y coherencia. Devuelve (errores, info)."""
    errs = []
    a = _first(spec)
    expected = list(range(a, a + N_ITEMS))
    text = spec["text"]
    paras = spec.get("paragraphs", {})
    items = spec["items"]
    # estructura del texto
    gaps = [x for x in text if isinstance(x, int)]
    if gaps != expected:
        errs.append(f"huecos del texto: {gaps}; se esperaban {expected}")
    if not text or not isinstance(text[0], str) or not isinstance(text[-1], str):
        errs.append("el texto base tiene que empezar y terminar con un párrafo")
    for i in range(len(text) - 1):
        if isinstance(text[i], int) and isinstance(text[i + 1], int):
            errs.append(f"huecos seguidos: {text[i]} y {text[i + 1]}")
    if [it.get("n") for it in items] != expected:
        errs.append(f"ítems de la clave: se esperaban {expected}")
    base_words = len(_norm(" ".join(_base(spec))).split())
    if not BASE_MIN <= base_words <= BASE_MAX:
        errs.append(f"texto base fuera de {BASE_MIN}–{BASE_MAX} palabras: {base_words}")
    if sorted(paras) != list(LETTERS):
        errs.append(f"párrafos {sorted(paras)}; se esperaban A–H")
    pw = {L: len(_norm(t).split()) for L, t in paras.items()}
    for L, w in pw.items():
        if not PARA_MIN <= w <= PARA_MAX:
            errs.append(f"párrafo {L} fuera de {PARA_MIN}–{PARA_MAX} palabras: {w}")
    for x in _base(spec) + list(paras.values()):
        if re.search(r"[\[\]{}<>]", x):
            errs.append(f"marcado en el texto: {x[:40]}…")
    # claves y sobrante
    keys = [it.get("key") for it in items]
    if any(k not in LETTERS for k in keys):
        errs.append(f"claves no válidas: {keys}")
    if len(set(keys)) != len(keys):
        errs.append(f"claves repetidas: {keys}")
    extra = spec.get("extra", {})
    rest = set(LETTERS) - set(keys)
    if len(rest) != 1 or extra.get("letter") not in rest:
        errs.append(f"sobrante: se esperaba {sorted(rest)}, consta {extra.get('letter')}")
    asc = [i for i in range(len(keys) - 1) if keys[i] in LETTERS and keys[i + 1] in LETTERS
           and ord(keys[i + 1]) == ord(keys[i]) + 1]
    if len(asc) > 2 or any(i + 1 in asc for i in asc):
        errs.append(f"las claves forman series alfabéticas: {''.join(k or '?' for k in keys)}")
    if errs:
        return errs, {}
    full = _norm(" ".join(_base(spec) + list(paras.values())))
    scopes = _scopes(spec)
    # enlaces de cada hueco
    for it in items:
        n, kp = it["n"], _norm(paras[it["key"]])
        before_all, _, after_all, _ = scopes[n]
        for field in ("before", "after", "theory"):
            if not it.get(field):
                errs.append(f"{n}: falta el campo '{field}'")
        for s in it.get("theory", []):
            if s not in THEORY:
                errs.append(f"{n}: sección de teoría inexistente §{s}")
        for field, other, side in (("before", before_all, "anterior"), ("after", after_all, "posterior")):
            cites = [_norm(c) for c in CITE_RE.findall(it.get(field, ""))]
            for c in cites:
                if c not in full:
                    errs.append(f"{n} ({field}): cita inexistente «{c}»")
            if not any(c in kp for c in cites):
                errs.append(f"{n} ({field}): no cita el párrafo clave {it['key']}")
            if not any(c in other for c in cites):
                errs.append(f"{n} ({field}): no cita el texto {side} al hueco")
        tr = it.get("trap")
        if tr:
            if tr.get("letter") not in LETTERS or tr.get("letter") == it["key"]:
                errs.append(f"{n}: párrafo tentador no válido {tr.get('letter')}")
            cites = [_norm(c) for c in CITE_RE.findall(tr.get("why", ""))]
            if not cites:
                errs.append(f"{n}: la explicación del párrafo tentador no cita el texto")
            for c in cites:
                if c not in full:
                    errs.append(f"{n} (tentador): cita inexistente «{c}»")
    # sobrante
    covered = set()
    for r in extra.get("rules_out", []):
        g = set(r.get("gaps", []))
        if not g or not g <= set(expected):
            errs.append(f"sobrante: grupo de huecos no válido {r.get('gaps')}")
        covered |= g
        cites = [_norm(c) for c in CITE_RE.findall(r.get("why", ""))]
        if not cites:
            errs.append(f"sobrante ({_gaps_label(g)}): la explicación no cita el texto")
        for c in cites:
            if c not in full:
                errs.append(f"sobrante: cita inexistente «{c}»")
    if covered != set(expected):
        errs.append(f"el sobrante no se descarta en los huecos {sorted(set(expected) - covered)}")
    for s in extra.get("theory", []):
        if s not in THEORY:
            errs.append(f"sobrante: sección de teoría inexistente §{s}")
    # marcado sin resolver
    texts = [(f"{it['n']} {f}", it.get(f, "")) for it in items for f in ("before", "after")]
    texts += [(f"{it['n']} tentador", it["trap"]["why"]) for it in items if it.get("trap")]
    texts += [("sobrante", r.get("why", "")) for r in extra.get("rules_out", [])]
    for where, t in texts:
        if re.search(r"\{\{|\}\}|\[\[|\]\]", markup(t)):
            errs.append(f"{where}: marcado sin resolver")
    # eco lexico: la clave no debe ser, en mas de MAX_KEY_ECHO huecos, el parrafo con mas vocabulario comun
    echo = []
    for it in items:
        _, prev_b, _, next_b = scopes[it["n"]]
        nb = _content_words(prev_b + " " + next_b)
        ov = {L: len(_content_words(paras[L]) & nb) for L in LETTERS}
        top = max(ov.values())
        if ov[it["key"]] == top and list(ov.values()).count(top) == 1:
            echo.append(it["n"])
    if len(echo) > MAX_KEY_ECHO:
        errs.append(f"la clave es el párrafo con más vocabulario en común con sus vecinos en {len(echo)} "
                    f"huecos (máximo {MAX_KEY_ECHO}): {echo}")
    # el sobrante tiene que compartir vocabulario con el texto (verosimil)
    bw = _content_words(" ".join(_base(spec)))
    share = {L: len(_content_words(paras[L]) & bw) for L in LETTERS}
    rank = sorted(share.values(), reverse=True).index(share[extra["letter"]]) + 1
    if share[extra["letter"]] < min(share[k] for k in keys):
        errs.append(f"sobrante poco verosímil: comparte menos vocabulario con el texto que cualquier clave "
                    f"({share[extra['letter']]})")
    info = {"base": base_words, "paras": f"{min(pw.values())}–{max(pw.values())}", "keys": "".join(keys),
            "extra": extra["letter"], "echo": echo, "extra_rank": rank}
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
    path = build_sheet(spec, os.path.join(out_dir, f"RDG-P6_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    print(f"RDG-P6_Practica_{spec['num']}.pdf · texto base {info['base']} palabras · párrafos {info['paras']} · "
          f"claves {info['keys']} · sobrante {info['extra']} (puesto {info['extra_rank']} de 8 en léxico común) · "
          f"clave con más eco léxico en {info['echo'] or 'ninguno'} · verificación sin errores")
    return path


# ---------- Hoja de ejemplo (contenido de RDG-P6_Practica_01, numerada como 99) ----------
DEMO = {
    "num": "99",
    "subtitle": "Hoja de prueba del generador (contenido de RDG-P6_Practica_01)",
    "intro": "an extract from a magazine article about a lighthouse",
    "title": "The rock that ate lighthouses",
    "standfirst": "For more than three centuries, a reef off Plymouth has been the proving ground of British "
                  "lighthouse engineering.",
    "text": [
        "Some fourteen miles south-west of Plymouth, a ragged line of rocks breaks the surface of the English "
        "Channel. At high water the Eddystone reef all but disappears, and for centuries ships making for the "
        "shelter of Plymouth Sound discovered it only when they struck it. By the end of the seventeenth century, "
        "with trade through the port growing year by year, the case for a light on the reef was obvious to "
        "everyone. What nobody could supply was a way of building one on a rock that the sea swept clean in "
        "every winter gale.",
        37,
        "Progress was painfully slow. Work was possible only in the summer months, and only on days calm enough "
        "to land, so that the first season’s labour amounted to little more than twelve holes drilled into the "
        "rock to anchor the foundations. In 1697 a French privateer seized Winstanley at the site and carried "
        "him off to France, where Louis XIV ordered his release, reportedly remarking that France was at war "
        "with England, not with humanity. By November 1698 a light was burning on the reef for the first time.",
        38,
        "So confident was Winstanley in the rebuilt tower that he is said to have wished to be inside it during "
        "‘the greatest storm that ever was’. In November 1703 he had his wish. He had gone out to the reef to "
        "supervise repairs when the worst storm in recorded British history swept in from the Atlantic. When it "
        "had passed, nothing remained on the rock but a few twisted iron stumps. Of Winstanley and the men with "
        "him, no trace was ever found.",
        39,
        "Simplicity served it well against the water. For almost half a century the cone stood unmoved through "
        "every winter the Channel could throw at it. Its weakness lay elsewhere. On a December night in 1755 "
        "the keeper on watch found the lantern in flames, and since every drop of water had to be hauled up "
        "from the sea in buckets, the three men on the rock could do little but retreat down the tower as the "
        "fire followed them.",
        40,
        "Hall’s ordeal made him briefly famous, but it was the loss of a second tower in little more than fifty "
        "years that alarmed the lighthouse’s owners. On the advice of the Royal Society, the commission went to "
        "John Smeaton, a maker of scientific instruments from Leeds who had never built anything in the sea. "
        "Smeaton began not with the tower but with the problem, and found his answer in the shape of an oak: "
        "broad at the base and tapering upwards, the form that lets a tree stand through gales that bring down "
        "buildings.",
        41,
        "It was the shape and the dovetailing together that made Smeaton’s tower so hard to shift. Within "
        "decades it had become the model for rock lighthouses around the world, and its designer is often "
        "described as the father of civil engineering. Yet when the tower finally had to go, the fault was not "
        "its own. In the 1870s inspectors found that the rock beneath it was being worn away, so that every "
        "large wave set the whole structure trembling.",
        42,
        "Its predecessor was not simply left to the waves. The upper part of Smeaton’s tower was taken down "
        "stone by stone and rebuilt on Plymouth Hoe, where it still stands as a memorial, painted in red and "
        "white bands. The lower courses proved too solid to remove and were left where they were. They can "
        "still be seen beside the newer tower, a stump of granite that has outlasted every storm since 1759.",
        43,
        "Winstanley, whose first season on the reef produced twelve holes in the rock, would have recognised "
        "that proviso. Three centuries of engineering have changed almost everything about the Eddystone light "
        "except the conditions in which it has to be built and kept. Each of its four towers was, in its way, "
        "an argument about how to survive them, and the approach that won was the plainest: give the waves as "
        "little as possible to hold on to, and let the weight of stone do the rest.",
    ],
    "paragraphs": {
        "A": "The oldest of them, Henry Hall, was ninety-four. As he stood throwing water up at the blaze, molten "
             "lead from the lantern roof poured down onto his upturned face and, he insisted afterwards, into "
             "his open mouth. The doctor who treated him ashore did not believe a word of it. Hall died twelve "
             "days later, and the post-mortem found a flat lump of lead in his stomach.",
        "B": "The remedy was to start again on a neighbouring rock. The new tower, designed by James Douglass, "
             "engineer-in-chief of Trinity House, was more than twice as tall as Smeaton’s and was completed in "
             "1882. Yet it owed almost everything to the older design: the curving profile, the dovetailed granite "
             "and the solid stone of its lower courses.",
        "C": "It did not burn for long without trouble. Over its first winter the waves broke so high that the "
             "lantern was often buried in spray, and its light lost to the very ships it was meant to warn. "
             "Winstanley’s answer was characteristically extravagant. He enlarged the whole structure, raising "
             "it higher and adding galleries, a crane and a profusion of ornamental ironwork.",
        "D": "Winstanley lost no time in turning his achievement to account. He engraved a detailed picture of "
             "the finished tower, ornate galleries and all, and copies circulated widely among people who would "
             "never see the reef. For a few years the lighthouse was almost as famous as the eccentric who had "
             "built it.",
        "E": "He was equally original in his choice of materials. In place of timber he used granite and Portland "
             "stone, each block cut ashore to fit its neighbours like the pieces of a puzzle, so that every "
             "course was locked to the one below. To bind them he developed a lime mortar that would set under "
             "water. The tower was first lit in October 1759.",
        "F": "The man who finally tried was not an engineer at all. Henry Winstanley was an engraver and "
             "something of a showman, whose house in Essex was crammed with trick furniture designed to alarm "
             "his guests. He also owned ships, and two of them had been wrecked on the Eddystone. In 1696 he set "
             "out for the reef.",
        "G": "The Douglass tower is still in service, although nobody has lived in it since 1982, when the light "
             "was automated and the last keepers came ashore. A helicopter pad built above the lantern now brings "
             "out the engineers who maintain it, on days when the weather allows, which on the Eddystone is still "
             "by no means every day.",
        "H": "The next attempt came from an equally unlikely quarter. John Rudyerd was a London silk merchant with "
             "no training in engineering, but he grasped what his predecessor had not: that anything projecting "
             "from a tower gave the sea something to grip. His tower, completed in 1709, was a plain cone of "
             "timber, weighted with courses of stone and as smooth as he could make it.",
    },
    "lex": ["all but disappears", "something of a showman", "a profusion of", "from an unlikely quarter",
            "not believe a word of it", "post-mortem", "dovetailing", "proviso", "turn sth to account"],
    "items": [
        {"n": 37, "key": "F", "theory": ["4.1", "3.4"],
         "before": "El texto base termina con un problema sin resolver: {{What nobody could supply was a way of "
                   "building one}}. F empieza respondiendo a esa carencia: {{The man who finally tried}}. Además, F "
                   "presenta a Winstanley con nombre completo y descripción ({{Henry Winstanley was an engraver "
                   "and something of a showman}}), así que tiene que ir antes de cualquier párrafo que lo nombre "
                   "solo por el apellido.",
         "after": "F termina con el comienzo de la obra ({{he set out for the reef}}), y el párrafo siguiente "
                  "cuenta cómo avanzaba: {{Progress was painfully slow}}. Ese párrafo ya nombra a Winstanley por el "
                  "apellido ({{seized Winstanley at the site}}), lo que confirma que la presentación va justo antes.",
         "trap": {"letter": "H",
                  "why": "{{The next attempt}} y {{his predecessor}} presuponen un intento anterior, y en este punto "
                         "del texto nadie lo ha intentado todavía."}},
        {"n": 38, "key": "C", "theory": ["4.1", "4.4"],
         "before": "El párrafo anterior acaba con la luz encendida por primera vez: {{By November 1698 a light was "
                   "burning on the reef for the first time}}. C retoma esa luz con un pronombre y el mismo verbo: "
                   "{{It did not burn for long without trouble}}.",
         "after": "C cuenta que Winstanley amplió la torre ({{He enlarged the whole structure}}), y el párrafo "
                  "siguiente presupone esa reforma: {{So confident was Winstanley in the rebuilt tower}}. El participio [[rebuilt]] "
                  "recoge [[enlarged]] con otra palabra (§4.4).",
         "trap": {"letter": "D",
                  "why": "Encaja por detrás: tras la primera luz, {{Winstanley lost no time in turning his "
                         "achievement to account}} suena natural. Pero falla por delante: D no habla de ninguna "
                         "reforma, y {{the rebuilt tower}} se queda sin antecedente."}},
        {"n": 39, "key": "H", "theory": ["4.1", "3.1"],
         "before": "El párrafo anterior termina con la destrucción de la torre y la muerte de su constructor: "
                   "{{Of Winstanley and the men with him, no trace was ever found}}. H empieza con {{The next "
                   "attempt}} y llama a Winstanley {{his predecessor}}. Además, {{equally unlikely}} remite a la "
                   "presentación de Winstanley en el hueco 37: {{was not an engineer at all}}.",
         "after": "H describe una torre lisa y sin adornos ({{a plain cone of timber}}, {{as smooth as he could "
                  "make it}}). El párrafo siguiente la valora con un sustantivo resumen y la retoma: {{Simplicity "
                  "served it well against the water}}, {{the cone stood unmoved}}.",
         "trap": {"letter": "B",
                  "why": "{{The remedy was to start again}} parece encajar tras la destrucción de la primera torre, "
                         "pero {{more than twice as tall as Smeaton’s}} da por conocido a alguien que todavía no ha "
                         "aparecido, y en B no hay nada sencillo a lo que pueda referirse {{Simplicity served it "
                         "well}}."}},
        {"n": 40, "key": "A", "theory": ["4.1", "3.4"],
         "before": "El párrafo anterior deja en la torre a {{the three men on the rock}}, y A escoge a uno de ellos "
                   "con un pronombre: {{The oldest of them, Henry Hall}} (§4.1).",
         "after": "A presenta a Hall con nombre completo y cuenta su muerte ({{Hall died twelve days later}}); el "
                  "párrafo siguiente lo nombra solo por el apellido: {{Hall’s ordeal made him briefly famous}}. "
                  "Ningún otro párrafo presenta a Hall (§3.4)."},
        {"n": 41, "key": "E", "theory": ["4.1", "4.4"],
         "before": "El párrafo anterior explica la primera idea de Smeaton, la forma ({{found his answer in the "
                   "shape of an oak}}). E añade otra: {{He was equally original in his choice of materials}}. "
                   "La palabra [[equally]] presupone una primera muestra de originalidad, y [[He]] solo puede ser Smeaton.",
         "after": "E describe bloques encajados entre sí ({{each block cut ashore to fit its neighbours}}, {{every "
                  "course was locked to the one below}}). El párrafo siguiente lo resume con una nominalización y "
                  "lo suma a la forma: {{It was the shape and the dovetailing together}} (§4.4).",
         "trap": {"letter": "B",
                  "why": "La mención de {{the dovetailed granite}} parece preparar {{the dovetailing}} del párrafo siguiente, pero "
                         "B empieza con {{The remedy was to start again}}, y en ese punto no hay nada que remediar: "
                         "Smeaton acaba de recibir el encargo. Además, B salta a 1882, y el párrafo siguiente vuelve "
                         "a las décadas que siguieron a 1759 ({{Within decades it had become the model}})."}},
        {"n": 42, "key": "B", "theory": ["3.2", "4.1"],
         "before": "El párrafo anterior plantea un problema que no se arregla reparando la torre: {{the rock beneath "
                   "it was being worn away}}. B empieza con un sustantivo resumen que presenta la solución: {{The "
                   "remedy was to start again on a neighbouring rock}} (§3.2, problema–solución).",
         "after": "B presenta la torre nueva ({{The new tower, designed by James Douglass}}), y el párrafo "
                  "siguiente la toma como punto de referencia con un posesivo: {{Its predecessor was not simply "
                  "left to the waves}}. [[Its]] es la torre de Douglass, y [[predecessor]], la de Smeaton.",
         "trap": {"letter": "G",
                  "why": "También habla de la torre nueva, pero {{The Douglass tower}} da por presentado a Douglass, "
                         "que aparece por primera vez en B. Además, {{Its predecessor}} necesitaría delante la "
                         "construcción de la torre nueva, y G empieza cuando ya lleva más de un siglo en servicio."}},
        {"n": 43, "key": "G", "theory": ["3.4", "4.1"],
         "before": "El párrafo anterior termina con los restos de la torre de Smeaton junto a la nueva ({{beside "
                   "the newer tower}}). G pasa a esa torre, que ya conocemos: {{The Douglass tower is still in "
                   "service}}. Douglass se presentó con nombre completo en el hueco 42 ({{designed by James "
                   "Douglass}}).",
         "after": "G termina con una condición: {{on days when the weather allows}}. El último párrafo la recoge "
                  "con un sustantivo resumen, {{would have recognised that proviso}}, y la enlaza con las "
                  "dificultades de Winstanley."},
    ],
    "extra": {
        "letter": "D", "theory": ["5.1", "3.1"],
        "rules_out": [
            {"gaps": [37],
             "why": "D nombra a Winstanley solo por el apellido ({{Winstanley lost no time}}), y en ese punto todavía "
                    "no se ha presentado: lo hace F. Además, {{the finished tower}} aún no existe (§3.4)."},
            {"gaps": [38],
             "why": "Encaje por un solo lado. Por detrás funciona, porque {{turning his achievement to account}} "
                    "puede seguir a la primera luz; pero el párrafo siguiente habla de {{the rebuilt tower}}, y D "
                    "no menciona ninguna reforma. Además, {{ornate galleries and all}} presupone las galerías que "
                    "añade la ampliación de C."},
            {"gaps": [39, 40, 41, 42, 43],
             "why": "Cronología imposible: Winstanley muere en 1703 ({{no trace was ever found}}), y D lo presenta "
                    "vivo, sacando partido de su torre. Del hueco 39 en adelante el relato ya va por Rudyerd, "
                    "Smeaton y Douglass."},
        ],
    },
}

if __name__ == "__main__":
    import runpy
    if len(sys.argv) < 2:
        print("Uso: python3 gen_RDG-P6.py --demo | mis_hojas.py [carpeta_salida]")
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
