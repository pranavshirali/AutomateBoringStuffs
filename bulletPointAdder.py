#!python3
#Author: Pranav
#bulletPointAdder.py - This helps in adding bullet point before every point,
#that you have copied.
'''
The TODO comment is a reminder that you should complete this part of 
the program eventually. The next step is to actually implement that piece 
of the program.


For example: Copy this point and run the program.
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars

'''


import pyperclip,

text = pyperclip.paste()

#Separate the lines and add star
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)