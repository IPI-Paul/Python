# Listing 3.11
# File faultytempconv.py
# Demonstrates the importance of the correct ordering os steps in a program
# Author: Rick Halterman
# Last modified: 

# Establish some variables
degreesF, degreesC = 0, 0
# Define relationship between F and C
degreesC = 5 / 9 * (degreesF - 32)
# Prompt the user for degree F
degreesF = float(input('Enter the temperatur in degrees F: '))
# Report the result
print(degreesF, 'degrees F =', degreesC, 'degrees C')
# Relationship between F and C should come after the user inputs the value for F
degreesC = 5 / 9 * (degreesF - 32)
# Report the result
print('Correctly Ordered',degreesF, 'degrees F =', degreesC, 'degrees C')