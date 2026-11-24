# Percorso AI Talent

Materiali didattici, deck, scalette, speech e consegne per un percorso formativo di **12 lezioni sull’intelligenza artificiale applicata al lavoro**.

Il progetto accompagna cinque colleghe dal primo uso di Claude alla costruzione di due agenti operativi su processi reali, organizzando dati, metodi e responsabilità lungo un percorso on the job.

## Obiettivi

Al termine del percorso, i partecipanti saranno in grado di:

- valutare dove l’IA può davvero liberare tempo;
- organizzare i dati in una struttura condivisa e affidabile;
- utilizzare Claude su documenti e processi concreti;
- progettare istruzioni riutilizzabili;
- costruire e testare un agente su un processo ripetitivo;
- definire limiti, responsabilità e verifiche d’uso;
- trasformare i materiali del percorso in risorse replicabili.

## Struttura del repository

```text
.
├── lezione-01/                         Materiali della prima lezione
├── ...
├── lezione-12/                         Materiali dell'ultima lezione
├── materiali-comuni/                   Risorse condivise tra le lezioni
├── templates/                          Template PowerPoint e script esemplificativo
├── _build/                             Sorgenti Python e JavaScript per rigenerare i materiali
├── _archivio-v1/                       Versione precedente del progetto
├── Percorso-AI-Talent.docx
├── Percorso-AI-Talent-staff-meeting.pptx
└── Simulazione-persona-feedback.docx
```

Ogni cartella `lezione-NN` contiene, quando disponibili:

- `LNN-deck-aula.pptx`: presentazione per l’aula;
- `LNN-scaletta-facilitatore.docx`: guida per il facilitatore;
- `LNN-consegna-colleghe.docx`: consegna settimanale;
- `LNN-speech.docx`: testo pronunciabile;
- eventuali demo e risorse aggiuntive.

## Rigenerazione dei materiali

Gli script in `_build/` generano i deck con `python-pptx` e i documenti Word con `docx-js`.

```bash
cd _build
python3 run_lesson.py NN
```

Sostituire `NN` con il numero della lezione, ad esempio `03` o `12`.

Gli altri script disponibili consentono di:

- generare il deck dello staff meeting;
- creare le bozze dei documenti generali;
- produrre speech;
- gestire template e helper comuni;
- spostare date e contenuti tra versioni del percorso.

> **Nota**
>
> Alcuni script nella versione corrente contengono percorsi assoluti creati durante lo sviluppo. Prima della rigenerazione potrebbero richiedere adattamenti a `BASE`, alle directory locali e alle template in uso.

## Requisiti indicativi

- Python 3;
- `python-pptx`;
- Node.js;
- `docx-js`;
- Microsoft PowerPoint o un altro software compatibile con `.pptx`;
- Microsoft Word o un software compatibile con `.docx`.

## Template

Il template `templates/template_TS.pptx` contiene la struttura grafica ufficiale.

Lo script `templates/build_deck_esempio.py` mostra come creare un deck a partire dal template:

```bash
python3 templates/build_deck_esempio.py \
  templates/template_TS.pptx \
  output.pptx
```

## Archiviazione

La cartella `_archivio-v1/` conserva la prima versione dei sorgenti e dei materiali.

Le nuove modifiche vanno apportate ai file attuali, evitando di sovrascrivere i contenuti dell’archivio.

## Tecnologia

- **Python**: generazione di deck, helper e automazioni;
- **JavaScript**: generazione dei documenti Word;
- **Shell**: utility ausiliarie;
- **PPTX/DOCX**: formati finali dei materiali.

## Licenza

Nel repository non è ancora specificata una licenza.

Prima di una redistribuzione esterna, definire le condizioni d’uso dei materiali e dei contenuti allegati.

## Autore

Repository mantenuto da Jacopo Rocchia e Massimiliano Peglia.
