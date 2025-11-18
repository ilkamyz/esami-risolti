def readSportelli(filename):
    sportelli = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                tasks = []
                group = line.strip().split(',')

                orario_chiusura = int(group[-1])
                idx = group[0]

                for task in group[1:len(group) - 1]:
                    tasks.append(task)

                sportelli[idx] = [tasks, orario_chiusura, 0]

        return sportelli
    except OSError:
        print('Impossibile aprire il file')

def readClienti(filename: str):
    clienti = {}
    try:
        with open(filename,'r') as f:
            for line in f:
                nome, task, tempo, orario_arrivo = line.strip().split(',')
                clienti[nome] = (task, int(tempo), int(orario_arrivo))
        return clienti
    except OSError: 
        print('Impossibile aprire il file')

def main():
    prints = []
    clienti = readClienti('clienti.txt')
    sportelli = readSportelli('sportelli.txt')

    for nome, (task, tempo, orario_arrivo) in clienti.items():
        servito = False

        for idx, (tasks, orario_chiusura, next_available) in sportelli.items():

            if task in tasks and next_available <= orario_arrivo and orario_arrivo + tempo < orario_chiusura:
                sportelli[idx][2] = orario_arrivo + tempo
                prints.append(f'{nome}, Arrivo: {orario_arrivo}, Uscita: {sportelli[idx][2]}, Sportello: {idx}')
                servito = True
                break

        if not servito:
            prints.append(f'{nome} non può essere servito/a, tutti gli sportelli sono occupati o chiusi')

    for prnt in prints:
        print(prnt)

if __name__ == '__main__':
    main()

