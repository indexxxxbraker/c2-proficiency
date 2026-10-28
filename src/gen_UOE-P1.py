# gen_UOE-P1.py · Generador de Use of English Part 1 (multiple-choice cloze) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py en la misma carpeta (no modifica nada de ella).
#
# QUE HACE
#   - Hoja de practica completa (texto con huecos, cuadricula de opciones A-D, hoja de respuestas y
#     soluciones con clave rapida), con el formato de UOE-P1_Practica_01-06.
#   - Bloques sueltos para insertar la Part 1 en un simulacro (SIM): enunciado, hoja de respuestas
#     y soluciones por separado.
#   - Verificacion automatica de la hoja antes y despues de generar el PDF.
#
# USO DESDE LA LINEA DE COMANDOS
#   python3 gen_UOE-P1.py --demo [carpeta_salida]        -> genera una hoja de ejemplo (Practica_99)
#   python3 gen_UOE-P1.py mis_hojas.py [carpeta_salida]  -> mis_hojas.py define SPECS = [spec, ...]
#
# USO DESDE OTRO SCRIPT (el guion del nombre impide un import normal)
#   import importlib.util
#   _s = importlib.util.spec_from_file_location("gen_p1", "/ruta/gen_UOE-P1.py")
#   gen = importlib.util.module_from_spec(_s); _s.loader.exec_module(gen)
#   errs, words = gen.verify(spec)
#   gen.build_sheet(spec, "/mnt/user-data/outputs/UOE-P1_Practica_07.pdf")
#   story += gen.question_flowables(spec)        # para un SIM
#
# FORMATO DE UNA HOJA (spec: diccionario)
#   num        "07"                         numero de hoja (para nombre, cabecera y pie)
#   subtitle   "Hoja 07 · Nivel de examen"  subtitulo en espanol
#   title      "Titulo del texto"           en ingles
#   example    {"opts": [4 opciones], "key": "B"}      ejemplo (0)
#   text       [parrafo, parrafo, ...]      en ingles; cada hueco se escribe {numero}: {0}, {1} ... {8}
#   minutes    10                           opcional; tiempo orientativo
#   first      1                            opcional; numero del primer item (la Part 1 va de la 1 a la 8)
#   items      8 diccionarios, uno por hueco, en orden:
#       n       1
#       opts    ["staged", "performed", "held", "played"]   opciones A-D, en ese orden
#       key     "A"                         letra de la unica respuesta correcta
#       theory  ["3.1"]                     secciones de UOE-P1_Teoria_v1 (ver THEORY); la primera
#                                           determina el tipo de distincion, salvo que se de 'type'
#       type    opcional; por defecto se deduce de theory[0] (ver TYPES)
#       why     por que es correcta la clave
#       wrong   {"B": "...", "C": "...", "D": "..."}  por que falla CADA distractor (las tres letras
#                                           que no son la clave, ni una mas ni una menos)
#
#   Marcado en why / wrong (y en cualquier texto en espanol):
#       [[texto]]   -> ingles en serif (equivale a E("texto"))
#       [[!texto]]  -> ingles en serif y negrita (equivale a EB("texto"))
#   Tambien se pueden usar directamente las funciones E() y EB() del modulo.
#
# REGLAS DEL PROYECTO QUE EL GENERADOR NO PUEDE COMPROBAR (hay que hacerlas a mano)
#   - Que cada hueco tenga una sola respuesta defendible: ningun distractor puede ser valido en
#     el contexto, y las alternativas correctas conocidas (p. ej. make a comeback junto a stage
#     a comeback) no pueden figurar entre las opciones.
#   - Ingles britanico en el texto y en las opciones.
#   - Que las explicaciones digan la verdad sobre cada palabra (collocation, preposicion, patron).
#   - Revisar el PDF renderizado antes de entregarlo.
#   - Si la teoria pasa a una v2 con otra numeracion, actualizar THEORY y TYPES.
#
# AVISOS (no bloquean la generacion; se imprimen)
#   - Reparto de letras desequilibrado (una letra mas de 3 veces o ninguna vez) o tres claves
#     iguales seguidas.
#   - La explicacion 'why' no menciona la palabra correcta, o la de un distractor no menciona
#     ese distractor (suele delatar una clave cambiada de letra).

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2_plantilla import *  # noqa: E402,F401,F403

