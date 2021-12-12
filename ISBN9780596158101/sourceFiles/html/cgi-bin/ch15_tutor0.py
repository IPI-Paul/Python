#!/usr/bin/env python3

# Example 15-3
# Illustrates the nature of CGI scripts.
# Author: Mark Lutz
# Last modified: 

"""
runs on a the server, prints HMTL to create a new page;
url=http://localhost/cgi-bin/ch15_tutor0.py
"""

print('Content-type: text/html\n')
print('<title>CGI 101</title>')
print('<h1>A First CGI Script</h1>')
print('<p>Hello, CGI World!</p>')