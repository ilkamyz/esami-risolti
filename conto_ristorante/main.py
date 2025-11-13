def main():
    ordine = {}
    with open ('ordine.txt', 'r') as f:
        for line in f:
            idx, quantity = line.strip().split(',')
            ordine[idx] = [int(quantity)]
    with open('menu.txt', 'r') as f:
        for line in f:
            (idx, nome, prezzo, iva) = line.strip().split(',')
            iva, prezzo = float(iva), float(prezzo)
            if idx in ordine.keys():
                ordine[idx] += [nome, prezzo, iva]
    print('RICEVUTA')
    totale, totaleIva = 0, 0
    for _, (quantity, nome, prezzo, iva) in ordine.items():
        print(f' {quantity}  {nome:<22} {quantity * prezzo:>5.2f} IVA {iva:>4.2f}%')
        totale += quantity * prezzo
        totaleIva += quantity * prezzo * iva/100
    print(f'Totale: {totale:.2f}€')
    print(f'Di cui IVA: {totaleIva:.2f}€')

if __name__ == '__main__':
    main()