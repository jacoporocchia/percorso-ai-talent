cover('Lezione 7 · Skill, plugin, connettori', 'Lunedì 1° febbraio 2027')

agenda('Oggi smontiamo il coach e ognuna costruisce la sua prima skill', [
    ('0-20’', 'Ripartenza', 'Gli errori di Claude, classificati'),
    ('20-35’', 'Pillola', 'Skill, plugin, connettore'),
    ('35-55’', 'Smontaggio', 'Com’è fatto il coach, dentro'),
    ('55-105’', 'Laboratorio', 'Una skill da una scheda al gradino 4'),
    ('105-120’', 'Consegna', 'Usarla tre volte, e le fonti')],
    'una skill tua, già provata su un caso reale, e le parole per capire come è fatto un agente.',
    notes='Blocco C, una sola lezione, una settimana prima che nella v1. È il ponte verso l’agente: chi ha costruito una skill ha già costruito un pezzo di agente. Nella simulazione è la lezione che riaggancia chi si era staccata nel blocco dati, perché la consegna coincide con un lavoro che va fatto comunque.')

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
    'Così scatta', BLU, ['“Bisogna scrivere a un docente esterno per confermare date e aula”', '“Un manager chiede la job description per una posizione tecnica nuova”', '“Una collega chiede quali corsi sono aperti in un periodo”']),
    [R('Claude non sa cosa c’è dentro la skill ', 'finché non la apre. Decide di aprirla dalla riga: la riga deve somigliare alla richiesta.')],
    notes='Fai riscrivere a voce alta una riga sbagliata in versione giusta. È l’abilità che servirà di più nelle lezioni 8-11. La riga “Usalo quando” somiglia al titolo di un annuncio: si scrive con le parole di chi cerca.')

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
           notes='Le skill in Cowork si creano e si gestiscono dall’app: il flusso l’hai verificato nella prova a secco con la collega pilota.')

rows('Dove vive la tua skill, e come la ritrovi lunedì prossimo', [
    ('Dove l’hai creata', 'Nella tua cartella di lavoro, non dentro la cartella del coach: lì si confonde con le sue.'),
    ('Come la vedi', 'In Cowork, nell’elenco delle skill. È una cartella con un file SKILL.md: lo apri con TextEdit.'),
    ('Come capisci se è scattata', 'Chiedi senza nominarla. Se Claude usa il tuo modello o i tuoi passi, è scattata da sola.'),
    ('Come la correggi', 'Modifichi SKILL.md, quasi sempre la riga “Usalo quando”, e riprovi.')],
    side=('Prima di uscire', ['Ognuna chiude Cowork, lo riapre e ritrova la sua skill.', 'Se non ci riesce, la ritroviamo insieme adesso, non lunedì.']),
    notes='Nella simulazione due colleghe su tre avevano creato la skill dentro la cartella del coach e a casa non la ritrovavano. Il controllo “chiudi, riapri, ritrova” prende due minuti e salva la consegna.')

cards2('Per lunedì 8: usare la skill tre volte, e leggere le fonti dell’agente', [
    (1, 'La tua skill, tre volte', '30 minuti nella settimana', 'Su casi reali. Ogni volta: ha scattato da sola? Il risultato era giusto? Correggi la riga o le istruzioni.'),
    (2, 'Le fonti, la tua parte', '15 minuti', 'Nella cartella del tuo agente, segna per ogni fonte che ti tocca: serve, non serve, non so.')],
    [R('Se la skill non scatta da sola, ', 'il problema è quasi sempre la riga “Usalo quando”.'), R('Settimana piena? ', 'Versione minima da 15: un uso e una correzione.')],
    notes='Le fonti annotate sono l’input della fase 3 del processo standard, alla lezione 8. Dividete le fonti tra le persone del gruppo in aula, prima di uscire: così nessuna aspetta le altre.')

