import csv
from statistics import mean
def readComponenti(filename: str) -> dict:
    componenti = {}
    #read componenti.csv file
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            
            for line in reader:
                componenti[line['id']] = (line['developer'], line['component'], line['module'], line['language'], line['version'], float(line['size_kb']))
        
        return componenti
    
    except OSError:
        print('Impossibile aprire il file')

def readRichieste(filename: str) -> list[tuple]:
    try:
        with open(filename, 'r') as f:
            richieste = []

            for line in f:
                richiesta, nome = line.strip().split(':')
                richieste.append((richiesta, nome))

        return richieste
    except OSError:
        print('impossibile aprire il file')

def main():
    printsDevelopers = []
    printsLanguages = []
    componenti = readComponenti('componenti.csv')
    richieste = readRichieste('richieste.txt')
    components = []

    for richiesta, nome in richieste:
        found = False
        count = 0
        sizes = []
        prevDeveloper = ''
        prevComponent = ''

        if richiesta == 'd':

            printsDevelopers.append(f'Componenti sviluppati da {nome}:')
            for id, (developer, component, module, language, version, size) in componenti.items():
                if developer == nome:
                    if component == prevComponent or prevComponent == '':
                        found = True
                        count += 1
                        sizes.append(size)
                        prevComponent = component
                    else:
                        printsDevelopers.append(f'- {version}: {prevComponent}, {sum(sizes):.2f}  KB')
                        printsDevelopers.append(f'{' ' * 8}{count} Moduli, in media: {mean(sizes):.2f} KB')
                        count = 1
                        sizes = [size]
                        prevComponent = component

            if found:
                printsDevelopers.append(f'- {version}: {prevComponent}, {sum(sizes):.2f}  KB')
                printsDevelopers.append(f'{' ' * 8}{count} Moduli, in media: {mean(sizes):.2f} KB')
            else:
                printsDevelopers.append('Sviluppatore non presente nella libreria')
    
        else:
            
            for id, (developer, component, module, language, version, size) in componenti.items():
                if language == nome:
                    found = True
                    if developer != prevDeveloper:
                        components.append((developer, version, component, language))
                        prevDeveloper = developer


            if not found:
                printsLanguages.append(f'Componenti sviluppati interamente in {nome}:')
                printsLanguages.append('Linguaggio non presente nella libreria')
    
    
    for prnt in printsDevelopers:
        print(prnt)
    prevLang = ''
    for developer0, version0, component0, language0 in components:
        warn = False
        if language0 != prevLang:
            printsLanguages.append(f'Componenti sviluppati interamente in {language0}:')
        for id, (developer, component, module, language, version, size) in componenti.items():
            if component0 == component and language != language0:
                warn = True
                printsLanguages.append(f'Attenzione: nessun componente è scritto interamente in {language0} solo moduli sparsi')
        if not warn:
            printsLanguages.append(f'- {developer0}, {component0}, {version0}')
        prevLang = language0
            
            
                

    for prnt in printsLanguages:
        print(prnt)

if __name__ == '__main__':
    main()



            