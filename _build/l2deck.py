exec(open('/tmp/claude-0/-home-user/fb6aa437-ef98-50a4-a83e-9179b450ba71/scratchpad/ts/tslib.py', encoding='utf-8').read())

def band(s, y, h, runs, size=17):
    box(s, 0.3, y, 12.7, h, BG2)
    text(s, 0.6, y, 12.1, h, runs, size=size, anchor=MSO_ANCHOR.MIDDLE)

# 1 Copertina
slide('2_Copertina-Blu', {0: 'Lezione 2 · Dove va il mio tempo', 1: 'Percorso AI per Talent', 13: 'Lunedì 14 dicembre 2026'})

# 2 Agenda
s = slide('Sezioni modificabili 2', {15: 'Oggi trasformiamo una sensazione sul tempo in un inventario classificato'}, widen=TITLE_W,
          notes='Il filo: la settimana scorsa abbiamo visto che Claude sbaglia con sicurezza. Oggi scopriamo che anche la nostra memoria lo fa, sul tempo.')
ag = [('0-15’', 'Ripartenza', 'Il goal.md e i tre usi di Claude', BLU), ('15-35’', 'Stima e pillola', 'Perché la memoria sbaglia sul tempo', CEL),
      ('35-45’', 'La griglia', 'Quattro etichette per ogni attività', BLU2), ('45-100’', 'Inventario', 'Con il coach: cosa fai sempre', FUX),
      ('100-120’', 'Consegna', 'Calendario avviato in aula, diario a gennaio', ARA)]
for i, (t, h, d, col) in enumerate(ag):
    x = 0.3 + i * 2.56
    box(s, x, 2.0, 1.35, 0.5, col, adj=0.5)
    text(s, x, 2.0, 1.35, 0.5, t, size=15, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 2.85, 2.36, 0.5, h, size=22, bold=True, color=BLU)
    text(s, x, 3.5, 2.2, 1.4, d, size=17)
band(s, 5.3, 1.2, [('Esci con: ', {'bold': True, 'color': BLU}), ('l’elenco delle tue attività ricorrenti, ognuna con il suo goal e con chi dovrebbe farla, e la raccolta dati già avviata.', {})])

# 3 Ripartenza
s = slide('Sezioni modificabili 2', {15: 'Si riparte dal lavoro portato: chi non l’ha finito lo chiude oggi'}, widen=TITLE_W,
          notes='Giro veloce, 2-3 minuti a testa. Sul goal.md solo sì o no: il contenuto resta loro. Sui tre usi, chiedi in particolare quanto era grande l’input e se hanno fatto una delle tre domande.')
cs = [('goal.md', 'Completato? Sì o no.', 'Il contenuto resta tuo. Se manca, lo chiudi nella prima parte dell’inventario: il coach riparte da dove eri.', BLU2),
      ('Tre usi di Claude', 'Raccontane uno.', 'Cosa hai chiesto, quanto era grande quello che gli hai dato, come hai verificato.', CEL)]
for i, (h, sub, d, col) in enumerate(cs):
    x = 0.3 + i * 6.45
    box(s, x, 1.7, 6.25, 3.0, BG2)
    numdot(s, x + 0.35, 2.0, 0.75, i + 1, col)
    text(s, x + 1.35, 2.0, 4.6, 0.45, h, size=22, bold=True, color=BLU)
    text(s, x + 1.35, 2.45, 4.6, 0.35, sub, size=16, color=GREY)
    text(s, x + 0.35, 3.15, 5.6, 1.4, d, size=17)
band(s, 5.05, 1.45, [[('Perché si parte da qui: ', {'bold': True, 'color': BLU}), ('il percorso è a catena. Senza goal non si legge il tempo,', {})], [('senza audit non ci sono schede, senza schede non c’è l’agente.', {})]])

# 4 Stima in busta
s = slide('Sezioni modificabili 2', {15: 'Prima di misurare, scrivi quanto pensi di dedicare a tre tipi di lavoro'}, widen=TITLE_W,
          notes='Distribuisci un foglietto e una busta. Tre percentuali che sommano a 100, senza pensarci troppo. La busta si chiude e si riapre alla lezione 3, davanti ai dati. Nessuno legge quella delle altre.')
