grade = {}
# name = ''
while True:
    name = input('Please enter student name. Enter -999 to exit: ')
    if name == '-999':
        break
    score = input('Please enter a score: ')
    # grade.update({name:score})
    grade |= {name:score}
print(grade)


while True:
    name_to_search = input('Please enter student name to search. Enter -999 to exit: ')
    if name_to_search == '-999':
        break
    print('Score of this ' + name_to_search + ' is: ' + grade.get(name_to_search, "Student Not Found"))
