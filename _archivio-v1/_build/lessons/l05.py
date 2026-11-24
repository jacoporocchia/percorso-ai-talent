cover('Lezione 5 · Dove vivono i dati', 'Lunedì 18 gennaio 2027')

agenda('Oggi contiamo dove stanno i dati di Talent e quante copie ne esistono', [
    ('0-15’', 'Ripartenza', 'Schede e fonti: a che punto siete'),
    ('15-30’', 'Il test', 'Cinque file da trovare, un minuto ciascuno'),
    ('30-45’', 'Pillola', 'Fonte unica contro copia'),
    ('45-105’', 'Laboratorio', 'Mappa dei luoghi e caccia ai duplicati'),
    ('105-120’', 'Consegna', 'La mappa dei tuoi file su un tema')],
    'il numero di copie che hai trovato su un caso reale, e un tempo di ricerca da battere alla lezione 7.',
    notes='Si apre il blocco B. Il filo con la lezione 1: il confronto era sbagliato perché il file giusto era un terzo, arrivato per mail. Oggi si guarda il problema dalla parte dei dati.')

rows('Il test dei cinque file: un minuto ciascuno, cronometro alla mano', [
    ('Cinque richieste', 'Tu leggi una richiesta reale alla volta: “trovami l’ultima versione di…”.'),
    ('Un minuto', 'Ognuna cerca dove cercherebbe davvero. Si ferma allo scadere.'),
    ('Si annota', 'Trovato sì o no, in quanto tempo, ed è la versione giusta?'),
    ('Si ripete', 'Alla lezione 7, sulla struttura nuova. Stesse richieste.')],
    side=('Perché misuriamo', ['È il secondo KPI del percorso: un dato si trova in meno di un minuto.', 'Oggi è la base. La differenza con la lezione 7 è il risultato delle lezioni 5 e 6.']),
    notes='Le cinque richieste le prepari tu prima della lezione, su file reali di Talent (vedi scaletta). Annota i risultati in forma aggregata: quante su cinque trovate in tempo, in media.')

cards3('Un dato vive in un solo posto: altrove si mette un link, non una copia', [
    ('La copia diverge', 'Appena qualcuno corregge l’originale, la copia è vecchia. E nessuno glielo dice.'),
    ('La copia non sa di esserlo', 'Un file “_def_v3” sembra l’ultimo. Lo era, forse, il giorno in cui è stato salvato.'),
    ('Chi cerca non sa scegliere', 'Tre file simili, tre date diverse: quale è vero? Lo sa solo chi li ha creati.')],
    R('Ricordi la lezione 1? ', 'Claude aveva fatto bene i conti sul file sbagliato. Il problema non era Claude, era la copia.'),
    notes='Fonte unica non vuol dire un solo file per tutto: vuol dire che per ogni dato c’è un posto che fa fede, e gli altri puntano lì.')

cards4('I dati di Talent stanno in almeno quattro tipi di posto', [
    ('Cartelle condivise', 'OneDrive, SharePoint, unità di rete. Spesso con copie locali.'),
    ('Mail e allegati', 'L’allegato come archivio: la versione giusta è nell’ultimo messaggio.'),
    ('Excel personali', 'Il file di lavoro sul desktop che diventa la fonte senza dirlo.'),
    ('Sistemi', 'Gestionale HR, piattaforma corsi, portale del fondo: i sistemi di record.')],
    R('Esercizio a coppie, 15 minuti: ', 'per un tema che conoscete bene, dove sta ogni pezzo? Quale fa fede?'),
    notes='I sistemi di record sono la fonte per definizione sui dati di persone: il resto dovrebbe esserne un’estrazione temporanea, non un archivio parallelo.')

code_slide('La cartella del coach è un esempio di struttura che regge', 'Struttura del coach',
           'plugin coach/          ← il metodo, per tutte\n   core, skill, comandi\n\ncoach-<nome>/          ← la tua istanza, privata\n   coach.json\n   memoria/             ← fatti su di te\n      profilo, goal, impegni\n   artefatti/           ← quello che produci\n      time-audit/\n      processi/\n      automazioni/',
           'Tre separazioni da copiare', [
               ('Metodo e istanza.', 'Le regole sono uguali per tutte, i dati sono di ognuna.'),
               ('Memoria e artefatti.', 'Chi sei e cosa vuoi sta separato da quello che produci.'),
               ('Un posto per ogni cosa.', 'La sintesi dell’audit sta in un punto solo, e lì la trovi.')],
           R('La lezione 6 parte da qui: ', 'la stessa logica, applicata alla cartella condivisa di Talent.'),
           notes='Fai aprire a ognuna la sua cartella del coach e ritrovare la sintesi dell’audit: è la prova che una struttura semplice funziona.')