tp = [('Skilled', 'Il lavoro per cui sei lì: progettare, facilitare, scrivere, selezionare.', CEL),
      ('Strategico', 'Pianificare, decidere priorità, pensare a dove andare.', BLU2),
      ('Coordinamento', 'Allineamenti, aggiornamenti, messaggi, cercare informazioni, passare tra strumenti.', FUX)]
for i, (h, d, col) in enumerate(tp):
    x = 0.3 + i * 4.3
    box(s, x, 1.7, 4.05, 3.4, BG2)
    box(s, x + 0.35, 2.0, 1.6, 0.85, col)
    text(s, x + 0.35, 2.0, 1.6, 0.85, '… %', size=26, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 0.35, 3.1, 3.4, 0.5, h, size=21, bold=True, color=BLU)
    text(s, x + 0.35, 3.65, 3.4, 1.4, d, size=16)
band(s, 5.4, 1.15, [('La busta si chiude adesso ', {'bold': True, 'color': BLU}), ('e si riapre alla lezione 3, quando avrai i dati. La leggi solo tu.', {})], size=16)

# 5 Pillola
s = slide('Sezioni modificabili 2', {15: 'La memoria ricorda gli episodi, non le durate: per questo il tempo si misura'}, widen=TITLE_W,
          notes='Tre idee. Aggancio alla lezione 1: come Claude, anche la memoria risponde con sicurezza su cose che non ha davvero davanti.')
pil = [('Sovrastimiamo', 'Chi stima le proprie ore tende a gonfiarle rispetto ai diari, e di più chi lavora molte ore.', CEL),
       ('Il coordinamento è invisibile', 'Messaggi, ricerche, passaggi tra strumenti: pezzi brevi che non ricordiamo ma che si sommano.', BLU2),
       ('Il confronto è con te', 'Non con i benchmark di settore. Conta la tua stima contro il tuo dato, e il prima contro il dopo.', FUX)]
for i, (h, d, col) in enumerate(pil):
    x = 0.3 + i * 4.3
    box(s, x, 1.7, 4.05, 3.4, BG2)
    numdot(s, x + 0.35, 2.0, 0.75, i + 1, col)
    text(s, x + 0.35, 2.95, 3.4, 0.9, h, size=21, bold=True, color=BLU)
    text(s, x + 0.35, 3.85, 3.4, 1.2, d, size=16)
band(s, 5.4, 1.15, [('Senza una domanda l’audit è autosorveglianza. ', {'bold': True, 'color': BLU}), ('Prima di raccogliere, decidi cosa vuoi sapere alla fine.', {})], size=16)

# 6 Demo Max
s = slide('Sezioni modificabili 2', {15: 'La mia stima contro il mio calendario: lo scarto è il punto di partenza'}, widen=TITLE_W,
          notes='DA COMPILARE PRIMA DELLA LEZIONE con i tuoi numeri (vedi scaletta, “Prima del 14 dicembre”). Mostra a schermo anche la tabella che Claude ha estratto dal tuo calendario e l’errore che hai trovato verificandola, se c’è.')
cols = [('La mia stima', ['Skilled  … %', 'Strategico  … %', 'Coordinamento  … %'], CEL),
        ('Il mio calendario, 4 settimane', ['Ore di riunione a settimana  …', 'Riunioni ricorrenti  … %', 'Blocchi liberi da 90’  …', 'Riunioni organizzate da me  … %'], BLU)]
for i, (h, rows, col) in enumerate(cols):
    x = 0.3 + i * 6.45
    box(s, x, 1.55, 6.25, 0.6, col)
    text(s, x + 0.3, 1.55, 5.7, 0.6, h, size=19, bold=True, color='FFFFFF', anchor=MSO_ANCHOR.MIDDLE)
    box(s, x, 2.15, 6.25, 2.75, BG2)
    for k, r in enumerate(rows):
        text(s, x + 0.3, 2.35 + k * 0.6, 5.7, 0.5, r, size=18)
    if i == 0:
        text(s, x + 0.3, 4.3, 5.7, 0.45, 'Scritta prima di aprire il calendario.', size=14, italic=True, color=GREY)
