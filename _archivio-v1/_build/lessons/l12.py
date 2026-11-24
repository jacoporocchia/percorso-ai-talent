cover('Lezione 12 · Uso, demo, rimisura', 'Lunedì 8 marzo 2027')

agenda('Oggi gli agenti si mostrano al responsabile, e il percorso passa nelle vostre mani', [
    ('0-25’', 'Registro', 'Una settimana d’uso, letta'),
    ('25-60’', 'Demo', 'Due agenti al responsabile'),
    ('60-85’', 'Retro', 'Cosa teniamo, cosa cambiamo'),
    ('85-100’', 'Rimisura', 'Il 19 aprile, preparata oggi'),
    ('100-120’', 'Docenti', 'Ognuna porta un pezzo al suo team')],
    'due agenti in uso con una owner, la data della rimisura, e il tuo piano per insegnare al tuo team.',
    notes='Ultima lezione. Il responsabile arriva per il blocco demo: avvisalo per le 25’ dall’inizio.')

cards3('Il registro dice se l’agente regge: si legge per esiti, non per impressioni', [
    ('Quanti ok', 'La quota sugli usi della settimana. È il secondo dato dopo la batteria.'),
    ('I fix', 'Cosa si correggeva a mano ogni volta? Se torna due volte, diventa una regola.'),
    ('I fail', 'Il più istruttivo, raccontato in due minuti. Cosa cambia nel core o nelle skill?')],
    R('Le correzioni di oggi ', 'diventano la versione 1.1, con una riga nel CHANGELOG.'),
    notes='Ogni gruppo legge il suo registro all’altro. Il fail più istruttivo lo racconta chi l’ha registrato.')

steps('Demo al responsabile: dieci minuti per agente, con i numeri', [
    ('Il problema', 'Il processo, il tempo che prendeva. Dalla scheda.'),
    ('Il perché', 'Perché un agente e non un gradino più basso.'),
    ('L’agente al lavoro', 'Un caso reale, dal vivo.'),
    ('I numeri', 'Batteria, registro, ore stimate liberate.'),
    ('Cosa non fa', 'Il “cosa non fa mai” e chi lo mantiene.')],
    [R('Parla la owner. ', 'Le altre del gruppo rispondono alle domande.'), R('Si chiede al responsabile una cosa: ', 'cosa gli servirebbe per continuare a sostenerlo.')],
    notes='Il quarto passo è quello che il responsabile ricorderà. I numeri vanno detti come sono, anche se piccoli: è la credibilità del percorso.')

cards3('Retrospettiva: cosa teniamo, cosa cambiamo, cosa lasciamo', [
    ('Teniamo', 'Cosa ha funzionato e va rifatto uguale quando il percorso passa a un altro team.'),
    ('Cambiamo', 'Cosa ha funzionato a metà: tempi, consegne, strumenti, ordine delle lezioni.'),
    ('Lasciamo', 'Cosa non è servito. Va detto, così chi rifà il percorso non lo ripete.')],
    R('Prima Direttiva: ', 'ognuna ha fatto il meglio possibile con quello che sapeva e il tempo che aveva.'),
    notes='Facilita in modo classico: scrittura individuale, poi raggruppamento, poi due azioni. Le risposte diventano la versione 2 del percorso nel basket.')

s = chain('Il 19 aprile si rimisura: è l’unico momento in cui le ore liberate diventano un dato', [
    ('8 marzo', 'oggi: si fissa la data'), ('15/3-9/4', 'calendario, 4 settimane'), ('12-16 aprile', 'diario, 5 giorni'), ('19 aprile', 'incontro di un’ora')],
    notes='Fase 6 del time audit (t01): campionamento più breve per vedere se le decisioni hanno spostato i numeri. Senza questa fase l’audit resta una fotografia.')
for i, (h, d) in enumerate([('Cosa si confronta', 'Il time audit di dicembre con il campionamento di aprile: quota sui goal, quota “solo io”, blocchi da 90 minuti.'),
                            ('Cosa si verifica', 'Le ore liberate stimate nelle schede: sono successe davvero? Dove sono finite?')]):
    x = 0.3 + i * 6.45
    box(s, x, 2.9, 6.25, 2.15, BG2)
    text(s, x + 0.35, 3.05, 5.6, 0.45, h, size=19, bold=True, color=BLU)
    text(s, x + 0.35, 3.55, 5.6, 1.4, d, size=16)
