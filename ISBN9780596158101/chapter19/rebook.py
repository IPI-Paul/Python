#!/usr/bin/env python3

# Example 19-9
# Shows how to go about parsing an XML file with the re module
# Author: Mark Lutz
# Last modified: 

"""
XML Parsing: regular expressions (no robust or general)
"""

import re, pprint
text = open('../sourceFiles/xml/ch19-books.xml').read() # str if str pattern
pattern = '(?s)isbn="(.*?)".*?<title>(.*?)</title>'     # *?=nongreedy
found = re.findall(pattern, text)                       # (?s)=dot matches /n
mapping = {isbn: title for (isbn, title) in found}      # dict from tuple list
pprint.pprint(mapping)