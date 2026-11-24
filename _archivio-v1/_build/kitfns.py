# Pattern di slide riusabili per i kit di lezione. Da eseguire dopo tslib.py (usa p, slide, box, text, ...).
COLS = [CEL, BLU2, FUX, ARA, BLU, MAG]


def band(s, y, h, runs, size=17):
    box(s, 0.3, y, 12.7, h, BG2)
    text(s, 0.6, y, 12.1, h, runs, size=size, anchor=MSO_ANCHOR.MIDDLE)


def R(label, rest, col=None):
    """Riga di band: etichetta in grassetto + testo."""
    return [(label, {'bold': True, 'color': col or BLU}), (rest, {})]


def cover(title, date):
    slide('2_Copertina-Blu', {0: title, 1: 'Percorso AI per Talent', 13: date})


def closing(q, nxt):
    slide('Chiusura-Blu', {0: q, 13: nxt})


def free(title, notes=None):
    return slide('Sezioni modificabili 2', {15: title}, widen=TITLE_W, notes=notes)


def agenda(title, items, esci, notes=None):
    s = free(title, notes)
    cols = [BLU, CEL, BLU2, FUX, ARA]
    for i, (t, h, d) in enumerate(items):
        x = 0.3 + i * 2.56
        box(s, x, 2.0, 1.35, 0.5, cols[i % 5], adj=0.5)
        text(s, x, 2.0, 1.35, 0.5, t, size=15, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x, 2.85, 2.36, 0.5, h, size=22, bold=True, color=BLU)
        text(s, x, 3.5, 2.2, 1.4, d, size=17)
    band(s, 5.3, 1.2, R('Esci con: ', esci))
    return s


def cards3(title, items, bandruns=None, notes=None, numbered=True):
    """items: (titolo, testo)"""
    s = free(title, notes)
    for i, (h, d) in enumerate(items):
        x = 0.3 + i * 4.3
        box(s, x, 1.7, 4.05, 3.4, BG2)
        if numbered:
            numdot(s, x + 0.35, 2.0, 0.75, i + 1, COLS[i])
        else:
            box(s, x, 1.7, 4.05, 0.14, COLS[i], MSO_SHAPE.RECTANGLE)
        text(s, x + 0.35, 2.95 if numbered else 2.1, 3.4, 0.9, h, size=21, bold=True, color=BLU)
        text(s, x + 0.35, 3.85 if numbered else 3.0, 3.4, 1.9 if not numbered else 1.2, d, size=16)
    if bandruns:
        band(s, 5.4, 1.15, bandruns, size=16)
    return s


