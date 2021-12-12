#!/usr/bin/env python3

# Example 19-12
# Shows how to use an Element Tree system (xml.etree) to parse an XML file
# Author: Mark Lutz
# Last modified: 

"""
XML parsing: ElementTree (etree) provides a Python-based API for parsing/generating
"""

import pprint
from xml.etree.ElementTree import parse

mapping = {}
path = '../sourceFiles/xml/ch19-'
tree = parse(path + 'books.xml')
for B in tree.findall('book'):
    isbn = B.attrib['isbn']
    for T in B.findall('title'):
        mapping[isbn] = T.text
pprint.pprint(mapping)