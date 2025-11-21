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
                d[composer][composition].append(seconds)
            except KeyError:
                d[composer][composition] = [seconds]
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
    for composition, seconds in nomiDict[nome].items():
        returnLst.append((composition, sum(seconds), len(seconds), mean(seconds)))
    return returnLst
        
            

def main():
    richieste = readRichieste('richieste.txt')
    nomiDict, musicnet = readMusicnet('musicnet.csv')
    for richiesta, nome in richieste:
        if richiesta == 'c':
            print(richiestaCompositore(nome, nomiDict))
        else:
            None
    
main()