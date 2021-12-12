#!/usr/bin/env python3

# Example 1-34
# Implements a Python CGI script that fetches and updates our shelve's records. 
# It echoes back a page similar to that produced by Example 1-33, but with the 
# form fields filled in from the attributes of actual class objects in the 
# shelve database
# Author: Mark Lutz
# Last modified: 

"""
Implement a web-based interface for view and updating class instances stored in 
a shelve; the shelve lives on the server (same machine if localhost)
"""

import cgi, shelve, sys, os                     # cgi.test() dumps inputs
path = '../shelve/ch01-'
shelvename = 'class-shelve'                     # shelve files are in cwd
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()                       # parse form data 
print('Content-type: text/html')                # hdr, blank line is in replyhtml
sys.path.insert(0, '../../chapter01')  # so this and pickle find person

# main html template
replyhtml = """
<html>
    <title>People Input Form</title>
    <body>
        <form method="POST" action="ch01_peoplecgi.py">
            <table>
                <tr><th>key</th><td>
                    <input type="text" name="key" value="%(key)s" />
                </td></tr>
$ROWS$
            </table>
            <p>
                <input type="submit" value="Fetch" name="action" />
                <input type="submit" value="Update" name="action" />
            </p>
        </form>
    </body>
</html>
"""

# insert html for data rows at $ROWS$
rowhtml = ' ' * 16 + '<tr><th>%s </th><td>' + """
""" + ' ' * 20 + '<input type="text" name="%s" value="%%(%s)s" />' + """
""" + ' ' * 16 + '</td></tr>\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)

def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:                        # values may have &, >, etc.
        value = new[field]                          # display as code: quoted
        new[field] = cgi.escape(repr(value))        # html-escape special chars
    return new

def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__                    # use attribute dict
        fields['key'] = key                         # to fill reply string
    except:
        fields = dict.fromkeys(fieldnames, '?')
        field['key'] = 'Missing or invalid key!'
    return fields

def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        field['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]                    # update existing record
        else:
            from person import Person # make/store new one for key
            record = Person(name='?', age='?')  # eval: strings must be quoted
        for field in fieldnames:
            if not ('__import__' in form[field].value and 'system' in \
               form[field].value):
                setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields

db = shelve.open(path + shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')     # bad submit button value
    fields['key'] = 'Missing or invalid action!'
db.close()
print(replyhtml % htmlize(fields))              # fill reply from dict