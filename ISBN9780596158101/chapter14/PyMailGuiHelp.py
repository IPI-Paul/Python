#!/usr/bin/env python3

# Example 14-11
# Lists the module that defines the text displayed in PyMailGUI's help pop up as 
# one triple quoted string, as well as a function for displaying the HTML
# rendition of this text.
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
PyMailGUI help text string and HTML  display function;

History: this display began as an info box pop up which had to be narrow for 
linux; it later grew to use scrolledtext with buttons instead; it now also 
displays an HTML rendition in a web browser;

2.1/3E: the help string is stored in this separate module to avoid distracting 
from the executable code. As coded, we throw up this text in a simple scrollable 
text box; in the future, we might instead use an HTML file opened with a browser
(use webbrowser module, or run a 'browser help.html' or DOS 'start help.html'
with os.system);

3.0/4E: the help text is now also popped up in a web browser in HTML form, with 
lists, section links, and separators; see the HTML file PyMailGuiHelp.html in
the examples package for the simple HTML translation of the help text string here,
popped up in a browser; both the scrolled text widget and HTML browser forms are 
currently supported: change mailconfig.py to use the flavor(s) you prefer;
################################################################################
"""
# new HTML help for 3.0/4E
helpfile = 'PyMailGuiHelp.html'     # see book examples package

def showHtmlHelp(helpfile=helpfile):
    """
    3.0: popup HTML version of help file in a local web browser via webbrowser;
    this module is importable, but html file might not be in current working dir
    """
    import os, wbbrowser
    mydir = os.path.dirname(__file__)       # dir of this module's filename
    mydir = os.path.abspath(mydir)          # make absolute:may be .., etc
    webbrowser.open_new('file://' + os.path.join(mydir, helpfile))

################################################################################
# string for older text display: client responsible fgor GUI construction
################################################################################

helptext = """
PyMailGUI, Version 3.0
May, 2010 (2.1 January, 2006)
Programming Python, 4th Edition
Mark Lutz, for O'Reilly Media, Inc.

PyMailGUI is a multiwindow interface for processing email, both online and 
offline. Its main interfaces include one list window for the mail server, zero
or more list windows for mail save files, and multiple view windows for composing
or viewing emails selected in a list window. On startup, the main (server) list 
window appears first, but no mail server connection is attempted until a Load or 
message send request. All PyMailGYUI windows may be resized, which is especially 
useful in list windows to see additional columns.

Note: To use PyMailGUI to read and write email of your own, you must change the 
POP and SMTP server names and login details in the file mailconfig.py, located 
in PyMailGUI's source-code directory. See section 11 for details.

Contents:
0)  VERSION ENHANCEMENTS
1)  LIST WINDOW ACTIONS
2)  VIEW WINDOW ACTIONS
3)  OFFLINE PROCESSING
4)  VIEWING TEXT AND ATTACHMENTS
5)  SENDING TEXT AND ATTACHMENTS
6)  MAIL TRANSFER OVERLAP
7)  MAIL DELETION
8)  INBOX MESSAGE NUMBER SYNCHRONIZATION
9)  LOADING EMAIL
10) UNICODE AND INTERNATIONALIZATION SUPPORT
11) THE mailconfig CONFIGURATION MODULE
12) DEPENDENCIES
13) MISCELLANEOUS HIBNTS ("Cheat Sheet")

- Use ',' between multiple addresses in To, Cc, and Bcc headers.
- Addresses may be given in the full '"name" <addr>' form.
- Payloads and headers are decoded on fetches and encoded on sends.
- HTML mail show extracted plain text plus HTML in a web browser.
- To, Cc, and Bcc receive composed mail, but no Bcc header is sent.
- If enabled in mailconfig, Bcc is prefilled with sender address.

- Reply and Fwd automatically quote the original mail text.
- If enabled, replies prefill Cc with all original recipients.
- Attachements may be added for sends and are encoded as required.
- Attachments may be opened after View via Split or part buttons.
- Double-click a mail in the list index to view its raw text.
- Select multiple mail to process as a set: Ctr|Shift + click, or All.

- Sent mail are saved to a file named in mailconfig: use Open to view.
- Save pops up a dialog for selecting a file to hold saved mail.
- Save always appends to the chosen save file, rather than erasing it.
- Split asks for a save directory; part buttons save in ./TempParts.
- Open text editor's Save to save a draft of email text being composed.

- Passwords are requested if/when needed, and not stored by PyMailGUI.
- You may list your passwrod in a file named in mailconfig.py.
- To print emails, 'Save' to a text file and print with other tools.
- See the altconfigs directory for using with multiple email accounts.

- Emails are never deleted from the mail server automatically.
- Delete does not reload message headers, unledd it fails.
- Delete checks your inbox to make sure it deletes the correct mail.
- Fetches detect inbox changes and may overlap in time.

- click this window's Source button to view PyMailGUI source-code files.
- Watch http://www.rmi.net/~lutz for updates and patches
- This is an Open Source system: change its code as you like.
"""

if __name__ == '__main__':
    print(helptext)                 # to stdout if run alone
    input('Press Enter key')        # pause in DOS console pop ups