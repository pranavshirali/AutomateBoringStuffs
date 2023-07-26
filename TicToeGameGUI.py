import tkinter as tk
from tkinter import messagebox

theBoard = {
    'topleft': ' ', 'topmid': ' ', 'topright': ' ',
    'midleft': ' ', 'center': ' ', 'midright': ' ',
    'botleft': ' ', 'botmid': ' ', 'botright': ' '
}

def check_win(player, board):
    # Check rows, columns, and diagonals
    for row in range(3):
        if (board[f'topleft'] == board[f'topmid'] == board[f'topright'] == player or
            board[f'midleft'] == board[f'center'] == board[f'midright'] == player or
            board[f'botleft'] == board[f'botmid'] == board[f'botright'] == player or
            board[f'topleft'] == board[f'midleft'] == board[f'botleft'] == player or
            board[f'topmid'] == board[f'center'] == board[f'botmid'] == player or
            board[f'topright'] == board[f'midright'] == board[f'botright'] == player or
            board[f'topleft'] == board[f'center'] == board[f'botright'] == player or
            board[f'topright'] == board[f'center'] == board[f'botleft'] == player):
            return True
    return False


def play_again():
    global turn
    for key in theBoard:
        theBoard[key] = ' '
        button_dict[key].config(text=' ')
    turn = 'X'

def on_click(key):
    global turn
    if theBoard[key] == ' ':
        theBoard[key] = turn
        button_dict[key].config(text=turn)
        if check_win(turn, theBoard):
            if messagebox.askyesno("Game Over", f"Congratulations! {turn} won!\nDo you want to play again?"):
                play_again()
            else:
                root.quit()
        elif ' ' not in theBoard.values():
            if messagebox.askyesno("Game Over", "It's a tie!\nDo you want to play again?"):
                play_again()
            else:
                root.quit()
        else:
            turn = 'O' if turn == 'X' else 'X'

position_to_indices = {
    'topleft': (0, 0), 'topmid': (0, 1), 'topright': (0, 2),
    'midleft': (1, 0), 'center': (1, 1), 'midright': (1, 2),
    'botleft': (2, 0), 'botmid': (2, 1), 'botright': (2, 2)
}

root = tk.Tk()
root.title("Tic-Tac-Toe")

button_dict = {}
for key, (row, col) in position_to_indices.items():
    button_dict[key] = tk.Button(root, text=' ', font=('Helvetica', 20), height=2, width=5, command=lambda k=key: on_click(k))
    button_dict[key].grid(row=row, column=col)

turn = 'X'
root.mainloop()