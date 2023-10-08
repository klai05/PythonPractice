odds = {1:'one', 3:'three', 5:'five'}
evens = {2:'two', 4:'four', 6:'six'}

print(odds.items())

odds.update({1:"111"})

print(odds.get(1))
# odds.clear()
#
# print("After clearing odds:")
# print(odds)
# print(evens)
# del evens
# print("After clearing evens:")
# print(evens)