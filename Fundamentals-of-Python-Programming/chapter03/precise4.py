# Listing 3.4
# Demonstrates that because computers store numbers in binary (base 2) form, 
# if we choose a binary fractional power, the mathematics will work out 
# precisely.
# Author: Rick Halterman
# Last modified: 

one = 1.0
one_fourth = 1.0 / 4
zero = one - one_fourth - one_fourth - one_fourth - one_fourth
print('one =', one, ' one_fourth =', one_fourth, ' zero =', zero)