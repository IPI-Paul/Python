# Listing 6.12
# Shows how we can select a random element from a tuple of strings
# Author: Rick Halterman
# Last modified: 

from random import choice

for i in range(10):
    print(choice(('one', 'two', 'three', 'four', 'five', 'six', 'seven', 
                  'eight', 'nine', 'ten')))