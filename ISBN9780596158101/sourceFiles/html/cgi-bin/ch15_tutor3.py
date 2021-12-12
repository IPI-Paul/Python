#!/usr/bin/env python3

# Example 15-8
# The submit button on this page is loaded to trigger the possible remote 
# program whose URL is listed in the form's action option, and passes this 
# program the input data typed by the user, according to the form's method 
# encoding style option
# Author: Mark Lutz
# Last modified: 

"""
runs on the server, reads form input, prints HTML;
url=http://server-name/cgi-bin/ch15_tutor3.py
"""

import cgi
form = cgi.FieldStorage()               # parse form data
print('Content-type: text/html')        # plus blank line

html = """
    <title>ch15_tutor3.py</title>
    <h1>Greetings<h1>
    <hr />
    <p>%s</p>
    <hr />
"""

if not 'user' in form:
    print(html % 'who are you?')
else:
    print(html % ('Hello, %s.' % form['user'].value))