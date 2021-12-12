#!/usr/bin/env python3

# Example 1-31
# Like the HTML file, this Python script resides on the same machine as the web 
# server; it's run on the server machine to handle the inputs and generate a 
# reply to the browser on the client
# Author: Mark Lutz
# Last modified: 

import cgi
form = cgi.FieldStorage()           # parse form data
print('Content-type: text/html\n')  # hdr plus blank line
print('<title>Reply Page</title>')  # html reply page
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Hello <i>%s</i>!</h1>'% cgi.escape(form['user'].value))