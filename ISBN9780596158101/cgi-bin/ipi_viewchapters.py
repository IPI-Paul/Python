#!/usr/bin/env python3

# Example by IPI-Paul.
# Is a Python CGI script that builds up a list of all other scripts in the
# selected chapter folder
# Author: Paul I Ighofose
# Last modified: 2019-03-27

import os, cgi, html

form = cgi.FieldStorage()                       # parse form data 
path, filename = os.path.split(__file__)
try:
    curr = form['chptr'].value
    cwd = form['chptr'].value
    cwd = '../' + cwd.split(os.sep)[-1]
except:
    curr = path
    cwd = path

print("""Content-type: text/html

<title>
    IPI Python Chapters Viewer
</title>
<body>
    <h1>List of Python Scripts Chapters</h1>
""")
print("""
    <h2>""" + curr.split(os.sep)[-1] + """</h2>
    <form method="POST" action="ipi_viewchapters.py">
        <select onchange="form.submit()" name="chptr">
            """)
print('<option value="">Select a Folder</option>')
for chpt in os.listdir('.'):
    if not chpt.split(os.sep)[-1] in ['web.config', '__pycache__']:
        print('<option value="%s">%s</option>' % 
              (os.path.abspath('./' + chpt), 
               chpt.split(os.sep)[-1]))
print("""
        </select>
        <ul>  
""")
for script in os.listdir(curr):
    if not script in [filename, '__pycache__'] and not os.path.isdir(
        os.path.join(curr, script)):
        sep = '            '
        print(sep + '<li>')
        sep += '    '
        if curr == path:
            print(sep + '<a href="' + script + '" target="_blank">' + 
                  script + '</a><br />')
        else:
            print(sep + '<a href="' + cwd + '/' + script + 
                  '" target="_blank">' + script + '</a><br />')
        try:
            print('%sExample %s' % 
                  (sep,
                   html.escape(open(os.path.join(curr, script), 'r')
                   .read().split('# Author:',1)[0].split('# Example')[1]
                   .replace('# ', sep)))) 
        except:
            print(sep, 'Unable to find Example...Author string block')
        sep = sep[:-4]
        print(sep + '</li>')
print("""        </ul>
    </form>
</body>
""")