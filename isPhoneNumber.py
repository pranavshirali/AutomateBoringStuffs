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

phonecheck = re.compile(r'(\+\d\d)?\s(\d[10])')
match_object = phonecheck.search('Phone number is: +91 80887 23275 and Tell number: +99 8722823570')
print('Contry code: ',match_object.group(1))
print('Phone number: ',match_object.group(2))


print('Enter a Gmail: ',end='')
gmail_input = input()
gmailcheck = re.compile(r'(\w+)\@(gmail.com$)')
Match_Object = gmailcheck.search(gmail_input)
if Match_Object:
    print('valid gmail')
else:
    print('Invalid gmail')