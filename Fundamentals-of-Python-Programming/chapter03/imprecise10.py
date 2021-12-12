# Listing 3.3
# Demonstrates that because computers store numbers in binary (base 2) form, 
# even one-tenth cannot be represented exactly with floating-point numbers 
# approximations of real numbers
# Author: Rick Halterman
# Last modified: 

one = 1.0
one_tenth = 1.0 / 10.0
zero = one - one_tenth - one_tenth - one_tenth \
           - one_tenth - one_tenth - one_tenth \
           - one_tenth - one_tenth - one_tenth \
           - one_tenth
print('one =', one, ' one_tenth =', one_tenth, ' zero = ', zero)