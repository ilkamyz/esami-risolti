import statistics
def getInts(string):
    newList = []
    l = string.strip().split(',')
    for e in l:
        newList.append(int(e))
    return newList
    
def main():

    skateboarders = {}
    with open('skateboardersLong.txt', 'r') as f:
        skmatrix = [line.strip().split(';') for line in f]
    for row in skmatrix:
        skateboarders[row[0]] = [row[1], statistics.mean(getInts(row[2]))]

    cities = {}
    with open('skateparksLong.txt', 'r') as f:
        cMatrix = [line.strip().split(';') for line in f]
    for row in cMatrix:
        cities[row[0]] = [row[1], row[2]]
    
    #aggiungi indice di sfida
    skateboardersToRemove = []
    for key, val in skateboarders.items():
        try:
            val.append(int(cities[val[0]][1]) * val[1])
        except KeyError:
            skateboardersToRemove.append(key)
    for e in skateboardersToRemove:
        skateboarders.pop(e)
    count = 0
    #UTILE!!
    sortedSkatedboarders = dict(sorted(skateboarders.items(), key = lambda x: x[1][2], reverse= True)) #UTILE!!
    #!!
    for key, val in sortedSkatedboarders.items():
        count += 1
        print(f'{count}. {key} - Indice di sfida: {val[2]:.2f} - Punteggio Medio: {val[1]:.2f}\n    {val[0]} - {cities[val[0]][0]} - (Indice di difficoltà: {cities[val[0]][1]})')
if __name__ == '__main__':
    main()   