prompt_slide('Caccia ai duplicati con Claude: prima l’elenco, poi il giudizio, che resta tuo', 'Il prompt, in Cowork sulla cartella scelta',
             '“Guarda la cartella che ti ho dato. Elenca i file con nome, data di modifica e dimensione. Raggruppa quelli che sembrano lo stesso documento in versioni diverse. Non spostare, non rinominare, non cancellare niente.”',
             'Poi decidi tu', 'Per ogni gruppo: quale è la versione vera? Claude propone, ma solo tu sai quale file è stato mandato al responsabile.',
             'Cosa contare, per ogni tema', [
                 ('Luoghi', 'dove sta il tema'), ('Copie', 'dello stesso documento'), ('La vera', 'quale fa fede, e perché'), ('Il tempo', 'per capirlo')],
             foot='Si lavora su una copia o in sola lettura: oggi non si sposta niente.',
             notes='Cowork lavora sulla cartella che la collega gli dà. Insisti su “non spostare, non cancellare”: la migrazione è il lavoro della lezione 6, con regole condivise.')

cards2('Per lunedì 25: la mappa dei tuoi file su un tema', [
    (1, 'Scegli un tema', '5 minuti', 'Uno che conosci bene e che usi spesso, per esempio la formazione 2026. Meglio stretto che largo.'),
    (2, 'Fai la mappa', '40 minuti', 'Dove stanno i file, quante copie per documento, qual è quella vera. Con il prompt della caccia ai duplicati.')],
    [R('Output: ', 'una tabella, salvata dove vuoi, con luoghi, copie e versione vera.'), R('Regola: ', 'non spostare e non cancellare niente. Si migra alla lezione 6, tutte insieme.')],
    notes='Il numero di copie trovate è la base del KPI “duplicati prima e dopo”. Raccoglilo in forma aggregata alla lezione 6.')

VIDEOS = [
    ('Come organizzo i file sul computer', 'Cinque regole per non perdere nulla.', 'https://www.youtube.com/watch?v=qzUO7GeIUjg', 'italiano'),
    ('Cosa sono gli embeddings?', 'Enkk: come un modello riconosce che due testi parlano della stessa cosa.', 'https://www.youtube.com/watch?v=oerMG3VRLXk', 'italiano'),
    ('The PARA method', 'Un sistema per organizzare file per progetti, aree, risorse, archivio.', 'https://www.youtube.com/watch?v=s8-wJ1RxWmY', 'inglese, sottotitoli'),
    ('PARA method explained', 'La stessa idea in sintesi.', 'https://www.youtube.com/watch?v=2T1nqYLlpGs', 'inglese, sottotitoli')]
EXTRA = None
links('Per approfondire: organizzare i file perché si trovino', VIDEOS)

closing('Quante copie hai trovato del file che pensavi unico?', 'Prossima lezione: lunedì 25 gennaio')

