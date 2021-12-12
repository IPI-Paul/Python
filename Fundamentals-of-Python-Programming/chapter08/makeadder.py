# Listing 8.16
# Is an example of a closure transporting a captured variable out of a function.
# Thisprogram includes a function that returns a function to its caller.
# Author: Rick Halterman
# Last modified: 

def make_adder():
    loc_val = 2 # Local variable definition
    return lambda x: x + loc_val    # Returns a function

def main():
    f = make_adder()
    print(f(10))
    print(f(2))

main()