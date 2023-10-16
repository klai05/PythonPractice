def return_cc_number(cc_num: str):
    if len(cc_num) == 16:
        masked = cc_num[0:len(cc_num) - 4]
        print("*" * len(masked) + cc_num[-4:])
    else:
        print('Credit Card Number should be 16 digit. Please try again later!')


CC_number = input('Please enter your credit card number: ')
return_cc_number(CC_number)
