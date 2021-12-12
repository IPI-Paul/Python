# Listing 5.15
# Uses a for loop to count the number of vowels in the text provided by the user
# Author: Rick Halterman
# Last modified: 

word = input('Please enter some text: ')
vowel_count = 0
for c in word:
    if c == 'A' or c == 'a' or c == 'E' or c == 'e' or c == 'I' or c == 'i' or \
    c == 'O' or c == 'o' or c == 'U' or c == 'u':
        print(c, ', ', sep='', end='')      # Print the vowel
        vowel_count += 1                    # Count the vowel
print(' (', vowel_count, ' vowels)', sep='')