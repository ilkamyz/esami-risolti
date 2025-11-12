import csv 
def getMaxLength(output):
    maxLen = max(output.keys(), key = lambda x: len(x))
    return len(maxLen) + 1
def main():
    publications = {}
    with open('PublicationData.csv','r') as f:
        reader = csv.reader(f, delimiter=';')
        for line in reader:
            (idx, publisher, open_access, year) = line
            open_access = open_access.lower() == 'true'
            publications[idx] = (publisher, open_access, year)

    fees = {}
    with open ('publisher_fees.txt','r') as f:
        for line in f:
            group = line.strip().split(';')
            fees[group[0]] = int(group[1])

    output = {}
    for editor in fees.keys():
        output[editor] = [0, 0]
                        #articles, open source
    for idx, (publisher, open_access, year) in publications.items():
        output[publisher][0] += 1
        if open_access:
            output[publisher][1] += 1
    
    revenue = {}
    for key, (_, a) in output.items():
        revenue[key] = a * fees[key]

    richest = max(revenue.keys(), key = lambda x: revenue[x])

    print('Pubblicazioni per editore: ')
    for editor, (articles, open_source) in output.items():
        try:
            print(f'{editor:<{getMaxLength(output)}}: {articles:>6} articoli,  {(open_source/articles) * 100:>.2f}% open source')
        except ZeroDivisionError:
            print(f'{editor:<{getMaxLength(output)}}: {articles:>6} articoli')
    print()
    print(f'Editore con costo massimo: {richest} ({revenue[richest]})')
if __name__ == '__main__':
    main()