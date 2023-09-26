numberOfNumbers = int(input('Please enter how many numbers you want to average? '))
sum = 0
for count in range(numberOfNumbers):
# for count in range(numberOfNumbers, 0, -1):
    sum += float(input('Please enter your ' + str(count + 1) + ' numbers: '))

# average = float(numbers / numberOfNumbers)
# print('The average is: ' + str(average))
average = sum / numberOfNumbers
print('The average is: ' + str(average))
