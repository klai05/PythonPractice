words = {}
value = input("Please enter a word (or -999 to quit): ")
while (value != '-999'):
    if value in words:
        words[value] = words[value] + 1
    else:
        words[value] = 1

    value = input("Please enter a word (or -999 to quit): ")

# for current_key in words.keys():
#     print(current_key, '\t', words[current_key])
# print(words)

# print("The ordered list of words are:")
# my_keys = list(words.keys())
# my_keys.sort()
# for current_key in my_keys:
#     print(current_key, '\t', words[current_key])

print()
print("Ordered by number of times entered:")
temp_list = []
# Select a key in the dictionary
for current_key in words.keys():
    # determine the number of words in the sorted list
    # list_length = len(temp_list)
    # print(list_length)

    # start looking at position 0
    placeholder = 0

    # As long as there are still items in the list
    while placeholder < len(temp_list):

        # Get the word in the sorted list
        key_to_compare = temp_list[placeholder]

        # Determine if this word has been entered
        # more times than the current word
        if words[key_to_compare] > words[current_key]:
            break

        # It wasn't, so let's look at the next word
        # in the sorted list
        placeholder = placeholder + 1

    # We found the location in the sorted list for
    # this word, insert it
    temp_list.insert(placeholder, current_key)

for current_key in temp_list:
    print(current_key, '\t', words[current_key])
