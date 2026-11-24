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

# 1 Copertina
slide('2_Copertina-Blu', {0: 'Percorso AI per Talent', 1: 'Dal capire dove l’AI serve al costruire un agente',
                          13: 'Staff meeting · novembre 2026'},
      notes='Presento un percorso di 12 settimane per portare le cinque colleghe di Talent da un uso occasionale di Claude alla capacità di decidere dove l’AI serve e di costruire un agente su un processo reale. Si parte venerdì 4 dicembre.')

# 1b Executive summary
s = slide('Sezioni modificabili 2', {15: 'In 12 venerdì cinque colleghe passano dall’uso occasionale di Claude a due agenti in uso'}, widen=TITLE_W,
          notes='Questa slide contiene tutta la storia. Se lo staff legge solo questa, sa cosa propongo e cosa chiedo.')
es = [('Oggi', 'Claude si usa su richieste singole, senza criteri per scegliere cosa automatizzare e con dati sparsi in copie e allegati.', GREY),
      ('Proposta', 'Un percorso on the job di 12 lezioni da 2 ore, dal 4 dicembre al 5 marzo, ognuna con un lavoro reale per la settimana dopo.', BLU2),
      ('Risultato', 'Ogni collega sa decidere dove l’AI libera tempo, i dati stanno in una struttura unica, due agenti sono in uso con una owner.', CEL),
      ('Dopo', 'Le lezioni registrate diventano un basket formativo e ogni collega forma il suo team: il percorso diventa riproducibile.', FUX),
      ('Richiesta', 'Tempo riconosciuto, spazio per i team dopo marzo, ok a registrare, perimetro chiaro sugli agenti.', ARA)]
for i, (k, v, col) in enumerate(es):
    y = 1.55 + i * 1.02
    box(s, 0.3, y + 0.25, 0.3, 0.3, col, MSO_SHAPE.OVAL)
    text(s, 0.8, y, 2.1, 0.8, k, size=19, bold=True, color=BLU, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 2.9, y, 10.1, 0.8, v, size=17, anchor=MSO_ANCHOR.MIDDLE)

# 2 Why
s = slide('Sezioni modificabili 2', {15: 'Claude accelera i compiti, ma oggi nessuno decide se valgono la pena né dove sta il dato giusto'}, widen=TITLE_W,
          notes='Il confronto Claude lo fa bene. Mancano tre cose: decidere se il compito va fatto, sapere dove vive il dato giusto, avere un metodo quando si costruisce qualcosa di ricorrente.')
text(s, 0.3, 1.4, 12.7, 1.0, [[('Una collega carica due Excel in Claude e chiede un confronto. Arriva in trenta secondi, ordinato.', {})],
                                [('Il file aggiornato era un terzo, allegato a una mail della settimana prima.', {'bold': True, 'color': BLU2})]], size=18)
for x, head, col, fill, items in [
    (0.3, 'Oggi', GREY, 'F2F4F7', ['Claude come calcolatrice evoluta, una richiesta alla volta', 'Nessun criterio per decidere se un compito vale la pena', 'Dati sparsi tra copie, versioni e allegati']),
    (6.85, 'Dove vogliamo arrivare', BLU2, BG2, ['Si decide prima dove l’AI porta valore o libera tempo', 'Un dato vive in un posto solo, in una struttura condivisa', 'Agenti costruiti con un metodo ripetibile, misurati nel tempo'])]:
    box(s, x, 2.75, 6.15, 3.6, fill)
    text(s, x + 0.4, 3.05, 5.4, 0.5, head, size=22, bold=True, color=col)
    bullets(s, x + 0.4, 3.75, 5.4, 2.4, items, size=17, gap=12)
arrow(s, 6.47, 4.3, 0.36, 0.5)

# 3 Sezione What (copertina di sezione)
slide('1_Copertina-Celeste', {13: 'Sezione 01', 0: 'What', 1: 'Tre risultati, in sequenza'})

# 4 Tre risultati (layout Roadmap: tre colonne)
s = slide('Roadmap', {13: 'Tre risultati in sequenza: ognuno produce l’input del successivo',
                      18: 'Risultato 1', 19: 'Dove serve', 27: 'Con il plugin coach: time audit, mappa di un processo, schede di automazione con criteri e pareggio.',
                      28: 'Risultato 2', 29: 'Dati in ordine', 31: 'Una struttura condivisa di Talent: fonti separate dalle elaborazioni, nessuna copia, un LEGGIMI per cartella.',
                      32: 'Risultato 3', 33: 'Un agente', 35: 'Due agenti sui processi scelti dalle schede, costruiti con il processo standard e misurati con casi di prova.'},
          notes='La sequenza è il cuore del design. Gli agenti non nascono da un caso inventato in aula ma dai processi che le colleghe hanno valutato con il coach.',
          widen={19: 2.3, 29: 2.3, 33: 2.3})
