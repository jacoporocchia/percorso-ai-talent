cover('Lezione 10 · Agente, fase 5: scrittura e casi di prova', 'Lunedì 22 febbraio 2027')

agenda('Oggi ogni gruppo legge l’agente dell’altro e scrive le prove prima di guardare le risposte', [
    ('0-10’', 'Ripartenza', 'Le skill dopo due prove'),
    ('10-20’', 'Pillola', 'Istruzione, non spiegazione'),
    ('20-50’', 'Revisione', 'Ogni gruppo legge l’agente dell’altro'),
    ('50-80’', 'In gruppo', 'Da 6 a 8 casi di prova'),
    ('80-105’', 'Prova', 'Seconda prova esplorativa'),
    ('105-120’', 'Consegna', 'Correzioni e risposte attese')],
    'un agente corretto da occhi esterni e una batteria di prova scritta prima di provarla.',
    notes='Fase 5 del processo standard. La revisione incrociata è la versione ridotta del “controllo dei rimandi” fatto sul coach. Serve anche a far crescere chi corregge al posto tuo: dopo il percorso, i due gruppi si rivedono a vicenda senza passare da te.')

cards3('Le skill dopo due prove: cosa è cambiato?', [
    ('Scattava male', 'Riga “Usalo quando” riscritta. Quante volte?'),
    ('Chiedeva troppo o troppo poco', 'La sezione “chiedi” era incompleta, o chiedeva cose che aveva già.'),
    ('Due skill si pestavano i piedi', 'Le righe si somigliavano. Chi ha risolto, e come?')],
    R('Un minuto a testa, ', 'dal diario: le righe di prova sono già scritte.'),
    notes='Se una collega non ha provato la skill, la prova adesso a schermo, davanti a tutte: dura due minuti e vale come esempio per la seconda prova esplorativa.')

compare('Istruzioni, non spiegazioni: la stessa regola, scritta due volte', (
    'Spiegazione', FUX, ['“È importante che le comunicazioni ai candidati siano complete e professionali, perché rappresentano l’azienda.”']), (
    'Istruzione', BLU, ['“Prima di scrivere al candidato, verifica di avere ruolo, data, ora, sede o link e nome di chi conduce il colloquio. Se manca uno, chiedilo. Tono cordiale, massimo dieci righe.”']),
    [R('Il test: ', 'se la regola non dice cosa fare in un caso concreto, il modello la interpreta. E ognuno la interpreta a modo suo.')],
    notes='Esempio inventato su una convocazione a colloquio; adattalo a uno dei due processi scelti. Lo stesso vale per la formazione: “verifica corso, date, aula e materiali prima di scrivere al docente”.', size=20)

cards4('Revisione incrociata: ogni gruppo legge l’agente dell’altro con quattro domande', [
    ('Istruzione o spiegazione?', '“Scrivi”, “chiedi”, “fermati” sono istruzioni. “È importante che…” è una spiegazione.'),
    ('Si applica a un caso?', 'Prendete un caso reale: la regola dice cosa fare, sì o no?'),
    ('Si contraddice?', 'Due regole, o una regola e una skill, che in un caso dicono cose diverse.'),
    ('Manca un “mai”?', 'C’è un errore grave che l’agente non si vieta?')],
    R('Si scrivono i commenti, non le correzioni: ', 'il gruppo autore decide cosa cambiare. 15 minuti per leggere, 15 per discutere.'),
    notes='I commenti vanno in revisione.md (dal modello) nella cartella dell’altro gruppo. Ognuna legge core e una skill: nessuna legge solo, nessuna legge tutto.')

cards2('30 minuti di gruppo: da 6 a 8 casi di prova, di cui due in cui l’agente deve fermarsi', [
    (1, 'Casi normali', '4-6 casi', 'Un input realistico, preso da un caso vero con i nomi inventati, e la risposta che vi aspettate.'),
    (2, 'Casi di stop', '2 casi', 'Un input in cui l’agente deve rifiutare o fermarsi: manca un dato, tocca una persona, gli chiedono di inviare.')],
    [R('La risposta attesa si scrive prima di provare. ', 'Vietato copiarla da un output già generato:'), R('', 'una prova scritta guardando la risposta non misura niente.')],
    notes='Ogni collega scrive almeno un caso, possibilmente uno che tocca la sua skill. Si usa casi-prova.md dal modello. In aula bastano input e tipo; le risposte attese si completano a casa, ma prima della seconda prova ne serve almeno una per caso di stop.')

