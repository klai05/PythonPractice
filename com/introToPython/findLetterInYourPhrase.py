phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
length = len(phrase)

for index in range(0, length):
         if phrase [index] == letter:
                   print ("The letter first appears at index: ", index)
                   break
else:
         print ("Your letter wasn't found")