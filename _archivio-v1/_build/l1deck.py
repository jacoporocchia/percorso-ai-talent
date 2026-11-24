exec(open('/tmp/claude-0/-home-user/6bc0d0f6-e1c3-52f7-92ec-9fb486a20c2c/scratchpad/ts/tslib.py', encoding='utf-8').read())

# 1 Copertina
slide('2_Copertina-Blu', {0: 'Lezione 1 · Il modello e il coach', 1: 'Percorso AI per Talent', 13: 'Lunedì 7 dicembre 2026'})

# 2 Agenda
s = slide('Sezioni modificabili 2', {15: 'Oggi vediamo dove il modello sbaglia, poi avviamo il coach'}, widen=TITLE_W,
          notes='Apertura: perché siamo qui. Il percorso parte da una domanda pratica: quando possiamo fidarci di quello che Claude ci restituisce, e dove ci libera davvero tempo.')
ag = [('0-10’', 'Patto', 'Tre regole per le 12 settimane', BLU), ('10-40’', 'Demo', 'Un confronto perfetto sul file sbagliato', CEL),
      ('40-65’', 'Pillola', 'Come ragiona un LLM e quanto può leggere', BLU2), ('65-110’', 'Coach', 'Cos’è, poi l’intake individuale', FUX),
      ('110-120’', 'Consegna', 'Il lavoro per lunedì 14', ARA)]
for i, (t, h, d, col) in enumerate(ag):
    x = 0.3 + i * 2.56
    box(s, x, 2.0, 1.35, 0.5, col, adj=0.5)
    text(s, x, 2.0, 1.35, 0.5, t, size=15, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 2.85, 2.36, 0.5, h, size=22, bold=True, color=BLU)
    text(s, x, 3.5, 2.2, 1.4, d, size=17)
box(s, 0.3, 5.3, 12.7, 1.2, BG2)
text(s, 0.6, 5.3, 12.1, 1.2, [('Esci con: ', {'bold': True, 'color': BLU}), ('il coach avviato sui tuoi goal di lavoro e tre domande che userai ogni volta che Claude ti dà un numero.', {})], size=17, anchor=MSO_ANCHOR.MIDDLE)

# 3 Regole (Roadmap: tre colonne)
s = slide('Roadmap', {13: 'Tre regole valgono per tutte le 12 settimane',
                      18: 'Regola 1', 19: 'Si registra', 27: 'La plenaria viene registrata e diventa materiale per i vostri team. Il lavoro individuale con il coach no.',
                      28: 'Regola 2', 29: 'L’istanza è tua', 31: 'La cartella del coach sta sul tuo Mac. La leggi e la correggi solo tu. In aula condividi solo ciò che scegli.',
                      32: 'Regola 3', 33: 'Ogni lezione lascia un lavoro', 35: 'Da fare entro il lunedì dopo, sul tuo lavoro reale, in 30-60 minuti. La lezione dopo parte da lì.'},
          widen={19: 2.3, 29: 2.3, 33: 2.3},
          notes='Chiedi un sì esplicito a ognuna sulla registrazione. Senza consenso di tutte, si registra solo la parte del facilitatore.')
text(s, 0.3, 4.4, 4.2, 1.6, 'Ti chiedo un sì esplicito, adesso, su tutte e tre.', size=18, color=BLU2)

# 4 Demo
s = slide('Sezioni modificabili 2', {15: 'Demo: chiediamo a Claude di confrontare due file di iscrizioni'}, widen=TITLE_W,
          notes='Leggi la risposta ad alta voce. Lascia che sembri giusta. Poi: vi fidereste? Lo mandereste al responsabile? Caccia all’errore a coppie, poi rivela le trappole e il file DEF_v3.')
for i, (fn, d, col) in enumerate([('iscrizioni_formazione_ottobre.xlsx', '40 iscrizioni, 5 corsi', CEL), ('iscrizioni_formazione_novembre.xlsx', 'La versione aggiornata', BLU2)]):
    x = 0.3 + i * 3.3
    box(s, x, 1.45, 3.1, 1.45, BG2)
    box(s, x + 0.25, 1.85, 0.5, 0.65, col, MSO_SHAPE.FOLDED_CORNER)
    text(s, x + 0.95, 1.8, 2.05, 0.9, [[('Iscrizioni ' + fn.split('_')[-1].replace('.xlsx', '') + ' (.xlsx)', {'bold': True, 'color': BLU, 'size': 14})], [(d, {'size': 14})]], size=14)
