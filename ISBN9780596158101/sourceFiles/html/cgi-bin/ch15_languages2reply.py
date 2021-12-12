#!/usr/bin/env python3

# Example 15-23
# Recodes the reply page script itself to import data that was factored out to 
# the common module and import the reusable form mock-up module's tools
# Author: Mark Lutz
# Last modified: 

"""
Same, but for easier maintenance, use HTML template strings, get the Language 
table and input key from common module file, and get reusable form field mockup
utilities module for testing.
"""

import cgi, sys
from ch15_formMockup import FieldMockup             # input field simulator
from ch15_languages2common import hellos, inputkey  # get common table, name
debugme = False

hdrhtml = """Content-type: text/html\n
<title>Languages</title>
<h1>Syntax</h1>
<hr />
"""

langhtml = """
<h3>%s</h3>
<p>
    <pre>
        %s
    </pre>
</p>
<br />
"""

def showHello(form):                        # HTML for one language
    choice = form[inputkey].value           # escape lang name too
    try:
        print(langhtml % (cgi.escape(choice),
                          cgi.escape(hellos[choice])))
    except KeyError:
        print(langhtml % (cgi.escape(choice),
                          "Sorry--I don't know that language"))

def main():
    if debugme:
        form = {inputkey: FieldMockup(sys.argv[1])}     # name on cmd line
    else:
        form = cgi.FieldStorage()                       # parse real inputs
    
    print(hdrhtml)
    if not inputkey in form or form[inputkey].value == 'All':
        for lang in hellos.keys():
            mock = {inputkey: FieldMockup(lang)}        # not dict(n=v) here!
            showHello(mock)
    else:
        showHello(form)
    print('<hr />')

if __name__ == '__main__': main()