# letter = 'A'
#
# if letter < 'S':
#     print('Bingo')
# else:
#     print('This is not the case')


# for i in range(0, 5):
#     print(i)


# d = 0
# while d == 10:
#     print(d)

# Let's write a program
# demonstrate working of extending function.

# assign list to values
list_one = ['January', 'February', 'March']

# use the extend method
# list_one.append(['April', 'May', 'June'])
#
# # displaying the list
# print(list_one)

colors = ['blue', 'white']

out_file = open("text.txt", "w")

out_file.write("colours")
out_file.writelines(colors)

out_file.close()