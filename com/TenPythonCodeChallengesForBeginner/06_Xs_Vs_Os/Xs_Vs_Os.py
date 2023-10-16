'''
If the count of Xs and Os are equal, then the function should return True.
If the count isn’t the same, it should return False.
If there are no Xs or Os in the string, it should also return True because 0 equals 0.
The string can contain any type and number of characters.
'''

def are_Xs_equalto_Os(string_to_evaluate: str):
    X_count = 0
    O_count = 0

    for string in string_to_evaluate:
        if string == 'X':
            X_count += 1
        if string == 'O':
            O_count += 1

    if X_count == O_count:
        return True

    else:
        return False


if __name__ == "__main__":
    import random, string

    # To Generate Random String with 10 Chars
    random_string = ''.join(random.choice(string.printable) for i in range(10))
    print('Random String is: ' + random_string)
    print(are_Xs_equalto_Os(random_string))
