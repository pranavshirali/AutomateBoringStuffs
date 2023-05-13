import random, sys

print('ROCK, PAPER, SCISSORS')
wins = 0
ties = 0
losses = 0


#The main game loop

while True:
    #This line keeps track of the status of game
    print('%s Wins, %s losses, %s ties'%(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissor and (q)uit')
        usermove = input()
        if usermove == 'q':
            if wins > losses:
                print('Hurray!!You won the game...')
            elif ties > wins or ties > losses or wins == ties or ties == losses:
                print('Ohh!!Game is tie...')
            elif losses > wins:
                print('You lose the game, better luck next time..')
            sys.exit()
        elif usermove =='r' or usermove == 'p' or usermove == 's':
            break
        else:
            print('Enter either r / p / s / q')
        
    if usermove == 'r':
        print('ROCK versus...')
    elif usermove == 'p':
        print('PAPER versus...')
    elif usermove == 's':
        print('SCISSOR versus...')

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