SCALETTA = {
    'title': 'Lezione 5 · Dove vivono i dati',
    'subtitle': 'Scaletta del facilitatore · lunedì 18 gennaio 2027 · 2 ore · 5 colleghe',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'Si apre il blocco B. Le colleghe misurano quanto ci mettono a trovare cinque file reali, capiscono perché la copia è il nemico, mappano dove stanno i dati di Talent e contano i duplicati su un caso reale con Claude. Escono con una base da battere: tempo di ricerca e numero di copie.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Prima di salvare un file, chiedersi se esiste già da qualche parte e se basta un link.'],
            ['Output in aula', 'Risultato del test dei cinque file (base). Mappa a coppie dei luoghi di un tema. Primo conteggio dei duplicati con Claude.'],
            ['Output per il 25/1', 'Mappa dei propri file su un tema: luoghi, copie, versione vera.'],
            ['Segnale che ha funzionato', 'Ognuna trova almeno un documento con più di due copie, e sa dire quale fa fede.']]],
        ['h1', 'Prima del 18 gennaio'],
        ['b', [{'text': 'Le cinque richieste del test. ', 'bold': True}, 'Scegli cinque file reali di Talent che tutte dovrebbero saper trovare: per esempio l’ultimo calendario corsi, il report presenze di un corso concluso, il template di una lettera, il budget formazione dell’anno, una procedura. Scrivi le richieste come le faresti a voce. Tienile identiche per la lezione 7.']],
        ['b', 'Un caso reale per la caccia ai duplicati da mostrare tu: una cartella in cui sai che ci sono copie.'],
        ['b', 'Verifica che Cowork possa lavorare sulle cartelle che le colleghe useranno, comprese quelle sincronizzate da OneDrive o SharePoint.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-15’', 'Ripartenza', 'Schede completate e cartelle fonti dei gruppi: a che punto. Due minuti per gruppo.'],
            ['15-30’', 'Il test dei cinque file', 'Slide 3. Leggi una richiesta alla volta, cronometro un minuto. Ognuna annota trovato, tempo, versione giusta. Raccogli in forma aggregata.'],
            ['30-45’', 'Pillola', 'Slide 4. Fonte unica contro copia, con il richiamo alla lezione 1. Fonte unica vuol dire un posto che fa fede per ogni dato.'],
            ['45-60’', 'I luoghi', 'Slide 5. A coppie, su un tema che conoscono: dove sta ogni pezzo, quale fa fede.'],
            ['60-70’', 'La struttura del coach', 'Slide 6. Ognuna apre la sua cartella del coach e ritrova la sintesi dell’audit.'],
            ['70-105’', 'Caccia ai duplicati', 'Slide 7. Prima la tua demo su una cartella reale, poi ognuna sulla sua. Elenco con Claude, giudizio loro. Non si sposta niente.'],
            ['105-120’', 'Consegna', 'Slide 8. Ognuna sceglie il tema e lo scrive in chat. Slide 9 e 10.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Il problema dei dati non è tecnico. È che ogni copia nasce con una buona ragione (lavorarci senza disturbare, mandarla a qualcuno, tenerla “per sicurezza”) e muore senza che nessuno se ne accorga. Una struttura condivisa funziona solo se rende il link più comodo della copia.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['Cowork non vede la cartella sincronizzata', 'Lavora su una copia locale di una sottocartella, solo per la caccia ai duplicati. Annota il problema: va risolto prima della lezione 6.'],
            ['Claude propone di cancellare o spostare', 'Ripeti nel prompt “non spostare, non cancellare niente”. Le azioni sui file si fanno alla lezione 6, con regole condivise.'],
            ['Il test mette in imbarazzo qualcuno', 'I risultati sono aggregati. Il punto è il sistema, non la persona.'],
            ['Emergono file con dati personali in posti sbagliati', 'Annotali senza aprirli in aula. Sono il primo input per le regole su cosa non entra, alla lezione 6.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda della consegna, il prompt della caccia ai duplicati, il format del test dei cinque file (senza le richieste reali, che sono specifiche di Talent).']]}

CONSEGNA = {
    'title': 'Lezione 5 · Il lavoro per lunedì 25 gennaio',
    'subtitle': 'Percorso AI per Talent · tempo stimato: circa 45 minuti',
    'blocks': [
        ['h1', '1. Scegli un tema (5’)'],
        ['p', 'Uno che conosci bene e usi spesso: per esempio la formazione 2026, un progetto, un processo ricorrente. Meglio stretto che largo.'],
        ['h1', '2. Fai la mappa (40’)'],
        ['p', 'In Cowork, dai a Claude le cartelle dove pensi stiano i file del tema, una alla volta, con questo prompt:'],
        ['quote', 'Guarda la cartella che ti ho dato. Elenca i file con nome, data di modifica e dimensione. Raggruppa quelli che sembrano lo stesso documento in versioni diverse. Non spostare, non rinominare, non cancellare niente.'],
        ['p', 'Poi cerca anche nella posta: gli allegati più recenti sul tema. Per ogni documento compila una riga.'],
        ['table', [2600, 2400, 1300, 3338], [
            ['Documento', 'Dove sta (tutti i posti)', 'Copie', 'Qual è la vera, e perché'],
            [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]],
        ['p', [{'text': 'Regola: ', 'bold': True}, 'non spostare e non cancellare niente. La migrazione si fa alla lezione 6, con regole decise insieme.']],
        ['h1', 'Cosa porti alla lezione 6'],
        ['b', 'La tabella del tuo tema, con il totale delle copie trovate.'],
        ['b', 'Un esempio di copia che ti ha sorpreso.']]}
