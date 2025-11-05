
with open('offerte.txt', 'r') as f:
    elements = [line.strip() for line in f]
    matrix = [el.split(',') for el in elements]

from collections import defaultdict

totalspent = defaultdict(int)
for row in range(len(matrix)):
    for col in range(1, len(matrix[row])):
        if col % 2 == 0:
            totalspent[matrix[row][0]] += int(matrix[row][col])
biggestSpender = max(totalspent.keys(), key= lambda x: totalspent[x])


itemPrices = defaultdict(dict)

for row in matrix:
    for col in range(1, len(row) - 1):
        if col % 2 != 0:
            itemPrices[row[col]][row[0]] = int(row[col+1])
keysToRemove = []
ties : defaultdict[str, list[int]] = defaultdict(list)
for key, value in itemPrices.items():
    frequency = defaultdict(int)
    for name, price in value.items():
       
        frequency[price] +=1
    for price2, freq in frequency.items():
        if freq != 1:
            keysToRemove.append(key)
            ties[key].append(price)
            for name, price in value.items():
                if price == price2:
                    ties[key].append(name)

for key in keysToRemove:
    itemPrices.pop(key)

            




wins = defaultdict(dict)
for key, value in itemPrices.items():
    bestBuyer = max(value.keys(), key= lambda x: value[x])
    wins[bestBuyer][key] = itemPrices[key][bestBuyer]

for name, winInfo in wins.items():
    print(f'{name}: ',end='')
    for key, value in winInfo.items():
        print(f'{key.lstrip()} {value}, ',end='')
    print(f'Totale: {sum(iter(winInfo.values()))}')
for key, value in ties.items():
    print(f'Stessa offerta per {key.lstrip()} ({value[0]}) da parte di: {', '.join(value[1:])}')
print(f"\nl'acquirente che ha speso di più è {biggestSpender}" )