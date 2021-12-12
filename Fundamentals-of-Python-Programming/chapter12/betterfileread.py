# Listing 12.22
# The with/as statement will not automatically handle any exceptions and can be
# remedied with another pair of nested statements
# Author: Rick Halterman
# Last modified: 

# Sum the values in a text file containing integers
try:
    with open('mydata.dat') as f:
        sum = 0
        try:
            for line in f:
                sum += int(line)
        except Exception as er:
            print(er)   # Show the problem
        print('Sum =', sum)
except OSError:
    print('Could not open file')