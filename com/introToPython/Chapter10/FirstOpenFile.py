# out_file = open('C:/Users/kevin/Desktop/mydata.txt', 'w')
# out_file = open('mydata.txt', 'a')
# # out_file.write('Hello\t')
# # out_file.write('World')
# out_file.write('\n')
# weekends = ['Sat', 'Sun']
# out_file.writelines(weekends)
# out_file.writelines(weekends)
# out_file.close()

# in_file = open('mydata.txt', 'r')
# # print(in_file.read())
# print(in_file.readlines())
# # print(in_file.readline())
# # print(in_file.readline())
# # print(in_file.readline())
# # print(in_file.readline())
# in_file.close()


# in_file = open('mydata.txt', 'r+')
# print(in_file.readline())
# # print(in_file.tell())
# in_file.seek(3)
# print(in_file.readline())
# in_file.close()

in_file = open('mydata.txt', 'r+')
print (in_file.readline())
in_file.seek(0)
in_file.write('Hi!')
in_file.seek(0)
print (in_file.readline())
in_file.close()