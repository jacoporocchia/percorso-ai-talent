cover('Lezione 3 · Leggere l’audit', 'Lunedì 21 dicembre 2026')

agenda('Oggi i dati del tempo diventano tre attività su cui decidere', [
    ('0-20’', 'La busta', 'La stima di due settimane fa contro il dato'),
    ('20-35’', 'Pillola', 'Tre numeri che contano più degli altri'),
    ('35-80’', 'Lettura', 'Con il coach, una domanda alla volta'),
    ('80-105’', 'Candidate', 'Quattro gruppi e tre attività scelte'),
    ('105-120’', 'Consegna', 'La regola zero, entro l’11 gennaio')],
    'la sintesi del tuo time audit salvata dal coach e tre attività candidate, scelte perché pesano.',
    notes='Ultima lezione prima della pausa. La consegna è leggera di proposito: 30 minuti, da fare prima del 23 dicembre o dopo il 6 gennaio.')

cards3('La busta si riapre: lo scarto tra stima e dato è il primo risultato dell’audit', [
    ('Apri la busta', 'Rileggi le tre percentuali scritte il 14 dicembre, prima di misurare.'),
    ('Mettile accanto ai dati', 'I quattro numeri del calendario e il diario della settimana.'),
    ('Trova lo scarto più grande', 'Dove la tua stima era più lontana? In che direzione?')],
    R('In plenaria si dice solo la direzione: ', '“pensavo meno coordinamento”, non i numeri. I numeri restano tuoi.'),
    notes='Giro veloce: ognuna dice in una frase dove la stima era più lontana. Se qualcuna non ha i dati completi, lavora sul calendario: il diario era il colore.')

cards3('Tre numeri contano più degli altri: tempo sui goal, tempo che richiede te, blocchi lunghi', [
    ('Quota sui goal', 'Quanta parte del tempo serve almeno uno dei tuoi goal. Misura l’allineamento tra quello che vuoi e quello che fai.'),
    ('Quota “solo io”', 'Quanta parte richiede davvero te. Il resto è potenziale di delega, a una persona o a uno strumento.'),
    ('Blocchi da 90’', 'Quanti blocchi liberi lunghi hai a settimana. Il lavoro skilled ne ha bisogno.')],
    R('Il confronto è con te stessa: ', 'nessun benchmark di settore, solo la tua stima contro il tuo dato, oggi e ad aprile.'),
    notes='Collegamento con la lezione 2: la quota sui goal usa il goal.md, la quota “solo io” usa l’etichetta chi deve farlo. Senza quelle due etichette questi numeri non esistono.')

steps('Il coach legge i dati con te, una domanda alla volta', [
    ('Cosa ti sorprende?', 'Si parte sempre da qui.'),
    ('Dove la stima era lontana?', 'Sulle due o tre attività principali.'),
    ('Quanto va ai goal?', 'Ti torna?'),
    ('Cosa dà energia?', 'E cosa la toglie, in che fasce orarie.'),
    ('Quanto richiede te?', 'Quante di queste ore, davvero.')],
    [R('Comando: ', '/coach audit, poi “leggiamo i dati dell’audit”.'), R('Alla fine: ', 'il coach salva la sintesi in artefatti/time-audit. Rileggila e correggila.')],
    notes='Ognuna lavora sola con il coach. Il coach usa t04. Tu giri e sblocchi solo problemi tecnici. Se il coach dà consigli invece di fare domande, la collega può scrivere “torna in modalità coach”.')

cards4('Ogni attività candidata finisce in uno di quattro gruppi', [
    ('Da smettere', '“Quale potresti smettere domani senza che nessuno se ne accorga?”'),
    ('Da passare', '“Chi potrebbe farla, con le giuste istruzioni?”'),
    ('Da ridisegnare', 'Richiede un cambiamento di processo o di struttura, non solo di persona.'),
    ('Da proteggere', '“Quale attività di valore vorresti avesse più spazio? Dove lo prendi?”')],
    R('Le prime tre liberano tempo. ', 'La quarta dice a cosa serve il tempo liberato: senza, finisce in altre email.'),
    notes='Il gruppo “da proteggere” è quello che si dimentica. Chiedilo sempre: dà senso a tutto il resto del percorso.')