band(s, 5.2, 1.35, [[('Cosa mi ha sorpreso: ', {'bold': True, 'color': FUX}), ('…', {})], [('Cosa il calendario non mi dice: ', {'bold': True, 'color': BLU}), ('i messaggi, le ricerche, i passaggi tra strumenti.', {})]])

# 7 Griglia
s = slide('Sezioni modificabili 2', {15: 'Ogni attività riceve quattro etichette, ma si può partire da due'}, widen=TITLE_W,
          notes='Classificate insieme tre attività della demo. Se le etichette pesano, si parte da goal e chi deve farlo: sono le due che servono alla lezione 4.')
gr = [('Tipo', 'Skilled, strategico o coordinamento?', CEL, False),
      ('Goal', 'A quale goal del tuo goal.md serve? Oppure nessuno.', FUX, True),
      ('Energia', 'Ti carica, è neutra o ti scarica?', BLU2, False),
      ('Chi deve farlo', 'Solo io, io per ora, chiunque.', FUX, True)]
for i, (h, d, col, key) in enumerate(gr):
    x = 0.3 + i * 3.21
    box(s, x, 1.7, 3.0, 3.2, BG2)
    box(s, x, 1.7, 3.0, 0.14, col, MSO_SHAPE.RECTANGLE)
    text(s, x + 0.3, 2.1, 2.5, 0.5, h, size=22, bold=True, color=BLU)
    text(s, x + 0.3, 2.75, 2.45, 1.4, d, size=17)
    if key:
        box(s, x + 0.3, 4.2, 1.9, 0.45, FUX, adj=0.5)
        text(s, x + 0.3, 4.2, 1.9, 0.45, 'si parte da qui', size=13, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
band(s, 5.25, 1.3, [('Le etichette le proponi tu o il coach, ', {'bold': True, 'color': BLU}), ('ma la conferma è sempre tua. Il coach può proporre una classificazione dalle tue descrizioni.', {})], size=16)

# 8 Chi deve farlo
s = slide('Sezioni modificabili 2', {15: 'La domanda che apre la delega: se domani non ci fossi, chi la farebbe?'}, widen=TITLE_W,
          notes='“Io per ora” è la categoria più interessante: oggi la fai tu perché mancano istruzioni, persone o fiducia. Sono spesso le candidate per un agente.')
lv = [('Solo io', 'Richiede il mio giudizio, il mio ruolo o la mia relazione.', BLU),
      ('Io per ora', 'Potrebbe farla altri, ma oggi mancano istruzioni, persone o fiducia.', FUX),
      ('Chiunque', 'Con le istruzioni giuste, la farebbe chiunque.', CEL)]
for i, (h, d, col) in enumerate(lv):
    y = 1.6 + i * 1.3
    box(s, 0.3, y, 7.6, 1.15, BG2)
    box(s, 0.3, y, 0.14, 1.15, col, MSO_SHAPE.RECTANGLE)
    text(s, 0.7, y, 2.3, 1.15, h, size=21, bold=True, color=BLU, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 3.0, y, 4.7, 1.15, d, size=16, anchor=MSO_ANCHOR.MIDDLE)
box(s, 8.2, 1.6, 4.8, 3.75, BLU)
text(s, 8.55, 1.85, 4.2, 0.45, 'Il test del neolaureato', size=19, bold=True, color='FFFFFF')
text(s, 8.55, 2.45, 4.2, 2.7, [[('“Quanti mesi servirebbero per formare un neolaureato brillante a farla?”', {'italic': True})],
                              [('Più mesi servono, più è lavoro profondo e difficile da delegare.', {})]], size=16, color='FFFFFF')
band(s, 5.65, 0.9, [('“Io per ora” ', {'bold': True, 'color': FUX}), ('è la categoria da guardare: lì nascono le schede di automazione della lezione 4.', {})], size=16)

# 9 Inventario
s = slide('Sezioni modificabili 2', {15: 'Nei prossimi 55 minuti il coach vi aiuta a elencare cosa fate sempre'}, widen=TITLE_W,
          notes='Ognuna lancia /coach audit nella sua cartella. Il coach parte dalla domanda dell’audit e dalle tre percentuali: riportano quelle della busta. Poi “Ripercorri un mese tipico: cosa fai sempre?” e “Cos’altro?”. Tu giri e sblocchi solo problemi tecnici.')
st = [('La domanda', 'Cosa vuoi sapere alla fine?'), ('La stima', 'Le tre percentuali della busta'), ('Un mese tipico', 'Cosa fai sempre? Cos’altro?'),
      ('Quanto', 'Frequenza, durata, ore al mese'), ('Le etichette', 'Almeno goal e chi deve farlo')]
for i, (h, d) in enumerate(st):
    x = 0.3 + i * 2.55
    box(s, x, 1.8, 2.45, 1.0, [CEL, CEL, BLU2, BLU2, FUX][i], MSO_SHAPE.CHEVRON)
    text(s, x + 0.35, 1.8, 1.6, 1.0, str(i + 1), size=26, color='FFFFFF', bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 3.1, 2.3, 0.45, h, size=19, bold=True, color=BLU)
    text(s, x, 3.6, 2.2, 1.2, d, size=16)
box(s, 0.3, 5.1, 12.7, 1.45, BG2)
text(s, 0.6, 5.1, 12.1, 1.45, [[('Obiettivo: almeno 15 attività ricorrenti. ', {'bold': True, 'color': BLU}), ('Comando: /coach audit', {})],
                              [('L’audit è tuo: ', {'bold': True, 'color': BLU}), ('resta nella tua cartella e alla lezione 3 porti solo ciò che scegli.', {})]], size=17, anchor=MSO_ANCHOR.MIDDLE)

# 10 Consegna
s = slide('Sezioni modificabili 2', {15: 'Per lunedì 21: quattro settimane di calendario. A gennaio, cinque giorni di diario'}, widen=TITLE_W,
          notes='Il calendario è il dato pesante: quattro settimane normali, dal 16 novembre all’11 dicembre, e basta da solo per aprire la busta alla lezione 3. Il diario non cade più sotto Natale: ognuna sceglie una settimana tra l’11 e il 29 gennaio, fuori dai suoi picchi, e lo compila all’ora che le va bene.')
cs = [('1', 'Il calendario', '30 minuti, entro mercoledì 16', 'Claude legge dal tuo Outlook le settimane dal 16/11 all’11/12. Una settimana alla volta: trascrive, tu verifichi, poi calcola quattro numeri.', BLU2),
      ('2', 'Il diario, a gennaio', '4 minuti, due volte al giorno', 'Cinque giorni in una settimana a scelta tra l’11 e il 29 gennaio. A metà giornata e quando esci, all’ora che va bene a te.', CEL)]
for i, (nn, h, t, d, col) in enumerate(cs):
    x = 0.3 + i * 6.45
    box(s, x, 1.6, 6.25, 3.0, BG2)
    numdot(s, x + 0.35, 1.9, 0.75, nn, col)
    text(s, x + 1.35, 1.9, 4.6, 0.45, h, size=22, bold=True, color=BLU)
    text(s, x + 1.35, 2.35, 4.6, 0.35, t, size=15, color=GREY)
    text(s, x + 0.35, 3.0, 5.6, 1.5, d, size=17)
band(s, 4.95, 1.6, [[('Prima di uscire: ', {'bold': True, 'color': BLU}), ('dai a Claude il primo prompt sulla prima settimana.', {})],
                    [('Settimana piena? ', {'bold': True, 'color': BLU}), ('Versione minima da 15: le ultime due settimane di calendario. Scrivi in chat la settimana del diario.', {})]])

# 11 Calendario: come
s = slide('Sezioni modificabili 2', {15: 'Claude legge il calendario in due passi: prima la tabella da verificare, poi i numeri'}, widen=TITLE_W,
          notes='Il connettore Microsoft 365 è in sola lettura: Claude non può modificare il calendario. È la lezione 1 applicata: Claude può saltare un evento o leggere male un orario ricorrente.  Se il connettore non risponde, ripiego: screenshot della vista settimanale con lo stesso prompt. Per questo la tabella si controlla prima dei conti. I titoli con nomi di persone non servono: Claude usa il tipo di riunione. Per chi fa recruiting gli eventi portano nomi di candidati: si usa la vista occupato/libero, in screenshot, invece del connettore.')
box(s, 0.3, 1.5, 6.25, 5.05, 'F2F4F7')
text(s, 0.6, 1.65, 5.7, 0.4, 'Passo 1 · Il prompt', size=15, bold=True, color=GREY)
text(s, 0.6, 2.1, 5.75, 2.4, '“Leggi dal mio calendario Outlook gli eventi della settimana dal 16 al 20 novembre. Trascrivi in una tabella: giorno, inizio, fine, tipo di riunione, se l’ho organizzata io. Non riportare nomi di persone. Non calcolare niente finché non ti confermo la tabella.” Poi la settimana dopo.', size=16, italic=True, color=TXT)
box(s, 0.55, 4.55, 5.75, 1.75, 'FFFFFF')
text(s, 0.8, 4.65, 5.3, 0.4, 'Poi verifica la tabella', size=16, bold=True, color=FUX)
text(s, 0.8, 5.1, 5.3, 1.1, 'Con Outlook aperto accanto: manca qualche evento? Gli orari sono giusti? Le tre domande della lezione 1 valgono anche qui.', size=15)
text(s, 6.9, 1.55, 6.1, 0.45, 'Passo 2 · Dopo la tua verifica, quattro numeri', size=17, bold=True, color=BLU)
nm = [('Ore di riunione', 'a settimana'), ('Riunioni ricorrenti', 'quota sul totale'), ('Blocchi liberi da 90’', 'quanti a settimana'), ('Organizzate da te', 'contro quelle a cui sei invitata')]
for i, (h, d) in enumerate(nm):
    y = 2.15 + i * 1.08
    box(s, 6.9, y, 6.1, 0.95, BG2)
    numdot(s, 7.1, y + 0.2, 0.55, i + 1, [CEL, BLU2, FUX, ARA][i], size=16)
    text(s, 7.85, y, 2.9, 0.95, h, size=17, bold=True, color=BLU, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 10.7, y, 2.2, 0.95, d, size=14, anchor=MSO_ANCHOR.MIDDLE)
text(s, 6.9, 6.5 - 0.0, 6.1, 0.3, 'Poi chiedi al coach di salvarli in artefatti/time-audit.', size=13, italic=True, color=GREY)

exec(open('/tmp/claude-0/-home-user/fb6aa437-ef98-50a4-a83e-9179b450ba71/scratchpad/ts/kitfns.py', encoding='utf-8').read())
links('Per approfondire: il tempo profondo e il tempo che si disperde', [
    ('Sei strategie da Deep Work', 'Il lavoro profondo di Cal Newport: perché servono blocchi lunghi.', 'https://www.youtube.com/watch?v=BsFnWKcZTss', 'italiano'),
    ('Recensione di Deep Work', 'Le idee del libro in breve, con esempi pratici.', 'https://www.youtube.com/watch?v=CjNLMVBJLNY', 'italiano'),
    ('Come gestire il tempo in ufficio', 'Pianificare tenendo conto delle emergenze, cioè del tempo non pianificato.', 'https://www.youtube.com/watch?v=syO4kcv1kSY', 'italiano'),
    ('Cos’è l’intelligenza artificiale?', 'Se non l’hai visto la settimana scorsa: la prima pillola di Enkk.', 'https://www.youtube.com/watch?v=0eyKR8P1WR0', 'italiano')])

# 12 Chiusura
slide('Chiusura-Blu', {0: 'Cosa ti aspetti di scoprire?', 13: 'Prossima lezione: lunedì 21 dicembre'})

p.save(OUT)
print('ok', len(p.slides))
