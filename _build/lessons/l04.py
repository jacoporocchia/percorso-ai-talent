cover('Lezione 4 · Dal processo alla scheda', 'Lunedì 11 gennaio 2027')

agenda('Oggi una candidata diventa una scheda, e il gruppo sceglie i due processi per gli agenti', [
    ('0-20’', 'Regola zero', 'Le tre candidate: va fatto? si semplifica?'),
    ('20-35’', 'Pillola', 'La scala delle opzioni, in otto gradini'),
    ('35-60’', 'Mappa', 'Il processo più promettente, con il coach'),
    ('60-85’', 'Scheda', 'Criteri, pareggio, rischi'),
    ('85-120’', 'Plenaria', 'Portfolio, due processi, due gruppi')],
    'una scheda di automazione con il gradino scelto, e il tuo gruppo per costruire l’agente.',
    notes='Lezione densa: è il punto di arrivo del blocco A. La regola zero, che nella v1 era la consegna delle feste, si fa qui nei primi 20 minuti. La consegna (5 minuti) si legge dentro la plenaria finale.')

cards3('Venti minuti di regola zero: dove finisce ognuna delle tre candidate?', [
    ('Smessa', 'Hai scoperto che non serviva, o serviva molto meno. È il risultato migliore: zero manutenzione.'),
    ('Semplificata', 'Meno passaggi, un formato unico. Spesso è la precondizione di ogni automazione.'),
    ('Ancora candidata', 'Serve, è già semplice, pesa. Oggi la portiamo fino alla scheda.')],
    R('Con /coach automazione, per ogni candidata: ', 'cosa succede se smetto? Si può eliminare, combinare, riordinare, semplificare? Poi il giro: quante in ogni colonna.'),
    notes='Quindici minuti di lavoro individuale con il coach, cinque di giro. Conta in plenaria le candidate per colonna, le smesse si applaudono. Se nessuna è stata smessa o semplificata, rifai la domanda “cosa succede se smetti?” su una a caso. La domanda “a chi riceve il risultato” è facoltativa: per qualcuna è un’esposizione.')

# Scala delle opzioni
s = free('Si sale dal basso e ci si ferma al primo gradino che risolve il problema',
         notes='Gradini 1-4: nessun sistema da mantenere. Gradini 5-7: un sistema che qualcuno deve mantenere. Gradino 8: la scelta deliberata di fare a mano. Il KPI del percorso guarda anche quante schede si fermano ai gradini 1-4.')
lad = [('1', 'Eliminare', 'Non serve, o molto meno'), ('2', 'Semplificare', 'Meno passaggi, un formato'), ('3', 'Delegare', 'Con istruzioni e criteri'),
       ('4', 'Template', 'Checklist, testi pronti'), ('5', 'A regole', 'Formule, Power Automate'), ('6', 'Con un LLM', 'Un passaggio interpreta'),
       ('7', 'Agente', 'Il modello sceglie i passaggi'), ('8', 'A mano', 'Apposta, se il giudizio è il valore')]
for i, (nn, h, d) in enumerate(lad):
    x = 0.3 + i * 1.59
    hgt = 0.9 + i * 0.36
    y = 5.0 - hgt
    col = CEL if i < 4 else (FUX if i < 7 else BLU)
    box(s, x, y, 1.5, hgt, col, adj=0.04)
    text(s, x, y + 0.08, 1.5, 0.45, nn, size=20, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER)
    text(s, x + 0.08, 5.1, 1.42, 0.4, h, size=14, bold=True, color=BLU)
    text(s, x + 0.08, 5.45, 1.42, 0.75, d, size=12)
