# gen_SPK.py · Generador de tests de Speaking completos (PDF + MP3) · v1
# Proyecto C2 Proficiency. Requiere c2_plantilla.py y lst_audio.py en la misma carpeta (no modifica ninguno).
#
# QUE HACE
#   - Hoja de practica = un test completo: material del candidato (hoja de fotos de la Part 2 y tarjetas A y B de
#     la Part 3), mapa del MP3, hoja de autocorreccion con la rubrica de SPK_Teoria_v1 §8.2 y soluciones (guion
#     completo del MP3, respuestas posibles de la Part 1, ideas y lenguaje de la Part 2, reacciones al companero
#     sintetico, plan y long turn modelo de cada tarjeta y lenguaje para la discusion).
#   - MP3 del interlocutor (voz Sonia, en-GB) con silencios cronometrados y, en la Part 2, un companero sintetico
#     (otra voz) con cinco intervenciones: una en la fase 1 y cuatro en la fase 2. Los huecos se reparten para que
#     las fases duren exactamente 60 y 180 segundos.
#   - Fotos de Wikimedia Commons: descarga y vuelve a comprobar la licencia en el momento (dominio publico, CC0 o
#     CC BY sin SA) e imprime la atribucion bajo la hoja de fotos.
#   - Verificacion: contenido (verify), audio (duracion de cada fase, reconocimiento de voz del companero y de
#     todas las lineas del interlocutor) y PDF (restos de marcado, glifos).
#
# USO
#   python3 gen_SPK.py spk_specs.py [carpeta_salida] [num ...]     spk_specs.py define SPECS = [spec, ...]
#   Ejemplos: python3 gen_SPK.py spk_specs.py out          (las seis hojas)
#             python3 gen_SPK.py spk_specs.py out 03 05    (solo la 03 y la 05)
#   Desde otro script (el guion impide import normal):
#     import importlib.util; s = importlib.util.spec_from_file_location("gen_spk", "/ruta/gen_SPK.py")
#     gen = importlib.util.module_from_spec(s); s.loader.exec_module(gen); gen.make(spec, out_dir)
#
# FORMATO DE UN SPEC (diccionario)
#   num, level (1-6), subtitle (espanol)
#   p1: {"questions": [{"q": "...", "pause": 15, "model": "..." | None}] x5}  (las dos primeras: donde vive y si
#       trabaja o estudia; model obligatorio en las tres ultimas)
#   p2: {"title": titulo de la hoja de fotos, "intro": "people ...", "q1_pics": ["A", "C"], "q1": "...",
#        "context": "I'd like you to imagine that ...", "task": "Talk together about ... Then decide ...",
#        "partner_voice": "Ryan", "photos": [{"letter", "file" (titulo en Commons), "what" (espanol), "spec"
#        (especulacion, espanol), "offers" (espanol), "decision" (espanol), "artist" opcional}] x4-5,
#        "phase1_lines": [ingles] , "decision": espanol, "language": [ingles],
#        "partner": [{"text": ingles, "provokes": espanol, "react": ingles, "theory": ["6.3"]}] x5 (la 1.a, fase 1)}
#   p3: {"theme": "learning", "cards": [{"q", "ideas": [3], "plan": {"Operación", "Postura", "Línea 1",
#        "Línea 2", "Contrapunto", "Cierre"}, "model": [parrafos], "comments": [uno por parrafo],
#        "follow_up": {"q": ingles, "ideas": espanol}}] x2,
#        "discussion": [{"q": ingles, "ideas": espanol, "lang": ingles}] x6}
#   lex: lexico para el modulo LEX (no se imprime)
#   Marcado en campos en espanol: [[ingles]] serif · [[!ingles]] serif negrita · [[/ingles]] serif cursiva.
#
# NOTAS
#   - Un test tarda unos 2 minutos con las voces ya en cache (sintesis nueva: 1-2 minutos mas). Si el entorno limita
#     cada orden a 5 minutos, generar un test por ejecucion.
#   - Commons responde 429 si se piden muchas miniaturas seguidas: _fetch reintenta con espera creciente.
#   - Hojas 01-06 (oct. 2026): fotos 4-5 por hoja; companero Ryan, Connor, Thomas, Natasha, Emily, Mitchell.

import hashlib, json, os, re, sys, urllib.error, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c2_plantilla import *
from c2_plantilla import _F
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, CondPageBreak, PageBreak
from reportlab.platypus import Image as RLImage
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
import lst_audio as A

