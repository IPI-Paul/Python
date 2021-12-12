# Listing 9.2
# Uses the rjust string method to right justify a string padded with a specified 
# character
# Author: Rick Halterman
# Last modified: 

word = 'ABCD'
print(word.rjust(10, '*'))
print(word.rjust(3, '*'))
print(word.rjust(15, '>'))
print(word.rjust(10))