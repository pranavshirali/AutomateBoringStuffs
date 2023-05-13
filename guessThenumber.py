import random

secertNumber = random.randint(1 , 5)
print('I am thinking of a number between 1 and 20, you have 6 chances')

for takeGuess in range(0 , 5):
    print('Take a guess')
    guess = int(input())

    if guess < secertNumber:
        print('Your guess is too low')
    elif guess > secertNumber:
        print('Your guess is too high')
    else:
        print('Hurray!! You got it correct, secret number was: '+str(secertNumber))
        break
else:
    print('Nope! I was thinking about number:'+str(secertNumber))