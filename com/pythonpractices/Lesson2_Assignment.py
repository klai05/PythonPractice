# userInput = input('Please enter two 1-digit Integer numbers separated by comma: ')
# number1 =  int(userInput[0:1])
# number2 = int(userInput[2:])
# print('Number 1 is: ' + str(number1))
# print('Number 2 is: ' + str(number2))

userInput = input('Please enter a phrase: ')
startPoint = input('Please enter a start point from 0: ')
endPoint = input('Please enter an end point: ')
Sliced = userInput[int(startPoint) : int(endPoint) + 1]
print(Sliced)

SlicedEncoded = str.encode(Sliced)
print(SlicedEncoded)