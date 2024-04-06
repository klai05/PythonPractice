import re
message = 'Call me 416-666-2311 tomorrow, or at 416-090-0190'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message)
print(mo)
