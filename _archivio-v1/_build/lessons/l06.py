cover('Lezione 6 · Disegnare la struttura', 'Lunedì 25 gennaio 2027')

agenda('Oggi il team decide la sua struttura condivisa, e ognuna ci migra un caso reale', [
    ('0-15’', 'Ripartenza', 'Quante copie avete trovato'),
    ('15-30’', 'Pillola', 'Quattro convenzioni che reggono'),
    ('30-75’', 'Progetto', 'La struttura di Talent, in gruppo'),
    ('75-105’', 'Laboratorio', 'Il primo dataset migrato in aula'),
    ('105-120’', 'Consegna', 'Migrare e scrivere il LEGGIMI')],
    'una struttura condivisa decisa insieme, con chi risponde di ogni cartella, e il primo dataset già dentro.',
    notes='È la lezione più “di team” del percorso: la struttura funziona solo se le cinque la sentono loro. La proposta è un punto di partenza, non un ordine.')

cards3('Prima di progettare: quante copie abbiamo trovato?', [
    ('Il totale', 'Ognuna dice il numero di copie trovate sul suo tema. Si somma: è la base del KPI.'),
    ('La copia più strana', 'Un esempio a testa. Dove stava, perché era nata.'),
    ('Chi decideva', 'Per quante di queste sapevate dire subito quale fosse la vera?')],
    R('Il numero di oggi ', 'si riconta sull’area migrata alla lezione 12. È il primo indicatore del blocco B.'),
    notes='Scrivi il totale aggregato. Non serve sapere di chi sono le copie.')

cards4('Quattro convenzioni bastano, se le rispettano tutte', [
    ('Il nome', 'AAAA-MM-GG_argomento. Si ordina da solo e si legge senza aprirlo.'),
    ('Niente “def” o “v3”', 'Le versioni le tiene lo strumento: la cronologia di OneDrive e SharePoint.'),
    ('Un LEGGIMI', 'Tre righe per cartella: cosa contiene, chi ne risponde, da dove arrivano i dati.'),
    ('Link, non copia', 'Se serve altrove, si mette il collegamento al file che fa fede.')],
    R('La cronologia delle versioni ', 'è già nel file: tasto destro, Cronologia versioni. Si torna indietro senza tenere copie.'),
    notes='Mostra dal vivo la cronologia delle versioni su un file in OneDrive o SharePoint. È la cosa che rende inutili le copie “per sicurezza”.')

code_slide('La proposta: sette cartelle, ognuna risponde a una domanda', 'Talent/  (cartella condivisa del team)',
           '00_LEGGIMI.md       regole e chi risponde\n01_fonti/           dati originali, sola lettura\n02_lavoro/<progetto>/  elaborazioni in corso\n03_output/          deliverable consegnati\n04_modelli/         template, checklist, skill\n05_agenti/<nome>/   core, skill, prove, registro\n99_archivio/        chiuso, non si modifica\n\ncoach-<nome>/       sul tuo Mac, privata',
           'Le domande che la struttura risponde', [
               ('01 contro 02:', 'il dato originale non si tocca, si elabora altrove.'),
               ('03:', 'cosa è stato consegnato, e a chi, in un posto solo.'),
               ('04 e 05:', 'gli strumenti del team: template, skill e agenti.'),
               ('99:', 'quello che è chiuso esce dai piedi senza sparire.')],
           R('È un punto di partenza: ', 'oggi la verificate sulle vostre mappe e la cambiate dove non regge.'),
           notes='Ricalca la logica della cartella del coach: ciò che è di tutti separato da ciò che è di una persona, le fonti separate dalle elaborazioni.')

cards3('Cosa non entra: i dati di persone restano nei sistemi di record', [
    ('Dati di candidati e dipendenti', 'Restano nel gestionale HR e nella piattaforma. Nella struttura solo anonimizzati, per uno scopo dichiarato.'),
    ('La tua istanza del coach', 'Resta sul tuo Mac. Nella struttura condivisa entra solo quello che scegli di portare.'),
    ('Gli allegati come archivio', 'Un allegato si salva una volta, nel posto giusto. La mail non è una cartella.')],
    R('Una regola in più, da decidere oggi: ', 'chi può scrivere in 01_fonti, e chi può svuotare 99_archivio.'),
    notes='La regola sui dati personali protegge le persone e protegge le colleghe: è quello che permette di usare Claude sulla struttura senza chiedersi ogni volta cosa c’è dentro.')

