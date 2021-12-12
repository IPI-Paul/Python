# Listing 4.26
# Uses a conditional expression in a statement
# Author: Rick Halterman
# Last modified: 

# Acquire a number from the user and print its absolute value.
n = int(input("Please enter an integer: "))
print('|', n, '| = ', (-n if n < 0 else n), sep='')