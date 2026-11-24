cover('Lezione 8 · Skill, plugin, connettori', 'Lunedì 8 febbraio 2027')

agenda('Oggi smontiamo il coach e ognuna costruisce la sua prima skill', [
    ('0-20’', 'Ripartenza', 'Gli errori di Claude, classificati'),
    ('20-35’', 'Pillola', 'Skill, plugin, connettore'),
    ('35-55’', 'Smontaggio', 'Com’è fatto il coach, dentro'),
    ('55-105’', 'Laboratorio', 'Una skill da una scheda al gradino 4'),
    ('105-120’', 'Consegna', 'Usarla tre volte, e le fonti')],
    'una skill tua, già provata su un caso reale, e le parole per capire come è fatto un agente.',
    notes='Blocco C, una sola lezione. È il ponte verso l’agente: chi ha costruito una skill ha già costruito un pezzo di agente.')

cards3('Gli errori della settimana hanno tre origini, e ognuna ha un rimedio diverso', [
    ('Il dato era sbagliato', 'Copia vecchia, file incompleto, colonna ambigua. Rimedio: la struttura e il LEGGIMI.'),
    ('L’istruzione era ambigua', 'Claude ha fatto una cosa ragionevole, ma non quella voluta. Rimedio: il prompt in quattro pezzi.'),
    ('Ha inventato', 'Un numero o un fatto che non stava da nessuna parte. Rimedio: “da dove viene?”, sempre.')],
    R('Giro: ', 'ognuna legge la sua nota sugli errori e la mettiamo in una delle tre colonne.'),
    notes='Se un errore torna spesso nella stessa forma, è un candidato per una skill: un’istruzione che Claude carica ogni volta che serve.')

cards3('Tre parole da distinguere: skill, plugin, connettore', [
    ('Skill', 'Un file di istruzioni che Claude carica quando riconosce la situazione. Come una procedura scritta bene.'),
    ('Plugin', 'Un pacchetto di skill, comandi e regole che si installa. Il coach è un plugin.'),
    ('Connettore', 'Una porta verso un sistema esterno. Outlook in sola lettura, nella lezione 2, era un connettore.')],
    R('Un agente, nel percorso, ', 'è un plugin: regole sempre attive, skill caricate al bisogno, a volte un connettore.'),
    notes='Tieni il lessico minimo. MCP è il protocollo dei connettori: nominalo solo se lo chiedono.')

code_slide('Smontiamo il coach: le regole stanno sempre attive, gli strumenti si caricano al bisogno', 'plugin coach/',
           'core/\n   core.md          ← sempre attivo: chi è,\n                      confini, cosa non fa mai\nskills/\n   coach-tempo/\n      SKILL.md      ← “Usalo quando…”\n      t01 … t04     ← il metodo, a pezzi\n   coach-processi/\n   coach-automazione/\n   … altre 5\ncommands/\n   coach.md         ← /coach intake, audit…\nistanza-modello/    ← la cartella vuota',
           'Cosa guardare', [
               ('Il core', 'è corto: circa 1.200 parole, solo regole di comportamento.'),
               ('Ogni skill', 'si presenta con una riga: “Usalo quando…”.'),
               ('Claude legge', 'solo le righe, e apre la skill quando la situazione corrisponde.'),
               ('Il comando', 'è una scorciatoia: /coach audit apre la skill giusta.')],
           R('Domanda per l’aula: ', 'perché le regole non stanno in una skill da caricare quando servono?'),
           notes='Risposta: perché un agente non si accorge di stare sbagliando, quindi non caricherebbe la regola proprio quando serve. Per questo il core è sempre attivo.')

compare('La riga “Usalo quando” descrive una situazione, non un contenuto', (
    'Così non scatta', FUX, ['“Contiene i criteri di automazione”', '“Template per le mail ai docenti”', '“Informazioni sul catalogo corsi”']), (
    'Così scatta', BLU, ['“Va valutata una singola attività: criteri, conto del pareggio, scheda”', '“Bisogna scrivere a un docente esterno per confermare date e aula”', '“Una collega chiede quali corsi sono aperti in un periodo”']),
    [R('Claude non sa cosa c’è dentro la skill ', 'finché non la apre. Decide di aprirla dalla riga: la riga deve somigliare alla richiesta.')],
    notes='Fai riscrivere a voce alta una riga sbagliata in versione giusta. È l’abilità che servirà di più nelle lezioni 9-11.')

