first_dict = {'Jan':'01', 'Feb':'02'}
first_dict['Mar'] = '04'
first_dict['Jan'] = '04'
print(type(first_dict['Jan']))
print('Jan is: ' + first_dict['Jan'])
print(type(first_dict))
print('First Dict is: ' + str(first_dict))
print(first_dict.keys())
print(first_dict.values())
print(first_dict.items())
print('Feb' in first_dict)