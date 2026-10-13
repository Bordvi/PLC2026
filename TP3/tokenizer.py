
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<COMMENT>#.*)|(?P<VAR>\?\w+)|(?P<LANGUAGE>@\w{2})|(?P<STR>"[^"]*")|(?P<DELIMITER>[{}.])|(?P<LIMIT>(?i:LIMIT)\b)|(?P<SELECT>(?i:SELECT)\b)|(?P<WHERE>(?i:WHERE)\b)|(?P<INT>\d+)|(?P<CONCEPT>\w+(?::\w+)*)|(?P<SKIP>[ \t])', input_string) # Procurar regex no texto
    for m in mo:
        dic = m.groupdict()
        if dic['COMMENT']:
            t = ("COMMENT", dic['COMMENT'], linha, m.span())

        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
    
        elif dic['LANGUAGE']:
            t = ("LANGUAGE", dic['LANGUAGE'], linha, m.span())
    
        elif dic['STR']:
            t = ("STR", dic['STR'], linha, m.span())
    
        elif dic['DELIMITER']:
            t = ("DELIMITER", dic['DELIMITER'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())
    
        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['INT']:
            t = ("INT", dic['INT'], linha, m.span())
    
        elif dic['CONCEPT']:
            t = ("CONCEPT", dic['CONCEPT'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and not dic['COMMENT'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)    

