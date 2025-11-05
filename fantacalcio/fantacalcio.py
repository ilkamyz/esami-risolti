from collections import defaultdict
def asta(players, budget, giocatoriMancanti):
    acquisti = []
    budgetRimanente = budget
    while budgetRimanente > 0 and giocatoriMancanti > 0 :
        giocatore = max(players.keys(), key= lambda x: players[x])
        if players[giocatore] < budgetRimanente and (budgetRimanente - players[giocatore]) >= giocatoriMancanti:
            acquisti.append([giocatore, players[giocatore]])
            budgetRimanente -= players[giocatore]
            giocatoriMancanti -= 1
            players.pop(giocatore)
            print(budgetRimanente)
        else:
            players.pop(giocatore)
    return acquisti

def dividiPerRuolo(giocatori, ruolo):
    d = {}
    for key, value in giocatori.items():
        if value[0] == ruolo:
            d[key] = value[1]
    return d


    None
def main():   
    with open('fantacalcio.txt', 'r') as f:
        elements = [line.strip() for line in f]
        matrice = [line.split(',') for line in elements]
    giocatori = {}
    for row in matrice:
        giocatori[row[0]] = [row[2].lstrip(), int(row[3])]
    print(giocatori)
    portieri = dividiPerRuolo(giocatori, 'portiere')
    difensori = dividiPerRuolo(giocatori, 'difensore')
    centrocampisti = dividiPerRuolo(giocatori, 'centrocampista')
    attaccanti = dividiPerRuolo(giocatori, 'attacante')

    portieriAcquistati = asta(portieri, 20, 3)
    
    print('\n', portieriAcquistati)
if __name__ == '__main__':
    main()
None
    