# Listing 12.2
# Defends against the ZeroDivisionError exception with a conditional statement.
# Author: Rick Halterman
# Last modified: 

# Get two integers from the user
print('Please enter two numbers to divide.')
num1 = int(input('Please enter dividend: '))
num2 = int(input('Please enter divisor: '))
if num2 != 0:
    print('{0} divided by {1} = = {2}'.format(num1, num2, num1 / num2))
else:
    print('Cannot divide by zero')