rows('Si scelgono tre candidate: quelle che pesano, non quelle che ci piacerebbe automatizzare', [
    ('Pesa', 'Molte ore al mese, o poche ore ma ripetute spesso.'),
    ('Non richiede te', 'Etichetta “io per ora” o “chiunque”.'),
    ('Si ripete', 'Ha una forma riconoscibile ogni volta.'),
    ('Ti scarica', 'A parità di ore, prima quella che toglie energia.')],
    side=('La domanda da farsi', ['“Voglio occuparmene perché sposta un numero, o perché costruire la soluzione mi piace?”', 'È la domanda più scomoda del coach. Va fatta.']),
    notes='Ognuna scrive le sue tre candidate nel coach. In plenaria, solo i nomi delle attività, se vogliono: servirà alla lezione 4 per vedere i processi comuni.')

cards4('Regola zero: prima di chiedere “l’AI può farlo?”, chiedersi “va fatto?”', [
    ('Eliminare', 'Si può togliere? Cosa succede se non si fa?'),
    ('Combinare', 'Si può accorpare con un’altra attività?'),
    ('Riordinare', 'Si può spostare in un momento o in una sequenza migliore?'),
    ('Semplificare', 'Si può fare con meno passaggi, meno varianti, un formato unico?')],
    R('Automatizzare un’attività inutile ', 'la rende solo più veloce a essere inutile, e più difficile da eliminare dopo.'),
    notes='È ECRS, ma non serve nominarlo. Fai un esempio dal vivo su una tua attività: quale delle quattro domande la cambia?')

cards2('Per l’11 gennaio: la regola zero sulle tre candidate', [
    (1, 'Cosa succede se smetto?', '10 minuti per candidata', 'Chiedilo a te stessa e, se serve, a chi riceve il risultato. Annota la risposta, anche se è “non succede niente”.'),
    (2, 'Si può semplificare?', 'Con le quattro domande', 'Eliminare, combinare, riordinare, semplificare. Annota cosa cambieresti prima di pensare a uno strumento.')],
    [R('Dove: ', 'nel coach, con /coach automazione: parte proprio da qui.'),
     R('Quando: ', 'prima del 23 dicembre o dopo il 6 gennaio. Circa 30 minuti in tutto.')],
    notes='La lezione 4 parte dagli esiti: le candidate che sopravvivono alla regola zero diventano schede di automazione.')

VIDEOS = [
    ('I 7 sprechi della lean production', 'Gli sprechi nati in fabbrica: molti esistono identici in ufficio.', 'https://www.youtube.com/watch?v=kvPBm6fXx3k', 'italiano'),
    ('Pillole di Lean: i 7 muda', 'La stessa idea in pochi minuti.', 'https://www.youtube.com/watch?v=YjpK6zO_-hI', 'italiano'),
    ('7 sprechi da evitare nel Lean Thinking', 'Una puntata della serie Fuga dai muda.', 'https://www.youtube.com/watch?v=0D0EqLqePXI', 'italiano'),
    ('Muda attesa', 'L’attesa: lo spreco più invisibile nel lavoro d’ufficio.', 'https://www.youtube.com/watch?v=0xEafcBjErs', 'italiano')]
EXTRA = None
links('Per approfondire: gli sprechi, prima di qualsiasi strumento', VIDEOS)

closing('Quale attività smetteresti domani?', 'Prossima lezione: lunedì 11 gennaio')

