def main():
    with open('australian_open.csv', 'r') as f:
        matriceTemp = [line.strip().split(';') for line in f]
    matrice = []
    for row in matriceTemp:
        matrice.append([row[7], row[8], row[-1]])
    players = set()
    for row in matrice:
        players.add(row[0])
        players.add(row[1])
    players = list(players)
    players.sort()
    count = 1
    for player in players:
        print(f'{count}. {player}')
        count += 1
    
    indice =  int(input('Scegli il giocatore: ')) - 1
    for row in matrice:
        if row[0] == players[indice] or row[1] == players[indice]:
            print(f'{row[0]} Vs. {row[1]} {row[2]}')

    
if __name__ == '__main__':
    main()