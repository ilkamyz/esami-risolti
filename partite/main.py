def getYearsDifference(dataimmatricolazione, datalaurea):
    #YYYY-MM-DD
    
    difference = int(datalaurea[0:4]) - int(dataimmatricolazione[0:4]) + (int(datalaurea[5:7]) - int(dataimmatricolazione[5:7]))/12 + (int(datalaurea[8:])- int(dataimmatricolazione[8:])) /365
    return difference
def getAverage(yearsDifference, partite):
    return float(int(partite) / yearsDifference)

def main():
    giocatori = {}
    inizio_not_found = []
    with open('inizio_carriera.txt','r') as f:
        next(f)
        for line in f:
            e = line.strip().split(',')
            giocatori[e[0]] = [e[i] for i in range(1,4)]
    with open('partite_giocate.txt','r') as f:
        next(f)
        for line in f:
            e = line.strip().split(',')
            try:
                giocatori[e[0]].append(e[3])
                giocatori[e[0]].append(e[4])
            except KeyError:
                inizio_not_found.append((e[1], e[2]))
#giocatori[id] = nome, cognome, data1, data2, partite
#                   0   1       2       3       4
    negative = []
    fine_not_found = []
    for key, value in giocatori.items():
        if len(value) != 5:
            fine_not_found.append(key)
    for key in fine_not_found:
        giocatori.pop(key)

    for key, (nome, cognome, data1, data2, partite) in giocatori.items():
        years = getYearsDifference(data1, data2)
        if years > 0:
            giocatori[key].append(getAverage(years, partite))
        else:
            negative.append((key, nome, cognome))
    for (nome, cognome) in inizio_not_found:
        print(f'Errore: non trovata la data di inizio carriera di {nome} {cognome}')
        
    for (key, nome, cognome) in negative:
        print(f'Errore: non corrisponde la data di aggiornamento per {nome} {cognome}')
        giocatori.pop(key)

    increasing = sorted(giocatori, key= lambda x:  giocatori[x][-1])
    decreasing = sorted(giocatori, key= lambda x: -giocatori[x][-1])
    for key, (nome, cognome, data1, data2, partite, media) in giocatori.items():
        print(f'{nome} {cognome}: {media:.2f} partite/anno')

    print('I 3 giocatori con la media più bassa')
    for key in increasing[0:3]:
        (nome, cognome, data1, data2, partite, media) = giocatori[key]
        print(f'{nome} {cognome}: {media:.2f} partite/anno')
    print('I 3 giocatori con la media più alta')

    for key in decreasing[0:3]:
        (nome, cognome, data1, data2, partite, media) = giocatori[key]
        print(f'{nome} {cognome}: {media:.2f} partite/anno')


if __name__ == '__main__':
    main()