def cards4(title, items, bandruns=None, notes=None, tags=None):
    s = free(title, notes)
    for i, (h, d) in enumerate(items):
        x = 0.3 + i * 3.21
        box(s, x, 1.7, 3.0, 3.25, BG2)
        box(s, x, 1.7, 3.0, 0.14, COLS[i], MSO_SHAPE.RECTANGLE)
        text(s, x + 0.3, 2.05, 2.5, 0.85, h, size=20, bold=True, color=BLU)
        text(s, x + 0.3, 2.95, 2.45, 1.95, d, size=15)
        if tags and tags[i]:
            box(s, x + 0.3, 4.35, 2.2, 0.42, COLS[i], adj=0.5)
            text(s, x + 0.3, 4.35, 2.2, 0.42, tags[i], size=12, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if bandruns:
        band(s, 5.3, 1.25, bandruns, size=16)
    return s


def cards2(title, items, bandruns=None, notes=None):
    """items: (n, titolo, sottotitolo, testo)"""
    s = free(title, notes)
    for i, (nn, h, t, d) in enumerate(items):
        x = 0.3 + i * 6.45
        box(s, x, 1.6, 6.25, 3.0, BG2)
        numdot(s, x + 0.35, 1.9, 0.75, nn, COLS[i])
        text(s, x + 1.35, 1.9, 4.7, 0.45, h, size=22, bold=True, color=BLU)
        text(s, x + 1.35, 2.35, 4.7, 0.35, t, size=15, color=GREY)
        text(s, x + 0.35, 3.0, 5.6, 1.55, d, size=17)
    if bandruns:
        band(s, 4.95, 1.6, bandruns)
    return s


def steps(title, items, bandruns=None, notes=None):
    """chevron 4-6 passi: (titolo, testo)"""
    s = free(title, notes)
    n = len(items)
    w = 12.7 / n
    for i, (h, d) in enumerate(items):
        x = 0.3 + i * w
        box(s, x, 1.8, w - 0.1, 1.0, COLS[i % 6] if n > 5 else [CEL, CEL, BLU2, BLU2, FUX][i], MSO_SHAPE.CHEVRON)
        text(s, x + 0.3, 1.8, w - 0.7, 1.0, str(i + 1), size=26, color='FFFFFF', bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x, 3.05, w - 0.2, 0.85, h, size=19 if n <= 5 else 17, bold=True, color=BLU)
        text(s, x, 3.95, w - 0.3, 1.1, d, size=16 if n <= 5 else 14)
    if bandruns:
        band(s, 5.1, 1.45, bandruns)
    return s


def rows(title, items, side=None, bandruns=None, notes=None):
    """righe con barra colorata (titolo, testo); side=(titolo, [paragrafi]) box blu a destra"""
    s = free(title, notes)
    n = len(items)
    W = 7.6 if side else 12.7
    hh = min(1.15, (3.9 - 0.15 * (n - 1)) / n)
    for i, (h, d) in enumerate(items):
        y = 1.6 + i * (hh + 0.15)
        box(s, 0.3, y, W, hh, BG2)
        box(s, 0.3, y, 0.14, hh, COLS[i % 6], MSO_SHAPE.RECTANGLE)
        text(s, 0.7, y, 2.5 if side else 3.4, hh, h, size=19, bold=True, color=BLU, anchor=MSO_ANCHOR.MIDDLE)
        text(s, 3.2 if side else 4.2, y, W - (3.05 if side else 4.05), hh, d, size=15 if side else 16, anchor=MSO_ANCHOR.MIDDLE)
    if side:
        box(s, 8.2, 1.6, 4.8, 3.9, BLU)
        text(s, 8.55, 1.85, 4.2, 0.45, side[0], size=19, bold=True, color='FFFFFF')
        text(s, 8.55, 2.45, 4.2, 2.9, [[(t, {})] for t in side[1]], size=15, color='FFFFFF')
    if bandruns:
        band(s, 5.75, 0.85, bandruns, size=16)
    return s


def compare(title, left, right, bandruns=None, notes=None, size=16):
    """left/right: (titolo, colore, [righe])"""
    s = free(title, notes)
    for i, (h, col, lines) in enumerate([left, right]):
        x = 0.3 + i * 6.45
        box(s, x, 1.55, 6.25, 0.6, col)
        text(s, x + 0.3, 1.55, 5.7, 0.6, h, size=19, bold=True, color='FFFFFF', anchor=MSO_ANCHOR.MIDDLE)
        box(s, x, 2.15, 6.25, 2.85, BG2)
        bullets(s, x + 0.3, 2.35, 5.7, 2.6, lines, size=size)
    if bandruns:
        band(s, 5.25, 1.3, bandruns)
    return s


def prompt_slide(title, label, prompt, check_title, check_text, right_title, right_items, foot=None, notes=None):
    s = free(title, notes)
    box(s, 0.3, 1.5, 6.25, 5.05, 'F2F4F7')
    text(s, 0.6, 1.65, 5.7, 0.4, label, size=15, bold=True, color=GREY)
    text(s, 0.6, 2.1, 5.75, 2.4, prompt, size=16, italic=True, color=TXT)
    box(s, 0.55, 4.55, 5.75, 1.75, 'FFFFFF')
    text(s, 0.8, 4.65, 5.3, 0.4, check_title, size=16, bold=True, color=FUX)
    text(s, 0.8, 5.1, 5.3, 1.1, check_text, size=15)
    text(s, 6.9, 1.55, 6.1, 0.45, right_title, size=17, bold=True, color=BLU)
    n = len(right_items)
    hh = min(0.95, (4.2 - 0.13 * (n - 1)) / n)
    for i, (h, d) in enumerate(right_items):
        y = 2.15 + i * (hh + 0.13)
        box(s, 6.9, y, 6.1, hh, BG2)
        numdot(s, 7.1, y + (hh - 0.55) / 2, 0.55, i + 1, COLS[i % 6], size=16)
        text(s, 7.85, y, 2.6, hh, h, size=16, bold=True, color=BLU, anchor=MSO_ANCHOR.MIDDLE)
        text(s, 10.45, y, 2.45, hh, d, size=13, anchor=MSO_ANCHOR.MIDDLE)
    if foot:
        text(s, 6.9, 6.5, 6.1, 0.3, foot, size=13, italic=True, color=GREY)
    return s


def code_slide(title, label, code, right_title, right_items, bandruns=None, notes=None):
    """Riquadro con testo monospazio (struttura cartelle, file) + elenco a destra."""
    s = free(title, notes)
    box(s, 0.3, 1.5, 6.25, 5.05 if not bandruns else 3.65, 'F2F4F7')
    text(s, 0.6, 1.65, 5.7, 0.4, label, size=15, bold=True, color=GREY)
    tb = text(s, 0.6, 2.05, 5.8, 4.3, [[(l, {})] for l in code.split('\n')], size=13, color=TXT)
    for pa in tb.text_frame.paragraphs:
        pa.space_before = Pt(1)
        for r in pa.runs:
            r.font.name = 'Courier New'
    text(s, 6.9, 1.55, 6.1, 0.45, right_title, size=17, bold=True, color=BLU)
    n = len(right_items)
    avail = (5.0 if not bandruns else 3.2) - 0.6
    hh = min(1.0, (avail - 0.12 * (n - 1)) / n)
    for i, (h, d) in enumerate(right_items):
        y = 2.15 + i * (hh + 0.12)
        box(s, 6.9, y, 6.1, hh, BG2)
        box(s, 6.9, y, 0.12, hh, COLS[i % 6], MSO_SHAPE.RECTANGLE)
        text(s, 7.2, y, 5.65, hh, [(h + ' ', {'bold': True, 'color': BLU}), (d, {})], size=14, anchor=MSO_ANCHOR.MIDDLE)
    if bandruns:
        band(s, 5.4, 1.15, bandruns, size=16)
    return s


def chain(title, items, below=None, notes=None):
    """catena di 3-5 riquadri con frecce (numero grande, didascalia); below=(sinistra, destra) liste"""
    s = free(title, notes)
    n = len(items)
    w = (12.7 - 0.4 * (n - 1)) / n
    for i, (big, small) in enumerate(items):
        x = 0.3 + i * (w + 0.4)
        col = FUX if i == n - 1 else BLU
        box(s, x, 1.5, w, 1.05, col)
        text(s, x, 1.52, w, 0.6, big, size=24, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x, 2.05, w, 0.45, small, size=14, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < n - 1:
            arrow(s, x + w + 0.04, 1.81)
    return s


def links(title, items, extra=None, tip=None, notes='Facoltativo, non è parte della consegna. I link sono cliccabili in presentazione e stanno anche nella scheda della consegna.'):
    """items: fino a 4 (titolo, perché, url, lingua); extra: (intestazione, [(titolo, url)]) fino a 2"""
    s = free(title, notes)

    def link(tb, url):
        for pa in tb.text_frame.paragraphs:
            for r in pa.runs:
                r.hyperlink.address = url
    for i, (h, d, url, lang) in enumerate(items):
        x = 0.3 + (i % 2) * 6.45
        y = 1.45 + (i // 2) * 1.9
        b = box(s, x, y, 6.25, 1.75, BG2); b.click_action.hyperlink.address = url
        pl = box(s, x + 0.3, y + 0.5, 0.75, 0.75, COLS[i], MSO_SHAPE.OVAL); pl.click_action.hyperlink.address = url
        tri = box(s, x + 0.57, y + 0.7, 0.3, 0.35, 'FFFFFF', MSO_SHAPE.ISOSCELES_TRIANGLE); tri.rotation = 90
        text(s, x + 1.3, y + 0.17, 4.8, 0.4, h, size=17, bold=True, color=BLU)
        text(s, x + 1.3, y + 0.6, 4.75, 0.6, d, size=14)
        tb = text(s, x + 1.3, y + 1.3, 4.8, 0.3, [(url.replace('https://www.youtube.com/watch?v=', 'youtu.be/'), {'color': CEL}), ('  ·  ' + lang, {'color': GREY})], size=13)
        tb.text_frame.paragraphs[0].runs[0].hyperlink.address = url
    if not extra:
        band(s, 5.3, 1.3, R('Come usarli: ', tip or 'scegline uno, guardalo in settimana e porta alla prossima lezione una frase che ti è rimasta.'), size=16)
    if extra:
        box(s, 0.3, 5.3, 12.7, 1.3, BG2)
        text(s, 0.6, 5.42, 12.1, 0.4, extra[0], size=16, bold=True, color=BLU)
        for i, (h, url) in enumerate(extra[1]):
            x = 0.6 + i * 6.2
            text(s, x, 5.85, 5.9, 0.35, h, size=14, bold=True)
            tb = text(s, x, 6.17, 5.9, 0.3, url.replace('https://www.', ''), size=13, color=CEL)
            link(tb, url)
    return s
