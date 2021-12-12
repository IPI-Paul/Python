#!/usr/bin/env python3

# Example 15-25
# This script displays the inputs sent from the client on the standard error 
# stream to avoid any additional translations
# Author: Mark Lutz
# Last modified: 

import cgi, sys
form = cgi.FieldStorage()       # print all inputs to stderr; stdout=reply page
print('Content-type: text/html\n\n<body>')
for name in form.keys():
    print('[%s:%s]' % (name, form[name].value), end=' ', file=sys.stderr)
    print('%s: %s<br />' % (name, form[name].value))
print('</body>')