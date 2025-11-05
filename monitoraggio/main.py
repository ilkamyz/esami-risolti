import statistics
def getSensorDataMean(sensor):
    values = []
    with open (sensor, 'r')as f:
        next(f)
        values = [float(line.strip().split(',')[2]) for line in f]
        return sum(values) / len(values)
        
def main():
    with open('sensori.txt', 'r') as f:
        temp = [line.strip() for line in f]
        sensoriMtx = [el.split(' ') for el in temp]
    sensori = {}
    for row in sensoriMtx:
        sensori[row[0]] = [row[1], row[2]]
    
    sensorsNotFound = []
    for key, value in sensori.items():
        fileName = key + '.csv'
        try:
            sensori[key].append(getSensorDataMean(fileName))
        except FileNotFoundError:
            sensorsNotFound.append(key)
    for sensor in sensorsNotFound:
        print(f'{sensor} data not found')
        sensori.pop(sensor)
    for key, value in sensori.items():
        print(f'{key}: {value[0]} - {value[1]} - {value[2]} ')
if __name__ == '__main__':
    main()
