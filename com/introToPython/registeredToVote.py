# age = int(input("How old are you? "))
# registered = input("Are you registered? (y/n) ")
#
# if age >= 18:
#     if registered == "y":
#         print("You are ready to vote!")
#     else:
#         print('You are old enough but not registered to vote')
# else:
#     print("You are not ready to vote.")



age = int(input("How old are you? "))
registered = input("Are you registered? (y/n) ")

if age >= 18 and registered == "y":
    print("You are ready to vote!")
else:
    print("You are not ready to vote.")