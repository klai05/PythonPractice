my_list = []
len(my_list)
while True:
    num = int(input('Please enter a number. To Exit, please enter "-999" to quit : '))

    if (num == -999):
        break

    # my_list = my_list + [num]
    # my_list.extend([num])
    my_list.append(num)
summation = 0
print('Using the numbers:')
for i in range(len(my_list)):
    summation += my_list[i]
    print(my_list[i], end=" ")

average = summation/len(my_list)
print('\nThe average is: ' + str(average))


