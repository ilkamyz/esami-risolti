from collections import defaultdict
def main():
    with open('ordini.csv', 'r') as f:
        ordini = [line.strip().split(',') for line in f]
        ordini.pop(0)
    print(ordini)
    numeroOrdini = defaultdict(int)
    for row in ordini:
        numeroOrdini[row[4]] += int(row[2])
    print('Numero di ordini di ciascun cliente: ')
    listaclienti = []
    for nome, numero in numeroOrdini.items():
        listaclienti.append(f' - {nome}: {numero}')
    listaclienti.sort()
    for e in listaclienti:
        print(e)

    spesaTotale = defaultdict(int)
    for row in ordini:
        spesaTotale[row[4]] += round(float(row[3]) * int(row[2]), 2)

    print(f'Cliente con la spesa maggiore:\n - {max(spesaTotale.keys(),key = lambda x: spesaTotale[x])} : {spesaTotale[max(spesaTotale.keys(),key = lambda x: spesaTotale[x])]} ')

    numeroAcquisti = defaultdict(int)
    for row in ordini:
        numeroAcquisti[row[1]] += int(row[2])
    leastBought = min(numeroAcquisti.keys(), key= lambda x: numeroAcquisti[x])
    print(f'Prodotto meno venduto:\n - {leastBought}, acquistato {numeroAcquisti[leastBought]} volte')
if __name__ =='__main__':
    main()
None