# Listing 10.31
# Illustrates the effect of replacing the outer brackets of a list comprehension
# with parentheses. The expression becomes a generator expression whic can be 
# iterated with a for loop.
# Author: Rick Halterman
# Last modified: 

for val in (2 ** x for x in range(10)):
    print(val, end=' ')
print()