VIDEOS = [
    ('Come usare le Skills per Claude', 'Cosa sono e come insegnano nuove capacità a Claude.', 'https://www.youtube.com/watch?v=gd5u63lx7Ug', 'italiano'),
    ('Tutorial: creare skill con Claude', 'Un esempio di costruzione passo per passo.', 'https://www.youtube.com/watch?v=rbKeqQEkgzY', 'italiano'),
    ('MCP spiegati in modo semplice', 'Il protocollo dietro i connettori, senza tecnicismi.', 'https://www.youtube.com/watch?v=B8HrcWybU78', 'italiano'),
    ('MCP: cos’è e come usarlo', 'Per chi vuole capire come si collegano gli strumenti.', 'https://www.youtube.com/watch?v=JHDAqk3_lWY', 'italiano')]
EXTRA = None
links('Per approfondire: skill e connettori, in italiano', VIDEOS)

closing('Quale lavoro ripetitivo diventerà la tua prossima skill?', 'Prossima lezione: lunedì 8 febbraio')

SCALETTA = {
    'title': 'Lezione 7 · Skill, plugin, connettori',
    'subtitle': 'Scaletta del facilitatore · lunedì 1° febbraio 2027 · 2 ore · 5 colleghe',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'Le colleghe classificano gli errori di Claude della settimana, imparano a distinguere skill, plugin e connettore, smontano il plugin coach per vedere core e skill, e costruiscono una prima skill da una scheda arrivata al gradino 4. È il ponte verso l’agente: una skill è già un pezzo di agente.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Quando un lavoro si ripete con la stessa forma, scriverlo una volta come istruzione invece di rispiegarlo ogni volta.'],
            ['Output in aula', 'Una skill personale creata e provata su un caso reale.'],
            ['Output per l’8/2', 'La skill usata tre volte e corretta. Fonti dei gruppi annotate: serve, non serve, non so.'],
            ['Segnale che ha funzionato', 'Tutte e cinque, una per una, ritrovano la loro skill dopo aver riaperto Cowork, e almeno tre skill su cinque scattano da sole. Chi non ci arriva recupera con la buddy prima della lezione 8.']]],
        ['h1', 'Prima del 1° febbraio'],
        ['b', 'Il flusso di creazione delle skill nella versione di Cowork installata è quello provato nella prova a secco con la collega pilota: dove si trovano, come si attivano, come si condividono. Se l’app è cambiata da allora, riprovalo.'],
        ['b', 'Fai degli screenshot di Cowork mentre ritrovi una skill: servono alla slide 9 e alla scheda “dove sta cosa”.'],
        ['b', 'Apri il plugin coach sul tuo Mac per lo smontaggio: core, una skill (coach-tempo), il comando.'],
        ['b', 'Una tua skill costruita da una scheda al gradino 4, da mostrare.'],
        ['b', 'Chiedi in chat chi ha una scheda al gradino 4. Chi non ce l’ha usa un template che manda spesso: una JD, una mail di convocazione, il benvenuto ai neoassunti.'],
        ['b', 'Una cartella di prova con dati finti, per chi va veloce e vuole sperimentare più skill.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-20’', 'Ripartenza', 'Slide 3. Ognuna legge la nota sugli errori; si classifica in tre colonne: dato, istruzione, invenzione.'],
            ['20-35’', 'Pillola', 'Slide 4. Skill, plugin, connettore. L’agente del percorso è un plugin.'],
            ['35-55’', 'Smontaggio del coach', 'Slide 5 e 6. Apri il plugin a schermo. La domanda: perché le regole non stanno in una skill? La riga “Usalo quando”, giusta e sbagliata.'],
            ['55-100’', 'Laboratorio', 'Slide 7 e 8. Ognuna costruisce la sua skill in cinque passi e la prova su un caso reale. Due le mostrano a fine blocco.'],
            ['100-108’', 'Dove vive la skill', 'Slide 9. Ognuna chiude Cowork, lo riapre e ritrova la sua skill. Si sistema adesso chi non ci riesce.'],
            ['108-120’', 'Consegna', 'Slide 10, 11 e 12. In gruppo, dividete le fonti da annotare.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Una skill non è un prompt più lungo. È un’istruzione con una condizione di attivazione: Claude la carica quando la situazione corrisponde alla riga “Usalo quando”. Per questo la riga descrive la situazione con le parole di chi chiede, non il contenuto. È anche la regola che terrà in piedi gli agenti delle lezioni 8-11.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['La skill non scatta da sola', 'Riscrivi la riga “Usalo quando” con le parole esatte che la collega userebbe per chiedere.'],
            ['La skill fa troppo', 'Dividila: una skill, una situazione.'],
            ['Una collega vuole costruire subito un agente', 'Dalle un ruolo invece di un rinvio: costruisce una seconda skill per 04_modelli, o fa la tester del suo gruppo sulla cartella di prova con dati finti. L’agente parte già lunedì prossimo, e lì la sua velocità servirà.'],
            ['A casa la skill non si ritrova', 'Quasi sempre è stata creata dentro la cartella del coach. La buddy la aiuta a ricrearla nella cartella di lavoro prima della lezione 8.'],
            ['Nessuna scheda al gradino 4', 'Si parte da un template che la collega manda spesso: è un gradino 4 non ancora scritto.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda, la registrazione dello smontaggio del coach, le skill che le colleghe scelgono di mettere in 04_modelli (sono già strumenti di team).']]}

