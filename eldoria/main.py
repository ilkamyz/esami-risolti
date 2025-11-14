def leggiCreatureEIncatesimi(filename1 : str, filename2: str) -> dict:
    creature = {}
    with open(filename1, 'r') as f:
        for line in f:
            idx, nome, tipo, potenza = line.strip().split(',')
            incantesimi = {}
            creature[idx] = (nome, tipo, potenza, incantesimi)
    with open(filename2, 'r') as f:
        #l'ID dell'incantesimo, il nome, il tipo, l'ID della creatura e la potenza dell'incantesimo
        for line in f:
            i_id, i_nome, i_tipo, idx, i_potenza = line.strip().split(',')
            if i_tipo != 'supporto' and idx in creature:
                _, _, _, incantesimi = creature[idx]
                incantesimi[i_id] = (i_nome, i_tipo, i_potenza)
    return creature

def stampaIncantesimi(incantesimi):

    sorted_idx = sorted(
        incantesimi.keys(),
        key=lambda x: (incantesimi[x][1], -int(incantesimi[x][2]), incantesimi[x][0])
    )

    attacchi = []
    difese = []

    for idx in sorted_idx:
        nome, tipo, potenza = incantesimi[idx]
        if tipo == "attacco":
            attacchi.append((nome, potenza))
        else: 
            difese.append((nome, potenza))

    print("  Attacco:")
    if not attacchi:
        print("    Nessun incantesimo")
    else:
        for nome, potenza in attacchi:
            print(f"    {nome}:{potenza}")

    print("  Difesa:")
    if not difese:
        print("    Nessun incantesimo")
    else:
        for nome, potenza in difese:
            print(f"    {nome}:{potenza}")


def main():
    creature = leggiCreatureEIncatesimi('creature.csv','incantesimi.csv')
    for _, (nome, tipo, potenza, incantesimi) in sorted(creature.items(), key = lambda x: (x[1][1], x[1][0])):
        print(f'{nome} ({tipo}, potenza : {potenza})')
        stampaIncantesimi(incantesimi)

if __name__ == '__main__':
    main()