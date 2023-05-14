#Author: Pranav Shirali

import random

def generatAnswer(getAnswer):
    if getAnswer == 1:
        return 'Hi, random number is 1.'
    elif getAnswer == 2:
        return 'Hi, random number is 2.'
    elif getAnswer == 3:
        return 'Hi, random number is 3.'
    elif getAnswer == 4:
        return 'Hi, random number is 4.'
    
Random_Number = random.randint(1,4)
Returned_Answer = generatAnswer(Random_Number)
print(Returned_Answer)

print('cats', 'dogs', 'foxs', sep='.')
print('Hello', end=' ')
print('Pranav')