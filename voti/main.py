import csv
from statistics import mean
def readAppello(filename: str) -> dict:
    idx1 = 0
    dizionario = {}
    with open(filename,'r') as f:
        dictreader = csv.DictReader(f)
        for line in dictreader:
            dizionario[idx1] = tuple(line.values())
            idx1 += 1
    return dizionario

def joinAppelli(appelli: list[dict]) -> dict:
    'return a 0 indexed dictionary with all the appelli joined'
    idx = 0
    return_dict = {}
    for appello in appelli:
        for val in appello.values():
            return_dict[idx] = val
            idx += 1
    return return_dict

primo_appello = readAppello('primo_appello.csv')
secondo_appello = readAppello('secondo_appello.csv')
joined_appelli = joinAppelli([primo_appello, secondo_appello])

sorted_keys = sorted(joined_appelli.keys(),key = lambda x: float(joined_appelli[x][-1]), reverse= True)

with open('sessione.csv', 'w') as f:

    f.write('Nome,Cognome,Voto,Anno_di_Nascita,Media_Voti\n')
    for i in sorted_keys:
        nome, cognome, voto, anno, media_voti = joined_appelli[i]
        f.write(f'{nome},{cognome},{anno},{voto},{media_voti}\n')
    f.close()

differenze = []
for key in sorted_keys[:5]:
    _, _, voto, _, media_voti = joined_appelli[key]
    differenze.append(float(voto) - float(media_voti))
print(f'La media delle differenze tra voto e media nei primi 5 studenti è {mean(differenze):.2f}')