def readListino(filename: str) -> dict:
    listino = {}
    with open(filename, 'r') as f:
        for line in f:
            group = line.strip().split(' ')
            idx = group[0]
            offerta = group[-1]
            city = ' '.join(group[1:-1])
        listino[idx] = [city, offerta]
    return listino
def readDistanze(filename: str) -> dict:
    distanze = {}
    with open(filename, 'r') as f:
        for line in f:
            group = line.strip().split(':')
            start, destination = group[0].split('-')
            
    return distanze

def calcolaDistanzeDaLA(listino: dict, distanze: dict):
    for idx, (nome, offerta) in listino:
        distanza_tot = 0



def main():
    listino = readListino('listino.txt')
    distanze = readDistanze('distanze.txt')
    distanze_da_losangeles = {}

    