THEORY_DOC = "SPK_Teoria_v1"
THEORY = {
    "1.1": "Formato, tiempos y guion del interlocutor", "1.2": "Qué cambia respecto al C1",
    "1.3": "Cómo se puntúa", "1.4": "Practicar sin compañero", "2": "Part 1 · Entrevista",
    "3.1": "La tarjeta", "3.2": "Los diez segundos", "3.3": "Arquitectura de dos minutos",
    "3.4": "Desarrollar una idea", "3.5": "Generar ideas sin fotos", "3.6": "El reloj",
    "3.7": "Después del long turn", "3.8": "Errores típicos",
    "4.1": "Qué separa la banda 3 de la 5", "4.2": "Señalizar en oral", "4.3": "Marcadores del discurso oral",
    "4.4": "Ganar tiempo, parafrasear y autocorregirse", "4.5": "Cohesión sin repetición",
    "4.6": "Gramática y léxico que estructuran",
    "5.1": "Las dos fases y el título de la hoja", "5.2": "El primer minuto", "5.3": "Los tres minutos",
    "5.4": "Errores típicos", "6.1": "Qué pide la banda 5", "6.2": "Escuchar y engarzar",
    "6.3": "Acuerdo, concesión y desacuerdo graduados", "6.4": "Moderar y reconducir",
    "6.5": "Invitar, ceder el turno, apoyar y ampliar el alcance", "6.6": "Cerrar la decisión",
    "6.7": "La discusión final a tres", "7": "Pronunciación", "8.1": "Cómo grabarse y corregir",
    "8.2": "Los criterios en preguntas", "8.3": "De las respuestas a una nota", "8.4": "Lista de comprobación",
    "9": "Caso completo",
}
RUBRIC = [
    ("Grammatical Resource", [
        ("GR1", "Variedad de estructuras complejas, no solo frases simples"),
        ("GR2", "Errores solo como despistes, no sistemáticos"),
        ("GR3", "Ningún error dificulta la comprensión"),
        ("GR4", "Estructuras complejas en todo el test, también en la interacción"),
        ("GR5", "Gramática flexible: enfatizar, matizar, deshacer ambigüedades")]),
    ("Lexical Resource", [
        ("LR1", "Palabras precisas ante lo abstracto, sin vaguedades"),
        ("LR2", "Colocaciones adecuadas, sin calcos ni falsos amigos"),
        ("LR3", "Paráfrasis sin cortar cuando falta una palabra"),
        ("LR4", "Variedad: sin repetir los mismos términos"),
        ("LR5", "Léxico menos común preciso y natural")]),
    ("Discourse Management", [
        ("DM1", "Long turns de unos dos minutos y 250 palabras o más"),
        ("DM2", "Muy pocas vacilaciones"),
        ("DM3", "Relevante y coherente: postura, sin repetir ideas"),
        ("DM4", "Cohesivos y marcadores variados"),
        ("DM5", "Ideas desarrolladas con detalle; cambios de plano con soltura")]),
    ("Pronunciation", [
        ("PR1", "Se entiende todo sin esfuerzo"),
        ("PR2", "Acento de palabra correcto, también en cognados"),
        ("PR3", "Sonidos claros: vocales, finales, -ed, s inicial"),
        ("PR4", "Entonación adecuada y ritmo con formas débiles"),
        ("PR5", "Acento contrastivo y entonación que realzan el significado")]),
    ("Interactive Communication", [
        ("IC1", "Inicio y respondo"),
        ("IC2", "Engarzo con lo que dice el otro antes de añadir"),
        ("IC3", "Invito, pregunto y apoyo, sin acaparar (*)"),
        ("IC4", "Negocio hacia un resultado en la Part 2"),
        ("IC5", "Amplío el alcance más allá de las fotos y las preguntas")]),
]
CODES = {c for _, qs in RUBRIC for c, _ in qs}
PAUSES_P1 = [15, 15, 30, 30, 30]
LONG_TURN_S, PREP_S, FOLLOW_S, DISC_S = 120, 10, 45, 40
PHASE1_S, PHASE2_S = 60, 180
PARTNER_WPM = 155
INTERLOCUTOR = "Sonia"
WPM_MODEL = 145
AMERICAN = re.compile(
    r"\b(colors?|favor\w*|honor\w*|labor\w*|neighbor\w*|behavior\w*|humor\w*|center\w*|theaters?|"
    r"traveled|traveling|traveler\w*|canceled|labeled|modeled|judgment\w*|programs?|analyz\w*|"
    r"realiz\w*|organiz\w*|recogniz\w*|apologiz\w*|emphasiz\w*|criticiz\w*|civiliz\w*|defense|offense|"
    r"gray|jewelry|skeptic\w*|fiber|practiced|practicing)\b", re.I)
NUMW = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve"}


# ---------- marcado ----------
def E(s): return f'<font name="EN">{s}</font>'
def EI(s): return f'<font name="EN"><i>{s}</i></font>'
def EB(s): return f'<font name="EN"><b>{s}</b></font>'
def M(s):
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: EB(m.group(1)), s)
    s = re.sub(r"\[\[/(.+?)\]\]", lambda m: EI(m.group(1)), s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: E(m.group(1)), s)
def P(s): return p(M(s))
def T(rows, widths, **kw): return table([[M(c) if isinstance(c, str) else c for c in r] for r in rows], widths, **kw)
def WC(s): return len([w for w in s.split() if re.search(r"[A-Za-z0-9]", w)])
def secs(lst): return " · ".join(f"§{s} {THEORY[s]}" for s in lst)
def mmss(t): return f"{int(t // 60)}:{int(round(t % 60)):02d}" if round(t % 60) < 60 else f"{int(t // 60) + 1}:00"

_card_q = ParagraphStyle("spk_card_q", parent=S["en"], fontName="EN-B", fontSize=11.5, leading=15, spaceAfter=6)
_card_b = ParagraphStyle("spk_card_b", parent=S["en"], fontSize=11, leading=14.5, leftIndent=14, bulletIndent=3,
                         spaceAfter=1)