steps('Il progetto in gruppo: in 45 minuti la struttura ha nomi, regole e owner', [
    ('Partire dalla proposta', 'Le sette cartelle, così come sono.'),
    ('Provarla sulle mappe', 'Ogni tema mappato: dove andrebbe?'),
    ('Cambiare dove non regge', 'Una sottocartella in più, un nome diverso.'),
    ('Dare un owner', 'Chi risponde di ogni cartella.'),
    ('Scrivere 00_LEGGIMI', 'Con Claude, dalle decisioni prese.')],
    [R('Il LEGGIMI lo scrive Claude, ', 'ma dalle vostre decisioni: “scrivi un LEGGIMI con queste regole, in una pagina”.'), R('Poi lo rileggete ad alta voce. ', 'Se una regola non si capisce, non verrà rispettata.')],
    notes='Facilita tu, ma non decidere tu. Se la discussione si blocca su un nome, scegliete il più semplice e andate avanti: si può cambiare.')

prompt_slide('Migrare un dataset: la versione vera entra, le copie escono, niente si cancella subito', 'Il prompt, in Cowork sulla cartella del tema',
             '“Ti ho dato la cartella del tema e la nuova struttura. Proponimi dove va ogni file, con il nuovo nome AAAA-MM-GG_argomento. Le copie che non sono la versione vera vanno in _copie-da-eliminare. Fammi vedere la proposta prima di spostare qualsiasi cosa.”',
             'Poi verifichi', 'Controlla la proposta riga per riga. Solo dopo il tuo ok Claude sposta i file. Le copie si cancellano dopo un mese, se nessuno le ha cercate.',
             'In aula, per ognuna', [
                 ('Un dataset', 'piccolo, dalla mappa'), ('La proposta', 'letta riga per riga'), ('Lo spostamento', 'dopo il tuo ok'), ('Il LEGGIMI', 'tre righe')],
             foot='Spostare file è un’azione: Claude la fa solo dopo il tuo ok.',
             notes='Prima la tua demo su un dataset piccolo. Il passaggio chiave è “fammi vedere la proposta prima di spostare”: è la stessa regola della lezione 2, prima la tabella poi l’azione.')

cards2('Per lunedì 1° febbraio: un dataset reale migrato, con il suo LEGGIMI', [
    (1, 'Migra il tuo tema', '45 minuti', 'Quello della tua mappa. Versione vera nel posto giusto, copie in _copie-da-eliminare, link dove serviva la copia.'),
    (2, 'Scrivi il LEGGIMI', '15 minuti', 'Tre righe nella sottocartella: cosa contiene, chi ne risponde, da dove arrivano i dati.')],
    [R('Prima di finire: ', 'cerca un file del tema nella struttura nuova. Lo trovi in meno di un minuto?'), R('Tempo totale: ', 'circa 60 minuti.')],
    notes='Il test di reperibilità della lezione 7 si fa sulla struttura nuova. Chi non migra il suo tema non vedrà la differenza.')

VIDEOS = [
    ('Come organizzo i file sul computer', 'Se non l’hai visto la settimana scorsa: cinque regole semplici.', 'https://www.youtube.com/watch?v=qzUO7GeIUjg', 'italiano'),
    ('Pillola Agile: la Prima Direttiva', 'Lavorare in gruppo su regole comuni partendo dalla fiducia.', 'https://www.youtube.com/watch?v=45w_LYaF4iQ', 'italiano'),
    ('Organizzare i file con PARA', 'Un esempio concreto di struttura per progetti e archivio.', 'https://www.youtube.com/watch?v=jTWbqd9vORY', 'inglese, sottotitoli'),
    ('Organize your Google Drive with PARA', 'La stessa logica su un drive condiviso.', 'https://www.youtube.com/watch?v=Txkn35XwwR4', 'inglese, sottotitoli')]
EXTRA = None
links('Per approfondire: strutture che reggono, e regole decise insieme', VIDEOS)

closing('Quale regola sarà la più difficile da rispettare?', 'Prossima lezione: lunedì 1° febbraio')

