# Listing 3.8
# File tempconv.py
# Demonstrates the use of comments to give an overview of the program's purpose 
# and provide some details about it's construction
# Author: Rick Halterman
# Last modified: August 22, 2014
# Converts degrees Fahrenheit to degrees Celsius
# Based on the formula found at 
# http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature

# Prompt user for temperature to convert and read the supplied value
degreesF = float(input('Enter the temperature in degrees F: '))
# Perform the conversion
degreesC = 5 / 9 *(degreesF - 32)
# Report the result
print(degreesF, 'degrees F =', degreesC, 'degrees C')
