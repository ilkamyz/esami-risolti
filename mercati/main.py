'''I Valori restituiti dal codice non coincidono con l'esempio fornito, tuttavia non ho trovati errori di logica
nel codice che ho scritto, non ho idea della causa di queste incongruenze'''
from statistics import mean
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