_spoken = ParagraphStyle("spk_spoken", parent=S["en"], leading=15.2, spaceAfter=6)
_vis_t = ParagraphStyle("spk_vis_t", parent=S["en"], fontName="EN-B", fontSize=13, leading=17, textColor=NAVY)
_letter = ParagraphStyle("spk_letter", parent=S["en"], fontName="EN-B", fontSize=13, leading=15, spaceAfter=2)
_attr = ParagraphStyle("spk_attr", parent=S["small"], fontSize=7.6, leading=9.8)
_PNUM = '<font name="Sans-B" color="#A4243B">{}</font>&nbsp;&nbsp;'


def card(question, ideas, label, width=105):
    inner = [Paragraph(label, ParagraphStyle("lab", parent=S["label"], textColor=ACCENT)),
             Paragraph(question, _card_q)] + [Paragraph(i, _card_b, bulletText="•") for i in ideas]
    t = Table([[inner]], colWidths=[width * mm])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.9, NAVY), ("LEFTPADDING", (0, 0), (-1, -1), 10),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    t.hAlign = "LEFT"
    return [t, Spacer(1, 12)]


# ---------- fotos de Wikimedia Commons ----------
UA = "C2-prep-study-material/1.0 (personal study use)"
OK_LIC = re.compile(r"^(CC0|Public domain|PD.*|CC BY \d(\.\d)?|CC BY-\d(\.\d)?)$", re.I)
PHOTO_DIR = os.environ.get("SPK_PHOTOS", "/home/claude/spk_photos")


def _strip(h): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h or "")).strip()


def _fetch(url, timeout=60, tries=5):
    """Descarga con reintentos: Wikimedia responde 429 si se piden demasiadas miniaturas seguidas."""
    import time
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=timeout).read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or k == tries - 1:
                raise
            time.sleep(8 * (k + 1))


def photo_info(title, width=1280):
    """Metadatos en vivo de Commons + descarga de una version de 'width' px. Comprueba la licencia."""
    os.makedirs(PHOTO_DIR, exist_ok=True)
    meta_path = os.path.join(PHOTO_DIR, hashlib.sha1(title.encode()).hexdigest()[:12] + ".json")
    if os.path.exists(meta_path):
        info = json.load(open(meta_path))
    else:
        q = {"action": "query", "format": "json", "titles": title, "prop": "imageinfo",
             "iiprop": "url|extmetadata|size|mime", "iiurlwidth": width,
             "iiextmetadatafilter": "LicenseShortName|LicenseUrl|Artist|UsageTerms"}
        raw = _fetch("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(q), timeout=40)
        pg = list(json.loads(raw)["query"]["pages"].values())[0]
        ii = pg["imageinfo"][0]; m = ii["extmetadata"]
        info = {"title": title, "lic": _strip(m.get("LicenseShortName", {}).get("value", "")),
                "lic_url": m.get("LicenseUrl", {}).get("value", ""),
                "artist": _strip(m.get("Artist", {}).get("value", "")), "page": ii["descriptionurl"],
                "thumb": ii.get("thumburl", ii["url"]), "w": ii.get("thumbwidth", ii["width"]),
                "h": ii.get("thumbheight", ii["height"])}
        json.dump(info, open(meta_path, "w"))
    path = meta_path[:-5] + ".jpg"
    if os.path.exists(path):
        try:
            from PIL import Image as _PIL
            _PIL.open(path).verify()
        except Exception:
            os.remove(path)
    if not os.path.exists(path):
        data = _fetch(info["thumb"])
        with open(path, "wb") as fh:
            fh.write(data)
    info["path"] = path
    info["lic_ok"] = bool(OK_LIC.match(info["lic"])) and "SA" not in info["lic"].upper()
    return info


def _lic_text(info):
    lic = info["lic"]
    if lic.lower().startswith("public domain") or lic.upper().startswith("PD"):
        return "dominio público"
    return lic


def visuals_flowables(spec):
    p2 = spec["p2"]
    out = [h2("Part 2 · Hoja de fotos")]
    tb = Table([[Paragraph(p2["title"], _vis_t)]], colWidths=[CONTENT_W])
    tb.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.9, NAVY), ("LEFTPADDING", (0, 0), (-1, -1), 10),
                            ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    out += [tb, Spacer(1, 8)]
    nrows = (len(p2["photos"]) + 1) // 2
    cw, box_w, box_h = CONTENT_W / 2, CONTENT_W / 2 - 6 * mm, (62 if nrows <= 2 else 50) * mm
    cells = []
    for ph in p2["photos"]:
        info = ph["_info"]
        r = min(box_w / info["w"], box_h / info["h"])
        img = RLImage(info["path"], width=info["w"] * r, height=info["h"] * r)
        img.hAlign = "LEFT"
        cells.append([Paragraph(ph["letter"], _letter), img])
    rows = [cells[i:i + 2] for i in range(0, len(cells), 2)]
    if len(rows[-1]) == 1:
        rows[-1].append("")
    g = Table(rows, colWidths=[cw, cw])
    g.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    out.append(g)
    parts = []
    for ph in p2["photos"]:
        i = ph["_info"]
        name = i["title"].replace("File:", "")
        parts.append(f"<b>{ph['letter']}</b> · «{name}», {ph.get('artist') or i['artist'] or 'autor desconocido'}, "
                     f"{_lic_text(i)}, Wikimedia Commons ({i['page'].replace('https://', '')})")
    out.append(Paragraph("Fotos: " + " · ".join(parts) + ".", _attr))
    return out


