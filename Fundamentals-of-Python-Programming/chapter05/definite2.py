# Listing 5.9
# Uses <= to print integers from one to the integer supplied by the user and is 
# another example of a definite loop
# Author: Rick Halterman
# Last modified: 

n = 1
stop = int(input('Please enter an integer to stop at: '))
while n <= stop:
    print(n)
    n += 1
