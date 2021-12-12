# Listing 7.12
# Illustrates the organinsation of code using functions
# Author: Rick Halterman
# Last modified: 

# Compute the greatest common factor of two integers provided by the user

def gcd(n1, n2):
    # Determine the smaller of n1 and n2
    min = n1 if n1 < n2 else n2
    # 1 definitely is a common factor to all ints
    largest_factor = 1
    for i in range(1, min + 1):
        if n1 % i == 0 and n2 % i == 0:
            largest_factor = i  # Found larger factor
    return largest_factor

# Get an integer from the user
def get_int():
    return int(input('Please enter an integer: '))

# Main code to execute
def main():
    n1 = get_int()
    n2 = get_int()
    print('gcd(', n1, ', ', n2, ') = ',gcd(n1, n2), sep='')
    
# Run the program
main()