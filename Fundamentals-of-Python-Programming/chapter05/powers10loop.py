# Listing 5.11
# Uses a for loop to re-write Listing 2.20 more compactly. It loops through and 
# prints the first 16 powers of 10
# Author: Rick Halterman
# Last modified: 

for i in range(16):
    print('{0:3} {1:16}'.format(i, 10 ** i))