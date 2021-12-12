#!/usr/bin/env python3

# Example 15-26
# Referenced by a hyperlink in the main ch15_language.html page, works around 
# only being able to see HTML output by opening the source file senting its text 
# as part of the HTML response
# Author: Mark Lutz
# Last modified: 

"Display ch15_languages.py script code without running it."

import cgi
filename = 'cgi-bin/ch15_languages.py'

print('Content-type: text/html\n')          # wrap up in HTML
print('<title>Languages</title>')
print("<h1>Source code: '%s'</h1>" % filename)
print('<hr />\n<pre>')
print(cgi.escape(open(filename).read()))    # decode per platform default
print('</pre>\n<hr />')