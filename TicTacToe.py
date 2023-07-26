#Author: Pranav
#Description: Tic-Tac-Toe game

theBoard = {
    'topleft': ' ', 'topmid': ' ', 'topright': ' ',
    'midleft': ' ', 'center': ' ', 'midright': ' ',
    'botleft': ' ', 'botmid': ' ', 'botright': ' '
}

def printboard():
    print()
    print(theBoard['topleft'] + '|' + theBoard['topmid'] + '|' + theBoard['topright'])
    print('-+-+-')
    print(theBoard['midleft'] + '|' + theBoard['center'] + '|' + theBoard['midright'])
    print('-+-+-')
    print(theBoard['botleft'] + '|' + theBoard['botmid'] + '|' + theBoard['botright'])
    print()


def check_win(player, board):
    
    # Check rows
    if board['topleft'] == board['topmid'] == board['topright'] == player:
        return True
    elif board['midleft'] == board['center'] == board['midright'] == player:
        return True
    elif board['botleft'] == board['botmid'] == board['botright'] == player:
        return True
    
    # Check columns
    elif board['topleft'] == board['midleft'] == board['botleft'] == player:
        return True
    elif board['topmid'] == board['center'] == board['botmid'] == player:
        return True
    elif board['topright'] == board['midright'] == board['botright'] == player:
        return True
    
    # Check diagonals
    elif board['topleft'] == board['center'] == board['botright'] == player:
        return True
    elif board['topright'] == board['center'] == board['botleft'] == player:
        return True
    else:
        return False

turn = 'X'
for i in range(9):
    printboard()
    print('Turn for ' + turn + '. Where do you want to move?')
    user_input = input()
    theBoard[user_input] = turn
    
    # The check_win function checks if the current player has won the game. 
    # If so, it prints a message to the console and ends the game. 
    # If no one has won after nine moves, the game is declared a tie.
    if check_win(turn, theBoard):
        printboard()
        print(f"Congratulations! {turn} won!")
        break
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
else:
    printboard()
    print("It's a tie!")