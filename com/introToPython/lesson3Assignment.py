

try:
    windSpeed = int(input('Please enter a windspeed: '))
    if windSpeed >= 0 and windSpeed < 74:
        print('This is not hurricane wind speed')
    elif windSpeed > 73 and windSpeed < 96:
        print('This is category 1 hurricane')
    elif windSpeed > 95 and windSpeed < 111:
        print('This is category 2 hurricane')
    elif windSpeed > 110 and windSpeed < 131:
        print('This is category 3 hurricane')
    elif windSpeed > 130 and windSpeed < 156:
        print('This is cateory 4 hurricane')
    elif windSpeed > 155:
        print('This is cateory 5 hurricane')
except ValueError:
    print('Please enter a valid windspeed in interger.')