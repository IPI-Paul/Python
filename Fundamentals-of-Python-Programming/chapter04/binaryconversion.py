# Listing 4.12
# Uses nested if/else statements to print a 10-bit binary string representing 
# the binary equivalent of a decimal integer supplied by the user.
# Author: Rick Halterman
# Last modified: 

# Get number from the user
value = int(input('Please enter an integer value in the range 0...1023: '))
# Create an empty binary string to build upon
binary_string = ''
calc_string = ''
calc1, calc2 = 0, 0
# Integer must be less than 1024
if 0 <= value < 1024:
    if value >= 512:
        binary_string += '1'
        value %= 512
        calc1 = 512
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 256:
        binary_string += '1'
        value %= 256
        calc1 = 256
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 128:
        binary_string += '1'
        value %= 128
        calc1 = 128
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 64:
        binary_string += '1'
        value %= 64
        calc1 = 64
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 32:
        binary_string += '1'
        value %= 32
        calc1 = 32
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 16:
        binary_string += '1'
        value %= 16
        calc1 = 16
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 8:
        binary_string += '1'
        value %= 8
        calc1 = 8
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 4:
        binary_string += '1'
        value %= 4
        calc1 = 4
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 2:
        binary_string += '1'
        value %= 2
        calc1 = 2
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2) + '+'
    else:
        binary_string += '0'
    if value >= 0:
        calc1 = 1
        calc2 += calc1
        calc_string += '(1*' + str(calc1) + ')=' + str(calc2)
    binary_string += str(value)
    
# Display the results
if binary_string != '':
    print(binary_string)
    print(calc_string)
else:
    print('Cannot convert')