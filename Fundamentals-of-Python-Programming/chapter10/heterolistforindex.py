# Listing 10.6
# Uses len and an explicit list index with a for loop instead of the code in 
# Listing 10.5
# Author: Rick Halterman
# Last modified: 

collection = [24.2, 4, 'word', print, 19, -0.03, 'end']
for i in range(len(collection)): # Not the preferred way to traverse a list
    print(collection[i])            # Print each element