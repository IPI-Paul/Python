#!/usr/bin/env python3

# Example 15-4
# Is a Python CGI script that prints an <IMG> HTML tag in its output to produce
# a graphic image in the client browser
# Author: Mark Lutz
# Last modified: 

text = """Content-type: text/html

<title>CGI 101</title>
<h1>A Second CGI Script</h1>
<hr />
<p>
    Hello, CGI World!
</p>
<img src="../images/queen-of-hearts.jpg" border=1 alt="[image]">
<hr />
"""

print(text)