VERSION = "1"
G = "__________"
LET = "ABCD"
GAP_RE = re.compile(r"\{(\d+)\}")
FIRST_ITEM = 1            # la Part 1 del examen va de la 1 a la 8
N_ITEMS = 8
WORDS_MIN, WORDS_MAX = 160, 300


# ---------- Ingles dentro del texto en espanol ----------
def E(s):
    return f'<font name="EN">{s}</font>'


def EB(s):
    return f'<font name="EN"><b>{s}</b></font>'


def markup(s):
    """[[!X]] -> EB(X); [[x]] -> E(x)."""
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)


def _plain(s):
    return re.sub(r"<[^>]+>", "", markup(s))


# ---------- Secciones de UOE-P1_Teoria_v1 ----------
THEORY = {
    "1": "Formato y puntuación",
    "2": "Método en cuatro pasos",
    "3.1": "Verbo + sustantivo",
    "3.2": "Adjetivo + sustantivo",
    "3.3": "Adverbio + adjetivo o verbo",
    "3.4": "Sustantivo + of",
    "4.1": "Binomials y pares fijos",
    "4.2": "Idioms con una palabra evaluada",
    "4.3": "Frases preposicionales fijas",
    "5.1": "Significado preciso y alcance",
    "5.2": "Connotación",
    "5.3": "Registro",
    "5.4": "Intensidad",
    "6.1": "Preposición dependiente",
    "6.2": "Patrón verbal",
    "6.3": "Transitividad: el verbo frente a su pareja",
    "6.4": "Conectores que se distinguen por su encaje",
    "7.1": "Misma partícula, distinto verbo",
    "7.2": "Mismo verbo, distinta partícula",
    "7.3": "Prepositional verbs y phrasal verbs de tres partes",
    "8": "Trampas típicas",
    "9": "Tabla de repaso por tipo de distinción",
}
THEORY_DOC = "UOE-P1_Teoria_v1"
TYPES = {"3": "Collocation", "4": "Expresión fija", "5": "Casi-sinónimos", "6": "Complementación",
         "7": "Phrasal verb"}


def _first(spec):
    return spec.get("first", FIRST_ITEM)


def _range(spec):
    a = _first(spec)
    return f"{a}–{a + N_ITEMS - 1}"


def _type(it):
    return it.get("type") or TYPES.get(it["theory"][0].split(".")[0], "")


def _word(it):
    return it["opts"][LET.index(it["key"])]


def gap(n):
    # espacio duro: el numero y la raya no se separan al final de una linea
    return f"<b>({n})</b>&nbsp;{G}"


def render_text(par):
    return GAP_RE.sub(lambda m: gap(m.group(1)), par)


def options_grid(rows):
    """rows: lista de (numero, [4 opciones]). Cuadricula A-D en serif."""
    data = [[f"<b>{n}</b>"] + [f"<b>{l}</b>&nbsp;&nbsp;{o}" for l, o in zip(LET, opts)] for n, opts in rows]
    return table(data, [10, 40, 40, 40, 40], header=False, en_cols=(0, 1, 2, 3, 4))


# ---------- Bloques reutilizables (hoja suelta o simulacro) ----------
def question_flowables(spec, with_title_block=False):
    """Rubrica, ejemplo, texto y cuadricula de opciones. Con with_title_block=True antepone el bloque
    de titulo de la hoja."""
    out = []
    if with_title_block:
        out += title_block(f"UOE-P1 · Práctica {spec['num']}", "Multiple-choice cloze", spec["subtitle"],
                           f"8 ítems (preguntas {_range(spec)}) · 1 punto por ítem · tiempo orientativo: "
                           f"{spec.get('minutes', 10)} minutos · sin consultar la teoría")
    out.append(en(f"For questions {_range(spec)}, read the text below and decide which answer (A, B, C or D) "
                  "best fits each gap. There is an example at the beginning (0). Mark your answers on the "
                  "answer sheet."))
    ex = spec["example"]
    out.append(en("<b>Example:</b>"))
    out += options_grid([(0, ex["opts"])])
    out.append(en(f"The answer is <b>{ex['key']}</b> ({ex['opts'][LET.index(ex['key'])]})."))
    out += [Spacer(1, 4), en(f"<b>{spec['title']}</b>")]
    out += [en(render_text(par)) for par in spec["text"]]
    out.append(Spacer(1, 4))
    out += options_grid([(it["n"], it["opts"]) for it in spec["items"]])
    return out


