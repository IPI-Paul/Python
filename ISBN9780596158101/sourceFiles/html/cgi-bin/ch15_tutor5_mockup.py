#!/usr/bin/env python3

# Example 15-22
# Is a rewrite of the ch15_tutor5.py example we saw earlier, using the form 
# mock-up utility to simulate field inputs
# Author: Mark Lutz
# Last modified: 

"""
run tutor5 logic with formMockup instead of cgi.FieldStorage() to test: python
ch15_tutor5_mockup.py > temp.html, and open temp.html
"""

from ch15_formMockup import formMockup
form = formMockup(name='Bob',
                  shoesize='Small',
                  language=['Python', 'C++', 'HTML'],
                  comment='ni, Ni, NI')

# rest same as original, less form assignment
import cgi, sys
# form = cgi.FieldStorage()                   # parse form data
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