steps('La prima skill nasce da una scheda arrivata al gradino 4: template o checklist', [
    ('Scegli la scheda', 'Una tua, ferma al gradino 4.'),
    ('Scrivi lo scopo', 'Cosa deve fare, in una frase.'),
    ('Scrivi “Usalo quando”', 'La situazione, con le parole di chi la chiede.'),
    ('Istruzioni ed esempio', 'Passi, formato, un esempio riuscito.'),
    ('Provala', 'Su un caso reale, subito.')],
    [R('In Cowork: ', 'chiedi a Claude “aiutami a creare una skill” e lavorate insieme sui cinque passi.'), R('Le skill di team ', 'vanno in 04_modelli, con un LEGGIMI.')],
    notes='Il gradino 4 è il più adatto: template e checklist sono istruzioni pure, senza sistemi da mantenere. Una skill è un template che si attiva da solo.')

code_slide('Com’è fatta una skill: un nome, una riga, delle istruzioni', 'conferma-docente/SKILL.md',
           '---\nname: conferma-docente\ndescription: Usalo quando bisogna\n  scrivere a un docente esterno per\n  confermare date, aula e materiali.\n---\n1. Chiedi corso, date, aula e\n   materiali se mancano.\n2. Scrivi la mail con il modello\n   in fondo, tono cordiale e breve.\n3. Elenca cosa manca prima di\n   proporre l’invio.\nModello: …',
           'Le regole di scrittura', [
               ('Istruzioni,', 'non spiegazioni: “scrivi”, “chiedi”, “elenca”.'),
               ('Un esempio', 'riuscito vale più di tre regole.'),
               ('Cosa manca:', 'la skill dice cosa chiedere se l’input è incompleto.'),
               ('Corta:', 'se supera una pagina, sono due skill.')],
           R('Esempio inventato: ', 'la tua skill parte da una tua scheda e dal tuo modo di lavorare.'),
           notes='Le skill in Cowork si creano e si gestiscono dall’app: prima della lezione verifica il flusso sulla versione installata.')

cards2('Per lunedì 15: usare la skill tre volte, e leggere le fonti dell’agente', [
    (1, 'La tua skill, tre volte', '30 minuti nella settimana', 'Su casi reali. Ogni volta: ha scattato da sola? Il risultato era giusto? Correggi la riga o le istruzioni.'),
    (2, 'Le fonti, per gruppo', '15 minuti', 'Leggete le fonti raccolte alla lezione 4 e segnate per ognuna: serve, non serve, non so.')],
    [R('Se la skill non scatta da sola, ', 'il problema è quasi sempre la riga “Usalo quando”.'), R('Tempo totale: ', 'circa 45 minuti.')],
    notes='Le fonti annotate sono l’input della fase 3 del processo standard, alla lezione 9.')

VIDEOS = [
    ('Come usare le Skills per Claude', 'Cosa sono e come insegnano nuove capacità a Claude.', 'https://www.youtube.com/watch?v=gd5u63lx7Ug', 'italiano'),
    ('Tutorial: creare skill con Claude', 'Un esempio di costruzione passo per passo.', 'https://www.youtube.com/watch?v=rbKeqQEkgzY', 'italiano'),
    ('MCP spiegati in modo semplice', 'Il protocollo dietro i connettori, senza tecnicismi.', 'https://www.youtube.com/watch?v=B8HrcWybU78', 'italiano'),
    ('MCP: cos’è e come usarlo', 'Per chi vuole capire come si collegano gli strumenti.', 'https://www.youtube.com/watch?v=JHDAqk3_lWY', 'italiano')]
EXTRA = None
links('Per approfondire: skill e connettori, in italiano', VIDEOS)

closing('Quale lavoro ripetitivo diventerà la tua prossima skill?', 'Prossima lezione: lunedì 15 febbraio')