text(s, 7.1, 1.75, 5.9, 1.1, [('La domanda: ', {'bold': True, 'color': BLU}), ('dopo la risposta, ve ne fidereste abbastanza da mandarla al responsabile?', {})], size=17)
box(s, 0.3, 3.3, 12.7, 2.0, 'F2F4F7')
text(s, 0.6, 3.45, 12.1, 0.4, 'Il prompt', size=15, bold=True, color=GREY)
text(s, 0.6, 3.9, 12.1, 1.3, '“Ti carico due file con le iscrizioni ai corsi di formazione, uno di ottobre e uno di novembre. Confrontali e dimmi: chi si è aggiunto, chi è stato cancellato, e di quante ore totali è cambiato il piano.”', size=19, italic=True, color=TXT)
text(s, 0.3, 5.75, 12.7, 0.8, [('Poi, a coppie: ', {'bold': True, 'color': FUX}), ('trovate almeno un errore nella risposta. Avete 10 minuti.', {})], size=18)

# 5 Pillola
s = slide('Sezioni modificabili 2', {15: 'Un LLM scrive ciò che è plausibile, non ciò che è vero'}, widen=TITLE_W,
          notes='Tre idee, una per card. Il modello non ha sbagliato i conti: li ha fatti bene su dati sporchi e sul file sbagliato, con lo stesso tono sicuro.')
pil = [('Prevede, non consulta', 'Genera la continuazione più probabile del testo. Non apre un archivio di fatti veri.', CEL),
       ('Vede solo ciò che gli dai', 'Non sa che esiste un file DEF_v3 nella tua mail. Se non è nel contesto, per lui non esiste.', BLU2),
       ('Sbaglia con lo stesso tono', 'Una cifra inventata suona sicura come una cifra giusta. La sicurezza del tono non è un segnale.', FUX)]
for i, (h, d, col) in enumerate(pil):
    x = 0.3 + i * 4.3
    box(s, x, 1.7, 4.05, 3.4, BG2)
    numdot(s, x + 0.35, 2.0, 0.75, i + 1, col)
    text(s, x + 0.35, 2.95, 3.4, 0.9, h, size=21, bold=True, color=BLU)
    text(s, x + 0.35, 3.85, 3.4, 1.2, d, size=16)
box(s, 0.3, 5.4, 12.7, 1.15, BG2)
text(s, 0.6, 5.4, 12.1, 1.15, [('Nella demo: ', {'bold': True, 'color': BLU}), ('conti giusti su nomi scritti in tre modi diversi, un duplicato e il file sbagliato. Il problema era nei dati, non nella matematica.', {})], size=16, anchor=MSO_ANCHOR.MIDDLE)

# 6 Tre domande
s = slide('Sezioni modificabili 2', {15: 'Tre domande da fare a Claude prima di fidarsi di un numero'}, widen=TITLE_W,
          notes='Rifate insieme il confronto aggiungendo le tre domande al prompt e guardate la differenza nella risposta.')
qs = [('Da dove viene?', 'Da quale file e da quali righe viene questo risultato? Mostramele.', CEL),
      ('Cosa non hai verificato?', 'Cosa non hai potuto verificare, o hai dovuto interpretare?', BLU2),
      ('Quali casi sono dubbi?', 'Nomi simili, duplicati, formati diversi: elencali prima di darmi il totale.', FUX)]
for i, (h, d, col) in enumerate(qs):
    y = 1.65 + i * 1.45
    box(s, 0.3, y, 12.7, 1.25, BG2)
    numdot(s, 0.6, y + 0.27, 0.7, i + 1, col)
    text(s, 1.6, y, 3.6, 1.25, h, size=21, bold=True, color=BLU, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 5.3, y, 7.4, 1.25, d, size=18, anchor=MSO_ANCHOR.MIDDLE)
text(s, 0.3, 6.15, 12.7, 0.5, 'Le trovi anche nella scheda della consegna: usale ogni volta, per tutta la settimana.', size=15, italic=True, color=GREY)

# 6b Token economy
s = slide('Sezioni modificabili 2', {15: 'Claude lavora su una scrivania da circa 200.000 token, e ogni messaggio la riempie di nuovo'}, widen=TITLE_W,
          notes='Tieni il concetto concreto: il token è la moneta, la finestra di contesto è la scrivania. Chiedi: quanto è lunga la chat più lunga che avete aperto questa settimana?')
