# Listing 7.3
# Provides a function that Counts to ten
# Author: Rick Halterman
# Last modified: 

# Count to ten and print each numer on its own line
def count_to_10():
    for i in range(1, 11):
        print(i, end=' ')
    print()

print('Going to count to ten...')
count_to_10()
print('Going to count to ten again...')
count_to_10()