# Listing 5.29
# Shows how a if/else statement works without the need of a while/else
# Author: Rick Halterman
# Last modified: 

# Add five nonnegative numbers supllied by the user
count = sum = 0
print('Please provide five nonnegative numbers when prompted')
while count < 5:
    # Get value from the user
    val = float(input('Enter number: '))
    if val < 0:
        break
    count += 1
    sum += val
if count < 5:
    print('Negative numbers are not acceptable! Terminating')
else:
    print('Average =', sum / count)