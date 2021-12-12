# Listing 6.5
# Measures how long it takes a user to enter a character from the keyboard
# Author: Rick Halterman
# Last modified: 

from time import clock

print('Enter your name: ', end='')
start_time = clock()
name = input()
elapsed = clock() - start_time
print(name, 'it took you', elapsed, 'seconds to respond')