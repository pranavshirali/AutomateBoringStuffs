birthday = {}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        print(birthday.keys())
        print(birthday.values())
        break

    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print('I do not have the birthday info. of ' + name)
        print('What is their birthday?')
        bday = input()
        birthday[name] = bday
        print('Birthday has been updated.')