box(s, 0.3, 6.25, 6.3, 0.4, CEL, adj=0.5)
text(s, 0.3, 6.25, 6.3, 0.4, 'Nessun sistema da mantenere', size=13, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
box(s, 6.66, 6.25, 4.7, 0.4, FUX, adj=0.5)
text(s, 6.66, 6.25, 4.7, 0.4, 'Qualcuno lo deve mantenere', size=13, bold=True, color='FFFFFF', align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

compare('Un prompt-agente di due pagine non è un agente: è il gradino 7 saltando i primi sei', (
    'Il prompt-agente “da reel”', FUX, ['Due pagine di istruzioni scritte di getto, spiegazioni comprese.', 'Provato su un caso che funziona, mai su quello che deve fallire.', 'Nessuno sa cosa fa quando il processo cambia.', 'Spesso con dati veri incollati dentro, per vedere se va.']), (
    'La scheda di oggi', BLU2, ['Prima la domanda: va fatto? quale gradino basta?', 'Valore, fattibilità, rischio, chi lo mantiene.', 'Se arriva al 7, l’agente si costruisce dalla lezione 8 con un metodo e dei casi di prova.', 'Dati personali: fuori, per regola.']),
    R('Se ne hai già costruito uno, ', 'portalo: è la miglior materia prima per una scheda. Spesso scopri che bastava un template.'),
    notes='Almeno una collega avrà già costruito un prompt-agente lungo, magari in un account personale durante le feste. Non giudicare: usalo come esempio della scala. Se ci sono dati veri dentro, la regola dati della lezione 1, in privato.')

steps('Mappare prima di automatizzare: il coach fa emergere il processo con le domande', [
    ('Il risultato', 'Cosa produce, per chi. Cosa vuoi poter decidere alla fine?'),
    ('I confini', 'Dove inizia, dove finisce.'),
    ('I passaggi', '5-15, verbo più oggetto, da un caso recente.'),
    ('Persone e tempi', 'Chi fa cosa, quanto lavoro, quanta attesa.'),
    ('La lettura', 'Sprechi, vincolo, il tuo ruolo.')],
    [R('Comando: ', '/coach processo, sulla candidata più promettente.'), R('Prima il percorso normale, ', 'poi le eccezioni. Il coach salva la scheda in artefatti/processi.')],
    notes='Il processo reale emerge da un caso concreto e recente, non dalla procedura scritta. Suggerisci: “pensa all’ultima volta che l’hai fatto”.')

cards4('La scheda mette in fila valore, fattibilità, rischio e chi la mantiene', [
    ('Valore', 'Quante volte, quanto tempo, e cosa faresti con il tempo liberato.'),
    ('Fattibilità', 'Regole scrivibili? Input strutturati? Processo stabile? Poche eccezioni?'),
    ('Rischio', 'Quanto costa un errore, quando te ne accorgi, se tocca dati personali.'),
    ('Chi mantiene', 'Quando qualcosa cambia, chi lo aggiusta? Se sei tu, è un nuovo carico.')],
    R('Comando: ', '/coach automazione, poi “facciamo la scheda”. Il coach la salva in artefatti/automazioni.'),
    notes='Sono i dodici criteri di a02 raggruppati in quattro. Il quarto è quello che le colleghe salteranno: insisti.')

s = chain('Il conto del pareggio dice quanto tempo puoi investire senza andare in perdita', [
    ('5 anni', 'orizzonte'), ('× volte l’anno', 'quante occorrenze'), ('× minuti', 'risparmiati ogni volta'), ('= ore', 'investibili senza perdere')],
    notes='È un ordine di grandezza, non un business case. Correzioni: togli la manutenzione; accorcia l’orizzonte se il processo cambierà; moltiplica se serve anche ad altre.')
for i, (h, calc, res) in enumerate([('Settimanale, 10 minuti risparmiati', '5 × 52 × 10 minuti', 'circa 43 ore'), ('Mensile, 30 minuti risparmiati', '5 × 12 × 30 minuti', '30 ore')]):
    x = 0.3 + i * 6.45
    box(s, x, 2.9, 6.25, 2.1, BG2)
    text(s, x + 0.35, 3.05, 5.6, 0.45, h, size=18, bold=True, color=BLU)
    text(s, x + 0.35, 3.6, 5.6, 0.45, calc, size=17, color=GREY)
    text(s, x + 0.35, 4.1, 5.6, 0.7, res, size=30, bold=True, color=FUX)
band(s, 5.3, 1.25, [R('Se costruirlo richiede più di così, ', 'resta ai gradini bassi.'), R('Il valore non è solo tempo: ', 'meno errori e meno carico mentale contano, ma vanno scritti.')], size=16)

cards4('Quando tocca persone, l’AI ordina le informazioni e decide un umano', [
    ('Dati personali', 'GDPR: solo i dati che servono, per uno scopo dichiarato.'),
    ('Controllo a distanza', 'Analizzare mail o calendari di altri ricade nell’art. 4 dello Statuto.'),
    ('Decisioni su persone', 'Per l’AI Act selezione e valutazione sono ad alto rischio.'),
    ('Fondi', 'L’errore emerge mesi dopo, in un controllo. Validazioni e approvazione.')],
    R('Gli agenti del percorso non decidono niente su persone. ', 'Per chi fa recruiting: checklist di screening scritta da te, JD, annunci, materiali career day, scorecard vuote. L’AI prepara, decide un umano.'),
    notes='È a04. Tono: non allarmare, rendere esplicito. Per la Talent Acquisition dai un’alternativa concreta, non solo un divieto: lo screening resta al gradino “Template”, con una checklist scritta dalla recruiter e senza dati di candidati in Claude.')

rows('In plenaria si scelgono due processi per gli agenti: i più condivisi, non i più brillanti', [
    ('Condiviso', 'Lo fanno almeno due colleghe, o lo riceve tutto il team.'),
    ('Gradino 6-7', 'La scheda dice che un passaggio LLM o un agente ha senso.'),
    ('Documenti esistenti', 'Ci sono procedure, template, esempi riusciti da cui partire.'),
    ('Rischio gestibile', 'Un umano approva prima dell’azione finale.')],
    side=('Poi i gruppi', ['Due gruppi, da due e da tre persone. Ognuno costruisce un agente su un processo.', 'Con quattro regole, nella slide dopo.']),
    notes='Metti le schede in fila, anche solo come titoli e gradino scelto. Se nessuna scheda arriva a 6-7, va benissimo: si sceglie il processo con più valore e si costruisce un agente che prepara e propone.')

cards4('Quattro regole per i gruppi, perché reggano fino a marzo', [
    ('Owner per tempo', 'La owner è chi ha tempo per mantenere l’agente, non chi fa il processo. Accanto, una co-owner.'),
    ('La titolare esperta', 'Chi fa il processo ogni giorno è l’esperta: dice cosa è giusto, non mantiene i file.'),
    ('Il gruppo da due', 'Prende il processo più stabile e le agende più prevedibili: un’assenza lo dimezza.'),
    ('Una skill a testa', 'Ognuna è titolare di almeno una skill dell’agente. Nessuna resta a guardare.')],
    R('Il lavoro di gruppo sta in aula: ', '30 minuti nelle lezioni 9, 10 e 11. Fuori dall’aula ognuna fa la sua parte, nel suo slot.'),
    notes='È a02 n.12, chi mantiene, applicato alle persone. Nella simulazione, con “chi fa quel processo entra in quel gruppo”, la owner finiva sempre per essere la più carica. Usa le settimane di picco raccolte nell’intake per decidere owner e gruppo da due.')

cards2('Per lunedì 18: una scheda completa e l’elenco delle fonti', [
    (1, 'Una scheda', '30 minuti', 'Completa la scheda iniziata oggi, con il gradino scelto. Anche “eliminare” è una scheda. La seconda è facoltativa.'),
    (2, 'L’elenco delle fonti', '15 minuti, la tua parte', 'Per il processo del tuo gruppo: dove stanno procedure, template, esempi riusciti. Posizione e link, senza copiarli.')],
    [R('Niente copie, niente allegati: ', 'lunedì 18 le fonti entrano nella cartella dell’agente, dalla posizione che hai scritto.'), R('Settimana piena? ', 'Versione minima da 15: solo l’elenco delle fonti.')],
    notes='Nella v1 le fonti si raccoglievano in una cartella temporanea e finivano in zip via mail, una settimana prima della lezione sulla copia. Qui si fa un elenco con i link. Dati personali di candidati e dipendenti: fuori dall’elenco.')

VIDEOS = [
    ('Come funzionano gli agenti AI?', 'Enkk spiega cosa distingue un agente da una singola risposta.', 'https://www.youtube.com/watch?v=AYeCGb2ZaSU', 'italiano'),
    ('Che cos’è l’AI Act e cosa prevede?', 'Il regolamento europeo in breve.', 'https://www.youtube.com/watch?v=YHeFsCjCevs', 'italiano'),
    ('AI Act nel recruiting', 'Perché la selezione è un caso ad alto rischio.', 'https://www.youtube.com/watch?v=Il-aSdEfqow', 'italiano'),
    ('Tips for building AI agents', 'Anthropic: quando un agente serve e quando basta molto meno.', 'https://www.youtube.com/watch?v=LP5OCa20Zpg', 'inglese, sottotitoli')]
EXTRA = None
links('Per approfondire: agenti, e le regole quando toccano persone', VIDEOS)

closing('Quale gradino hai scelto, e perché non uno più in alto?', 'Prossima lezione: lunedì 18 gennaio')

SCALETTA = {
    'title': 'Lezione 4 · Dal processo alla scheda',
    'subtitle': 'Scaletta del facilitatore · lunedì 11 gennaio 2027 · 2 ore · 5 colleghe',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'Le colleghe fanno la regola zero sulle tre candidate, mappano con il coach il processo più promettente, ne fanno una scheda di automazione con criteri, pareggio e rischi, e in plenaria scelgono i due processi su cui costruire gli agenti, con gruppi che reggono. Chiude il blocco A: da qui in poi il percorso lavora su ciò che le schede hanno deciso.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Scegliere il gradino più basso che risolve il problema, e chiedersi chi manterrà la soluzione prima di costruirla.'],
            ['Output in aula', 'Una scheda processo (m07) e una scheda di automazione (a02) per collega. Due processi scelti e due gruppi formati.'],
            ['Output per il 18/1', 'Una scheda completa per collega (la seconda facoltativa). Elenco delle fonti per ciascun gruppo, con posizione e link, senza copie e senza dati personali.'],
            ['Segnale che ha funzionato', 'Almeno una candidata per collega esce dalla regola zero come smessa o semplificata. I gruppi scelgono il processo per condivisione, non per fascino, e la owner è scelta per tempo disponibile.']]],
        ['h1', 'Prima dell’11 gennaio'],
        ['b', 'Una tua scheda già fatta, da mostrare come esempio di lettura (anche “eliminare” va bene).'],
        ['b', 'Una regola da dire prima della plenaria: i processi che toccano dati di candidati o valutazioni di persone restano fuori dalla scelta degli agenti. È il modo più semplice per non aprire adesso un tema privacy che il percorso non deve affrontare.'],
        ['b', 'Una lavagna o un foglio condiviso per il portfolio delle schede in plenaria.'],
        ['b', [{'text': 'Una proposta di gruppi in tasca. ', 'bold': True}, 'Guarda le settimane di picco raccolte nell’intake: chi ha febbraio pieno (review, career day) non fa la owner, il gruppo da due prende le agende più prevedibili.']],
        ['b', 'Un esempio di “prompt-agente” lungo da mostrare nella slide 5: va bene uno tuo dei primi tempi.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-20’', 'Regola zero', 'Slide 3. Quindici minuti con /coach automazione sulle tre candidate: cosa succede se smetto, si può semplificare. Poi il giro: smesse, semplificate, ancora candidate. Le smesse si celebrano: è il gradino 1.'],
            ['20-35’', 'Pillola', 'Slide 4 e 5. La scala delle otto opzioni: si sale dal basso, ci si ferma al primo gradino che risolve. Gradini 1-4 senza sistema da mantenere, 5-7 con. Il gradino 8 è una scelta, non una sconfitta. Poi il confronto tra un prompt-agente lungo e la scheda.'],
            ['35-60’', 'Mappa del processo', 'Slide 6. /coach processo sulla candidata più promettente. Prima il caso recente, poi le eccezioni. Il coach salva la scheda in artefatti/processi.'],
            ['60-85’', 'Scheda di automazione', 'Slide 7, 8 e 9. /coach automazione, “facciamo la scheda”. Criteri raggruppati in valore, fattibilità, rischio, chi mantiene. Conto del pareggio. Se tocca persone, a04, con l’alternativa per chi fa recruiting.'],
            ['85-115’', 'Plenaria', 'Slide 10 e 11. Portfolio: ognuna dice titolo della scheda e gradino scelto. Si scelgono due processi con i quattro criteri. Si formano i gruppi con le quattro regole: owner e co-owner per tempo disponibile, titolare del processo come esperta, processo più stabile al gruppo da due, una skill a testa.'],
            ['115-120’', 'Consegna', 'Slide 12, 13 e 14.']]],
        ['h1', 'La matrice per scegliere il tipo di soluzione (a03)'],
        ['table', [2800, 3419, 3419], [
            ['', 'Errore poco costoso', 'Errore costoso'],
            ['Regole, bassa variabilità', 'Flusso a regole, controllo a campione', 'Flusso a regole con validazioni e approvazione umana prima dell’azione finale'],
            ['Giudizio, alta variabilità', 'Passaggio LLM o agente, revisione a campione', 'AI come assistente: prepara e propone, decide un umano. Oppure a mano']]],
        ['p', 'Automatizzare raccolta e analisi è quasi sempre più sicuro che automatizzare decisione e azione. Per Talent questo vuol dire: l’agente prepara, ordina, propone; la collega decide e preme il pulsante.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['Tutte le schede puntano all’agente', 'Chiedi per ognuna: qual è la versione più semplice che risolve l’80% del problema? Spesso è un template.'],
            ['Il processo scelto per l’agente tocca dati di candidati', 'L’agente può lavorare su documenti anonimi o su template. Se non è possibile, quel processo esce dalla scelta.'],
            ['I gruppi non si formano da soli', 'Proponi tu, con la proposta preparata: chi fa quel processo entra in quel gruppo come esperta, la owner è chi ha tempo.'],
            ['Nessuna vuole fare la owner', 'Nomina owner e co-owner provvisorie per tempo disponibile e ridiscutile alla lezione 8. Non fare tu la owner: è il collo di bottiglia che il percorso vuole evitare.'],
            ['Una collega resta senza il proprio processo', 'Sarà titolare di una skill dell’agente dell’altro gruppo o del suo. Se la sua scheda più pesante resta fuori (per esempio perché tocca dati personali), proponi il binario “metodo, non dati”: una skill che scrive formule o passi di Power Query.'],
            ['Una collega non ha candidate sopravvissute', 'Fa la scheda di una candidata smessa: il gradino 1 è un risultato e va documentato.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'La registrazione della pillola e della plenaria, il deck, la scheda della consegna, la matrice di a03, le schede che le colleghe scelgono di condividere come esempi.']]}

CONSEGNA = {
    'title': 'Lezione 4 · Il lavoro per lunedì 18 gennaio',
    'subtitle': 'Percorso AI per Talent · 45 minuti nel tuo slot · versione minima: 15 minuti',
    'blocks': [
        ['p', [{'text': 'Settimana piena? Fai la versione minima: ', 'bold': True}, 'solo il punto 2, la tua parte dell’elenco delle fonti (15’). La scheda la completi la settimana dopo.']],
        ['h1', '1. Una scheda completa (30’)'],
        ['p', 'Nella tua cartella del coach, /coach automazione. Porta a termine la scheda iniziata in aula, con il gradino scelto. Anche una scheda che si ferma a “eliminare” o “template” è una scheda completa. La seconda è facoltativa.'],
        ['b', 'Valore: volte al mese, minuti per volta, cosa faresti con il tempo liberato.'],
        ['b', 'Fattibilità: regole scrivibili, input strutturati, processo stabile, poche eccezioni.'],
        ['b', 'Rischio: costo dell’errore, quando te ne accorgi, dati personali sì o no.'],
        ['b', 'Chi mantiene: se la risposta sei tu, scrivilo.'],
        ['h1', '2. L’elenco delle fonti per l’agente del tuo gruppo (15’, la tua parte)'],
        ['p', 'Elencate i documenti che esistono già per il processo scelto: procedure, template, esempi riusciti, mail tipo. Nessuna ricerca nuova, e nessuna copia: lunedì 18 li portiamo nella cartella dell’agente partendo da dove stanno.'],
        ['table', [2600, 3000, 4038], [
            ['Documento', 'Dove sta (posizione o link)', 'Cos’è e perché potrebbe servire'],
            [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]],
        ['b', 'Non scaricare, non allegare, non mandare zip per mail: scrivi dove sta.'],
        ['b', 'Niente dati personali di candidati o dipendenti. Se un esempio li contiene, segnalo con “da pulire”: lo sistemiamo in aula.'],
        ['h1', 'Cosa porti alla lezione 5'],
        ['b', 'La scheda, salvata dal coach in artefatti/automazioni.'],
        ['b', 'L’elenco delle fonti del tuo gruppo, con le posizioni.'],
        ['h1', 'Se hai saltato la lezione'],
        ['p', 'Le decisioni prese: i due processi per gli agenti, i due gruppi con owner e co-owner, le quattro regole dei gruppi. Il passo minimo (20 minuti): chiedi alla tua buddy in quale gruppo sei e qual è la tua skill, fai la regola zero sulle tue candidate con /coach automazione, e scrivi la tua parte dell’elenco fonti. La scheda la completi nel tuo slot. Nessun ruolo ti viene assegnato senza che tu lo confermi.']]}
