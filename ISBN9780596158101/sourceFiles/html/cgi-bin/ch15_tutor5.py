#!/usr/bin/env python3

# Example 15-12
# Runs on the server to process all the input data typed or selected in the form
# Author: Mark Lutz
# Last modified: 

"""
runs on the server, reads form input, prints HTML;
"""

import cgi, sys
form = cgi.FieldStorage()                   # parse form data
print('Content-type: text/html')            # plus blank line

html = """
    <title>tutor5.py</title>
    <h1>Greetings</h1>
    <hr />
    <h4>Your name is %(name)s</h4>
    <h4>You wear rather %(shoesize)s shoes</h4>
    <h4>Your current job: %(job)s</h4>
    <h4>You program in %(language)s</h4>
    <h4>You also said:<h4>
    <p>
        %(comment)s
    </p>
    <hr />
"""

data = {}
for field in ('name', 'shoesize', 'job', 'language', 'comment'):
    if not field in form:
        data[field] = '(unknown)'
    else:
        if not isinstance(form[field], list):
            data[field] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[field] = ' and '.join(values)
print(html % data)