from collections import defaultdict
def main():
    avvistamenti = {}
    id = 1
    with open('ufo_sightings.csv', 'r') as f:
        for line in f:
            line = line.strip().split(',')
            avvistamenti[id] = (line[2], line[3], int(line[4]), line[5])#paese, forma, durata, desc
            id += 1                                 

    counter = defaultdict(int)
    for id, (paese, forma, durata, desc) in avvistamenti.items():
        counter[paese] += 1
    
    paeseMax = max(counter.keys(), key= lambda x: counter[x])
    print(f'il paese con il maggior numero di avvistamenti è {paeseMax}')

    maxLength = max(avvistamenti.keys(), key= lambda x: avvistamenti[x][2])
    paese1, forma, durata, desc = avvistamenti[maxLength]
    print(f"Avvistamento di durata più lunga: {desc} (Forma: {forma}, Durata: {durata})")
if __name__ == '__main__':
    main()



