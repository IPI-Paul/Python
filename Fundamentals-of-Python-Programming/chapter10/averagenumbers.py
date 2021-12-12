# Listing 10.1
# Averages five numbers entered by the user.
# Author: Rick Halterman
# Last modified: 

def get_number(n):
    return float(input('Please enter number ' + str(n) + ': '))

def main():
    print('Please enter five numbers: ')
    n1 = get_number(1)
    n2 = get_number(2)
    n3 = get_number(3)
    n4 = get_number(4)
    n5 = get_number(5)
    print('Numbers entered:', n1, n2, n3, n4, n5)
    print('Average:', (n1 + n2 + n3 + n4 + n5) / 5)

main()