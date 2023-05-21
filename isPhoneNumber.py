def isPhoneNumber(number):
    if len(number) != 10:
        return False
    for i in range(0, 4):
        if not number.isdecimal():
            return False
    for i in range(5, 9):
        if not number.isdecimal():
            return False
        
    return True
        

print('Write a message to check for phone number in it...')
message = input()
for i in range(len(message)):
    chuck = message[i:i+10]
    if isPhoneNumber(chuck):
        print(f'Phone number found {chuck}')

print('Done')