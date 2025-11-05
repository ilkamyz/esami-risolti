def safe_get(m, r, c, default=0):
    """Return m[r][c] if within bounds, else default."""
    if 0 <= r < len(m) and 0 <= c < len(m[r]):
        return m[r][c]
    return default

def getScore(row: int, col: int, mappa: list) -> int:
    center = safe_get(mappa, row, col, 0)
    score = 0
    for i in (-1, 0, 1):

        score += center - safe_get(mappa, row - 1, col + i, 0)
        score += center - safe_get(mappa, row + 1, col + i, 0)

    score += (center - safe_get(mappa, row, col - 1, 0))
    score += (center - safe_get(mappa, row, col + 1, 0))
    return score

def main():
    with open('mappa.txt', 'r') as f:
        mappa = [list(line.strip()) for line in f]
    # convert chars to ints
    for r in range(len(mappa)):
        mappa[r] = [int(x) for x in mappa[r]]

    scores = {}
    for row in range(len(mappa)):
        for col in range(len(mappa[row])):
            scores[(col, row)] = getScore(row, col, mappa)
    order = sorted(scores, key= lambda x: -scores[x])
    for i, key in enumerate(order):
        print(f'{i + 1:2d}. {key} : Valore =  {scores[key]}')
if __name__ == '__main__':
    main()