CONSEGNA = {
    'title': 'Lezione 7 · Il lavoro per lunedì 8 febbraio',
    'subtitle': 'Percorso AI per Talent · 45 minuti nel tuo slot · versione minima: 15 minuti',
    'blocks': [
        ['p', [{'text': 'Settimana piena? Fai la versione minima: ', 'bold': True}, 'un uso della skill su un caso reale e una correzione (15’). Le fonti annotate restano: sono la tua parte del gruppo.']],
        ['h1', '1. La tua skill, tre volte (30’ nella settimana)'],
        ['p', 'Usala su tre casi reali. Dopo ogni uso, una riga:'],
        ['table', [1800, 2000, 2000, 3838], [
            ['Caso', 'È scattata da sola?', 'Risultato giusto?', 'Cosa ho corretto'],
            [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]],
        ['p', 'Se non scatta da sola, il problema è quasi sempre la riga “Usalo quando”: riscrivila con le parole che useresti per chiedere.'],
        ['h1', '2. Le fonti dell’agente, la tua parte (15’)'],
        ['p', 'Nella cartella del tuo agente, in 05_agenti, prendi le fonti che vi siete divise in aula. Per ognuna segna:'],
        ['b', 'Serve: dice all’agente cosa fare o come farlo.'],
        ['b', 'Non serve: doppione, vecchio, fuori tema.'],
        ['b', 'Non so: lo decidiamo insieme alla lezione 8.'],
        ['h1', 'Dove sta cosa'],
        ['table', [2900, 6738], [
            ['Domanda', 'Risposta'],
            ['Dove sta la mia skill?', 'Nella cartella di lavoro dove l’hai creata, come cartella con dentro un file SKILL.md. In Cowork la vedi nell’elenco delle skill.'],
            ['Come capisco se è scattata da sola?', 'Chiedi senza nominarla. Se Claude usa il tuo modello o i tuoi passi, è scattata.'],
            ['Come la correggo?', 'Apri SKILL.md con TextEdit, cambia la riga “Usalo quando” o le istruzioni, salva, riprova in una chat nuova.'],
            ['Non la ritrovo più', 'Probabilmente l’hai creata dentro la cartella del coach. Chiedi alla tua buddy: la ricreate nella cartella giusta in dieci minuti.']]],
        ['h1', 'Cosa porti alla lezione 8'],
        ['b', 'La skill corretta e le righe d’uso.'],
        ['b', 'Le tue fonti annotate.'],
        ['h1', 'Se hai saltato la lezione'],
        ['p', 'Le decisioni prese: la differenza tra skill, plugin e connettore, come è fatto il coach dentro, la regola della riga “Usalo quando”. Il passo minimo (25 minuti, prima della lezione 8): con la tua buddy, crea una skill da un template che mandi spesso, seguendo i cinque passi della slide 7, e ritrovala dopo aver riaperto Cowork. Le fonti da annotare te le dice il tuo gruppo.']]}