text(s, 0.3, 4.4, 4.2, 1.6, 'Le schede del risultato 1 decidono su quali processi nascono gli agenti del risultato 3.', size=18, color=BLU2)
for cx, o in zip([5.3, 8.0, 10.7], ['Output: almeno 2 schede a testa', 'Output: un dataset migrato a testa', 'Output: 2 agenti in uso con owner']):
    text(s, cx, 5.0, 2.3, 0.9, o, size=15, bold=True, color='FFFFFF')

# 5 Obiettivi (Tabella)
s = slide('Tabella', {13: 'Misuriamo comportamenti e output, non ore d’aula', 14: 'Un KPI verificabile per ogni risultato'},
          widen={13: 12.7, 14: 12.7},
          notes='Il KPI del primo obiettivo diventa un dato solo alla rimisura del 16 aprile: fino ad allora è una stima.')
rows = [('Risultato', 'Output minimo', 'KPI'),
        ('Decidere dove l’AI serve', 'Per ciascuna: time audit, un processo mappato, almeno 2 schede di automazione', 'Ore/mese liberate, stimate e verificate alla rimisura'),
        ('Dati in un posto solo', 'Struttura condivisa con convenzioni; un dataset reale migrato a testa', 'Duplicati prima/dopo; file trovato in meno di un minuto'),
        ('Un agente con metodo', '2 agenti con core, skill, contratto e batteria di prova', 'Almeno 80% di casi di prova ok; usi a settimana; owner nominata')]
tbl = s.shapes.add_table(len(rows), 3, Inches(0.3), Inches(1.6), Inches(12.7), Inches(4.5)).table
text(s, 0.3, 6.35, 12.7, 0.4, 'Filtro unico: quale comportamento cambia, qual è l’output minimo, quale indicatore lo dimostra.', size=14, color=GREY, italic=True)
for j, w in enumerate([3.1, 5.0, 4.6]):
    tbl.columns[j].width = Inches(w)
for i, r in enumerate(rows):
    tbl.rows[i].height = Inches(0.6 if i == 0 else 1.3)
    for j, v in enumerate(r):
        c = tbl.cell(i, j); c.fill.solid(); c.fill.fore_color.rgb = rgb(BLU2 if i == 0 else ('FFFFFF' if i % 2 else BG2))
        c.vertical_anchor = MSO_ANCHOR.MIDDLE; c.margin_left = c.margin_right = Inches(0.15)
        tf = c.text_frame; tf.text = ''
        run = tf.paragraphs[0].add_run(); run.text = v
        run.font.name = 'Roboto'; run.font.size = Pt(16); run.font.bold = (i == 0 or j == 0)
        run.font.color.rgb = rgb('FFFFFF' if i == 0 else (BLU if j == 0 else TXT))

# 6 Sezione How
slide('2_Copertina-Fucsia', {13: 'Sezione 02', 0: 'How', 1: 'On the job, a catena'})

# 7 How (6 Categorie)
s = slide('6 Categorie', {13: 'Si impara sul proprio lavoro: ogni lezione lascia un compito reale per la settimana dopo',
                      17: 'Formato', 18: '12 lezioni da 2 ore', 19: 'Una lezione a settimana, il venerdì, per 5 colleghe.',
                      20: 'On the job', 21: 'Un lavoro a settimana', 22: 'Sul caso reale, 30-60 minuti. La lezione dopo parte da lì.',
                      23: 'Filo', 24: 'Il plugin coach', 25: 'Istanza privata: time audit, processo, scheda di automazione.',
                      32: 'Strumento', 33: 'Cowork', 34: 'Cartelle, plugin e skill dall’app. Niente shell.',
                      29: 'Teoria', 30: 'Pillole da 15’', 31: 'Come funziona un LLM entra quando serve, sul caso concreto.',
                      26: 'Agenti', 27: 'Due agenti, in gruppo', 28: 'Gruppi da 2 e 3 persone, ognuno con una owner.'},
      widen={13: 12.9, 18: 3.9, 21: 3.9, 24: 3.9, 27: 3.9, 30: 3.9, 33: 3.9},
      notes='Ogni lezione: 20 minuti di revisione del lavoro portato, 15 di pillola, 70 di laboratorio sul proprio caso, 15 per avviare la consegna. L’istanza del coach è privata: in aula si condivide solo quello che ognuna sceglie.')