def answer_sheet_flowables(spec, heading="Hoja de respuestas"):
    out = [h2(heading), p("Escribe la letra elegida (A, B, C o D). Al corregir, marca 1 punto por acierto; "
                          "una respuesta doble vale 0.")]
    rows = [["Nº", "Respuesta (A–D)", "Punto"]]
    rows += [[str(it["n"]), "", "/ 1"] for it in spec["items"]]
    rows.append(["<b>Total</b>", "", f"<b>/ {N_ITEMS}</b>"])
    out += table(rows, [20, 110, 40], zebra=False,
                 extra=[("TOPPADDING", (0, 1), (-1, -1), 9), ("BOTTOMPADDING", (0, 1), (-1, -1), 9),
                        ("VALIGN", (0, 1), (-1, -1), "MIDDLE")])
    return out


def solutions_flowables(spec, with_band=True, heading=None):
    """Soluciones. with_band=True abre con el salto de pagina y la banda de la plantilla.
    heading: titulo opcional (p. ej. 'Part 1 · Multiple-choice cloze' dentro de un simulacro)."""
    out = solutions_start("Soluciones") if with_band else []
    if heading:
        out.append(h2(heading))
    out.append(p("1 punto por acierto. Cada solución indica el tipo de distinción, explica por qué es correcta "
                 "la clave y por qué falla cada distractor, y remite al apartado de "
                 f"{THEORY_DOC} que lo trabaja."))
    out.append(h3("Clave rápida"))
    rows = [["Nº", "Clave", "Tipo de distinción", "Teoría"]]
    for it in spec["items"]:
        rows.append([str(it["n"]), f"{it['key']} · {E(_word(it))}", _type(it),
                     " · ".join(f"§{s} {THEORY[s]}" for s in it["theory"])])
    out += table(rows, [12, 46, 36, 76])
    for it in spec["items"]:
        block = [h3(f"{it['n']} · {it['key']} {E(_word(it))}"),
                 p(f"<b>Por qué:</b> {markup(it['why'])}")]
        for k, l in enumerate(LET):
            if l != it["key"]:
                block.append(p(f"<b>{l} {E(it['opts'][k])}</b>: {markup(it['wrong'][l])}"))
        block.append(Paragraph("Teoría: " + " · ".join(f"§{s} {THEORY[s]}" for s in it["theory"]), S["small"]))
        out.append(KeepTogether(block))
    return out


def build_sheet(spec, out_path):
    """Hoja de practica completa: enunciado, hoja de respuestas (pagina nueva) y soluciones."""
    n = spec["num"]
    story = question_flowables(spec, with_title_block=True)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec)
    build(out_path, story, f"UOE-P1 · Práctica {n}", f"UOE-P1_Practica_{n}.pdf",
          title=f"UOE-P1 · Práctica {n} · Multiple-choice cloze")
    return out_path


# ---------- Verificacion ----------
def _check_opts(opts, where, errs):
    if not isinstance(opts, (list, tuple)) or len(opts) != 4:
        errs.append(f"{where}: hacen falta exactamente 4 opciones")
        return
    if any(not str(o).strip() for o in opts):
        errs.append(f"{where}: opción vacía")
    if len({str(o).strip().lower() for o in opts}) != 4:
        errs.append(f"{where}: opciones repetidas")
    if any(re.search(r"\[\[|\]\]|[{}]", str(o)) for o in opts):
        errs.append(f"{where}: marcado dentro de una opción")