tk = [('Il token è la moneta', 'Circa tre quarti di parola. Italiano, numeri e tabelle costano più dell’inglese.', CEL),
      ('La finestra è la scrivania', 'Circa 200.000 token: un romanzo di 500 pagine, o 10.000 righe di una tabella da 10 colonne.', BLU2),
      ('Ogni messaggio rilegge tutto', 'A ogni turno Claude riceve di nuovo tutta la conversazione. Chat lunga: più consumo e risposte peggiori.', FUX)]
for i, (h, d, col) in enumerate(tk):
    x = 0.3 + i * 4.3
    box(s, x, 1.7, 4.05, 3.4, BG2)
    numdot(s, x + 0.35, 2.0, 0.75, i + 1, col)
    text(s, x + 0.35, 2.95, 3.4, 0.9, h, size=21, bold=True, color=BLU)
    text(s, x + 0.35, 3.85, 3.4, 1.2, d, size=16)
box(s, 0.3, 5.4, 12.7, 1.15, BG2)
text(s, 0.6, 5.4, 12.1, 1.15, [('Regola pratica: ', {'bold': True, 'color': BLU}), ('un compito, una chat. Quando cambi argomento o la risposta peggiora, apri una chat nuova e riparti da un riassunto.', {})], size=16, anchor=MSO_ANCHOR.MIDDLE)

# 6c Due Excel da 60 MB
s = slide('Sezioni modificabili 2', {15: 'Due Excel da 60 MB valgono circa 300 scrivanie: prima si riduce, poi si chiede'}, widen=TITLE_W,
          notes='I numeri sono una stima su un file di iscrizioni a 10 colonne: cambiano con il file, l’ordine di grandezza no. Messaggio: Claude ragiona, Excel conta. A Claude chiedi il metodo, il conto lo fa Excel.')