SCALETTA = {
    'title': 'Lezione 8 · Skill, plugin, connettori',
    'subtitle': 'Scaletta del facilitatore · lunedì 8 febbraio 2027 · 2 ore · 5 colleghe',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'Le colleghe classificano gli errori di Claude della settimana, imparano a distinguere skill, plugin e connettore, smontano il plugin coach per vedere core e skill, e costruiscono una prima skill da una scheda arrivata al gradino 4. È il ponte verso l’agente: una skill è già un pezzo di agente.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Quando un lavoro si ripete con la stessa forma, scriverlo una volta come istruzione invece di rispiegarlo ogni volta.'],
            ['Output in aula', 'Una skill personale creata e provata su un caso reale.'],
            ['Output per il 15/2', 'La skill usata tre volte e corretta. Fonti dei gruppi annotate: serve, non serve, non so.'],
            ['Segnale che ha funzionato', 'Almeno tre skill su cinque scattano da sole, senza essere chiamate per nome.']]],
        ['h1', 'Prima dell’8 febbraio'],
        ['b', 'Verifica come si creano e si gestiscono le skill nella versione di Cowork installata sui Mac delle colleghe: dove si trovano, come si attivano, come si condividono. La slide 7 dice “chiedi a Claude di aiutarti a creare una skill”: controlla che sia il flusso giusto.'],
        ['b', 'Apri il plugin coach sul tuo Mac per lo smontaggio: core, una skill (coach-tempo), il comando.'],
        ['b', 'Una tua skill costruita da una scheda al gradino 4, da mostrare.'],
        ['b', 'Chiedi in chat chi ha una scheda al gradino 4. Chi non ce l’ha usa un template che manda spesso.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-20’', 'Ripartenza', 'Slide 3. Ognuna legge la nota sugli errori; si classifica in tre colonne: dato, istruzione, invenzione.'],
            ['20-35’', 'Pillola', 'Slide 4. Skill, plugin, connettore. L’agente del percorso è un plugin.'],
            ['35-55’', 'Smontaggio del coach', 'Slide 5 e 6. Apri il plugin a schermo. La domanda: perché le regole non stanno in una skill? La riga “Usalo quando”, giusta e sbagliata.'],
            ['55-105’', 'Laboratorio', 'Slide 7 e 8. Ognuna costruisce la sua skill in cinque passi e la prova su un caso reale. Due le mostrano a fine blocco.'],
            ['105-120’', 'Consegna', 'Slide 9, 10 e 11.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Una skill non è un prompt più lungo. È un’istruzione con una condizione di attivazione: Claude la carica quando la situazione corrisponde alla riga “Usalo quando”. Per questo la riga descrive la situazione con le parole di chi chiede, non il contenuto. È anche la regola che terrà in piedi gli agenti delle lezioni 9-11.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['La skill non scatta da sola', 'Riscrivi la riga “Usalo quando” con le parole esatte che la collega userebbe per chiedere.'],
            ['La skill fa troppo', 'Dividila: una skill, una situazione.'],
            ['Una collega vuole costruire subito un agente', 'Va bene l’entusiasmo: la skill è il primo pezzo. L’agente si costruisce dalla lezione 9 con il processo standard.'],
            ['Nessuna scheda al gradino 4', 'Si parte da un template che la collega manda spesso: è un gradino 4 non ancora scritto.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda, la registrazione dello smontaggio del coach, le skill che le colleghe scelgono di mettere in 04_modelli (sono già strumenti di team).']]}

CONSEGNA = {
    'title': 'Lezione 8 · Il lavoro per lunedì 15 febbraio',
    'subtitle': 'Percorso AI per Talent · tempo stimato: circa 45 minuti',
    'blocks': [
        ['h1', '1. La tua skill, tre volte (30’ nella settimana)'],
        ['p', 'Usala su tre casi reali. Dopo ogni uso, una riga:'],
        ['table', [1800, 2000, 2000, 3838], [
            ['Caso', 'È scattata da sola?', 'Risultato giusto?', 'Cosa ho corretto'],
            [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]],
        ['p', 'Se non scatta da sola, il problema è quasi sempre la riga “Usalo quando”: riscrivila con le parole che useresti per chiedere.'],
        ['h1', '2. Le fonti dell’agente, per gruppo (15’)'],
        ['p', 'Riprendete la cartella fonti della lezione 4. Per ogni documento segnate:'],
        ['b', 'Serve: dice all’agente cosa fare o come farlo.'],
        ['b', 'Non serve: doppione, vecchio, fuori tema.'],
        ['b', 'Non so: lo decidiamo insieme alla lezione 9.'],
        ['h1', 'Cosa porti alla lezione 9'],
        ['b', 'La skill corretta e le tre righe d’uso.'],
        ['b', 'Le fonti annotate del tuo gruppo.']]}
