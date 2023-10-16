'''
Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.

The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.
'''


def compute(first_number: int, math_operator: str, second_number: int):
    from operator import add, sub, mul, truediv

    mapping = {'+': add, '-': sub, '/': truediv, '.': mul}
    try:
        f = mapping[math_operator]
    except KeyError:
        raise Exception('Please enter a valid operator and try again')
    else:
        answer = f(first_number, second_number)
        return answer


if __name__ == "__main__":
    print(compute(2, '.', 6))