def verify(spec):
    """Comprobaciones de formato y coherencia antes de generar. Devuelve (errores, palabras_del_texto)."""
    errs = []
    for field in ("num", "subtitle", "title", "example", "text", "items"):
        if not spec.get(field):
            errs.append(f"falta el campo '{field}'")
    if errs:
        return errs, 0
    a = _first(spec)
    expected = list(range(a, a + N_ITEMS))
    nums = [int(m.group(1)) for par in spec["text"] for m in GAP_RE.finditer(par)]
    if nums != [0] + expected:
        errs.append(f"numeración de huecos en el texto: {nums} (se esperaba {[0] + expected})")
    ex = spec["example"]
    _check_opts(ex.get("opts"), "ejemplo (0)", errs)
    if ex.get("key") not in tuple(LET):
        errs.append("ejemplo (0): la clave tiene que ser A, B, C o D")
    if [it.get("n") for it in spec["items"]] != expected:
        errs.append(f"ítems de la clave: {[it.get('n') for it in spec['items']]} (se esperaba {expected})")
    for it in spec["items"]:
        n = it.get("n")
        for field in ("opts", "key", "theory", "why", "wrong"):
            if not it.get(field):
                errs.append(f"{n}: falta el campo '{field}'")
        if not all(it.get(f) for f in ("opts", "key", "theory", "why", "wrong")):
            continue
        _check_opts(it["opts"], str(n), errs)
        if it["key"] not in tuple(LET):
            errs.append(f"{n}: la clave '{it['key']}' no es A, B, C ni D")
            continue
        distractors = set(LET) - {it["key"]}
        if set(it["wrong"]) != distractors:
            errs.append(f"{n}: 'wrong' tiene que explicar exactamente {sorted(distractors)}; "
                        f"tiene {sorted(it['wrong'])}")
        if isinstance(it["theory"], str):
            errs.append(f"{n}: 'theory' tiene que ser una lista, p. ej. [\"3.1\"]")
        else:
            for s in it["theory"]:
                if s not in THEORY:
                    errs.append(f"{n}: sección de teoría inexistente §{s}")
            if not _type(it):
                errs.append(f"{n}: no se puede deducir el tipo de distinción de §{it['theory'][0]}; usa 'type'")
        texts = [("why", it["why"])] + [(f"wrong[{l}]", t) for l, t in it["wrong"].items()]
        for field, txt in texts:
            if re.search(r"\[\[|\]\]|\{E|EB\(", markup(txt)):
                errs.append(f"{n}: marcado sin resolver en '{field}'")
    for par in spec["text"]:
        if re.search(r"\[\[|\]\]", par):
            errs.append("marcado [[ ]] dentro del texto en inglés")
    words = len(GAP_RE.sub("X", " ".join(spec["text"])).split())
    if not WORDS_MIN <= words <= WORDS_MAX:
        errs.append(f"longitud del texto fuera de {WORDS_MIN}–{WORDS_MAX} palabras: {words}")
    return errs, words


# Formas irregulares frecuentes -> forma base (solo para el aviso de _mentions)
IRREGULAR = {
    "bore": "bear", "borne": "bear", "brought": "bring", "bought": "buy", "came": "come", "caught": "catch",
    "chose": "choose", "chosen": "choose", "dealt": "deal", "drew": "draw", "drawn": "draw", "dying": "die",
    "fell": "fall", "fallen": "fall", "found": "find", "gave": "give", "given": "give", "got": "get",
    "gone": "go", "went": "go", "had": "have", "has": "have", "did": "do", "done": "do", "grew": "grow", "grown": "grow", "held": "hold", "kept": "keep",
    "knew": "know", "known": "know", "laid": "lay", "led": "lead", "left": "leave", "lost": "lose",
    "lying": "lie", "made": "make", "meant": "mean", "paid": "pay", "ran": "run", "rose": "rise",
    "risen": "rise", "said": "say", "sent": "send", "sold": "sell", "sought": "seek", "spent": "spend",
    "spoke": "speak", "spoken": "speak", "stood": "stand", "struck": "strike", "taught": "teach",
    "thought": "think", "threw": "throw", "thrown": "throw", "told": "tell", "took": "take",
    "taken": "take", "won": "win", "wore": "wear", "worn": "wear", "wrote": "write", "written": "write",
}


