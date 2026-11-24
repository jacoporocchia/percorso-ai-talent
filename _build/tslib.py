"""Deck 'Percorso AI per Talent' sul template TeamSystem (layout ufficiali + forme in palette brand)."""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
BLU, BLU2, CEL, FUX, MAG, ARA, TXT, BG2, GREY = '15428E', '1860A8', '0A9BD7', 'E52E70', 'C10B6A', 'EB684A', '0E2841', 'EEF4FA', '5B6B7F'
rgb = lambda h: RGBColor.from_string(h)

p = Presentation(TEMPLATE)
lst = p.slides._sldIdLst
for sid in list(lst):
    p.part.drop_rel(sid.rId); lst.remove(sid)
L = {l.name: l for l in p.slide_masters[0].slide_layouts}


def slide(layout, fills, notes=None, widen=None):
    s = p.slides.add_slide(L[layout])
    for ph in list(s.placeholders):
        idx = ph.placeholder_format.idx
        if idx in fills:
            ph.text_frame.text = fills[idx]
            if widen and idx in widen:
                ph.width = Inches(widen[idx])
        elif ph.placeholder_format.type is not None and 'SLIDE_NUMBER' in str(ph.placeholder_format.type):
            continue
        else:
            ph._element.getparent().remove(ph._element)
    if notes:
        s.notes_slide.notes_text_frame.text = notes
    return s


def box(s, x, y, w, h, fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.06):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    sh.line.fill.background(); sh.shadow.inherit = False
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = adj
    return sh


def text(s, x, y, w, h, runs, size=15, color=TXT, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    if isinstance(runs, str):
        runs = [[(runs, {})]]
    elif runs and isinstance(runs[0], tuple):
        runs = [runs]
    for i, para in enumerate(runs):
        pa = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        pa.alignment = align
        if i: pa.space_before = Pt(6)
        for t, o in para:
            r = pa.add_run(); r.text = t
            f = r.font; f.name = 'Roboto'; f.size = Pt(o.get('size', size))
            f.bold = o.get('bold', bold); f.italic = o.get('italic', italic)
            f.color.rgb = rgb(o.get('color', color))
    return tb


def bullets(s, x, y, w, h, items, size=16, color=TXT, gap=8):
    from pptx.oxml.ns import qn
    from lxml import etree
    tb = text(s, x, y, w, h, [[(t, {})] for t in items], size=size, color=color)
    for k, pa in enumerate(tb.text_frame.paragraphs):
        pa.space_before = Pt(gap if k else 0)
        pPr = pa._p.get_or_add_pPr()
        pPr.set('marL', str(int(Inches(0.28)))); pPr.set('indent', str(-int(Inches(0.28))))
        bf = etree.SubElement(pPr, qn('a:buFont')); bf.set('typeface', 'Arial')
        bc = etree.SubElement(pPr, qn('a:buChar')); bc.set('char', '•')
    return tb


def numdot(s, x, y, d, n, fill, size=22):
    box(s, x, y, d, d, fill, MSO_SHAPE.OVAL)
    text(s, x, y, d, d, str(n), size=size, color='FFFFFF', bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def arrow(s, x, y, w=0.32, h=0.42):
    box(s, x, y, w, h, FUX, MSO_SHAPE.RIGHT_ARROW)


TITLE_W = {15: 12.9}
