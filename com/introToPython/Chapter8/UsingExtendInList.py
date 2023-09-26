my_list = []
# my_list.append(10)
# my_list.append('ten')
my_list.extend([20, 'twenty'])
my_list = my_list + ['YoYo', 'HeyHey']
my_list.insert(1, "Hey Kev")
my_list.remove('HeyHey')
print(my_list)
print('Length of this list is: ' + str(len(my_list)))