#!/usr/bin/env python3

# Example
# Is a Python CGI script that builds up a list of all other scripts in the same
# folder
# Author: Paul I Ighofose
# Last modified: 2019-03-26

import os

path, filename = os.path.split(__file__)

print("""Content-type: text/html

<title>
    IPI CGI Scripts Viewer
</title>
<body>
    <h1>List of Python CGI Scripts</h1>
    <ul>  
""")
for script in os.listdir('./cgi-bin/'):
    if not script in [filename, '__pycache__']:
        print('        <li>')
        print('            <a href="' + script + '" target="_blank">' + script 
              + '</a><br />')
        sep = '            '
        print('%sExample %s' % 
              (sep,
               open(os.path.join(path, script), 'r')
               .read().split('# Author:',1)[0].split('# Example')[1]
               .replace('# ', sep).replace('<', '&lt;'))) 
        print('        </li>')
print("""    </ul>
</body>
""")