SCALETTA = {
    'title': 'Lezione 6 · Disegnare la struttura',
    'subtitle': 'Scaletta del facilitatore · lunedì 25 gennaio 2027 · 2 ore · 5 colleghe',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'Il team parte dalla proposta delle sette cartelle, la prova sulle mappe della settimana, la cambia dove non regge, assegna un owner a ogni cartella e scrive con Claude il 00_LEGGIMI. Poi ognuna migra in aula un dataset piccolo. A casa migra il suo tema completo.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Un dato vive in un solo posto. Si collega, non si copia. Le versioni le tiene lo strumento.'],
            ['Output in aula', 'Struttura condivisa creata, con owner per cartella e 00_LEGGIMI. Un dataset piccolo migrato per collega.'],
            ['Output per l’1/2', 'Il tema della mappa migrato, con LEGGIMI della sottocartella. Copie in _copie-da-eliminare.'],
            ['Segnale che ha funzionato', 'Le regole del LEGGIMI sono scritte con le parole delle colleghe, e ognuna sa di quale cartella risponde.']]],
        ['h1', 'Prima del 25 gennaio'],
        ['b', 'Crea la cartella condivisa Talent in OneDrive o SharePoint, vuota, con i permessi per le cinque. Verifica che sia sincronizzata sui loro Mac e che Cowork ci lavori.'],
        ['b', 'Prepara il totale aggregato delle copie dalla lezione 5, se le colleghe te l’hanno mandato.'],
        ['b', 'Un dataset piccolo per la tua demo di migrazione.'],
        ['b', 'Prova la cronologia delle versioni su un file condiviso: la mostri dal vivo.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-15’', 'Ripartenza', 'Slide 3. Totale delle copie, la più strana, quante volte sapevate quale era la vera.'],
            ['15-30’', 'Pillola', 'Slide 4. Quattro convenzioni. Demo della cronologia delle versioni.'],
            ['30-75’', 'Progetto in gruppo', 'Slide 5, 6 e 7. Proposta, cosa non entra, poi i cinque passi: provarla sulle mappe, cambiarla, owner, 00_LEGGIMI scritto con Claude e letto ad alta voce.'],
            ['75-105’', 'Migrazione in aula', 'Slide 8. Tua demo, poi ognuna su un dataset piccolo. Proposta prima, spostamento dopo l’ok.'],
            ['105-120’', 'Consegna', 'Slide 9, 10 e 11.']]],
        ['h1', 'Il prompt per il 00_LEGGIMI'],
        ['quote', 'Scrivi il file 00_LEGGIMI.md della cartella condivisa del team Talent, in una pagina. Contiene: a cosa serve ogni cartella, chi ne risponde, le quattro regole (nomi AAAA-MM-GG_argomento, niente def o v3, LEGGIMI di tre righe in ogni sottocartella, link e non copia), cosa non entra (dati personali di candidati e dipendenti, se non anonimizzati e per uno scopo dichiarato), chi può scrivere in 01_fonti e chi svuota 99_archivio. Usa solo le decisioni che ti scrivo qui sotto, senza aggiungerne.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['Il gruppo si blocca su un nome o su una cartella', 'Scegliete la versione più semplice e andate avanti. La struttura si rivede alla lezione 12.'],
            ['Claude sposta file senza aspettare', 'Ripeti nel prompt “fammi vedere la proposta prima di spostare qualsiasi cosa”. Se è già successo, la cronologia e il cestino della cartella condivisa permettono di tornare indietro.'],
            ['Un dataset contiene dati personali', 'Non entra. Resta nel sistema di record, e nella struttura va solo un link o un estratto anonimo.'],
            ['Una collega vuole tenere la sua copia “di lavoro”', 'Va bene in 02_lavoro, con il nome giusto e un link alla fonte in 01_fonti.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda della consegna, la struttura e il 00_LEGGIMI finali (sono già un modello per altri team), il prompt di migrazione, la registrazione della pillola e della discussione sulle regole.']]}

CONSEGNA = {
    'title': 'Lezione 6 · Il lavoro per lunedì 1° febbraio',
    'subtitle': 'Percorso AI per Talent · tempo stimato: circa 60 minuti',
    'blocks': [
        ['h1', '1. Migra il tuo tema (45’)'],
        ['p', 'È il tema della tua mappa. In Cowork, dai a Claude la cartella del tema e la struttura condivisa, con questo prompt:'],
        ['quote', 'Ti ho dato la cartella del tema e la nuova struttura. Proponimi dove va ogni file, con il nuovo nome AAAA-MM-GG_argomento. Le copie che non sono la versione vera vanno in _copie-da-eliminare. Fammi vedere la proposta prima di spostare qualsiasi cosa.'],
        ['b', 'Controlla la proposta riga per riga, poi dai l’ok.'],
        ['b', 'Dove prima serviva una copia, metti un link al file vero.'],
        ['b', 'Le copie restano in _copie-da-eliminare per un mese: se nessuno le cerca, si cancellano.'],
        ['b', 'Niente dati personali di candidati o dipendenti: restano nei sistemi di record.'],
        ['h1', '2. Scrivi il LEGGIMI della sottocartella (15’)'],
        ['p', 'Tre righe, in un file LEGGIMI.md:'],
        ['n', 'Cosa contiene.'],
        ['n', 'Chi ne risponde.'],
        ['n', 'Da dove arrivano i dati.'],
        ['h1', 'Prima di finire'],
        ['p', 'Cerca un file del tema nella struttura nuova, come se non sapessi dov’è. Lo trovi in meno di un minuto? Annota il tempo.'],
        ['h1', 'Cosa porti alla lezione 7'],
        ['b', 'Il tema migrato e il suo LEGGIMI.'],
        ['b', 'Quante copie sono finite in _copie-da-eliminare.']]}
