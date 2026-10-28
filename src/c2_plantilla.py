# c2_plantilla.py · Plantilla visual del proyecto C2 Proficiency (v1.1: fuentes desde fonts/)
# Uso: from c2_plantilla import *   ->  story = [...]; build(ruta, story, cabecera, pie)
# Convencion: explicaciones en espanol con fuente sans (Carlito);
# todo lo que esta en ingles va en serif (Caladea) mediante en() / estilo 'en'.

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                CondPageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas

# ---------- Fuentes ----------
_F = {
    "Sans": "/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf",
    "Sans-B": "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf",
    "Sans-I": "/usr/share/fonts/truetype/crosextra/Carlito-Italic.ttf",
    "Sans-BI": "/usr/share/fonts/truetype/crosextra/Carlito-BoldItalic.ttf",
    "EN": "/usr/share/fonts/truetype/crosextra/Caladea-Regular.ttf",
    "EN-B": "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf",
    "EN-I": "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf",
    "EN-BI": "/usr/share/fonts/truetype/crosextra/Caladea-BoldItalic.ttf",
    "Head": "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf",
    "Head-L": "/usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf",
}
# Las fuentes se buscan primero en la carpeta fonts/ del repositorio (junto a src/) y, si no, en el sistema.
import os as _os
_FONT_DIRS = [_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "fonts"),
              _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "fonts"),
              _os.environ.get("C2_FONTS", "")]


def _font_path(sys_path):
    name = _os.path.basename(sys_path)
    for d in _FONT_DIRS:
        if d and _os.path.exists(_os.path.join(d, name)):
            return _os.path.join(d, name)
    return sys_path


for _n, _p in _F.items():
    pdfmetrics.registerFont(TTFont(_n, _font_path(_p)))
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-B", italic="Sans-I", boldItalic="Sans-BI")
pdfmetrics.registerFontFamily("EN", normal="EN", bold="EN-B", italic="EN-I", boldItalic="EN-BI")

# ---------- Colores ----------
NAVY = colors.HexColor("#1B2A41")
INK = colors.HexColor("#1E2633")
GREY = colors.HexColor("#5B6577")
RULE = colors.HexColor("#D5DCE6")
ZEBRA = colors.HexColor("#F5F7FA")
ACCENT = colors.HexColor("#A4243B")       # granate C2
TEAL = colors.HexColor("#1F7A6E")
BG_CLAVE = colors.HexColor("#EEF2F7")
BG_OJO = colors.HexColor("#FBEFF1")
BG_EST = colors.HexColor("#E9F5F3")
BG_EJ = colors.HexColor("#FAF8F3")

CALLOUTS = {  # tipo: (etiqueta, color barra, fondo)
    "clave": ("CLAVE", NAVY, BG_CLAVE),
    "ojo": ("OJO · TRAMPA TÍPICA", ACCENT, BG_OJO),
    "estrategia": ("ESTRATEGIA DE EXAMEN", TEAL, BG_EST),
    "ejemplo": ("EJEMPLO", GREY, BG_EJ),
}

# ---------- Estilos ----------
PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 20 * mm, 20 * mm, 24 * mm, 20 * mm
CONTENT_W = PAGE_W - ML - MR

S = {
    "body": ParagraphStyle("body", fontName="Sans", fontSize=10.5, leading=14.6, textColor=INK, spaceAfter=6),
    "en": ParagraphStyle("en", fontName="EN", fontSize=10.5, leading=14.6, textColor=INK, spaceAfter=6),
    "h1": ParagraphStyle("h1", fontName="Head", fontSize=14, leading=18, textColor=NAVY, spaceBefore=14, spaceAfter=6, keepWithNext=1),
    "h2": ParagraphStyle("h2", fontName="Head", fontSize=11.5, leading=15, textColor=NAVY, spaceBefore=10, spaceAfter=4, keepWithNext=1),
    "h3": ParagraphStyle("h3", fontName="Sans-B", fontSize=10.5, leading=14, textColor=INK, spaceBefore=6, spaceAfter=2, keepWithNext=1),
    "title": ParagraphStyle("title", fontName="Head", fontSize=22, leading=27, textColor=NAVY, spaceAfter=4),
    "subtitle": ParagraphStyle("subtitle", fontName="Sans", fontSize=12.5, leading=16, textColor=GREY, spaceAfter=4),
    "code": ParagraphStyle("code", fontName="Head", fontSize=8, leading=10, textColor=ACCENT, spaceAfter=6),
    "meta": ParagraphStyle("meta", fontName="Sans", fontSize=9, leading=12, textColor=GREY),
    "small": ParagraphStyle("small", fontName="Sans", fontSize=9, leading=12, textColor=GREY, spaceAfter=4),
    "label": ParagraphStyle("label", fontName="Head", fontSize=7.5, leading=10, spaceAfter=3),
    "cell": ParagraphStyle("cell", fontName="Sans", fontSize=9.5, leading=12.4, textColor=INK),
    "cell_en": ParagraphStyle("cell_en", fontName="EN", fontSize=9.5, leading=12.4, textColor=INK),
    "th": ParagraphStyle("th", fontName="Head", fontSize=8.2, leading=10.5, textColor=colors.white),
    "bullet": ParagraphStyle("bullet", fontName="Sans", fontSize=10.5, leading=14.6, textColor=INK,
                             leftIndent=14, bulletIndent=3, spaceAfter=3),
    "banner": ParagraphStyle("banner", fontName="Head", fontSize=13, leading=16, textColor=colors.white),
}

