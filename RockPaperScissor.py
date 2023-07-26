#Author: Pranav Shirali

import random, sys

print('ROCK, PAPER, SCISSORS')
wins = 0
ties = 0
losses = 0
#Asks for user name before game begins...
print('Hello there!! What is your name?')
user_name = input()
print(f'All the best for the game {user_name}...')
print()

#The main game loop
while True:
    #This line keeps track of the status of game
    print('%s Wins, %s losses, %s ties'%(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissor and (q)uit')
        usermove = input()
        if usermove == 'q':
            if wins > losses:
                print(f'Hurray!!{user_name} won the game...')
            elif losses > wins and losses > ties:
                print(f'Ohh {user_name}, you have lost the game :(  try again...')
            elif ties > wins or ties > losses or losses == wins:
                print(f'Wow {user_name} you have made this game a tie...')
            sys.exit()
        elif usermove =='r' or usermove == 'p' or usermove == 's':
            break
        else:
            print('Enter either r / p / s / q')


#User inputs are takes from this block of code      
    if usermove == 'r':
        print('ROCK versus...')
    elif usermove == 'p':
        print('PAPER versus...')
    elif usermove == 's':
        print('SCISSOR versus...')

#Random funtion generates a random number which is assigned either rock / paper / scissor
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        AiMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        AiMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        AiMove = 's'
        print('SCISSOR')


#Logic go the game is written here....
    if usermove == AiMove:
        print('The game is tie!')
        ties = ties + 1
    elif usermove == 'r' and AiMove == 'p':
        print('AI wins!')
        losses = losses + 1
    elif usermove == 'r' and AiMove == 's':
        print('You win!')
        wins = wins + 1
    elif usermove == 'p' and AiMove == 's':
        print('You lose :(')
        losses = losses + 1
    elif usermove == 'p' and AiMove == 'r':
        print('You win!')
        wins = wins + 1
    elif usermove == 's' and AiMove == 'p':
        print('You win!')
        wins = wins + 1
    elif usermove == 's' and AiMove == 'r':
        print('You lose!')
        losses = losses + 1