from csv import DictReader
from statistics import mean
from collections import defaultdict
def readMusicnet(filename: str) -> dict:
    #assumiamo che musicnet.csv sia ordinato bene
    try:
        muiscnet = {}
        d = defaultdict(dict)
        with open(filename,'r') as f:
            reader = DictReader(f)
            for line in reader:
                muiscnet[line['id']] = (line['composer'], line['composition'], line['movement'], line['ensemble'], line['catalog_name'], float(line['seconds']))
        for id, (composer, composition, movement, ensemble, catalog_name, seconds) in muiscnet.items():
            try:
                d[composer][(composition, catalog_name)].append(seconds)
            except KeyError:
                d[composer][(composition, catalog_name)] = [seconds]
        return d, muiscnet

    
    except OSError:
        print('Impossibile aprire il file')

def readRichieste(filename:str) -> list:
    try:
        richieste = []
        with open(filename, 'r') as f:
            for line in f:
                request, name = line.strip().split(':')
                richieste.append((request, name))
        return richieste
    except OSError:
        print('Impossbile aprire il file')

def richiestaCompositore(nome: str, nomiDict) -> list:
    returnLst = []
    for (composition, catalog_name), seconds in nomiDict[nome].items():
        returnLst.append((composition, catalog_name, sum(seconds), len(seconds), mean(seconds)))
    return returnLst

def richiestaStrumento(nome, musicnet)-> list:
    returnLst = []
    for idx, (composer, _,_, ensemble, catalog_name, seconds) in musicnet.items():
        if ensemble == nome:
            key = (composer, catalog_name)
            if key not in returnLst:
                returnLst.append(key)

    return returnLst

            

def main():
    richieste_compositori = {}
    richieste_strumenti = {}
    richieste = readRichieste('richieste.txt')
    nomiDict, musicnet = readMusicnet('musicnet.csv')

    for richiesta, nome in richieste:
        if richiesta == 'c':
            richieste_compositori[nome] = richiestaCompositore(nome, nomiDict)

        else:
            richieste_strumenti[nome] = richiestaStrumento(nome, musicnet)
    
    for nome, lista in richieste_compositori.items():
        print(f'Opere di {nome}')
        if lista != []:

            for composition, catalog_name, seconds, count, mean in lista:
                print(f'- {catalog_name}: {composition}, {seconds:.2f} secondi')
                print(f'    {count} movimenti, in media {mean:.2f} secondi')

        else:
            print('Compositore non presente in catalogo')
            
    
    for nome, lista in richieste_strumenti.items():
        print(f'Opere con formazione musicale: {nome}')
        if lista != []:
            for composer, catalog_name in lista:
                print(f'- {composer}: opera: {catalog_name}')
        else:
            print('Strumento non presente in catalogo')
                
if __name__ == '__main__':
    main()