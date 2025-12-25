def readCalendario(filename: str) -> dict:
    calendario = {}
    with open(filename, 'r') as f:

        for i, line in enumerate(f):
            calendario[line.strip()] = i + 1

    return calendario
def readOccupazione(filename: str, calendario: dict) -> dict:
    clienti = {}
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            group = line.strip().split(';')

            try:
                id_cliente, arrivo, partenza,tipo_abitazione, numero_adulti, numero_bambini, elettricità = group

                if elettricità.lower() == 'no':
                    el_float = False
                else:
                    el_float = True

                clienti[id_cliente] = calendario[arrivo], calendario[partenza], tipo_abitazione, int(numero_adulti) + int(numero_bambini), el_float

            except:
                next(f)
    return clienti

def readPrezzi(filename: str, calendario: dict) -> dict:
    prezzi = {}
    ranges = {}
    idx = 1
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            
            try:
                group = line.strip().split(';') 
                print(group)
                dal, al, prezzo_tenda, prezzo_camper, prezzo_persone, prezzo_elettricita, _ = group
                prezzi[idx] = calendario[dal], calendario[al], float(prezzo_tenda), float(prezzo_camper), float(prezzo_persone), float(prezzo_elettricita)
                ranges[idx] = range(calendario[dal], calendario[al] + 1)
                idx += 1
            except:
                next(f)
    return prezzi, ranges
def getPrices(id_cliente, prezzi, occupazione, ranges):
    prezzo = 0
    arrivo, partenza, tipo_abitazione, numero_persone, el_float = occupazione[id_cliente]
    notti = partenza - arrivo
    for day in range(arrivo, partenza):

        for idx, rnge in ranges.items():
            if day in rnge:
                _, _, prezzo_tenda, prezzo_camper, prezzo_persone, prezzo_elettricita = prezzi[idx]

                if tipo_abitazione == 'camper':
                    prezzo += prezzo_camper
                else:
                    prezzo += prezzo_tenda

                if el_float:
                    prezzo += prezzo_elettricita
                
                prezzo += prezzo_persone * numero_persone
    
    return prezzo, notti

def main():
    calendario = readCalendario('calendario.txt')
    occupazione = readOccupazione('occupazione.txt', calendario)
    prezzi, ranges = readPrezzi('prezzi.txt', calendario)
    print(ranges, prezzi, occupazione)
    for client_id in occupazione.keys():
        prezzo, notti = getPrices(client_id, prezzi, occupazione, ranges)
        print(client_id, prezzo, notti)

if __name__ == '__main__':
    main()