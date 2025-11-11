'''I Valori restituiti dal codice non coincidono con l'esempio fornito, tuttavia non ho trovati errori di logica
nel codice che ho scritto, non ho idea della causa di queste incongruenze
comunque chatgpt dice questo:

    Ho caricato ESATTAMENTE i due file che mi hai fornito e ho calcolato i rendimenti esattamente come dice il testo:

    primo valore di chiusura del mese

    ultimo valore di chiusura del mese

    rendimento = (last − first) / firstù

    Consumer Defensive: 2.32%
    Financial Services: 10.51%
    Technology: 5.09%
    Industrials: 8.55%
    Utilities: 4.33%
    Energy: 9.04%
    Healthcare: 2.02%
    Communication Services: 5.53%
    Real Estate: 6.42%
    Consumer Cyclical: 6.93%
    Basic Materials: -2.91%


    ✅ Conclusione

    Il tuo codice è corretto..

    ❗ Perché non coincidono con l’output dell’esempio dell’esercizio?

    Perché i file che hai tu NON sono gli stessi usati nell’esempio nel testo.

anche se mi sembra strano..., 
Nota personale x ripasso: comunque se funziona o no il calcolo in senso stretto non fa niente,la cosa da ricordare per questo codice è come estrarre soltanto i dati
significativi da un grande dataset, come dividere in maniera efficace in funzioni e come organizzare i dati estratti in dizionari funzionali'''
import csv
def getRevenuePerSector(sector, companies, trades):
    sectorCompanies = set()
    returns = []
    for symbol, sector0 in companies.items():
        if sector0 == sector:
            sectorCompanies.add(symbol)
    
    for company in iter(sectorCompanies):
        firstClose = None
        lastClose = None

        for idx, (_, symbol, close) in trades.items():
            if company == symbol:
                firstClose = close
                break

        for idx in sorted(trades.keys(), reverse=True):
            _, symbol, close = trades[idx]
            if company == symbol:
                lastClose = close
                break

        if firstClose is not None and lastClose is not None and firstClose != 0:
            returns.append((lastClose - firstClose) / firstClose)

    return sum(returns) / len(returns)


def main():
    companies = {}
    with open('sp500_companies.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        for row in rows[1:]:
            Exchange,Symbol,Shortname,Longname,Sector,Industry,Currentprice,Marketcap,Ebitda,Revenuegrowth,City,State,Country,Fulltimeemployees,Weight = row
            companies[Symbol] = Sector
    sectors = set(companies.values())
    idx = 1
    trades = {}
    with open('sp500_historical.csv','r') as f:
        next(f)
        for line in f:
            group = line.strip().split(',')
            Date,Symbol,Close,High,Low,Open,Volume = group
            trades[idx] = (Date, Symbol, float(Close))
            idx += 1 
    for sector in sectors:
        print(f'Sector: {sector}, Average return: {getRevenuePerSector(sector,companies, trades)*100:.2f}%')
if __name__ == '__main__':
    main()