#Author: Pranav

import pprint

#If you import the pprint module into your programs, you’ll have access to 
#the pprint() and pformat() functions that will “pretty print” a dictionary’s 
#values. This is helpful when you want a cleaner display of the items in a dictionary than what print() provides

message = "Hello guy's I'm Pranav. This message is an example for this program for which output you'll be seeing below."
message_dictionary = {}

for character in message:
    message_dictionary.setdefault(character, 0)
    message_dictionary[character] += 1

for key, value in message_dictionary.items():
    print(str(key) +' = '+ str(value))

#pprint.pprint(message_dictionary)  #This module print