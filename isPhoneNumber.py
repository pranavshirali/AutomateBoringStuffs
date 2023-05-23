# def isPhoneNumber(number):
#     if len(number) != 10:
#         return False
#     for i in range(0, 4):
#         if not number.isdecimal():
#             return False
#     for i in range(5, 9):
#         if not number.isdecimal():
#             return False
        
#     return True
        

# print('Write a message to check for phone number in it...')
# message = input()
# for i in range(len(message)):
#     chuck = message[i:i+10]
#     if isPhoneNumber(chuck):
#         print(f'Phone number found {chuck}')

# print('Done')


#Pattern matching using Regular Expression(Regex)
import re

phonecheck = re.compile(r'(\+\d\d)(\d\d\d\d\d\s\d\d\d\d\d)')
match_object = phonecheck.search('Phone number is: +9180887 23275')
print('Contry code: ',match_object.group(1))
print('Phone number: ',match_object.group(2))