def _roots(word):
    """Raices candidatas de una opcion: 5 primeras letras, forma base de irregulares y sin -ing/-ed/-s."""
    w = word.lower().split()[0]
    cands = {w[:5]}
    if w in IRREGULAR:
        cands.add(IRREGULAR[w][:5])
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            b = w[:-len(suf)]
            if suf == "ed" and b.endswith("i"):
                b = b[:-1] + "y"                       # carried -> carry
            cands.add(b[:5])
            if len(b) >= 4 and b[-1] == b[-2]:
                cands.add(b[:-1][:5])                  # getting -> get, mulling -> mul
    return cands


def _mentions(text, word):
    """Comprobacion aproximada: el texto contiene alguna raiz de la palabra."""
    low = _plain(text).lower()
    return any(r in low for r in _roots(word))


def warnings(spec):
    """Avisos que no impiden generar: reparto de letras y coherencia aproximada de las explicaciones."""
    out = []
    keys = [it["key"] for it in spec["items"]]
    counts = {l: keys.count(l) for l in LET}
    if max(counts.values()) > 3 or min(counts.values()) == 0:
        out.append(f"reparto de letras desequilibrado: {counts}")
    for i in range(len(keys) - 2):
        if keys[i] == keys[i + 1] == keys[i + 2]:
            out.append(f"tres claves seguidas iguales ({keys[i]}) desde el ítem {spec['items'][i]['n']}")
    for it in spec["items"]:
        if not _mentions(it["why"], _word(it)):
            out.append(f"{it['n']}: 'why' no menciona «{_word(it)}»; comprueba que la clave es la correcta")
        for k, l in enumerate(LET):
            if l in it["wrong"] and not _mentions(it["wrong"][l], it["opts"][k]):
                out.append(f"{it['n']}: la explicación de {l} no menciona «{it['opts'][k]}»")
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
        print(f"  aviso · hoja {spec['num']} · {w}")
    path = build_sheet(spec, os.path.join(out_dir, f"UOE-P1_Practica_{spec['num']}.pdf"))
    leftovers = check_pdf(path)
    if leftovers:
        raise ValueError(f"Hoja {spec['num']}: restos de código en el PDF: {leftovers}")
    clave = "".join(it["key"] for it in spec["items"])
    print(f"UOE-P1_Practica_{spec['num']}.pdf · {words} palabras · clave {clave} · verificación sin errores")
    return path


