#!/usr/bin/env python3

# Example 15-10
# Uses string formatting to plug input values into a response page's HTML 
# triple-quoted template string with one line per input field.
# Author: Mark Lutz
# Last modified: 

"""
runs on the server, reads form input, prints HTML;
URL http://server-name/cgibin/ch15_tutor4.py
"""

import cgi, sys
sys.stderr = sys.stdout                 # errors to browser
form = cgi.FieldStorage()               # parse form data
print('Content-type: text/html\n')      # plus blank line

# class dummy:
#       def __init__(self, s): self.value = s
# form = {'user': dummy('bob'), 'age': dummy('10')}

html = """
    <title>tutor4.py</title>
    <h1>Greetings</h1>
    <hr />
    <h4>%s</h4>
    <h4>%s</h4>
    <h4>%s</h4>
    <hr />
"""

if not 'user' in form:
    line1 = 'Who are you?'
else:
    line1 = 'Hello, %s.' % form['user'].value

line2 = "You're talking to a %s server." % sys.platform

line3 = ""
if 'age' in form:
    try:
        line3 = "Your age squared is %d!" % (int(form['age'].value) ** 2)
    except:
        line3 = "Sorry, I can't compute %s ** 2." %  form['age'].value

print(html % (line1, line2, line3))