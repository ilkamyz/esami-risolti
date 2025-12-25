from collections import defaultdict
def convertiData(data:str) -> int:
    return int(data[3:5] + data[0:2])
def readZodiaco(filename:str) -> dict:
    zodiac = {}
    with open(filename, 'r') as f:
        for line in f:

            segno, data1, data2, = line.strip().split(',')
            data1 = convertiData(data1)
            data2 = convertiData(data2)
            zodiac[segno] = range(data1, data2 + 1)

    return zodiac
def readSportivi(filename:str) -> dict:
    sportivi = {}
    with open(filename, 'r') as f:
        for line in f:

            nome, goals, _, data = line.strip().split(',')
            sportivi[nome] = (int(goals), convertiData(data))
    
    return sportivi
def getGoalsPerZodiac(sportivi: dict, zodiac: dict) -> dict:
    goalsPerZodiac = defaultdict(int)
    for nome, (goals, data) in sportivi.items():
        for segno, date in zodiac.items():

            if data in date:
                goalsPerZodiac[segno] += goals

    return goalsPerZodiac
    
def main():
    sportivi = readSportivi('sportivi.csv')
    zodiac = readZodiaco('zodiaco.csv')
    goalsPerZodiac = getGoalsPerZodiac(sportivi, zodiac)
    sortedByGoals = sorted(goalsPerZodiac, key = lambda x: goalsPerZodiac[x])
    maxGoals = max(goalsPerZodiac, key = lambda x: goalsPerZodiac[x])
    asterisk = '*'
    
    for segno in sortedByGoals[::-1]:
        print(f'{segno} ({goalsPerZodiac[segno]}) {asterisk * int(50 * (goalsPerZodiac[segno] / goalsPerZodiac[maxGoals]))}')

if __name__ == '__main__':
    main()
        


