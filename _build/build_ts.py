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
      notes='Presento un percorso di 12 settimane per portare le cinque colleghe di Talent da un uso occasionale di Claude alla capacità di decidere dove l’AI serve e di costruire un agente su un processo reale. Si parte lunedì 7 dicembre.')

# 1b Executive summary
s = slide('Sezioni modificabili 2', {15: 'In 12 lunedì cinque colleghe passano dall’uso occasionale di Claude a due agenti in uso'}, widen=TITLE_W,
          notes='Questa slide contiene tutta la storia. Se lo staff legge solo questa, sa cosa propongo e cosa chiedo.')
es = [('Oggi', 'Claude si usa su richieste singole, senza criteri per scegliere cosa automatizzare e con dati sparsi in copie e allegati.', GREY),
      ('Proposta', 'Un percorso sul lavoro vero, 12 lezioni da 2 ore, dal 7 dicembre all’8 marzo, ognuna con un lavoro reale per la settimana dopo.', BLU2),
      ('Risultato', 'Ogni collega sa dove l’AI le libera tempo, i file di Talent si trovano al primo colpo, due agenti fanno un lavoro ripetitivo e una persona decide.', CEL),
      ('Dopo', 'Le lezioni registrate diventano materiale formativo e chi vuole, in coppia, lo porta al suo team: il percorso si riproduce.', FUX),
      ('Richiesta', 'Uno slot fisso di 45 minuti a settimana per nome, spazio per i team dopo marzo, ok a registrare, perimetro dati verificato con il DPO.', ARA)]
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

# 2b Quattro parole
s = slide('Sezioni modificabili 2', {15: 'Quattro parole che useremo, spiegate senza gergo'}, widen=TITLE_W,
          notes='Per uno staff che usa poco l’AI: chiarire le parole prima dei risultati, altrimenti “agente” suona come fantascienza.')
gl = [('Claude', CEL, 'Un modello linguistico: scrive la risposta più plausibile, non consulta un archivio di fatti. Per questo è utile e per questo va verificato.'),
      ('Il coach', BLU2, 'Un assistente Claude già pronto che fa domande a ogni collega su tempo e attività. La sua cartella resta sul Mac di ognuna: privata.'),
      ('Un agente', FUX, 'Claude con istruzioni scritte una volta per tutte su un processo preciso: cosa produrre, cosa chiedere, cosa non fare mai. Prepara e propone, decide una persona.'),
      ('La struttura', ARA, 'Le cartelle condivise di Talent organizzate con poche regole comuni, perché ogni file esista in un posto solo e si trovi al primo colpo.')]
