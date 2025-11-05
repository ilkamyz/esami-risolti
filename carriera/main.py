def getYearsDifference(dataimmatricolazione, datalaurea):
    #YYYY-MM-DD
    
    difference = int(datalaurea[0:4]) - int(dataimmatricolazione[0:4]) + (int(datalaurea[5:7]) - int(dataimmatricolazione[5:7]))/12 + (int(datalaurea[8:])- int(dataimmatricolazione[8:])) /365
    return difference
   

def main():
    with open('immatricolazione.txt', 'r') as f:
        immatricolazione = {}
        next(f)
        for line in f:
            line = line.strip().split(',')
            immatricolazione[line[0]] = [line[1], line[2], line[3]]
    with open('laurea.txt', 'r') as f:
        laurea = {}
        next(f)

        for line in f:
            line = line.strip().split(',')
            laurea[line[0]] = (line[1], line[2], line[3])
    differenze = {}
    toRemoveTime = []
    toRemoveImmatricolazione = []
    studenti = {}
    for matricola, (nome, cognome, datalaurea) in laurea.items():
        try:
            immatricolazione[matricola].append(datalaurea)
        except KeyError:
            toRemoveImmatricolazione.append((matricola, nome, cognome))
            
    for matricola, (nome, cognome, dataimmatricolazione, datalaurea) in immatricolazione.items():
            differenze[matricola] = getYearsDifference(dataimmatricolazione, datalaurea)
            if differenze[matricola] < 0:
                toRemoveTime.append((matricola))
                
    print('Le date di Immatricolazione/laurea non sono compatibili per ', end='')
    for matricola in toRemoveTime:
        differenze.pop(matricola)
        print(f'{immatricolazione[matricola][0]  + '+ ' + immatricolazione[matricola][1]} ', end='')

    differenzeTop3 = differenze.copy()
    top3 = []
    for _ in range(3):
        least = min(differenzeTop3.keys(), key= lambda x: differenzeTop3[x])
        differenzeTop3.pop(least)
        top3.append(least)
    
    differenzeBot3 = differenze.copy()
    bot3 = []
    for _ in range(3):
        most = max(differenzeBot3.keys(), key= lambda x: differenzeBot3[x])
        differenzeBot3.pop(most)
        bot3.append(most)



    
    print('manca la data di Immatricolazione di: ', end= '')
    for matricola, nome, cognome in toRemoveImmatricolazione:
        print(f'{nome +' ' + cognome}', end='')

    print('Lista studenti e anni di carriera universitaria:')
    for matricola, tempo in differenze.items():
        print(f'{immatricolazione[matricola][0], immatricolazione[matricola][1]}: {tempo}')
    print(f'i 3 studenti più veloci a laurearsi:') 
    for matricola in top3:
        print(f'{immatricolazione[matricola][0], immatricolazione[matricola][1]}: {differenze[matricola]}')
    print(f'i 3 studenti più lenti a laurearsi:') 
    for matricola in bot3:
        print(f'{immatricolazione[matricola][0], immatricolazione[matricola][1]}: {differenze[matricola]}')
if __name__ == '__main__':
    main()
    




            

