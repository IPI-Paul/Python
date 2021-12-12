# Listing 3.2
# Demonstrates the weakness of floating-point numbers as they are imprecise 
# approximations of real numbers
# Author: Rick Halterman
# Last modified: 

one = 1.0
one_third = 1.0 / 3.0
zero = one - one_third - one_third - one_third

print('one =', one, ' one_third =', one_third, ' zero=', zero)