# ---------- guion del MP3 ----------
def _say_lines(spec):
    p1, p2, p3 = spec["p1"], spec["p2"], spec["p3"]
    qs = p1["questions"]
    a, b = p2["q1_pics"]
    L = {}
    L["open"] = f"C2 Proficiency. Speaking. Practice test {NUMW[int(spec['num'])]}."
    L["hello"] = ("Good morning. My name is Sarah Hall, and this is my colleague, David Price. "
                  "And your name is?")
    L["q"] = ([f"Thank you. First of all, we'd like to know something about you. {qs[0]['q']}"] +
              [x["q"] for x in qs[1:]])
    L["p1_end"] = "Thank you."
    L["p2_intro"] = (f"Now, in this part of the test, you're going to do something together. Here are some "
                     f"pictures of {p2['intro']}.")
    L["p2_q1"] = (f"First, I'd like you to look at pictures {a} and {b} and talk together about {p2['q1']}. "
                  "You have about a minute for this, so don't worry if I interrupt you.")
    L["p2_mid"] = f"Thank you. Now look at all the pictures. {p2['context']}"
    L["p2_task"] = f"{p2['task']} You have about three minutes to talk about this."
    L["p2_end"] = "Thank you. Can I have the booklet, please?"
    L["p3_intro"] = ("Now, in this part of the test, you're each going to talk on your own for about two minutes. "
                     "You need to listen while your partner is speaking, because you'll be asked to comment "
                     "afterwards.")
    L["p3_cardA"] = ("So, I'm going to give you a card with a question written on it, and I'd like you to tell "
                     "us what you think. There are also some ideas on the card for you to use if you like. All "
                     "right? Here is your card. It's card A. Remember, you have about two minutes to talk before "
                     "we join in.")
    L["begin"] = "Would you like to begin now?"
    L["thanks"] = "Thank you."
    L["p3_cardB"] = ("Now, it's your turn to be given a question. Here is your card. It's card B. Remember, you "
                     "have about two minutes to tell us what you think, and there are some ideas on the card for "
                     "you to use if you like. All right?")
    L["fuA"] = p3["cards"][0]["follow_up"]["q"]
    L["fuB"] = p3["cards"][1]["follow_up"]["q"]
    L["disc_intro"] = f"Now, to finish the test, we're going to talk about {p3['theme']} in general."
    L["disc"] = [d["q"] for d in p3["discussion"]]
    L["end"] = "Thank you. That is the end of the test."
    return L


def _partner_turns(spec):
    v = spec["p2"]["partner_voice"]
    return [[(v, t["text"])] for t in spec["p2"]["partner"]]


def build_events(spec):
    """Eventos para lst_audio.render y el guion legible (lista de (quien, texto o segundos, nota))."""
    L = _say_lines(spec)
    turns = _partner_turns(spec)
    dur = [A.build_recording(t, PARTNER_WPM)["total_s"] for t in turns]
    g1_0 = 25.0
    g1_1 = PHASE1_S - g1_0 - dur[0]
    sp2 = sum(dur[1:])
    g2_0 = 25.0
    rest = (PHASE2_S - g2_0 - sp2) / 4
    gaps2 = [g2_0, rest, rest, rest, rest]
    if g1_1 < 15 or rest < 20:
        raise ValueError(f"Huecos demasiado cortos: fase 1 {g1_1:.1f} s, fase 2 {rest:.1f} s")
    ev, script = [], []

    def S_(key, text=None):
        t = text if text is not None else L[key]
        ev.append(A.say(t)); script.append(("Interlocutor", t, ""))

    def Z(s, note):
        ev.append(A.pause(s)); script.append(("—", s, note))

    def MK(lbl):
        ev.append(A.mark(lbl))

    ev += [A.say(L["open"]), A.pause(2)]
    MK("Part 1 · Interview")
    S_("hello"); Z(4, "tu nombre")
    for i, (q, ps) in enumerate(zip(L["q"], PAUSES_P1)):
        S_(None, q); Z(ps, "tu respuesta")
    S_("p1_end")
    MK("Part 2 · Fase 1 (un minuto)")
    S_("p2_intro"); S_("p2_q1")
    Z(g1_0, "empiezas tú")
    ev.append(A.rec("PT1", turns[0], PARTNER_WPM, "Compañero 1")); script.append(("Compañero", turns[0][0][1], "1"))
    Z(g1_1, "tu turno")
    MK("Part 2 · Fase 2 (tres minutos)")
    S_("p2_mid"); S_("p2_task")
    for k in range(4):
        Z(gaps2[k], "empiezas tú" if k == 0 else "tu turno")
        ev.append(A.rec(f"PT{k + 2}", turns[k + 1], PARTNER_WPM, f"Compañero {k + 2}"))
        script.append(("Compañero", turns[k + 1][0][1], str(k + 2)))
    Z(gaps2[4], "tu turno: cerrad la decisión")
    S_("p2_end")
    MK("Part 3 · Tarjeta A")
    S_("p3_intro"); S_("p3_cardA"); Z(PREP_S, "preparas"); S_("begin"); Z(LONG_TURN_S, "long turn A")
    S_("thanks"); S_("fuA"); Z(FOLLOW_S, "pregunta de seguimiento"); S_("thanks")
    MK("Part 3 · Tarjeta B")
    S_("p3_cardB"); Z(PREP_S, "preparas"); S_("begin"); Z(LONG_TURN_S, "long turn B")
    S_("thanks"); S_("fuB"); Z(FOLLOW_S, "pregunta de seguimiento"); S_("thanks")
    MK("Part 3 · Discusión")
    S_("disc_intro")
    for q in L["disc"]:
        S_(None, q); Z(DISC_S, "tu respuesta")
    S_("end")
    MK("Fin")
    return ev, script, {"phase1_gaps": [g1_0, round(g1_1, 1)], "phase2_gaps": [round(g, 1) for g in gaps2],
                        "partner_s": dur}


