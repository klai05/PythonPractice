# numbers = 0
summation = 0
count = 0
while True:
    numbers = float(input('Please enter your number. When you finish, please enter -1 to exit this program: '))
    if numbers == -1:
        break
    summation += numbers
    count += 1

print('The sum is', summation)
print('The average is', summation / count)

# total = 0.0
# count = 0
# average = 0.0
# numtoadd = 0
#
# while ( numtoadd != -1):
#    total = total + numtoadd;
#    count = count + 1;
#    numtoadd = int(input("Enter a number: "))
#
# if (count != 0):
#    average = total / count
#
# print("Sum = ",total);
# print("Average = ",average)
