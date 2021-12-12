#!/usr/bin/env python3

# Example by IPI-Paul.
# Functions to change string case to proper case or convert lower/upper and vice 
# versa
# Author: Paul I Ighofose
# Last modified: 2018-11-22

"""
Changes each character to it's opposite case
"""
def changeCase(text, txtOut=''):
    for ltr in text:
        txtOut += ltr.lower() if ltr == ltr.upper() else ltr.upper()
    return toClipboard(txtOut)

def properCase(text, txtOut=''):
    for i in range(len(text)):
        txtOut += text[i].upper() if i == 0 or \
            text[i-1] == '' or text[i-1] == ' ' \
            else text[i].lower()
    return toClipboard(txtOut)

def toClipboard(text):
    from subprocess import check_call as copy
    copy("echo %s|clip" % text, shell=True)
    return print(text, end='')

if __name__ == '__main__': 
    from sys import argv
    if len(argv) == 1:
        print("""
Usage: changecase.py cc string                            (upper <-> lower)
       changecase.py pc string                            (Proper Case)
    optional
       changecase.py cc string string(to append to)       (upper <-> lower)
       changecase.py pc string string(to append to)       (Proper Case)
        """)
    elif argv[1].lower() == 'cc':
        changeCase(argv[2])
    elif argv[1].lower() == 'pc':
        properCase(argv[2])