#! python3
#mclip.py - A multi-clipboard program.

'''
Description:

    1.The script imports two modules: sys and pyperclip. sys is a standard Python 
        module for system-specific parameters and functions, while pyperclip is a third-party module used for accessing the clipboard.

    2.The program defines a dictionary called text, which associates keyphrases (keys) with corresponding text snippets (values). 
        This dictionary serves as the storage for your predefined texts.

    3.The script checks the command-line arguments provided when running the program. 
        If the number of arguments is less than 2 (only the script name itself), it prints an error message and exits.

    4.If the keyphrase provided as an argument exists in the text dictionary, the corresponding text snippet 
        is copied to the clipboard using pyperclip.copy(). It also prints a message confirming that the text has been copied.

    5.If the keyphrase doesn't exist in the text dictionary, it prints a message indicating that the keyphrase is not available.

'''


import sys, pyperclip

text = {'agree': """Yes, I agree. That sounds fine to me.""",
 'busy': """Sorry, can we do this later this week or next week?""",
 'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2:
    print('Error: Enter the keyphrase..')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f'Text for {keyphrase} has been copied to clipboard.')

else:
    print(f'Keyphrase -{keyphrase} is not available.')

    