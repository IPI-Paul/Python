# Listing 8.7
# Contains a sample program that uses our packaged is_prime function
# Author: Rick Halterman
# Last modified: 

from primecode import is_prime

num = int(input("Enter an integer: "))
if is_prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")