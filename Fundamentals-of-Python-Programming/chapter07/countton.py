# Listing 7.4
# Provides a function that Counts to the number given by the user input
# Author: Rick Halterman
# Last modified: 

# Count to n and print each numer on its own line
def count_to_n(n):
    for i in range(1, n + 1):
        print(i, end=' ')
    print()

print('Going to count to ten...')
count_to_n(10)
print('Going to count to five...')
count_to_n(5)