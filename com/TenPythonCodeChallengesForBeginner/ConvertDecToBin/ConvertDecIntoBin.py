# This function converts decimal number to binary. Decimal number must be less than or equal to 1024

def convert_dec_to_bin(number):
    if number > 1024:
        raise ValueError('Please only enter decimal number less than or equal to 1024!')
    binary = bin(number)
    return binary


# convert_dec_to_bin(17)

if __name__ == '__main__':
    deicimal_to_convert = 1024
    print(f"Binary is :{convert_dec_to_bin(deicimal_to_convert)[2:]}")
