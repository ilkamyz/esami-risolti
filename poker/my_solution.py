from random import shuffle, randint
VALORI = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SEMI = ['C', 'Q', 'F', 'P']
VALORI_NETTI = {
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14,
}
def sortMano(mano):
    global VALORI_NETTI
    return mano.sort(key = lambda x: VALORI_NETTI[x[0]])
def generaMazzo(VALORI, SEMI):
    mazzo = []
    for valore in VALORI:
        for seme in SEMI:
            carta = {
                'valore': valore,
                'seme' : seme
            }
            mazzo.append(carta)
    return mazzo
    
def scriviMazzo(filename, mazzo):
    shuffle(mazzo)
    with open(filename, 'w') as f:
        for carta in mazzo:
            f.write(f'{carta['valore']} {carta['seme']}\n')
def generaMani(mazzo: list) -> list:
    mani = []
    while len(mazzo) > 5:
        mano =[]
        for carta in mazzo[:5]:
            mano.append((carta['valore'], carta['seme']))
        mani.append(mano)
        mazzo = mazzo[5:]
    return mani

    
def main():
    mazzo = generaMazzo(VALORI, SEMI)
    scriviMazzo('mazzo.txt', mazzo)
    mani = generaMani(mazzo)
    for mano in mani:
        print(scalaReale(mano))



def scalaReale(mano: list[tuple]) -> bool:
    global VALORI_NETTI
    sortMano(mano)
    valore0, seme0 = mano[0]
    valorePrec = valore0
    for valore, seme in mano[1:]:
        if seme0 != seme:
            return False
        if VALORI_NETTI[valore] - VALORI_NETTI[valorePrec] != 1:
            return False
        valorePrec = valore
    return True
def Poker(mano):
    sortMano(mano)
    valore0 = valoreprec, _ = mano[0]
    valore1, _ = mano[1]

    for valore, _ in mano[1:4]:
        if valore == valoreprec:
            count += 1
        valoreprec = valore
    if count == 4:
        return True
    
    count = 0
    valoreprec = valore1
    for valore, _ in mano[2:]:
        if valoreprec == valore:
            count += 1
        valoreprec = valore
    if count == 4:
        return True
    return False




if __name__ == '__main__':
    main()


    
    

        
        