text(s, 0.3, 1.3, 12.7, 0.5, [('Ogni lezione:  ', {'bold': True, 'color': BLU}),
                              ('20’ revisione del lavoro  ·  15’ pillola  ·  70’ laboratorio sul proprio caso  ·  15’ consegna', {})], size=18)

# 8 Processo standard
s = slide('Sezioni modificabili 2', {15: 'Gli agenti seguono lo stesso metodo in sei fasi dell’agente coach'}, widen=TITLE_W,
          notes='Per l’agente coach sono servite sei ricerche approfondite e 37 file di metodo. Per un agente di processo al primo tentativo bastano le fonti che Talent già possiede, un core di una pagina e una o due skill.')
ph = [('Spazio', 'Una cartella dell’agente nella struttura condivisa'), ('Fonti', 'Procedure, template ed esempi che Talent ha già'),
      ('Selezione', 'Cosa cambia il comportamento, cosa è solo riferimento'), ('Architettura', 'Regole sempre attive più skill caricate al bisogno'),
      ('Scrittura', 'Istruzioni, non spiegazioni. Revisione incrociata'), ('Contratto', 'Cosa non fa mai, prove, owner, registro usi')]
for i, (h, d) in enumerate(ph):
    x = 0.3 + i * 2.12
    box(s, x, 1.8, 2.02, 1.0, [CEL, CEL, BLU2, BLU2, FUX, FUX][i], MSO_SHAPE.CHEVRON)
    text(s, x + 0.3, 1.8, 1.4, 1.0, str(i + 1), size=26, color='FFFFFF', bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 3.15, 1.95, 0.45, h, size=18, bold=True, color=BLU)
    text(s, x, 3.7, 1.9, 1.6, d, size=15)
box(s, 0.3, 5.5, 12.7, 1.1, BG2)
text(s, 0.6, 5.5, 12.1, 1.1, [('È il metodo con cui è stato costruito l’agente coach, a un decimo del volume. ', {'bold': True, 'color': BLU}),
                             ('Le sei fasi restano tutte: è la sequenza che rende il risultato ripetibile.', {})], size=16, anchor=MSO_ANCHOR.MIDDLE)

# 9 Roadmap con date
s = slide('Sezioni modificabili 2', {15: '12 venerdì, dal 4 dicembre al 5 marzo, fino a due agenti in uso'}, widen=TITLE_W,
          notes='Lezioni il venerdì, pausa il 25 dicembre e l’1 gennaio. La settimana 4 (8 gennaio) è lo snodo: dalle schede escono i due processi per gli agenti e si formano i gruppi, con le owner già nominate.')
X0, WK = 0.3, 0.88
DATES = ['4/12', '11/12', '18/12', '8/1', '15/1', '22/1', '29/1', '5/2', '12/2', '19/2', '26/2', '5/3']
for w in range(12):
    text(s, X0 + w * WK, 1.5, WK, 0.3, f'S{w + 1}', size=14, bold=True, color=BLU, align=PP_ALIGN.CENTER)
    text(s, X0 + w * WK, 1.82, WK, 0.3, DATES[w], size=12, color=GREY, align=PP_ALIGN.CENTER)
RX = X0 + 12 * WK + 0.3
text(s, RX, 1.5, 1.4, 0.3, '+6 sett.', size=14, bold=True, color=BLU, align=PP_ALIGN.CENTER)
text(s, RX, 1.82, 1.4, 0.3, '16/4', size=12, color=GREY, align=PP_ALIGN.CENTER)
blocks = [(1, 4, CEL, 'A. Dove serve', 'Time audit e schede di automazione. Scelta dei 2 processi e dei gruppi'),
          (5, 7, BLU2, 'B. Dati e struttura', 'Struttura condivisa, dataset migrati, Claude sui dati ordinati'),
          (8, 8, FUX, 'C', 'Prima skill personale'),
          (9, 12, ARA, 'D. Agente', '2 agenti in uso, con owner e prove superate')]
for a, b, col, name, ms in blocks:
    x, w = X0 + (a - 1) * WK + 0.03, (b - a + 1) * WK - 0.06
    box(s, x, 2.2, w, 0.75, col)
    text(s, x + 0.1, 2.2, w - 0.2, 0.75, name, size=16 if a == b else 15, bold=True, color='FFFFFF', anchor=MSO_ANCHOR.MIDDLE,
         align=PP_ALIGN.CENTER if a == b else PP_ALIGN.LEFT)
