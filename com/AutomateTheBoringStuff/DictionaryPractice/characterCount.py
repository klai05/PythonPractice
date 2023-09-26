import pprint

message = 'Weather is nice today'
count = {}


for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print(count)
pprint.pprint(count)
pprint.pprint('Hello')
# formattedString = pprint.pformat(count)
# print(formattedString)