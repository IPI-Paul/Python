# Listing 5.22
# Demonstrates a while loop's top exit behaviour
# Author: Rick Halterman
# Last modified: 

x = 10
while x == 10:
    print('First print statement in the while loop')
    x = 5       # Condition no longer true; do we exit immediately?
    print('Second statement in the while loop')