# ---------- Bloques ----------
def title_block(code, title, subtitle=None, meta=None):
    out = [Paragraph(code.upper(), S["code"]), Paragraph(title, S["title"])]
    if subtitle:
        out.append(Paragraph(subtitle, S["subtitle"]))
    if meta:
        out.append(Paragraph(meta, S["meta"]))
    line = Table([[""]], colWidths=[CONTENT_W], rowHeights=[2])
    line.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.2, NAVY)]))
    out += [Spacer(1, 6), line, Spacer(1, 8)]
    return out

def h1(text, num=None):
    t = f'<font color="#A4243B">{num}</font>&nbsp;&nbsp;{text}' if num is not None else text
    return [CondPageBreak(40 * mm), Paragraph(t, S["h1"])]

def h2(text):
    return Paragraph(text, S["h2"])

def h3(text):
    return Paragraph(text, S["h3"])

def p(text):
    return Paragraph(text, S["body"])

def en(text):
    return Paragraph(text, S["en"])

def bullets(items, style="bullet"):
    return [Paragraph(i, S[style], bulletText="•") for i in items]

def numbered(items, style="bullet"):
    return [Paragraph(i, S[style], bulletText=f"{k}.") for k, i in enumerate(items, 1)]

def _as_flowables(content, style="body"):
    if isinstance(content, str):
        return [Paragraph(content, S[style])]
    return list(content)

def callout(kind, content, label=None):
    lab, bar, bg = CALLOUTS[kind]
    lab = label or lab
    lab_style = ParagraphStyle("lab_" + kind, parent=S["label"], textColor=bar)
    inner = [Paragraph(lab, lab_style)] + _as_flowables(content)
    t = Table([["", inner]], colWidths=[1.8 * mm, CONTENT_W - 1.8 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), bar),
        ("BACKGROUND", (1, 0), (1, 0), bg),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (1, 0), (1, 0), 9), ("RIGHTPADDING", (1, 0), (1, 0), 9),
        ("TOPPADDING", (1, 0), (1, 0), 7), ("BOTTOMPADDING", (1, 0), (1, 0), 4),
        ("LEFTPADDING", (0, 0), (0, 0), 0), ("RIGHTPADDING", (0, 0), (0, 0), 0),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 8)]

def table(rows, col_widths, header=True, en_cols=(), zebra=True, extra=None):
    """rows: lista de filas (strings o flowables). col_widths en mm.
    en_cols: indices de columnas cuyo contenido esta en ingles (serif)."""
    data = []
    for r_i, row in enumerate(rows):
        new = []
        for c_i, cell in enumerate(row):
            if isinstance(cell, str):
                if header and r_i == 0:
                    cell = Paragraph(cell, S["th"])
                else:
                    cell = Paragraph(cell, S["cell_en"] if c_i in en_cols else S["cell"])
            new.append(cell)
        data.append(new)
    t = Table(data, colWidths=[w * mm for w in col_widths], repeatRows=1 if header else 0)
    st = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
    ]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), NAVY), ("LINEBELOW", (0, 0), (-1, 0), 0, NAVY)]
    if zebra:
        start = 1 if header else 0
        for i in range(start, len(data)):
            if (i - start) % 2 == 1:
                st.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    if extra:
        st += extra
    t.setStyle(TableStyle(st))
    return [t, Spacer(1, 8)]

def solutions_start(title="Soluciones"):
    """Salto de pagina + banda de soluciones (siempre al final del mismo PDF)."""
    band = Table([[Paragraph(title.upper(), S["banner"])]], colWidths=[CONTENT_W])
    band.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return [PageBreak(), band, Spacer(1, 10)]

# ---------- Cabecera, pie y numeracion "pag. X de Y" ----------
def _make_canvas(header_right, footer_left):
    class NumberedCanvas(rl_canvas.Canvas):
        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self._pages = []

        def showPage(self):
            self._pages.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            total = len(self._pages)
            for st in self._pages:
                self.__dict__.update(st)
                self._decorate(total)
                super().showPage()
            super().save()

        def _decorate(self, total):
            y_top = PAGE_H - 13 * mm
            self.setFont("Head", 6.8)
            self.setFillColor(GREY)
            self.drawString(ML, y_top, "CAMBRIDGE C2 PROFICIENCY  ·  MATERIAL DE PREPARACIÓN")
            self.setFillColor(ACCENT)
            self.drawRightString(PAGE_W - MR, y_top, header_right.upper())
            self.setStrokeColor(RULE)
            self.setLineWidth(0.6)
            self.line(ML, y_top - 2.8 * mm, PAGE_W - MR, y_top - 2.8 * mm)
            y_bot = 11 * mm
            self.line(ML, y_bot + 4 * mm, PAGE_W - MR, y_bot + 4 * mm)
            self.setFont("Sans", 7.8)
            self.setFillColor(GREY)
            self.drawString(ML, y_bot, footer_left)
            self.drawRightString(PAGE_W - MR, y_bot, f"pág. {self._pageNumber} de {total}")
    return NumberedCanvas

def build(path, story, header_right, footer_left, title=None):
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=ML, rightMargin=MR,
                          topMargin=MT, bottomMargin=MB, title=title or footer_left,
                          author="Proyecto C2 Proficiency")
    frame = Frame(ML, MB, CONTENT_W, PAGE_H - MT - MB, id="f", leftPadding=0,
                  rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame])])
    doc.build(story, canvasmaker=_make_canvas(header_right, footer_left))
