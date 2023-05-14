#Author: Pranav Shirali
#Description: This program is slot machine game


import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

'''This function is main, which is the logical function of the program.'''
def check_winnings(coloumns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = coloumns[0][line]
        for coloum in coloumns:
            symbol_to_check = coloum[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)
        
    return winnings, winning_line

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    coloumns = []
    for _ in range(cols):
        coloumn = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coloumn.append(value)

        coloumns.append(coloumn)

    return coloumns

def print_slot_machine(coloumns):
    for row in range(len(coloumns[0])):
        for i, coloumn in enumerate(coloumns):
            if i != len(coloumns) - 1:
                print(coloumn[row], end="|")
            else:
                print(coloumn[row], end="")

        print()

def deposit():
    while True:
        amount = input('What is amount you do like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Please enter amount greater than 0.')
        else:
            print('Please enter a number.')
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on 1-{MAX_LINES}: ") #Example for f-String
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print(f"Enter number of lines between 1-{MAX_LINES}")
        else:
            print('Please enter a number.')
    return lines

def get_bet():
    while True:
        amount = input('Enter the bet amount you want to place on each line: $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Please enter the bet between ${MIN_BET}-${MAX_BET}')
        else:
            print('Please enter valid number')
    return amount

def spin(balance):

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You don not have enough balance to bet, your current balance is ${balance}')
        else:
            break    

    print(f'You are betting for amount ${bet} on {lines} lines.So your total bet is ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    print_slot_machine(slots)

    winnings, winning_line = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_line)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press 'E' to spin (q to quit):")
        if answer == "E" or answer == "e":
            balance += spin(balance)
        elif answer == 'q':
            print(f"You leave with ${balance}")
            break
        
main()