band(s, 5.3, 1.25, [R('Gli stessi prompt di dicembre, ', 'lo stesso file del diario.'), R('Il confronto resta tuo: ', 'all’incontro si porta solo ciò che scegli.')], size=16)

cards4('Da allieva a docente: ognuna porta un pezzo del percorso al suo team', [
    ('Cosa', 'Una o due lezioni del basket, quelle che hai vissuto meglio.'),
    ('A chi', 'Il tuo team, o un gruppo di colleghe che fanno un lavoro simile al tuo.'),
    ('Con cosa', 'Deck, scaletta, scheda, registrazioni: tutto è nel basket, pronto.'),
    ('Quando', 'Una data entro due mesi. Senza una data resta un’intenzione.')],
    R('Tutto quello che avete prodotto ', 'è già materiale: registrazioni, LEGGIMI, scarti, contratti diventano la KB del team e degli agenti.'),
    notes='È la parte della visione di Max: il percorso diventa un basket di formazione riproducibile. Ognuna esce con un piano di una pagina, non con una promessa.')

cards2('Dopo oggi: l’agente in uso, la rimisura, il tuo piano da docente', [
    (1, 'L’agente nel lavoro ordinario', 'Da subito', 'Si usa e si registra. La owner raccoglie i fix e fa uscire la v1.1 entro fine marzo.'),
    (2, 'Il piano da docente', 'Entro lunedì 22 marzo', 'Una pagina: cosa porti, a chi, con quali materiali del basket, in che data. Mandalo a Max.')],
    [R('Rimisura: ', 'calendario 15 marzo-9 aprile, diario 12-16 aprile, incontro lunedì 19 aprile.'), R('Il coach resta tuo: ', 'la cartella è sul tuo Mac e continua a funzionare.')],
    notes='Il coach continua dopo il percorso: ricorda che /coach checkin e /coach sessione restano disponibili.')

VIDEOS = [
    ('Pillola Agile: la Prima Direttiva', 'Il principio con cui si apre ogni retrospettiva.', 'https://www.youtube.com/watch?v=45w_LYaF4iQ', 'italiano'),
    ('Retrospettiva di progetto', 'Un framework semplice per guardare indietro e decidere.', 'https://www.youtube.com/watch?v=g7zX4tusPSs', 'italiano'),
    ('La retrospettiva in Scrum', 'Come la fanno i team agili, per rifarla con il tuo team.', 'https://www.youtube.com/watch?v=PNMiEpPWD80', 'italiano'),
    ('Nessuno sa davvero come funziona l’AI', 'Enkk, in una conversazione lunga: per chiudere con una domanda aperta.', 'https://www.youtube.com/watch?v=F45dThGJgyg', 'italiano')]
EXTRA = None
links('Per approfondire: guardare indietro bene, e continuare', VIDEOS, tip='scegline uno e guardalo mentre prepari la tua prima lezione al team.')

closing('Cosa porti al tuo team?', 'Rimisura: lunedì 19 aprile 2027')

