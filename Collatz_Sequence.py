"""Author: Pranav Shirali
Description: 
The Collatz conjecture is one of the most famous unsolved problems in mathematics. 
The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. 
It concerns sequences of integers in which each term is obtained from the previous term as follows: 
    -->if the previous term is even, the next number in sequence would be coltz_number / 2.
    -->If the previous term is odd, the next number in sequence would be 3 * coltz_number + 1. 
The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.
"""

import sys

def coltz_series(coltz_number):
    while coltz_number != 1:
        if coltz_number % 2 == 0:
            result = coltz_number // 2
            print(result)
            return coltz_series(result)
        elif coltz_number % 2 == 1:
            result = 3 * coltz_number + 1
            print(result)
            return coltz_series(result)

print("Enter a number for it's collatz series")
#while True:
try:
    user_input = int(input())
except ValueError:
    print('ERROR: Enter valid integer.')
    sys.exit()

coltz_series(user_input)