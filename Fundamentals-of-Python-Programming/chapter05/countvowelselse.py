# Listing 5.30
# Uses a for/else statement. The break statement does not allow the else part.
# Author: Rick Halterman
# Last modified: 

word = input('Please enter some text (no X\'s, please): ')
vowel_count = 0
for c in word:
    if c == 'A' or c == 'a' or c == 'E' or c == 'e' or c == 'I' or c == 'i' or \
       c == 'O' or c == 'o' or c == 'U' or c == 'u':
        print(c, ', ', sep='', end='')      # Print the vowel
        vowel_count += 1                    # Count the vowel
    elif c == 'X' or c == 'x':
        print('X not allowed')
        break
else:
    print(' (', vowel_count, ' vowels)', sep='')