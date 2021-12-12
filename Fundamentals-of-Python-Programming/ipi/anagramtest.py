# Uses a for loop to print all the differrent arrangements of the user input
# Author: Paul I Ighofose
# Last modified: 2018-09-11

word = ''

def perm(lst, begin):
    global word
    end = len(lst) - 1
    if begin == end:
        yield lst[:]
    else:
        for i in range(begin, end + 1):
            lst[begin], lst[i] = lst[i], lst[begin]
            yield from perm(lst, begin + 1)
            lst[begin], lst[i] = lst[i], lst[begin]

def permutations(lst):
    yield from perm(lst, 0)

def main():
    # Get the user input
    global word
    word = input('Please enter a word: ')
    print('Running algorithm!')        
    lst = list(range(len(word)))        
    with open('anagram.txt', 'w') as f:
        for p in permutations(lst):
            words = ''
            for item in p:
                words += word[item]
            print(words, file = f)
    print('Done')

main()