for i, (k, col, v) in enumerate(gl):
    x = 0.3 + (i % 2) * 6.45; y = 1.5 + (i // 2) * 2.6
    box(s, x, y, 6.25, 2.4, BG2)
    box(s, x, y, 0.14, 2.4, col, MSO_SHAPE.RECTANGLE)
    text(s, x + 0.45, y + 0.25, 5.6, 0.5, k, size=22, bold=True, color=BLU)
    text(s, x + 0.45, y + 0.9, 5.6, 1.4, v, size=16)

# 3 Sezione What (copertina di sezione)
slide('1_Copertina-Celeste', {13: 'Sezione 01', 0: 'What', 1: 'Tre risultati, in sequenza'})

# 4 Tre risultati
s = slide('Sezioni modificabili 2', {15: 'Tre risultati in sequenza: ognuno prepara il successivo'}, widen=TITLE_W,
          notes='La sequenza è il cuore del design. Gli agenti non nascono da un caso inventato in aula ma dalle attività che le colleghe hanno misurato e valutato con il coach.')
res = [(CEL, '1', 'Sapere dove l’AI aiuta davvero', 'Ognuna misura dove va il suo tempo e valuta le attività che pesano: si possono smettere, semplificare, affidare a uno strumento?', 'A marzo: almeno 2 attività valutate a testa, con le ore in gioco'),
       (BLU2, '2', 'Trovare il file giusto al primo colpo', 'Talent decide insieme come organizzare le cartelle condivise, così ogni file esiste una volta sola e anche Claude lavora sulla versione giusta.', 'A marzo: una struttura con regole e un tema reale migrato a testa'),
       (FUX, '3', 'Un agente su un lavoro ripetitivo', 'Due gruppi costruiscono un agente ciascuno, sulle attività scelte al punto 1. Lo provano su casi scritti prima e lo usano per una settimana vera.', 'A marzo: 2 agenti in uso, con owner e co-owner')]
for i, (col, n, h, d, o) in enumerate(res):
    x = 0.3 + i * 4.3
    box(s, x, 1.45, 3.95, 4.15, BG2)
    box(s, x, 1.45, 3.95, 1.15, col)
    text(s, x + 0.3, 1.45, 3.4, 1.15, [[(n + '  ', {'size': 26, 'bold': True, 'color': 'FFFFFF'}), (h, {'size': 18, 'bold': True, 'color': 'FFFFFF'})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 0.3, 2.85, 3.4, 1.9, d, size=16)
    text(s, x + 0.3, 4.75, 3.4, 0.75, o, size=14, bold=True, color=BLU)
    if i < 2:
        arrow(s, x + 3.98, 3.3, 0.3, 0.42)
box(s, 0.3, 5.85, 12.55, 0.85, BLU)
text(s, 0.6, 5.85, 12.0, 0.85, 'Le attività valutate nel risultato 1 decidono su quali processi nascono gli agenti del risultato 3: non si parte da un caso inventato in aula.', size=16, color='FFFFFF', anchor=MSO_ANCHOR.MIDDLE)


def outcome(title, notes, col, oggi, marzo, verifica, esempio):
    s = slide('Sezioni modificabili 2', {15: title}, widen=TITLE_W, notes=notes)
    for x, head, fill, hc, tc, body in [(0.3, 'Oggi', 'F2F4F7', GREY, TXT, oggi), (4.6, 'A marzo', BG2, BLU, TXT, marzo), (8.9, 'Come lo verifichiamo', col, 'FFFFFF', 'FFFFFF', verifica)]:
        box(s, x, 1.45, 4.05, 3.75, fill)
        text(s, x + 0.3, 1.65, 3.5, 0.45, head, size=19, bold=True, color=hc)
        text(s, x + 0.3, 2.25, 3.5, 2.85, [[(t, {})] for t in body.split('\n\n')], size=15, color=tc)
    arrow(s, 4.29, 3.1, 0.3, 0.42)
    box(s, 0.3, 5.45, 12.65, 1.25, 'FFFFFF').line.color.rgb = rgb(col)
    text(s, 0.6, 5.45, 12.1, 1.25, [[('Un esempio  ', {'bold': True, 'color': col}), (esempio, {})]], size=15, anchor=MSO_ANCHOR.MIDDLE)
    return s


outcome('Risultato 1: ogni collega sa dove va il suo tempo e dove l’AI lo libera davvero',
        'Il punto per lo staff: non partiamo dallo strumento ma dal tempo. Spesso la risposta migliore non è l’AI ma smettere o semplificare, e anche questo conta come risultato.',
        CEL,
        'Sappiamo di essere sempre di corsa, ma nessuno sa dire quante ore vanno in riunioni, report e messaggi. Se chiediamo cosa automatizzare, la risposta è la cosa più fastidiosa, non quella che pesa di più.',
        'Ognuna ha letto quattro settimane del suo calendario e una di diario, con l’aiuto del coach. Ha almeno due “schede”: per un’attività, quante ore al mese prende, se si può smettere o semplificare, se conviene uno strumento e quanto tempo vale la pena investirci.',
        'Ore al mese liberate: stimate nelle schede a marzo, verificate il 19 aprile rifacendo la stessa misura del tempo.\n\nI dati del tempo restano di ciascuna: allo staff arrivano solo numeri aggregati.',
        'il report mensile delle iscrizioni prende 3 ore. La scheda dice che prima si unifica il modulo di raccolta e poi basta un modello pronto: l’agente non serve, e lo sappiamo prima di costruirlo. (Esempio ipotetico.)')
outcome('Risultato 2: un file esiste in un posto solo, e si trova in meno di un minuto',
        'Il legame con l’AI: Claude lavora su ciò che gli diamo. Con tre copie dello stesso file sceglie, e può scegliere quella vecchia con la stessa sicurezza.',
        BLU2,
        'Lo stesso file esiste in tre versioni: nella cartella condivisa, in un allegato, sul desktop di qualcuno. Chi cerca non sa quale sia quella vera. Claude nemmeno, e lavora su quella sbagliata con la stessa sicurezza.',
        'Talent ha una cartella condivisa con poche regole decise insieme: i dati originali separati dai lavori in corso, un nome standard per i file, una responsabile per ogni cartella. Ognuna ci ha portato un tema che usa ogni settimana: spostato, o indicizzato se è un documento vincolato come la rendicontazione dei fondi.',
        'Un test semplice: cinque file da trovare, un minuto ciascuno, a gennaio prima e dopo la nuova struttura.\n\nIl numero di copie dello stesso documento, contato prima e dopo.',
        'le iscrizioni ai corsi stanno in una cartella sola, un file per mese, con la matricola come chiave. In aula rifacciamo il confronto della prima lezione: stesso prompt, risultato giusto, perché è cambiata la cartella.')
outcome('Risultato 3: due agenti fanno un pezzo di lavoro ripetitivo, e una persona decide',
        'Definizione da dare a voce: un agente è Claude con istruzioni scritte una volta per tutte. Non è un software da comprare né qualcosa che decide da solo. Su persone non decide niente: selezione e valutazione sono ad alto rischio per l’AI Act.',
        FUX,
        'Claude si usa come una chat: ogni volta si rispiega tutto da capo e il risultato dipende da come è scritta la domanda. Quello che una collega ha capito non resta al team.',
        'Due agenti, uno per gruppo, su due attività scelte dalle schede. Ognuno ha istruzioni scritte: cosa produce, cosa chiede se manca un dato, cosa non fa mai. Prepara e propone. Decide e invia una persona. Owner e co-owner lo tengono aggiornato.',
        'Prima dell’uso: una prova su 6-8 casi scritti in anticipo, almeno 8 su 10 corretti e tutti i casi in cui deve fermarsi rispettati.\n\nDopo: un registro di ogni uso, con l’esito.',
        'le mail di conferma ai docenti esterni. L’agente controlla che ci siano date, aula e materiali, chiede quello che manca e prepara la mail. La collega la rilegge e la invia. (Esempio ipotetico: i processi veri li scelgono le colleghe a gennaio.)')

# 5 Obiettivi (Tabella)
s = slide('Tabella', {13: 'Misuriamo cosa cambia nel lavoro, non le ore d’aula', 14: 'Un indicatore verificabile per ogni risultato'},
          widen={13: 12.7, 14: 12.7},
          notes='Il primo indicatore diventa un dato solo alla rimisura del 19 aprile: fino ad allora è una stima. Non misuriamo gradimento né presenze.')
rows = [('Risultato', 'Cosa deve esistere a marzo', 'Come capiamo che ha funzionato'),
        ('Sapere dove l’AI aiuta', 'Almeno 2 attività valutate a testa (ore in gioco, alternative, conviene o no)', 'Ore al mese liberate: stimate a marzo, verificate il 19 aprile'),
        ('Trovare il file giusto', 'Una cartella condivisa con regole comuni; un tema reale migrato o indicizzato a testa', 'File trovato in meno di un minuto; meno copie dello stesso documento'),
        ('Un agente che regge', '2 agenti con istruzioni scritte, prove, owner e co-owner', 'Almeno 8 casi di prova su 10 corretti; quante volte si usa a settimana')]
tbl = s.shapes.add_table(len(rows), 3, Inches(0.3), Inches(1.6), Inches(12.7), Inches(4.5)).table
text(s, 0.3, 6.35, 12.7, 0.4, 'Per ogni risultato tre domande: quale comportamento cambia, cosa deve esistere alla fine, quale numero lo dimostra.', size=14, color=GREY, italic=True)
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
                      17: 'Formato', 18: '12 lezioni da 2 ore', 19: 'Una lezione a settimana, il lunedì, per 5 colleghe.',
                      20: 'On the job', 21: 'Un lavoro a settimana', 22: 'Slot fisso di 45’ in orario, versione minima da 15’. La lezione dopo parte da lì.',
                      23: 'Filo', 24: 'Il plugin coach', 25: 'Un assistente che fa domande a ognuna. La sua cartella resta sul suo Mac.',
                      32: 'Strumento', 33: 'Cowork', 34: 'L’app di Claude che lavora sui file. Niente programmazione.',
                      29: 'Teoria', 30: 'Pillole da 15’', 31: 'Come funziona Claude, spiegato quando serve, sul caso concreto.',
                      26: 'Agenti', 27: 'Due agenti, in gruppo', 28: 'Gruppi da 2 e 3, owner e co-owner, una skill a testa.'},
      widen={13: 12.9, 18: 3.9, 21: 3.9, 24: 3.9, 27: 3.9, 30: 3.9, 33: 3.9},
      notes='Ogni lezione: 20 minuti di revisione del lavoro portato, 15 di pillola, 70 di laboratorio sul proprio caso, 15 per avviare la consegna. L’istanza del coach è privata: in aula si condivide solo quello che ognuna sceglie.')

text(s, 0.3, 1.3, 12.7, 0.5, [('Ogni lezione:  ', {'bold': True, 'color': BLU}),
                              ('20’ revisione del lavoro  ·  15’ pillola  ·  70’ laboratorio sul proprio caso  ·  15’ consegna', {})], size=18)

# 8 Processo standard
s = slide('Sezioni modificabili 2', {15: 'Gli agenti seguono lo stesso metodo in sei fasi dell’agente coach'}, widen=TITLE_W,
          notes='Per l’agente coach sono servite sei ricerche approfondite e 37 file di metodo. Per un agente di processo al primo tentativo bastano le fonti che Talent già possiede, un core di una pagina e una skill per collega. Il lavoro di gruppo si fa in aula, 30 minuti nelle lezioni 9, 10 e 11.')
ph = [('Spazio', 'Una cartella per l’agente, nella struttura condivisa'), ('Fonti', 'I documenti che Talent ha già: procedure, modelli, esempi'),
      ('Selezione', 'Si tiene solo ciò che cambia il modo di lavorare'), ('Architettura', 'Regole sempre valide, più istruzioni richiamate al bisogno'),
      ('Scrittura', 'Istruzioni precise, rilette dall’altro gruppo'), ('Contratto', 'Cosa non fa mai, prove, owner e co-owner, un registro')]
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
s = slide('Sezioni modificabili 2', {15: '12 lunedì, dal 7 dicembre all’8 marzo, fino a due agenti in uso'}, widen=TITLE_W,
          notes='Lezioni il lunedì, pausa il 28 dicembre e il 4 gennaio. La settimana 4 (11 gennaio) è lo snodo: dalle schede escono i due processi per gli agenti e si formano i gruppi, con owner e co-owner scelte per tempo disponibile. Rispetto alla prima bozza il blocco dati passa da tre lezioni a due e il blocco agente da quattro a cinque: l’agente si accende in bozza già alla lezione 8.')
X0, WK = 0.3, 0.88
DATES = ['7/12', '14/12', '21/12', '11/1', '18/1', '25/1', '1/2', '8/2', '15/2', '22/2', '1/3', '8/3']
for w in range(12):
    text(s, X0 + w * WK, 1.5, WK, 0.3, f'S{w + 1}', size=14, bold=True, color=BLU, align=PP_ALIGN.CENTER)
    text(s, X0 + w * WK, 1.82, WK, 0.3, DATES[w], size=12, color=GREY, align=PP_ALIGN.CENTER)
RX = X0 + 12 * WK + 0.3
text(s, RX, 1.5, 1.4, 0.3, '+6 sett.', size=14, bold=True, color=BLU, align=PP_ALIGN.CENTER)
text(s, RX, 1.82, 1.4, 0.3, '19/4', size=12, color=GREY, align=PP_ALIGN.CENTER)
blocks = [(1, 4, CEL, 'A. Dove serve', 'Misura del tempo e attività valutate. Scelta dei 2 processi e dei gruppi'),
          (5, 6, BLU2, 'B. Dati', 'Cartelle condivise con regole, fonti degli agenti dentro, Claude sui dati in ordine'),
          (7, 7, FUX, 'C', 'Prima istruzione riusabile per Claude'),
          (8, 12, ARA, 'D. Agente', '2 agenti in uso, con owner e co-owner e prove superate')]
for a, b, col, name, ms in blocks:
    x, w = X0 + (a - 1) * WK + 0.03, (b - a + 1) * WK - 0.06
    box(s, x, 2.2, w, 0.75, col)
    text(s, x + 0.1, 2.2, w - 0.2, 0.75, name, size=16 if a == b else 15, bold=True, color='FFFFFF', anchor=MSO_ANCHOR.MIDDLE,
         align=PP_ALIGN.CENTER if a == b else PP_ALIGN.LEFT)
box(s, RX, 2.2, 1.4, 0.75, BLU)
text(s, RX, 2.2, 1.4, 0.75, 'Rimisura', size=14, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(X0 + 3 * WK), Inches(1.5), Inches(X0 + 3 * WK), Inches(2.12))
ln.line.color.rgb = rgb(FUX); ln.line.width = Pt(1.5); ln.line.dash_style = 4
mls = [(c, 'C. Strumenti' if n == 'C' else n, m) for _, _, c, n, m in blocks] + [(BLU, 'Rimisura', 'Ore liberate verificate, rifacendo la misura del tempo')]
for i, (col, name, ms) in enumerate(mls):
    x = 0.3 + i * 2.55
    box(s, x, 3.62, 0.3, 0.3, col, MSO_SHAPE.OVAL)
    text(s, x + 0.42, 3.55, 2.0, 0.45, name, size=16, bold=True, color=BLU, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 4.15, 2.35, 1.5, ms, size=15)
box(s, 0.3, 5.75, 12.7, 0.85, BG2)
text(s, 0.6, 5.75, 12.1, 0.85, 'Lezioni il lunedì, pausa natalizia il 28/12 e il 4/1 (tratteggio tra S3 e S4). Prima di S1: prova a secco del coach, passaggio con il DPO, slot firmati.', size=15, color=BLU, anchor=MSO_ANCHOR.MIDDLE)

# 10 Dopo il percorso
s = slide('Sezioni modificabili 2', {15: 'Dopo marzo il percorso si moltiplica: chi vuole diventa docente del suo team, in coppia'}, widen=TITLE_W,
          notes='Il percorso non finisce l’8 marzo. Chi vuole, in coppia con una collega, diventa docente per il suo team con i materiali registrati: è volontario, perché un obbligo detto alla fine farebbe rileggere tutto il percorso come lavoro in più; le registrazioni, trascritte e selezionate, diventano la knowledge base del team e le fonti degli agenti futuri. Il risultato è un percorso formativo che si riproduce senza passare ogni volta da me.')
fly = [('Registriamo tutto', 'Lezioni, consegne, schede e casi reali diventano una raccolta di materiale formativo.', CEL),
       ('Docenti in coppia', 'Chi vuole porta una lezione al suo team, in coppia, con i materiali già pronti.', BLU2),
       ('Il materiale diventa conoscenza', 'Una selezione diventa la base di conoscenza del team e la fonte per gli agenti futuri.', FUX),
       ('Percorso riproducibile', 'Lo stesso percorso riparte con un nuovo gruppo, senza ripartire da zero.', ARA)]
for i, (h, d, col) in enumerate(fly):
    x = 0.3 + i * 3.22
    box(s, x, 1.7, 2.9, 3.4, BG2)
    numdot(s, x + 0.3, 2.0, 0.75, i + 1, col)
    text(s, x + 0.3, 2.95, 2.4, 0.75, h, size=18, bold=True, color=BLU)
    text(s, x + 0.3, 3.75, 2.4, 1.3, d, size=14)
    if i < 3: arrow(s, x + 2.96, 3.22, 0.2, 0.36)
box(s, 0.3, 5.4, 12.7, 1.2, BG2)
text(s, 0.6, 5.4, 12.1, 1.2, [('La raccolta è già il primo passo per costruire un agente. ', {'bold': True, 'color': BLU}),
                             ('Le registrazioni si selezionano prima: non tutto quello che si dice in aula è materiale per un agente.', {})], size=15, anchor=MSO_ANCHOR.MIDDLE)

# 11 Richieste
s = slide('Sezioni modificabili 2', {15: 'Per partire il 7 dicembre servono quattro decisioni dello staff, prese a novembre'}, widen=TITLE_W,
          notes='Se il tempo settimanale non è riconosciuto esplicitamente, sarà il primo a saltare, e il percorso è costruito a catena: senza schede non ci sono agenti. La simulazione con tre colleghe tipo lo conferma: il lavoro settimanale regge solo con uno slot fisso per nome, firmato dal responsabile, e una versione minima da 15 minuti per le settimane piene.')
asks = [('Tempo riconosciuto', '2 ore di lezione più uno slot fisso di 45 minuti a settimana, per nome, in orario, firmato dal responsabile.', BLU2),
        ('Spazio dopo marzo', 'Un’ora al mese per owner e co-owner degli agenti, e tempo per le coppie che porteranno il percorso al loro team.', CEL),
        ('Ok a registrare', 'Lezioni registrate con il consenso delle colleghe. Alla demo, ore liberate per processo, mai per persona.', FUX),
        ('Perimetro chiaro', 'Nessun agente decide su persone. Dati minimi verificati con il DPO prima di partire.', ARA)]
for i, (h, d, col) in enumerate(asks):
    x = 0.3 + i * 3.22
    box(s, x, 1.7, 2.95, 4.8, BG2)
    numdot(s, x + 0.3, 2.0, 0.7, i + 1, col)
    text(s, x + 0.3, 2.9, 2.4, 0.9, h, size=19, bold=True, color=BLU)
    text(s, x + 0.3, 3.85, 2.4, 2.4, d, size=15)

# 12 Chiusura
slide('Chiusura-Blu', {0: 'Domande e decisioni', 13: 'Si parte lunedì 7 dicembre'})

p.save(OUT)
print('ok', len(p.slides))