SCALETTA = {
    'title': 'Lezione 3 · Leggere l’audit',
    'subtitle': 'Scaletta del facilitatore · lunedì 21 dicembre 2026 · 2 ore · 5 colleghe',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'Le colleghe riaprono la busta con la stima, leggono con il coach i dati di calendario e diario, raggruppano le attività in quattro gruppi e scelgono tre candidate. Escono con la sintesi del time audit salvata e un lavoro leggero per la pausa: la regola zero sulle tre candidate.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Davanti a un’attività che pesa, chiedersi prima se va fatta e se si può semplificare, poi chi o cosa può farla.'],
            ['Output in aula', 'Sintesi del time audit in artefatti/time-audit (template di t04). Tre attività candidate scritte nel coach.'],
            ['Output per l’11/1', 'Per ogni candidata, l’esito della regola zero: cosa succede se smetto, cosa si può semplificare.'],
            ['Segnale che ha funzionato', 'Almeno una candidata per collega è “da smettere” o “da semplificare”, non solo “da automatizzare”.']]],
        ['h1', 'Prima del 21 dicembre'],
        ['b', 'Tieni pronta la tua sintesi dell’audit della lezione 2: la usi come esempio di lettura e per l’esempio dal vivo della regola zero.'],
        ['b', 'Verifica in chat chi ha i dati completi. Chi ha solo il calendario lavora su quello: il diario era il colore.'],
        ['b', 'Le buste sono loro: ricorda di portarle nel messaggio di promemoria.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-20’', 'La busta', 'Slide 2 e 3. Ognuna apre la busta e mette le percentuali accanto ai dati. Giro: una frase a testa sulla direzione dello scarto più grande, senza numeri.'],
            ['20-35’', 'Pillola', 'Slide 4. Tre numeri: quota sui goal, quota “solo io”, blocchi da 90 minuti. Mostrali sulla tua sintesi.'],
            ['35-80’', 'Lettura con il coach', 'Slide 5. /coach audit, “leggiamo i dati dell’audit”. Il coach fa le cinque domande di t04 una alla volta e alla fine salva la sintesi. Tu giri.'],
            ['80-105’', 'I quattro gruppi e le candidate', 'Slide 6 e 7. Ognuna raggruppa le attività: da smettere, da passare, da ridisegnare, da proteggere. Poi sceglie tre candidate con i quattro criteri. Fai la domanda scomoda: sposta un numero o mi piace costruirlo?'],
            ['105-120’', 'Regola zero e consegna', 'Slide 8 e 9. Esempio dal vivo della regola zero su una tua attività. Ognuna avvia /coach automazione sulla prima candidata prima di uscire. Slide 10 e 11.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Il percorso non è “troviamo cosa automatizzare”. È “troviamo dove va il tempo e decidiamo”. Eliminare e semplificare sono decisioni di pari dignità rispetto ad automatizzare, e spesso valgono di più: non lasciano un sistema da mantenere. Il KPI del primo obiettivo lo dice in chiaro: conta anche la quota di schede che si fermano ai gradini bassi.'],
        ['h1', 'Template di sintesi (dal coach, t04)'],
        ['quote', 'DOMANDA DELL’AUDIT · PERIODO E METODO · STIMA vs DATO · METRICHE: tipo, sui goal, solo io, deep work, blocchi da 90’ · COSA SORPRENDE · DECISIONI: elimina, delega, automatizza, ridisegna, proteggi · RIMISURA: 19 aprile 2027'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['Una collega non ha fatto il diario né il calendario', 'Lavora sull’inventario della lezione 2: ore al mese stimate per attività. Lo dice apertamente come stima e fa il calendario durante la pausa.'],
            ['Il coach dà consigli invece di fare domande', 'Scrivere “torna in modalità coach, una domanda alla volta”. È una buona occasione per un /coach lezione.'],
            ['Tutte le candidate sono “da automatizzare”', 'Chiedi per ognuna: cosa succede se smetti? Se nessuno ha mai provato a non farla, la risposta non è nota.'],
            ['Emergono dati delicati sul carico di lavoro', 'Restano nella sua istanza. In aula si condivide solo ciò che lei sceglie.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'La registrazione della plenaria (pillola, quattro gruppi, regola zero), il deck, la scheda della consegna, il template di sintesi senza dati. Non entrano buste, sintesi e candidate delle colleghe.']]}

CONSEGNA = {
    'title': 'Lezione 3 · Il lavoro per lunedì 11 gennaio',
    'subtitle': 'Percorso AI per Talent · tempo stimato: 30 minuti, prima del 23 dicembre o dopo il 6 gennaio',
    'blocks': [
        ['h1', 'La regola zero sulle tre candidate'],
        ['p', 'Nella tua cartella del coach scrivi /coach automazione e indica la prima candidata. Il coach parte da qui: prima di automatizzare, si chiede se va fatto. Ripeti per le altre due.'],
        ['h2', '1. Cosa succede se smetto?'],
        ['p', 'Chiedilo a te stessa e, se serve, a chi riceve il risultato. Annota la risposta, anche se è “non succede niente”: è il risultato migliore possibile.'],
        ['h2', '2. Si può semplificare?'],
        ['n', 'Eliminare: si può togliere del tutto, o in parte?'],
        ['n', 'Combinare: si può accorpare con un’altra attività?'],
        ['n', 'Riordinare: si può fare in un momento o in una sequenza migliore?'],
        ['n', 'Semplificare: meno passaggi, meno varianti, un formato unico?'],
        ['table', [2600, 3519, 3519], [
            ['Candidata', 'Se smetto…', 'Cosa semplificherei'],
            [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]],
        ['h1', 'Cosa porti alla lezione 4'],
        ['b', 'La sintesi del tuo audit, salvata dal coach.'],
        ['b', 'Le tre candidate con l’esito della regola zero.'],
        ['p', [{'text': 'La lezione 4 parte da qui: le candidate che sopravvivono diventano schede di automazione.', 'italics': True, 'color': '1860A8'}]]]}