def render_audio(spec, out_mp3):
    A.setup()
    A.NARRATOR = INTERLOCUTOR
    ev, script, plan = build_events(spec)
    rep = A.render(ev, out_mp3)
    # tiempos del guion legible a partir de la linea de tiempo
    tl = [x for x in rep["timeline"] if x[1] != "mark"][2:]   # sin la identificacion inicial
    timed = []
    for (t0, kind, lab), (who, txt, note) in zip(tl, script):
        timed.append((t0, who, txt, note))
    marks = [(t, lab) for t, k, lab in rep["timeline"] if k == "mark"]
    rep["script"], rep["marks"], rep["plan"] = timed, marks, plan
    return rep


def check_audio(spec, rep):
    errs, info = [], {}
    mk = dict((lab, t) for t, lab in rep["marks"])
    ph1 = mk["Part 2 · Fase 2 (tres minutos)"] - mk["Part 2 · Fase 1 (un minuto)"]
    info["fases"] = rep["plan"]
    # duraciones de las fases medidas sobre el guion: desde el fin de la instruccion hasta la siguiente
    s = rep["script"]
    def span(i0, i1): return s[i1][0] - s[i0][0]
    idx = [i for i, x in enumerate(s) if x[1] == "Interlocutor"]
    p1q = next(i for i, x in enumerate(s) if x[2] == _say_lines(spec)["p2_q1"])
    mid = next(i for i, x in enumerate(s) if x[2] == _say_lines(spec)["p2_mid"])
    task = next(i for i, x in enumerate(s) if x[2] == _say_lines(spec)["p2_task"])
    end2 = next(i for i, x in enumerate(s) if x[2] == _say_lines(spec)["p2_end"])
    f1 = s[mid][0] - (s[p1q + 1][0])
    f2 = s[end2][0] - (s[task + 1][0])
    info["fase1_s"], info["fase2_s"] = round(f1, 1), round(f2, 1)
    if abs(f1 - PHASE1_S) > 1.5 or abs(f2 - PHASE2_S) > 1.5:
        errs.append(f"duración de fases: {f1:.1f} / {f2:.1f} s")
    # reconocimiento de voz: companero
    for k, t in enumerate(spec["p2"]["partner"], 1):
        r = A.check_recording(rep["recs"][f"PT{k}"]["wav"], t["text"])
        info[f"PT{k}"] = r["sim"]
        if not r["ok"]:
            errs.append(f"compañero {k}: parecido {r['sim']} · ASR: {r['asr']}")
    # reconocimiento de voz: lineas del interlocutor
    lines = sorted({x[2] for x in s if x[1] == "Interlocutor"})
    wavs = A.synth([(t, INTERLOCUTOR, rep["narrator_rate"]) for t in lines])
    worst = 1.0
    for t, w in zip(lines, wavs):
        r = A.check_recording(w, t, min_sim=0.85)
        worst = min(worst, r["sim"])
        if not r["ok"]:
            errs.append(f"interlocutor: parecido {r['sim']} en «{t[:50]}» · ASR: {r['asr']}")
    info["interlocutor_min_sim"] = worst
    info["duracion_s"] = rep["duration_s"]
    return errs, info


# ---------- verificacion del contenido ----------
def _english_fields(spec):
    p1, p2, p3 = spec["p1"], spec["p2"], spec["p3"]
    xs = [q["q"] for q in p1["questions"]] + [q["model"] or "" for q in p1["questions"]]
    xs += [p2["title"], p2["intro"], p2["q1"], p2["context"], p2["task"]] + p2["phase1_lines"] + p2["language"]
    xs += [t["text"] for t in p2["partner"]] + [t["react"] for t in p2["partner"]]
    for c in p3["cards"]:
        xs += [c["q"], c["follow_up"]["q"]] + c["ideas"] + c["model"]
    xs += [d["q"] for d in p3["discussion"]] + [d["lang"] for d in p3["discussion"]]
    return xs


def _all_spanish(spec):
    p2, p3 = spec["p2"], spec["p3"]
    xs = [spec["subtitle"], p2["decision"]]
    for ph in p2["photos"]:
        xs += [ph["what"], ph["spec"], ph["offers"], ph["decision"]]
    xs += [t["provokes"] for t in p2["partner"]]
    for c in p3["cards"]:
        xs += list(c["plan"].values()) + c["comments"] + [c["follow_up"]["ideas"]]
    xs += [d["ideas"] for d in p3["discussion"]]
    return xs