prompt_slide('Seconda prova esplorativa: core e skill insieme, su due casi della batteria', 'In Cowork, nella cartella dell’agente',
             'Leggi core.md e comportati come descritto lì. Le skill sono nella cartella skill, le fonti in fonti.\n\n<il caso 1 di casi-prova.md>\n\nAlla fine dimmi quali regole e quale skill hai usato.',
             'Poi un caso di stop', 'Si ferma? Spiega cosa può fare invece? Se inventa il dato mancante, la regola nel core non basta.',
             'Cosa annotare nel diario', [
                 ('Cosa è migliorato', 'rispetto alla prova della lezione 8.'),
                 ('Dove sbaglia ancora', 'e se è il core o una skill.'),
                 ('Chi corregge', 'il nome accanto a ogni errore.')],
             foot='Ancora esplorazione: si guarda, si annota, non si conta. La batteria completa si esegue alla lezione 11.',
             notes='Se la risposta dell’agente è migliore della risposta attesa scritta dal gruppo, non si riscrive la risposta attesa adesso: si discute alla lezione 11 se la regola va cambiata. È il punto più delicato del metodo.')

cards2('Per lunedì 1° marzo: correzioni e risposte attese', [
    (1, 'Le correzioni della revisione', '15 minuti', 'Ognuna corregge la sua parte di core o la sua skill secondo i commenti in revisione.md che il gruppo ha accettato.'),
    (2, 'Le risposte attese', '15 minuti', 'Ognuna completa la risposta attesa dei casi che ha scritto, senza provare l’agente su quei casi.')],
    [R('Totale: 30 minuti nel tuo slot. ', 'Versione minima, 15 minuti: solo le risposte attese dei tuoi casi.')],
    notes='La batteria si esegue alla lezione 11. Obiettivo del percorso: almeno 80% di casi ok. Prima della lezione 11 l’agente non va usato su casi reali con dati di persone.')

VIDEOS = [
    ('La masterclass su Claude: 5 livelli', 'Dalle richieste semplici alle istruzioni strutturate.', 'https://www.youtube.com/watch?v=iAgSjh0_H4I', 'italiano'),
    ('Scrivere prompt migliori in 12 minuti', 'Le regole di scrittura che valgono anche per core e skill.', 'https://www.youtube.com/watch?v=bviJO4SPzh4', 'italiano'),
    ('Building more effective AI agents', 'Anthropic: istruzioni chiare e strumenti ben descritti.', 'https://www.youtube.com/watch?v=uhJJgc-0iTQ', 'inglese, sottotitoli')]
EXTRA = None
links('Per approfondire: scrivere istruzioni che un modello segue', VIDEOS)

closing('Quale regola avete riscritto dopo aver letto l’agente dell’altro gruppo?', 'Prossima lezione: lunedì 1° marzo')

SCALETTA = {
    'title': 'Lezione 10 · Agente, fase 5: scrittura e casi di prova',
    'subtitle': 'Scaletta del facilitatore · lunedì 22 febbraio 2027 · 2 ore · 5 colleghe in 2 gruppi',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'I gruppi imparano a scrivere istruzioni invece di spiegazioni, si rivedono a vicenda core e skill con quattro domande, scrivono in aula da 6 a 8 casi di prova (due di stop) e fanno una seconda prova esplorativa con core e skill insieme. A casa ognuna applica le correzioni e completa le risposte attese dei suoi casi.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Scrivere regole che dicono cosa fare in un caso concreto, e decidere cosa è giusto prima di vedere cosa fa l’agente.'],
            ['Output in aula', 'revisione.md per ogni agente, scritto dall’altro gruppo. casi-prova.md con 6-8 input, di cui 2 di stop. Seconda prova annotata nel diario.'],
            ['Output per l’1/3', 'Correzioni accettate applicate da ciascuna sulla sua parte. Risposte attese complete, scritte senza provare l’agente.'],
            ['Segnale che ha funzionato', 'Nessuna regola comincia con “è importante che”. Ogni collega ha scritto almeno un caso di prova.']]],
        ['h1', 'Prima del 22 febbraio'],
        ['b', 'Passaggio con il DPO: se non è stato fatto prima della lezione 1, va fatto adesso, prima che un agente vada in uso reale alla lezione 11. Le domande: quali dati minimi possono usare gli agenti in Cowork aziendale, per quanto si conservano, chi ne risponde.'],
        ['b', 'Leggi le skill dei due gruppi: annota dove la revisione incrociata potrebbe non vedere un problema, senza correggere.'],
        ['b', 'Adatta l’esempio della slide 4 a uno dei due processi reali.'],
        ['b', 'Controlla che in 04_modelli ci siano revisione.md e casi-prova.md.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-10’', 'Ripartenza', 'Slide 3. Le skill dopo due prove, dal diario.'],
            ['10-20’', 'Pillola', 'Slide 4. La stessa regola scritta due volte. Ogni gruppo riscrive a voce una regola del suo core.'],
            ['20-50’', 'Revisione incrociata', 'Slide 5. Scambio delle cartelle, 15 minuti di lettura con le quattro domande, 15 di discussione. Commenti in revisione.md.'],
            ['50-80’', 'Casi di prova', 'Slide 6. Trenta minuti di gruppo. Almeno un caso a testa; i due di stop con la risposta attesa già scritta.'],
            ['80-105’', 'Seconda prova', 'Slide 7. Un caso normale e uno di stop per gruppo. Errori nel diario, con il nome di chi corregge.'],
            ['105-120’', 'Consegna', 'Slide 8, 9 e 10.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Il modello non “capisce l’intenzione” di una regola: la esegue. Una spiegazione lascia a lui la scelta di cosa fare, e la scelta cambia da una risposta all’altra. Un’istruzione toglie la scelta dove non deve esserci. Lo stesso vale per i casi di prova: se la risposta attesa si scrive dopo aver visto quella dell’agente, si finisce per misurare quanto ci piace, non quanto è giusta.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['La revisione incrociata diventa una critica', 'Riporta alle quattro domande: si commenta il testo, non le persone. Decide il gruppo autore.'],
            ['Un gruppo vuole correggere direttamente i file dell’altro', 'No: solo commenti in revisione.md. Chi scrive una parte la corregge.'],
            ['I casi sono tutti facili', 'Chiedi: qual è la richiesta che vi arriva e che vi mette in difficoltà? Quella è un caso.'],
            ['Qualcuna incolla una risposta dell’agente come risposta attesa', 'Si cancella e si riscrive a mano. È la regola della slide 6.'],
            ['La seconda prova va peggio della prima', 'Succede quando le skill si sovrappongono. Annotatelo: si sistema con la batteria.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda, i core e le skill prima e dopo la revisione (ottimo materiale didattico), le due revisione.md, le batterie di prova.']]}

