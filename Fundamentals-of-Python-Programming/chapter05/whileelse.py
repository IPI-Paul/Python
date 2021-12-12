# Listing 5.28
# Shows how a while/else statement works. 
# Author: Rick Halterman
# Last modified: 

# Add five nonnegative numbers supllied by the user
count = sum = 0
print('Please provide five nonnegative numbers when prompted')
while count < 5:
    # Get value from the user
    val = float(input('Enter number: '))
    if val < 0:
        print('Negative numbers are not acceptable! Terminating')
        break
    count += 1
    sum += val
else:
    print('Average =', sum / count)