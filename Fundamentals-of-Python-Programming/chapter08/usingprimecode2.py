# Listing 8.8
# Illustrates an alternative way of importing code from another module
# Author: Rick Halterman
# Last modified: 

import primecode

num = int(input("Enter an integer: "))
if primecode.is_prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")