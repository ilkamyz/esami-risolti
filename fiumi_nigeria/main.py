#I FILE DI INPUT SONO ROTTI
from statistics import mean
def getRiverData(filename:str):
    with open(filename, 'r') as file:
        f = file.readlines()
        humidities, windspeeds, temperatures, rainfalls = [], [], [], []
        group = f[1].strip().split(' ') 
        _, station, lat, long, _ = group
        for line in f[4:]:
            group = line.strip().split('\t')
            Humidity, _, Windspeed, Rainfall, _, _, Tearth, _ = group
            
            humidities.append(float(Humidity))
            windspeeds.append(float(Windspeed))
            temperatures.append(float(Tearth))
            rainfalls.append(float(Rainfall))
    
    return mean(humidities), max(windspeeds), mean(temperatures), max(temperatures), rainfalls, station, lat, long
def getAverageRainfalls(global_rainfalls: list[list]):
    average_rainfalls = []
    for j in range(len(global_rainfalls[0])):
        rainfalls = []
        for i in range(len(global_rainfalls)):
            rainfalls.append(global_rainfalls[i][j])
        average_rainfalls.append(mean(rainfalls))
    
    return average_rainfalls
def main():
    with open('rivers.txt','r') as f:
        global_rainfalls = []
        for line in f:
            try:
                filename = line.strip() + '.dat'
                avg_humidity, max_windspeed, avg_temperature, max_temperature, rainfalls, station, lat, long = getRiverData(filename)
                print(f'{line.strip().upper():<11}measured in {station} (lat: {lat}, long: {long})\nAvg. Humidity: {avg_humidity:.2f}% \nMax wind speed: {max_windspeed:.2f} m/s\nAverage Temperature: {avg_temperature:.2f} C (Max: {max_temperature} C)')
                global_rainfalls.append(rainfalls)
            except:
                print(f'{line.strip} file not found')

    average_rainfalls = getAverageRainfalls(global_rainfalls)
    print()
    print('Average weekly rainfalls (mm)')
    for i, average in enumerate(average_rainfalls):
        print(f'{average:.2f}', end=' ')
        if i % 7 == 6 and i!= 0:
            print('\n')
    print(f'\nYearly average: {mean(average_rainfalls):.2f} mm')
if __name__ == '__main__':
    main()