box(s, RX, 2.2, 1.4, 0.75, BLU)
text(s, RX, 2.2, 1.4, 0.75, 'Rimisura', size=14, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(X0 + 3 * WK), Inches(1.5), Inches(X0 + 3 * WK), Inches(2.12))
ln.line.color.rgb = rgb(FUX); ln.line.width = Pt(1.5); ln.line.dash_style = 4
mls = [(c, 'C. Strumenti' if n == 'C' else n, m) for _, _, c, n, m in blocks] + [(BLU, 'Rimisura', 'Ore liberate verificate rispetto al time audit iniziale')]
for i, (col, name, ms) in enumerate(mls):
    x = 0.3 + i * 2.55
    box(s, x, 3.62, 0.3, 0.3, col, MSO_SHAPE.OVAL)
    text(s, x + 0.42, 3.55, 2.0, 0.45, name, size=16, bold=True, color=BLU, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 4.15, 2.35, 1.5, ms, size=15)
box(s, 0.3, 5.75, 12.7, 0.85, BG2)
text(s, 0.6, 5.75, 12.1, 0.85, 'Lezioni il venerdì, pausa natalizia il 25/12 e l’1/1 (tratteggio tra S3 e S4). Prima di S1: pilota del coach con una collega.', size=15, color=BLU, anchor=MSO_ANCHOR.MIDDLE)

# 10 Dopo il percorso
s = slide('Sezioni modificabili 2', {15: 'Dopo marzo il percorso si moltiplica: ogni collega diventa docente del suo team'}, widen=TITLE_W,
          notes='Il percorso non finisce il 5 marzo. Ogni collega diventa docente per il suo team con i materiali registrati; le registrazioni, trascritte e selezionate, diventano la knowledge base del team e le fonti degli agenti futuri. Il risultato è un percorso formativo che si riproduce senza passare ogni volta da me.')
fly = [('Registriamo tutto', 'Lezioni, consegne, schede e casi reali diventano un basket di formazione.', CEL),
       ('Ognuna diventa docente', 'Ogni collega demoltiplica il percorso con il suo team, con i materiali già pronti.', BLU2),
       ('Il basket diventa kb', 'I materiali selezionati sono le fonti per il team e per gli agenti che creerà.', FUX),
       ('Percorso riproducibile', 'Lo stesso percorso riparte con un nuovo gruppo, senza ripartire da zero.', ARA)]
for i, (h, d, col) in enumerate(fly):
    x = 0.3 + i * 3.22
    box(s, x, 1.7, 2.9, 3.4, BG2)
    numdot(s, x + 0.3, 2.0, 0.75, i + 1, col)
    text(s, x + 0.3, 2.95, 2.4, 0.75, h, size=18, bold=True, color=BLU)
    text(s, x + 0.3, 3.75, 2.4, 1.3, d, size=14)
    if i < 3: arrow(s, x + 2.96, 3.22, 0.2, 0.36)
box(s, 0.3, 5.4, 12.7, 1.2, BG2)
text(s, 0.6, 5.4, 12.1, 1.2, [('Il basket è la fase 2 del processo standard già fatta. ', {'bold': True, 'color': BLU}),
                             ('Le registrazioni si selezionano prima di entrare nella kb: non tutto quello che si dice in aula è materiale per un agente.', {})], size=15, anchor=MSO_ANCHOR.MIDDLE)

# 11 Richieste
s = slide('Sezioni modificabili 2', {15: 'Per partire il 4 dicembre servono quattro decisioni dello staff'}, widen=TITLE_W,
          notes='Se il tempo settimanale non è riconosciuto esplicitamente, sarà il primo a saltare, e il percorso è costruito a catena: senza schede non ci sono agenti.')
asks = [('Tempo riconosciuto', '2 ore di lezione più 30-60 minuti di lavoro a settimana, per 12 settimane, come tempo di lavoro.', BLU2),
        ('Spazio per i team', 'Dopo marzo, tempo perché ogni collega porti il percorso al suo team come docente.', CEL),
        ('Ok a registrare', 'Lezioni registrate e trascritte, con il consenso delle colleghe, per costruire il basket.', FUX),
        ('Perimetro chiaro', 'Nessun agente decide su persone. Selezione e valutazione sono ad alto rischio per l’AI Act.', ARA)]
for i, (h, d, col) in enumerate(asks):
    x = 0.3 + i * 3.22
    box(s, x, 1.7, 2.95, 4.8, BG2)
    numdot(s, x + 0.3, 2.0, 0.7, i + 1, col)
    text(s, x + 0.3, 2.9, 2.4, 0.9, h, size=19, bold=True, color=BLU)
    text(s, x + 0.3, 3.85, 2.4, 2.4, d, size=15)

# 12 Chiusura
slide('Chiusura-Blu', {0: 'Domande e decisioni', 13: 'Si parte venerdì 4 dicembre'})

p.save(OUT)
print('ok', len(p.slides))
