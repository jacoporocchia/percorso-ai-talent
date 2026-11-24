# Sorgenti dei kit di lezione

Script che generano deck (python-pptx sul template TS) e Word (docx-js) delle lezioni.
- tslib.py: helper base (slide, box, text, bullets, numdot). kitfns.py: pattern di slide (agenda, cards3/4, steps, rows, compare, code_slide, prompt_slide, chain, links).
- Lezioni 3-12: lessons/lNN.py (slide + VIDEOS + SCALETTA + CONSEGNA), si generano con `python3 run_lesson.py NN`.
- Lezioni 1-2: l1deck.py / l2deck.py + doc/l1.js / doc/l2.js (versioni precedenti, scritte a mano).
Nota: gli script hanno percorsi assoluti dello scratchpad della sessione che li ha creati (BASE in run_lesson.py, exec in l1deck/l2deck): vanno aggiornati se si rigenera da un'altra sessione.
- Deck staff meeting: build_ts.py (python3 build_ts.py template_TS.pptx out.pptx). Diario L2: diario.py.
- Speech: speech/sNN.txt, python3 speech/build.py NN.
- shift.py: lo script usato l'11/11/2026 per spostare tutte le date dal venerdì al lunedì.

## v2 (16/11/2026)
Dopo la simulazione con tre colleghe tipo: blocco A 1-4, B 5-6 (dati fuso in una lezione), C 7, D 8-12. bozza_v2.py genera Percorso-AI-Talent.docx; regola_dati.py genera lezione-01/L01-regola-dati.docx. La v1 completa (materiali e sorgenti) è in _archivio-v1. kitfns.agenda ora accetta fino a 7 blocchi. I file modello per 04_modelli sono in materiali-comuni/04_modelli.
