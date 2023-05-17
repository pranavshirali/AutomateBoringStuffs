#Author: Pranav Shirali
#Description: ->
'''Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. 
Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, 
and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can 
find out what percentage of the coin flips contains a streak of six heads or tails in a row. 
As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value 
the other 50% of the time.'''

import random
numberOfstreak = 0
streak_list = []
# Code that creates a list of 100 'heads' or 'tails' values.
for experimentNumber in range(10000):
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            streak_list.append('H')
        else:
            streak_list.append('T')

# Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(streak_list)-5):
        if streak_list[i:i+6] == ['H','H','H','H','H','H'] or streak_list[i:i+6] == ['T','T','T','T','T','T']:
            numberOfstreak += 1
            break

print(streak_list)
print('Chance of streak: %s%%' % (numberOfstreak / 100))
