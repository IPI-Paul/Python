# Listing 5.12
# Attempts to thwart the range's loop variable for the for loop by changing its 
# value inside the loop
# Author: Rick Halterman
# Last modified: 

# Abuse the for statement
for i in range(10):
    print(i, end=' ')        # Print i as served by the range object
    if i == 5:
        i = 20              # Change i inside the loop?
    print('({})'.format(i), end=' ')
print()