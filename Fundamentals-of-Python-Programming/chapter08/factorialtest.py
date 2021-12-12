# Listing 8.3
# Includes a factorial function that exactly models the mathematical definition
# Author: Rick Halterman
# Last modified: 

def factorial(n):
    """
    Computes n!
    Returns the factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """ Try out the factorial function """
    print(" 0! = ", factorial(0))
    print(" 1! = ", factorial(1))
    print(" 6! = ", factorial(6))
    print("10! = ", factorial(10))
    
main()