CONSEGNA = {
    'title': 'Lezione 10 · Il lavoro per lunedì 1° marzo',
    'subtitle': 'Percorso AI per Talent · 30 minuti nel tuo slot · versione minima: 15 minuti',
    'blocks': [
        ['p', [{'text': 'Settimana piena? Fai la versione minima: ', 'bold': True}, 'completa solo le risposte attese dei casi che hai scritto (15’). Le correzioni le fate in gruppo all’inizio della lezione 11.']],
        ['h1', '1. Le correzioni della revisione (15’)'],
        ['p', 'Apri revisione.md nella cartella del tuo agente. Per ogni commento che il gruppo ha accettato e che riguarda la tua parte di core o la tua skill:'],
        ['b', 'Correggi il testo.'],
        ['b', 'Segna nel diario PROCESSO.md: commento, cosa hai cambiato, il tuo nome.'],
        ['b', 'Se non sei d’accordo con un commento accettato, scrivilo nel diario: lo decide la owner.'],
        ['h1', '2. Le risposte attese (15’)'],
        ['p', 'In casi-prova.md, completa la risposta attesa dei casi che hai scritto tu. Non provare l’agente su quei casi prima della lezione 11.'],
        ['table', [800, 3700, 3500, 1638], [
            ['#', 'Input realistico', 'Risposta attesa', 'Tipo'],
            ['1', 'Preso da un caso vero, con i nomi inventati', 'Cosa deve fare e cosa deve contenere la risposta', 'normale'],
            ['…', ' ', ' ', ' '],
            ['7', 'Manca un dato essenziale', 'Si ferma e lo chiede, senza inventarlo', 'stop'],
            ['8', 'Gli si chiede di inviare o di decidere su una persona', 'Rifiuta e spiega cosa può fare invece', 'stop']]],
        ['h2', 'Regole'],
        ['b', 'Scrivi la risposta attesa prima di provare l’agente, mai copiandola da un output già generato.'],
        ['b', 'Niente dati personali di candidati o dipendenti: nomi inventati.'],
        ['b', 'Non usare ancora l’agente su casi reali con dati di persone.'],
        ['h1', 'Cosa porti alla lezione 11'],
        ['b', 'casi-prova.md completo, con le tue risposte attese.'],
        ['b', 'La tua parte di core o la tua skill, corretta.'],
        ['h1', 'Se hai saltato la lezione'],
        ['p', 'Le decisioni prese: l’altro gruppo ha letto il vostro agente e ha scritto i commenti in revisione.md; il gruppo ha scritto da 6 a 8 casi di prova, due dei quali di stop, e ha fatto una seconda prova. Il passo minimo (25 minuti, prima della lezione 11): leggi i commenti che riguardano la tua parte e correggi; scrivi un caso di prova legato alla tua skill, con la risposta attesa.']]}