# ---------- Hoja de ejemplo (contenido de UOE-P1_Practica_06, con el marcado [[ ]]) ----------
DEMO = {
    "num": "99",
    "subtitle": "Hoja de prueba del generador",
    "title": "The rehabilitation of nostalgia",
    "example": {"opts": ["coined", "forged", "cast", "stamped"], "key": "A"},
    "text": [
        "In 1688 a young Swiss medical student, Johannes Hofer, {0} the word ‘nostalgia’ to describe the {1} "
        "homesickness he had observed among Swiss mercenaries serving abroad. Sufferers lost their appetite, wept "
        "uncontrollably and, in the worst cases, were said to waste away entirely. Later physicians {2} the "
        "condition down to the incessant clanging of cowbells in the Alpine valleys, which was thought to damage "
        "the eardrums and the brain. Absurd as such theories now sound, the underlying assumption – that nostalgia "
        "was a disorder to be cured – {3} sway for the best part of two centuries.",
        "{4} to its reputation, however, nostalgia appears to do us more good than harm. Psychologists have found "
        "that people who regularly {5} about the past report a stronger sense of connection to others and a "
        "greater conviction that their lives have meaning. The pleasure is admittedly often {6} with sadness, "
        "since what we remember is by definition lost. Yet far from being merely benign, the experience may be "
        "positively {7}, offering comfort in times of loneliness or upheaval. Whether it can be cultivated "
        "deliberately is another matter; on that question, the jury is still {8}.",
    ],
    "items": [
        {"n": 1, "opts": ["sharp", "keen", "steep", "acute"], "key": "D", "theory": ["3.2"],
         "why": "[[acute homesickness]]: añoranza intensa. [[Acute]] va con estados intensos "
                "([[acute pain, anxiety, shortage]]).",
         "wrong": {"A": "[[sharp]] va con [[rise, fall, contrast]] o con un dolor repentino; no con [[homesickness]].",
                   "B": "[[keen]] va con [[interest, sense, eye]].",
                   "C": "[[steep]] va con [[rise, decline, price]]."}},
        {"n": 2, "opts": ["put", "set", "laid", "brought"], "key": "A", "theory": ["7.1"],
         "why": "[[put sth down to sth]]: atribuir algo a una causa.",
         "wrong": {"B": "[[set down]]: poner por escrito o dejar en el suelo; no se combina con [[to]] en este sentido.",
                   "C": "[[lay down]]: establecer normas ([[lay down the rules]]); [[laid]] es su pasado.",
                   "D": "[[bring down]]: reducir, o derrocar a un gobierno; [[brought]] es su pasado."}},
        {"n": 3, "opts": ["kept", "held", "took", "carried"], "key": "B", "theory": ["3.1"],
         "why": "[[hold sway]]: predominar, imponerse. Collocation fija; [[held]] es el pasado.",
         "wrong": {"A": "[[*keep sway]] no existe ([[kept]]).",
                   "C": "[[*take sway]] no existe ([[took]]).",
                   "D": "[[*carry sway]] no existe ([[carried]]); [[carry weight]] sí, con otro sentido "
                        "(tener peso, influencia)."}},
        {"n": 4, "opts": ["Opposite", "Adverse", "Contrary", "Averse"], "key": "C", "theory": ["6.4"],
         "why": "[[contrary to]]: al contrario de lo que cabría esperar ([[contrary to its reputation]]).",
         "wrong": {"A": "[[opposite]] indica posición física u oposición entre dos cosas ([[the house opposite]]); "
                        "no introduce así un contraste.",
                   "B": "[[adverse]]: adverso ([[adverse effects]]); adjetivo que no se construye con [[to]] aquí.",
                   "D": "[[averse to]]: reacio a ([[averse to risk]]); se dice de personas. [[Adverse]] y "
                        "[[averse]] son confusables clásicos."}},
        {"n": 5, "opts": ["recall", "reminisce", "recollect", "evoke"], "key": "B", "theory": ["6.3"],
         "why": "[[reminisce about]]: rememorar con gusto. Lleva [[about]] y es el único intransitivo del conjunto.",
         "wrong": {"A": "[[recall]] es transitivo, sin preposición ([[recall the past]]).",
                   "C": "[[recollect]] también ([[recollect the details]]).",
                   "D": "[[evoke]] es transitivo y significa «evocar» en otro o «suscitar», no «recordar» uno."}},
        {"n": 6, "opts": ["dyed", "stained", "tinged", "painted"], "key": "C", "theory": ["5.4"],
         "why": "[[tinged with]]: con un ligero matiz de una emoción ([[tinged with sadness, regret, irony]]). "
                "El grado leve encaja con [[admittedly]] y [[often]].",
         "wrong": {"A": "[[dyed]]: teñido en sentido literal (pelo, tela).",
                   "B": "[[stained]]: manchado de forma permanente; en sentido figurado va con culpa o deshonra "
                        "([[stained by scandal]]).",
                   "D": "[[painted]]: no se usa con emociones."}},
        {"n": 7, "opts": ["beneficial", "benevolent", "beneficent", "benign"], "key": "A", "theory": ["5.1"],
         "why": "[[beneficial]]: beneficioso, que hace bien. Encaja con [[positively]] y con [[offering comfort]].",
         "wrong": {"B": "[[benevolent]]: benévolo; se dice de personas o instituciones.",
                   "C": "[[beneficent]]: benefactor, que hace el bien; formal y dicho de personas.",
                   "D": "[[benign]]: inofensivo (o benigno en medicina). El texto acaba de decir "
                        "[[far from being merely benign]], así que lo contradice."}},
        {"n": 8, "opts": ["off", "over", "away", "out"], "key": "D", "theory": ["4.2"],
         "why": "[[the jury is (still) out]]: todavía no hay una conclusión. Expresión fija.",
         "wrong": {"A": "[[off]]: no forma la expresión.",
                   "B": "[[over]]: ídem.",
                   "C": "[[away]]: ídem."}},
    ],
}


if __name__ == "__main__":
    import runpy
    if len(sys.argv) < 2:
        print("Uso: python3 gen_UOE-P1.py --demo [carpeta_salida] | mis_hojas.py [carpeta_salida]")
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