SCALETTA = {
    'title': 'Lezione 12 · Uso, demo, rimisura',
    'subtitle': 'Scaletta del facilitatore · lunedì 8 marzo 2027 · 2 ore · 5 colleghe e il responsabile (25’-60’)',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'I gruppi leggono il registro di una settimana d’uso e decidono le correzioni, presentano i due agenti al responsabile con i numeri, fanno la retrospettiva del percorso, preparano la rimisura del 19 aprile ed escono con un piano di una pagina per insegnare un pezzo del percorso al proprio team.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Un agente ha una owner e un registro; un percorso ha una rimisura; quello che si è imparato si insegna.'],
            ['Output in aula', 'Correzioni per la v1.1 dei due agenti. Demo fatta. Retrospettiva con due azioni. Date della rimisura fissate.'],
            ['Output dopo', 'Agenti in uso con registro. Piano da docente entro il 22/3. Calendario e diario per la rimisura. Incontro il 19/4.'],
            ['Segnale che ha funzionato', 'Il responsabile chiede come continuare, e ognuna ha una data per la sua prima lezione al team.']]],
        ['h1', 'Prima dell’8 marzo'],
        ['b', 'Conferma il responsabile per le 25’-60’ e mandagli due righe sui due processi scelti.'],
        ['b', 'Leggi i due registri d’uso: prepara la quota di ok per agente.'],
        ['b', 'Ricostruisci le ore stimate liberate dalle schede dei due processi: servono nella demo.'],
        ['b', 'Prepara la lavagna per la retrospettiva e un modello di una pagina per il piano da docente.'],
        ['b', 'Fissa in calendario l’incontro di rimisura del 19 aprile, un’ora.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-25’', 'Registro', 'Slide 3. Ogni gruppo legge il registro all’altro: quota di ok, i fix ricorrenti, il fail più istruttivo. Le correzioni diventano la v1.1.'],
            ['25-60’', 'Demo al responsabile', 'Slide 4. Dieci minuti per agente nei cinque passi, poi domande. Ultima domanda: cosa ti servirebbe per sostenerlo.'],
            ['60-85’', 'Retrospettiva', 'Slide 5. Scrittura individuale, raggruppamento, due azioni. Registrata: diventa la versione 2 del percorso.'],
            ['85-100’', 'Rimisura', 'Slide 6. Date, metodo, cosa si confronta. Ognuna mette in calendario diario e incontro.'],
            ['100-115’', 'Da allieva a docente', 'Slide 7. Ognuna abbozza il piano: cosa, a chi, con cosa, quando.'],
            ['115-120’', 'Chiusura', 'Slide 8, 9 e 10. Giro finale: “Cosa porti al tuo team?”.']]],
        ['h1', 'Il modello del piano da docente'],
        ['table', [2600, 7038], [
            ['Cosa porto', 'Lezione o lezioni del basket, e perché proprio quelle.'],
            ['A chi', 'Team o gruppo, quante persone, che lavoro fanno.'],
            ['Con cosa', 'Deck, scaletta, scheda, registrazione, esempi del nostro percorso.'],
            ['Quando', 'Data e durata.'],
            ['Come capisco se è servito', 'Un comportamento da osservare dopo, come negli obiettivi di ogni lezione.']]],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['Un agente ha molti fail nel registro', 'Si dice nella demo, con le correzioni previste. Un agente che migliora per versioni è più credibile di uno perfetto.'],
            ['Il responsabile chiede di estendere subito gli agenti', 'Prima la v1.1 e un mese di registro. Le estensioni passano dalla stessa scheda e dagli stessi controlli.'],
            ['Una collega non si sente pronta a insegnare', 'Il piano può essere piccolo: una lezione, a due colleghe, in coppia con un’altra del gruppo.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'La retrospettiva, la registrazione della demo (se il responsabile è d’accordo), i due agenti come plugin con contratto, casi di prova e CHANGELOG, i piani da docente. Con le lezioni 1-11, il basket è completo: un percorso riproducibile e una KB per il team e per gli agenti.']]}

CONSEGNA = {
    'title': 'Lezione 12 · Dopo il percorso',
    'subtitle': 'Percorso AI per Talent · le prossime sei settimane',
    'blocks': [
        ['h1', '1. L’agente nel lavoro ordinario'],
        ['p', 'Si usa e si registra, come nella settimana di prova. La owner raccoglie i fix ricorrenti e fa uscire la versione 1.1 entro fine marzo, con una riga nel CHANGELOG. Il core si cambia solo quando una correzione torna due volte.'],
        ['h1', '2. Il piano da docente (entro lunedì 22 marzo)'],
        ['p', 'Una pagina, da mandare a Max:'],
        ['table', [2600, 7038], [
            ['Cosa porto', ' '],
            ['A chi', ' '],
            ['Con cosa (dal basket)', ' '],
            ['Quando', ' '],
            ['Come capisco se è servito', ' ']]],
        ['h1', '3. La rimisura'],
        ['b', 'Calendario dal 15 marzo al 9 aprile: stessi due prompt di dicembre, con il connettore.'],
        ['b', 'Diario dal 12 al 16 aprile: stesso file Excel, nuove date.'],
        ['b', 'Incontro lunedì 19 aprile, un’ora. Porti il confronto con il tuo audit di dicembre, solo per la parte che scegli.'],
        ['h1', 'Il coach resta tuo'],
        ['p', 'La cartella è sul tuo Mac e continua a funzionare: /coach checkin per fare il punto, /coach sessione quando hai un tema.']]}
