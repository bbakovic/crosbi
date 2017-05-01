#!/usr/bin/python
#  -*- coding: utf-8 -*-
import codecs

def reformat(no):


    out = codecs.open('modTxt/out'+str(no)+'.json', 'w', 'utf-8')
    doc = codecs.open('modTxt/cro'+str(no)+'.txt', 'r', 'utf-8').read().replace('Mje\t', 'Mjesto\t').replace('Me\t', 'Mentor\t')
    docRe = doc.split('\nnew_DB_entry\n')
    for a in docRe[:-1]:
        aRe = a.split('\n')
        inp2 = '{'
        for x in aRe:
            key = '"' + x.split('\t')[0].strip().replace(' ', '_').replace(',', '_') + '"'
            value = '"' + x.split('\t')[1].strip().replace('\\', '/').replace('"', '\\"') + '"'
            if key == '"Autori"' and ';' in value:
                value = '[' + value.replace(' ; ', '","') + ']'
            if key == '"Ključne_riječi"' and ';' in value:
                value = '[' + value.replace('; ', '","') + ']'
            if key == '"Projekt_/_tema"' and ',' in value:
                value = '[' + value.replace(', ', '","') + ']'
            if key == '"Znanstvena_područja"' and ',' in value.replace('stvo, na','stvo_na').replace('stvo, ra','stvo_ra'):
                value = '[' + value.replace('stvo, na','stvo_na').replace('stvo, ra','stvo_ra').replace(', ', '","') + ']'
            inp2 += key + ':' + value.replace('<strong>', '').replace('</strong>', '').replace('<br/>', '//') + ',\n'

        inp2 += '}\n'
        inp2 = inp2.replace(',\n}', '\n}')
        inp2 = inp2.replace('Rudarstvo, naf','Rudarstvo_naf').replace('Zrakoplovstvo, rak','Zrakoplovstvo_rak')
        out.write(str(inp2))

for a in range(1,19):
    reformat(a)