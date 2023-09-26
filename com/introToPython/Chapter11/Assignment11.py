import time
try:
    counter = 1
    while (counter >= 1):
        number = 2.0 ** counter
        counter = counter + 0.001
        # time.sleep(1)
except (OverflowError, KeyboardInterrupt):
    print('When this exception, the value of the number is: ' + str(number))