def verify(spec):
    errs, info = [], {}
    p1, p2, p3 = spec["p1"], spec["p2"], spec["p3"]
    qs = p1["questions"]
    if len(qs) != 5:
        errs.append("Part 1: hacen falta 5 preguntas")
    for i, q in enumerate(qs[2:], 3):
        if not q.get("model") or not 35 <= WC(q["model"]) <= 75:
            errs.append(f"Part 1 pregunta {i}: respuesta posible de 35-75 palabras ({WC(q.get('model') or '')})")
    letters = [ph["letter"] for ph in p2["photos"]]
    if letters != list("ABCDE"[:len(letters)]) or not 4 <= len(letters) <= 5:
        errs.append(f"Part 2: letras de fotos {letters}")
    if any(l not in letters for l in p2["q1_pics"]) or len(p2["q1_pics"]) != 2:
        errs.append("Part 2: q1_pics")
    if len(p2["partner"]) != 5:
        errs.append("Part 2: hacen falta 5 intervenciones del compañero")
    for k, t in enumerate(p2["partner"], 1):
        if not 18 <= WC(t["text"]) <= 50:
            errs.append(f"compañero {k}: {WC(t['text'])} palabras (18-50)")
        for s in t["theory"]:
            if s not in THEORY:
                errs.append(f"compañero {k}: sección {s}")
    if len(p3["cards"]) != 2:
        errs.append("Part 3: dos tarjetas")
    for c, lab in zip(p3["cards"], "AB"):
        n = WC(" ".join(c["model"]))
        info[f"long turn {lab}"] = n
        if not 250 <= n <= 320:
            errs.append(f"tarjeta {lab}: {n} palabras (250-320)")
        if len(c["ideas"]) != 3:
            errs.append(f"tarjeta {lab}: tres ideas")
        if len(c["comments"]) != len(c["model"]) or not 4 <= len(c["model"]) <= 6:
            errs.append(f"tarjeta {lab}: comentarios por párrafo / 4-6 párrafos")
        for k in ("Operación", "Postura", "Línea 1", "Línea 2", "Contrapunto", "Cierre"):
            if k not in c["plan"]:
                errs.append(f"tarjeta {lab}: plan sin {k}")
    if len(p3["discussion"]) != 6:
        errs.append("discusión: 6 preguntas")
    for d in p3["discussion"]:
        if not d.get("theory") or any(x not in THEORY for x in d["theory"]):
            errs.append(f"discusión: secciones de teoría en «{d['q'][:30]}»")
    for x in _english_fields(spec):
        for m in AMERICAN.findall(x):
            errs.append(f"ortografía americana: {m}")
    for x in _all_spanish(spec) + [t["react"] for t in p2["partner"]]:
        for s in re.findall(r"§(\d+(?:\.\d+)?)", x):
            if s not in THEORY:
                errs.append(f"sección inexistente §{s}")
        if x.count("[[") != x.count("]]"):
            errs.append(f"marcado sin cerrar: {x[:40]}")
    for ph in p2["photos"]:
        if not ph.get("_info", {}).get("lic_ok", False):
            errs.append(f"foto {ph['letter']}: licencia no válida o sin comprobar")
    return errs, info


# ---------- PDF ----------
def _theory_note():
    return P(f"Los números de sección remiten a {THEORY_DOC}.")


def front_flowables(spec, rep):
    n = spec["num"]
    out = title_block(f"SPK · Práctica {n}", "Speaking test completo", spec["subtitle"],
                      f"Unos {round(rep['duration_s'] / 60)} minutos con el MP3 SPK_Practica_{n}.mp3 · "
                      "sin consultar la teoría")
    out.append(h2("Cómo hacer el test"))
    out += numbered([M(x) for x in [
        "Ten delante solo el material del candidato (págs. 2 y 3). Las preguntas de la Part 1, las instrucciones "
        "de la Part 2 y las de la discusión solo se oyen.",
        "Pon a grabar el móvil y reproduce el MP3 de principio a fin, sin pausar. Los silencios están "
        "cronometrados; el [[Thank you]] del interlocutor marca el final de cada respuesta.",
        "Part 2: empiezas tú cada fase. El compañero interviene en momentos fijos y no te escucha (§1.4): habla "
        "unos 20 segundos por turno y reacciona a lo que dice cuando termine.",
        "Part 3: respondes las dos tarjetas y las dos preguntas de seguimiento, y luego las seis de la discusión.",
        "Al día siguiente, corrige con la hoja de autocorrección y solo después mira las soluciones (§8.1).",
    ]])
    out.append(h2("Mapa del MP3"))
    rows = [["Minuto", "Parte"]]
    for t, lab in rep["marks"]:
        rows.append([mmss(t), lab])
    out += T(rows, [30, 140])
    return out


def cards_flowables(spec):
    p3 = spec["p3"]
    out = [h2("Part 3 · Tarjetas")]
    for c, lab in zip(p3["cards"], "AB"):
        out += card(c["q"], c["ideas"], f"TARJETA {lab}")
    out.append(P("En el examen cada candidato recibe solo su tarjeta. Aquí haces las dos, una detrás de otra."))
    return out


