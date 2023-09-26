# def change_value(value):
#     """This function changes the value passed in to 1"""
#     print("Inside, value is:", value)
#     value = 1
#     print("Inside, value is changed to:", value)
#
# number = 5
# print("Outside, number is:", number)
# change_value(number)
# print("Outside, number is now:", number)


# def change_value(value):
#     """This function changes the value passed in to 1"""
#     print("Inside, value is:", value)
#     value = 1
#     print("Inside, value is changed to:", value)
#
# number = 5
# value = 0
# print("Outside, number is:", number)
# change_value(number)
# print("Outside, number is now:", change_value(number))


def change_number():
    """This function changes the value passed in to 1 (global)"""
    global number
    number = 1

number = 6
print ("Outside, number is:", number)
change_number()
print ("Outside, number is now:", number)