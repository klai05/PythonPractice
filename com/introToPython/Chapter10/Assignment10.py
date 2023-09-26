import shelve

db_file = shelve.open('grades', 'c')
db_file.clear()

while True:
    name = input('Please enter student name. Enter -999 to exit: ')
    if name == '-999':
        break
    score = input('Please enter a score: ')

    db_file[name] = score

print('db_file values are: ' + str(dict(db_file)))


while True:
    name_to_search = input('Please enter student name to search. Enter -999 to exit: ')
    if name_to_search == '-999':
        break
    # print('Score of this ' + name_to_search + ' is: ' + grade.get(name_to_search, "Student Not Found"))
    if name_to_search in db_file:
        print(name_to_search + "'s score is: " + str(db_file[name_to_search]))
    else:
        print('Your Search Is Not Found Unfortunately. Please try again.')

db_file.close()