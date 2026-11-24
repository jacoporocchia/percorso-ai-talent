import re, sys
PROTECT = ['14 al 18 dicembre', '14-18 dicembre', '14-18/12', '14 dicembre al 18 dicembre', 'all’11 dicembre', 'all’11/12', '16/11-11/12', 'Calendario 16/11-11/12']
M = {  # forme lunghe prima, tutto in un solo passaggio
 'venerdì 29 gennaio': 'lunedì 1° febbraio', 'Venerdì 29 gennaio': 'Lunedì 1° febbraio',
 'venerdì 26 febbraio': 'lunedì 1° marzo', 'Venerdì 26 febbraio': 'Lunedì 1° marzo',
 '29 gennaio': '1° febbraio', '26 febbraio': '1° marzo',
 '4 dicembre': '7 dicembre', '11 dicembre': '14 dicembre', '18 dicembre': '21 dicembre',
 '25 dicembre': '28 dicembre', 'l’1 gennaio': 'il 4 gennaio', '1 gennaio': '4 gennaio',
 '8 gennaio': '11 gennaio', '15 gennaio': '18 gennaio', '22 gennaio': '25 gennaio',
 '5 febbraio': '8 febbraio', '12 febbraio': '15 febbraio', '19 febbraio': '22 febbraio',
 '5 marzo': '8 marzo', '19 marzo': '22 marzo', '16 aprile': '19 aprile',
 '7-13 aprile': '12-16 aprile', '7 al 13 aprile': '12 al 16 aprile', '13 aprile': '16 aprile',
 'l’11/12': 'il 14/12', 'dell’11 dicembre': 'del 14 dicembre', 'l’11 dicembre': 'il 14 dicembre',
 '4/12': '7/12', '11/12': '14/12', '18/12': '21/12', '25/12': '28/12', 'l’1/1': 'il 4/1', '1/1': '4/1',
 '8/1': '11/1', '15/1': '18/1', '22/1': '25/1', '29/1': '1/2', '5/2': '8/2', '12/2': '15/2',
 '19/2': '22/2', '26/2': '1/3', '5/3': '8/3', '19/3': '22/3', '16/4': '19/4', '7-13/4': '12-16/4',
 'entro lunedì 14': 'entro mercoledì 16', 'entro lunedì': 'entro mercoledì',
 'venerdì 29': 'lunedì 1° febbraio', 'venerdì 26': 'lunedì 1° marzo',
 'venerdì 4': 'lunedì 7', 'venerdì 11': 'lunedì 14', 'venerdì 18': 'lunedì 21', 'Venerdì 18': 'Lunedì 21',
 'venerdì 8': 'lunedì 11', 'venerdì 15': 'lunedì 18', 'venerdì 22': 'lunedì 25', 'venerdì 5': 'lunedì 8',
 'venerdì 12': 'lunedì 15', 'venerdì 19': 'lunedì 22', 'venerdì 16': 'lunedì 19',
 'Venerdì scorso': 'Lunedì scorso', 'Venerdì': 'Lunedì', '12 venerdì': '12 lunedì', 'venerdì': 'lunedì',
}
keys = sorted(M, key=len, reverse=True)
rx = re.compile('|'.join(re.escape(k) + (r'(?!\d)' if k[-1].isdigit() else '') for k in keys))
def fix(s):
    toks = {}
    for i, p in enumerate(sorted(PROTECT, key=len, reverse=True)):
        t = '\x00%d\x00' % i; toks[t] = p; s = s.replace(p, t)
    # (?<!\d) davanti a ogni chiave numerica
    s = rx.sub(lambda m: M[m.group(0)] if not (m.start() and s[m.start()-1].isdigit() and m.group(0)[0].isdigit()) else m.group(0), s)
    for a, b in [('al 8 ', 'all’8 '), ('dal 8 ', 'dall’8 '), ('del 8 ', 'dell’8 '), (' il 8 ', ' l’8 '), (' il 8/', ' l’8/'), (' il 1/', ' l’1/'), ('Il 8 ', 'L’8 ')]:
        s = s.replace(a, b)
    for t, p in toks.items(): s = s.replace(t, p)
    return s
if __name__ == '__main__':
    for f in sys.argv[1:]:
        a = open(f, encoding='utf-8').read(); b = fix(a)
        if a != b: open(f, 'w', encoding='utf-8').write(b); print('mod', f)
