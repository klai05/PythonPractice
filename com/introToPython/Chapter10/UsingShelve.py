import shelve
db_file = shelve.open('letters.txt', 'c')
db_file['vowels'] = ['a','e','i','o','u']
db_file['end'] = ['x','y','z']
db_file.close()

print(db_file['vowels'])
print(db_file['end'])
# import shelve
db_file = shelve.open('letters.txt', 'c')
print(list(db_file.keys()))
print('Original containing vowels:', 'vowels' in db_file)
del db_file['vowels']
print('After deleting vowels:', 'vowels' in db_file)
print(list(db_file.keys()))
db_file.close()