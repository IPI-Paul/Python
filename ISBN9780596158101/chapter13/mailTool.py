#!/usr/bin/env python3

# Example 13-22
# Contains common superclasses for the other classes in the package. This is in 
# part meant for future expansion. at present these are used only to enable or 
# disable trace message output (some clients, such as web-based programs, may 
# not want text to be printed to the output stream
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
common superclasses: used to turn trace messages on/off
################################################################################
"""

class MailTool:                         # superclass for all mail tools
    def trace(self, message):           # redef me to disable or log to file
        print(message)

class SilentMailTool:                   # to mixin instead of subclassing
    def trace(self, message):
        pass