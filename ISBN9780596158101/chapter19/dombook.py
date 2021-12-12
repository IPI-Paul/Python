#!/usr/bin/env python3

# Example 19-11
# Is a DOM-based equivalent to the SAX parser
# Author: Mark Lutz
# Last modified: 

"""
XML parsing: DOM gives whole document to the application as a traversable object
"""

import pprint
import xml.dom.minidom
from xml.dom.minidom import Node

path = '../sourceFiles/xml/ch19-'
doc = xml.dom.minidom.parse(path + 'books.xml')     # load doc into object

mapping = {}
for node in doc.getElementsByTagName('book'):       # traverse DOM object
    isbn = node.getAttribute('isbn')                # via DOM object API
    L = node.getElementsByTagName('title')
    for node2 in L:
        title = ''
        for node3 in node2.childNodes:
            if node3.nodeType == Node.TEXT_NODE:
                title += node3.data
        mapping[isbn] = title

# mapping now has the same value as in the SAX example
pprint.pprint(mapping)