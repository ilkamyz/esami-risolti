def printGriglia(griglia):
    for row in griglia:
        print(' '.join(row))

def in_bounds(r, c, R=6, C=7):
    return 0 <= r < R and 0 <= c < C

def checkWin(griglia, row, col, simbolo):
    R, C = len(griglia), len(griglia[0])

    def check_dir(dr, dc):
        # controlla 4 in fila che PARTONO da (row, col) e proseguono nella direzione (dr, dc)
        cells = []
        for k in range(4):
            r = row + dr * k
            c = col + dc * k
            if not in_bounds(r, c, R, C):
                return False
            cells.append(griglia[r][c])
        return cells == [simbolo] * 4

    # 1) sinistra  (dr=0,  dc=-1)
    if check_dir(0, -1):
        return True
    # 2) destra    (dr=0,  dc=+1)
    if check_dir(0, +1):
        return True
    # 3) basso     (dr=+1, dc=0)
    if check_dir(+1, 0):
        return True
    # 4) diag basso-sx (dr=+1, dc=-1)
    if check_dir(+1, -1):
        return True
    # 5) diag basso-dx (dr=+1, dc=+1)
    if check_dir(+1, +1):
        return True

    return False
def main():
    mosse = []
    with open('mosse.txt','r') as f:
        for line in f:
            group = line.strip().split(' ')
            mosse.append((group[0], group[1]))
    SIMBOLI = {
        'G1' : 'O',
        'G2' : 'X'
    }
    nextFreeRow = {
        0 : 5,
        1 : 5,
        2: 5,
        3: 5,
        4: 5,
        5: 5,
        6: 5
    }
    rows, cols = 6, 7
    griglia = [['-' for _ in range(cols)] for _ in range(rows)]

    print('Griglia Vuota:')
    printGriglia(griglia)
    moves = 0
    for giocatore, col in mosse:
        moves += 1
        col = int(col)
        print(nextFreeRow[col], col)
        griglia[nextFreeRow[col]][col] = SIMBOLI[giocatore]

        print(f'Gioca il giocatore {giocatore}')
        printGriglia(griglia)
        if checkWin(griglia, nextFreeRow[col], col, SIMBOLI[giocatore]):
            print(f'{giocatore} ha vinto in {moves} mosse')
            break
        nextFreeRow[col] -= 1
        print()

if __name__ == '__main__':
    main()