ch = [('60 MB', 'un file .xlsx'), ('1,4 milioni', 'di righe'), ('30 milioni', 'di token'), ('150 volte', 'la scrivania, per file')]
for i, (big, small) in enumerate(ch):
    x = 0.3 + i * 3.25
    col = FUX if i == 3 else BLU
    box(s, x, 1.5, 2.85, 1.05, col)
    text(s, x, 1.52, 2.85, 0.6, big, size=24, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 2.05, 2.85, 0.45, small, size=14, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if i < 3:
        arrow(s, x + 2.92, 1.81)
box(s, 0.3, 2.85, 5.6, 3.95, BG2)
text(s, 0.55, 2.98, 5.2, 0.45, 'Se lo carichi così', size=19, bold=True, color=FUX)
bullets(s, 0.55, 3.5, 5.15, 3.2, ['In chat non passa: il limite è 30 MB per file.',
                                  'Se lo strumento lo accetta, Claude non lo legge: scrive codice, ne guarda un pezzo e sceglie da solo colonne e chiavi.',
                                  'Consumi il limite d’uso e carichi dati personali che non servivano.'], size=15)
box(s, 0.55, 5.4, 5.1, 1.2, 'FFFFFF')
text(s, 0.75, 5.4, 4.75, 1.2, [[('Prima di caricare chiediti: ', {'bold': True, 'color': BLU})], [('quante righe servono davvero per rispondere?', {})]], size=15, anchor=MSO_ANCHOR.MIDDLE)
box(s, 6.15, 2.85, 6.85, 3.95, BG2)
text(s, 6.4, 2.98, 6.4, 0.45, 'Cosa fai invece', size=19, bold=True, color=BLU)
mv = [('Riduci', 'solo le colonne e le righe che servono, con la chiave (matricola).'),
      ('Chiedi il metodo', 'la formula CERCA.X o i passi di Power Query, non il risultato.'),
      ('Prova su 50 righe', 'di cui conosci già la risposta.'),
      ('Applica in Excel', 'il metodo al file intero: Excel conta, Claude ragiona.')]
for i, (h, d) in enumerate(mv):
    y = 3.5 + i * 0.8
    numdot(s, 6.4, y + 0.05, 0.48, i + 1, [CEL, BLU2, FUX, ARA][i], size=15)
    text(s, 7.05, y, 5.8, 0.75, [('%s: ' % h, {'bold': True, 'color': BLU}), (d, {})], size=15)

# 7 Coach (6 Categorie)
s = slide('6 Categorie', {13: 'Il coach fa domande: l’agenda e la memoria restano vostre',
                          17: 'Cos’è', 18: 'Un’AI che fa domande', 19: 'Ti aiuta a chiarire cosa vuoi, dove va il tuo tempo, cosa automatizzare.',
                          20: 'Cosa non è', 21: 'Né un coach né un giudice', 22: 'Non è un coach certificato, non fa terapia, non valuta nessuno.',
                          23: 'Dove vive', 24: 'Sul tuo Mac', 25: 'Cartella coach-<nome>: profilo, goal, impegni. La correggi tu.',
                          32: 'Modalità coach', 33: 'Domande', 34: 'Una per messaggio. È il default: l’agenda è tua.',
                          29: 'Modalità consulente', 30: 'Proposte', 31: 'Quando la chiedi: “passa in modalità consulente”.',
                          26: 'Oggi ti servono', 27: '/coach intake', 28: 'E /coach memoria per vedere cosa ha scritto.'},
          widen={13: 12.9, 17: 3.9, 20: 3.9, 23: 3.9, 32: 3.9, 29: 3.9, 26: 3.9, 18: 3.9, 21: 3.9, 24: 3.9, 27: 3.9, 30: 3.9, 33: 3.9},
          notes='Insisti sulla privacy dell’istanza: è la condizione perché il time audit della lezione 2 sia sincero.')
text(s, 0.3, 1.3, 12.7, 0.5, [('È lo stesso plugin che usa Max, ', {'bold': True, 'color': BLU}), ('con una cartella vuota tutta per te.', {})], size=18)

# 8 Intake
s = slide('Sezioni modificabili 2', {15: 'Nei prossimi 35 minuti il coach vi chiede dove volete arrivare'}, widen=TITLE_W,
          notes='Indicazione chiave: i goal sono di lavoro, perché la prossima settimana li usiamo per leggere il tempo. Giri tra i tavoli, sblocchi solo problemi tecnici.')
st = [('Accordo', 'Cos’è il coach e come lavora'), ('Come lavorare', 'Quanto spingerti, che ritmo'), ('Il quadro', 'Ruolo, progetti, vincoli'),
      ('I goal', '2-3 goal di lavoro a 12 mesi'), ('Primo passo', 'Un goal a 4-6 settimane e un impegno')]
for i, (h, d) in enumerate(st):
    x = 0.3 + i * 2.55
    box(s, x, 1.8, 2.45, 1.0, [CEL, CEL, BLU2, FUX, FUX][i], MSO_SHAPE.CHEVRON)
    text(s, x + 0.35, 1.8, 1.6, 1.0, str(i + 1), size=26, color='FFFFFF', bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 3.1, 2.3, 0.45, h, size=19, bold=True, color=BLU)
    text(s, x, 3.6, 2.2, 1.2, d, size=16)
box(s, 0.3, 5.1, 12.7, 1.45, BG2)
text(s, 0.6, 5.1, 12.1, 1.45, [[('Oggi arriva almeno al punto 3. ', {'bold': True, 'color': BLU}), ('Il resto è il lavoro per la settimana.', {})],
                              [('Porta goal di lavoro: ', {'bold': True, 'color': BLU}), ('lunedì prossimo li useremo per capire dove va il tuo tempo.', {})]], size=17, anchor=MSO_ANCHOR.MIDDLE)

# 9 Consegna
s = slide('Sezioni modificabili 2', {15: 'Per lunedì 14: finire l’intake e annotare tre usi reali di Claude'}, widen=TITLE_W,
          notes='Ognuna scrive in chat a che punto dell’intake è arrivata. Ricorda che la lezione 2 parte dal goal.md.')
cs = [('1', 'Finisci l’intake', '30 minuti', 'Fino ai goal e al primo impegno. Poi /coach memoria: controlla e correggi.', BLU2),
      ('2', 'Tre usi di Claude', '15 minuti nella settimana', 'Cosa hai chiesto, quanto era grande ciò che hai dato, quanto tempo hai risparmiato, come hai verificato.', CEL)]
for i, (nn, h, t, d, col) in enumerate(cs):
    x = 0.3 + i * 6.45
    box(s, x, 1.7, 6.25, 2.6, BG2)
    numdot(s, x + 0.35, 2.0, 0.75, nn, col)
    text(s, x + 1.35, 2.0, 4.6, 0.45, h, size=22, bold=True, color=BLU)
    text(s, x + 1.35, 2.45, 4.6, 0.35, t, size=15, color=GREY)
    text(s, x + 0.35, 3.1, 5.6, 1.5, d, size=17)
box(s, 0.3, 4.7, 12.7, 1.55, BG2)
text(s, 0.6, 4.7, 12.1, 1.55, [[('Cosa porti alla lezione 2: ', {'bold': True, 'color': BLU}), ('il tuo goal.md compilato e le tre righe sugli usi di Claude.', {})],
                              [('Tempo totale: circa 45 minuti. ', {'bold': True, 'color': BLU}), ('La scheda con la tabella da compilare te la mando dopo la lezione.', {})]], size=17, anchor=MSO_ANCHOR.MIDDLE)

# 11b Per approfondire
s = slide('Sezioni modificabili 2', {15: 'Per approfondire: quattro pillole di Enkk coprono le basi di oggi'}, widen=TITLE_W,
          notes='Facoltativo, non è parte della consegna. I link sono cliccabili in presentazione e li trovate anche nella scheda della consegna.')
def link(tb, url):
    for pa in tb.text_frame.paragraphs:
        for r in pa.runs:
            r.hyperlink.address = url
yt = [('Cos’è l’intelligenza artificiale?', 'Il punto di partenza: cosa intendiamo quando diciamo AI.', 'https://www.youtube.com/watch?v=0eyKR8P1WR0', CEL),
      ('Cosa sono i Large Language Models?', 'Perché Claude prevede il testo e non consulta un archivio.', 'https://www.youtube.com/watch?v=fse5LxSRZAM', BLU2),
      ('Come si allena un modello?', 'Da dove viene quello che sa, e perché non conosce i tuoi file.', 'https://www.youtube.com/watch?v=NAJxUKCQwEE', FUX),
      ('Come funzionano gli agenti AI?', 'Dove arriviamo nelle lezioni 9-11, quando costruiamo il nostro.', 'https://www.youtube.com/watch?v=AYeCGb2ZaSU', ARA)]
for i, (h, d, url, col) in enumerate(yt):
    x = 0.3 + (i % 2) * 6.45; y = 1.45 + (i // 2) * 1.9
    b = box(s, x, y, 6.25, 1.75, BG2); b.click_action.hyperlink.address = url
    pl = box(s, x + 0.3, y + 0.5, 0.75, 0.75, col, MSO_SHAPE.OVAL); pl.click_action.hyperlink.address = url
    tri = box(s, x + 0.57, y + 0.7, 0.3, 0.35, 'FFFFFF', MSO_SHAPE.ISOSCELES_TRIANGLE); tri.rotation = 90
    text(s, x + 1.3, y + 0.17, 4.8, 0.4, h, size=17, bold=True, color=BLU)
    text(s, x + 1.3, y + 0.6, 4.75, 0.6, d, size=14)
    link(text(s, x + 1.3, y + 1.3, 4.8, 0.3, url.replace('https://www.', ''), size=13, color=CEL), url)
box(s, 0.3, 5.3, 12.7, 1.3, BG2)
text(s, 0.6, 5.42, 12.1, 0.4, [('Per chi vuole vedere il motore ', {'bold': True, 'color': BLU}), ('(Andrej Karpathy, in inglese con sottotitoli)', {'color': GREY})], size=16)
kp = [('Intro to Large Language Models · 1 ora', 'https://www.youtube.com/watch?v=zjkBMFhNj_g'),
      ('Deep Dive into LLMs like ChatGPT · 3,5 ore', 'https://www.youtube.com/watch?v=7xTGNNLPyMI')]
for i, (h, url) in enumerate(kp):
    x = 0.6 + i * 6.2
    text(s, x, 5.85, 5.9, 0.35, h, size=14, bold=True)
    link(text(s, x, 6.17, 5.9, 0.3, url.replace('https://www.', ''), size=13, color=CEL), url)

# 10 Chiusura
slide('Chiusura-Blu', {0: 'Una cosa che ti ha sorpreso oggi?', 13: 'Prossima lezione: lunedì 14 dicembre'})

p.save(OUT)
print('ok', len(p.slides))