def answer_sheet_flowables(spec):
    yn = '<font color="#5B6577">Sí · No</font>'
    out = [h2("Hoja de autocorrección"),
           P(f"Escucha la grabación al día siguiente y marca la rúbrica antes de mirar las soluciones (preguntas "
             f"completas en {THEORY_DOC} §8.2). Nota por criterio: 5 las cinco sí · 4 sí a las cuatro primeras · 3 "
             f"falla una de las cuatro primeras · 2 fallan dos · 1 fallan tres o cuatro. GA: la fila de §8.2 que "
             f"mejor describa un minuto cualquiera de la Part 3. (*) IC3 solo se valora del todo con un compañero "
             f"real.")]
    out += T([["Dato", "Tu resultado"],
              ["Long turn A: palabras transcritas y duración", "________ palabras · ____:____ (objetivo: 250+ · 2:00)"],
              ["Long turn B: palabras transcritas y duración", "________ palabras · ____:____ (objetivo: 250+ · 2:00)"],
              ["Part 2: ¿llegaste a una decisión negociada?", "Sí · No"],
              ["Part 2: reacciones al compañero que recogían lo que había dicho", "____ / 5"],
              ["<b>Notas</b> (§8.2–8.3)", "GR __ · LR __ · DM __ · PR __ · IC __ · GA __ · <b>total __ / 30</b>"]],
             [80, 90], zebra=False, extra=[("TOPPADDING", (0, 1), (-1, -1), 2.5),
                                          ("BOTTOMPADDING", (0, 1), (-1, -1), 2.5)])
    rows, shade = [["Código", "Pregunta", ""]], []
    for crit, qs in RUBRIC:
        rows.append([f"<b>{crit}</b>", "", ""])
        shade.append(len(rows) - 1)
        rows += [[c, q, yn] for c, q in qs]
    extra = [("BACKGROUND", (0, r), (-1, r), ZEBRA) for r in shade] + [("SPAN", (0, r), (-1, r)) for r in shade]
    extra += [("TOPPADDING", (0, 1), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 1), (-1, -1), 1.5)]
    out += table(rows, [20, 126, 24], zebra=False, extra=extra)
    return out


def script_flowables(spec, rep):
    out = [h2("Guion del MP3"),
           P("Transcripción completa. Los silencios llevan entre corchetes lo que te tocaba hacer en ellos; las "
             "intervenciones del compañero van numeradas como en la tabla de la Part 2.")]
    rows = [["Minuto", "Quién", "Texto"]]
    for t, who, txt, note in rep["script"]:
        if who == "—":
            rows.append([mmss(t), "", f"<i>[silencio · {int(round(txt))} s · {note}]</i>"])
        else:
            lab = "Interlocutor" if who == "Interlocutor" else f"<b>Compañero {note}</b>"
            rows.append([mmss(t), lab, E(txt)])
    out += table(rows, [16, 26, 128], extra=[("TOPPADDING", (0, 1), (-1, -1), 2.5),
                                             ("BOTTOMPADDING", (0, 1), (-1, -1), 2.5)])
    return out


def solutions_flowables(spec, rep):
    p1, p2, p3 = spec["p1"], spec["p2"], spec["p3"]
    out = solutions_start("Soluciones")
    out.append(P(f"No hay una única respuesta correcta: estas soluciones dan ideas, lenguaje y modelos que apuntan "
                 f"a la banda 5. Los números de sección remiten a {THEORY_DOC}."))
    out += script_flowables(spec, rep)
    # Part 1
    out.append(CondPageBreak(60 * mm))
    out.append(h2("Part 1 · Respuestas posibles"))
    out.append(P("Respuesta, razón o caso y matiz, en 20–30 segundos (§2)."))
    out += T([["Pregunta", "Una respuesta posible"]] +
             [[E(q["q"]), E(q["model"])] for q in p1["questions"][2:]], [52, 118])
    # Part 2
    out.append(CondPageBreak(60 * mm))
    a, b = p2["q1_pics"]
    out.append(h2("Part 2 · Fase 1"))
    out.append(P(f"Pregunta: [[{p2['q1'][0].upper() + p2['q1'][1:]}]] (fotos {a} y {b}). Hay que especular, no "
                 "describir (§5.2)."))
    ph = {x["letter"]: x for x in p2["photos"]}
    out += T([["Foto", "Qué se ve", "Qué se puede especular"]] +
             [[f"<b>{l}</b>", ph[l]["what"], ph[l]["spec"]] for l in (a, b)], [14, 60, 96])
    out.append(P("<b>Cómo puede sonar:</b> " + " · ".join(f"[[{x}]]" for x in p2["phase1_lines"])))
    out.append(CondPageBreak(60 * mm))
    out.append(h2("Part 2 · Fase 2"))
    out.append(P(f"Contexto: [[{p2['context']}]] Tarea: [[{p2['task']}]] Empieza fijando el criterio (§5.3)."))
    out += T([["Foto", "Qué ofrece o qué dice", "Para la decisión"]] +
             [[f"<b>{x['letter']}</b>", x["offers"], x["decision"]] for x in p2["photos"]], [14, 78, 78])
    out.append(P("<b>Una decisión posible:</b> " + p2["decision"]))
    out.append(P("<b>Lenguaje para esta tarea:</b> " + " · ".join(f"[[{x}]]" for x in p2["language"])))
    out.append(CondPageBreak(70 * mm))
    out.append(h2("Las intervenciones del compañero"))
    out.append(P("Cada intervención está pensada para provocar una reacción de §6. La reacción propuesta es una "
                 "entre varias posibles: lo que cuenta es recoger lo que ha dicho antes de añadir lo tuyo (§6.2)."))
    rows = [["Nº", "El compañero dice", "Qué provoca", "Una reacción posible"]]
    for k, t in enumerate(p2["partner"], 1):
        rows.append([f"<b>{k}</b>", E(t["text"]), M(t["provokes"]) + " " + " · ".join(f"§{s}" for s in t["theory"]),
                     E(t["react"])])
    out += table(rows, [9, 58, 41, 62])
    # Part 3
    for c, lab in zip(p3["cards"], "AB"):
        out.append(CondPageBreak(90 * mm))
        out.append(h2(f"Part 3 · Tarjeta {lab}"))
        out.append(Paragraph(EB(c["q"]) + E("  (" + " · ".join(c["ideas"]) + ")"), S["body"]))
        out += T([["Decisión", "Plan de diez segundos (§3.2)"]] + [[f"<b>{k}</b>", v] for k, v in c["plan"].items()],
                 [32, 138])
        n = WC(" ".join(c["model"]))
        paras = [Paragraph(_PNUM.format(i) + t, _spoken) for i, t in enumerate(c["model"], 1)]
        out += callout("ejemplo", paras, label=f"LONG TURN MODELO · {n} PALABRAS · UNOS DOS MINUTOS A {WPM_MODEL} "
                                               "PALABRAS POR MINUTO")
        rows, acc = [["Tramo", "Tiempo", "Qué hace y con qué recursos"]], 0
        for i, (t, cm) in enumerate(zip(c["model"], c["comments"]), 1):
            w = WC(t)
            rows.append([f"<b>{i}</b>", f"{mmss(acc / WPM_MODEL * 60)}–{mmss((acc + w) / WPM_MODEL * 60)}", M(cm)])
            acc += w
        out += table(rows, [14, 24, 132])
        out.append(P(f"<b>Pregunta de seguimiento:</b> [[{c['follow_up']['q']}]] {c['follow_up']['ideas']} (§3.7)"))
    # discussion
    out.append(CondPageBreak(70 * mm))
    out.append(h2(f"Part 3 · Discusión: {E(p3['theme'])}"))
    out.append(P("Respuestas de 30–45 segundos: postura, razón y caso, sin convertirlas en otro long turn (§6.7)."))
    out += T([["Pregunta", "Ideas", "Cómo puede sonar"]] +
             [[E(d["q"]), M(d["ideas"]) + " " + " · ".join(f"§{x}" for x in d["theory"]), E(d["lang"])]
              for d in p3["discussion"]], [48, 64, 58])
    return out


def build_pdf(spec, rep, out_pdf):
    n = spec["num"]
    story = front_flowables(spec, rep)
    story.append(PageBreak())
    story += visuals_flowables(spec)
    story.append(PageBreak())
    story += cards_flowables(spec)
    story.append(PageBreak())
    story += answer_sheet_flowables(spec)
    story += solutions_flowables(spec, rep)
    build(out_pdf, story, f"SPK · Práctica {n}", f"SPK_Practica_{n}.pdf", title=f"SPK · Práctica {n}")
    return story


def check_pdf(path, story):
    import subprocess
    from fontTools.ttLib import TTFont
    txt = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout
    errs = [f"resto de marcado: {m}" for m in re.findall(r"\[\[|\]\]|<font|&lt;|&gt;", txt)]
    cm = {k: TTFont(v).getBestCmap() for k, v in _F.items()}

    def walk(f):
        if isinstance(f, Paragraph):
            yield f
        elif isinstance(f, Table):
            for row in f._cellvalues:
                for cell in row:
                    for x in (cell if isinstance(cell, (list, tuple)) else [cell]):
                        yield from walk(x)
        elif hasattr(f, "_content"):
            for x in f._content:
                yield from walk(x)
    miss = set()
    for fl in story:
        for par in walk(fl):
            for fr in par.frags:
                for ch in getattr(fr, "text", ""):
                    if ch.strip() and ord(ch) not in cm.get(fr.fontName, cm["Sans"]):
                        miss.add((fr.fontName, ch))
    if miss:
        errs.append(f"glifos ausentes: {miss}")
    return errs


def make(spec, out_dir="/mnt/user-data/outputs", audio=True):
    n = spec["num"]
    for ph in spec["p2"]["photos"]:
        ph["_info"] = photo_info(ph["file"])
    errs, info = verify(spec)
    if errs:
        raise ValueError(f"Hoja {n}:\n  - " + "\n  - ".join(errs))
    mp3 = os.path.join(out_dir, f"SPK_Practica_{n}.mp3")
    rep = render_audio(spec, mp3)
    aerrs, ainfo = check_audio(spec, rep)
    if aerrs:
        raise ValueError(f"Audio {n}:\n  - " + "\n  - ".join(aerrs))
    pdf = os.path.join(out_dir, f"SPK_Practica_{n}.pdf")
    story = build_pdf(spec, rep, pdf)
    perrs = check_pdf(pdf, story)
    if perrs:
        raise ValueError(f"PDF {n}:\n  - " + "\n  - ".join(perrs))
    info.update(ainfo)
    return pdf, mp3, info


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 gen_SPK.py spk_specs.py [carpeta_salida] [num ...]")
        sys.exit(1)
    ns = {}
    exec(open(sys.argv[1]).read(), ns)
    out = sys.argv[2] if len(sys.argv) > 2 else "/mnt/user-data/outputs"
    want = set(sys.argv[3:])
    os.makedirs(out, exist_ok=True)
    for sp in ns["SPECS"]:
        if want and sp["num"] not in want:
            continue
        pdf, mp3, info = make(sp, out)
        print(pdf, mp3, json.dumps(info, ensure_ascii=False, default=str))
