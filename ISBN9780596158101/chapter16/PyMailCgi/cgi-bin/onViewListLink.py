#!/usr/bin/env python3

# Example 16-8
# Is invoked by stateful URLs on the message selection list, and sends the 
# selected message number and mail account information (user, password, and site)
# as parameters on the end of the script's URL
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-04-07

"""
################################################################################
On user click of message link in main selection list: make mail view page;

cgi.FieldStorage undoes any urllib.parse escapes in link's input parameters 
(%xx and '+' for spaces already undone); in 2.0+ we only fetch 1 mail here, not 
the entire list again; in 2.0+ we also find mail's main text part intelligently 
instead of blindly displaying full text (with any attachments), and we generate
 links to attachment files saved on the server; saved attachment files only work 
 for 1 user and 1 message; most 2.0 enchancements inherited from mailtools pkg;
 
 3.0: mailtools decode the message's full-text bytes to email parsing;
 3.0: for display, mailtools decodes main text, commonhtml decodes message hdrs;
################################################################################
"""

import cgi
import commonhtml, secret
from externs import mailtools
# commonhtml.dumpstatepage(0)

def saveAttachments(message, parser, savedir='partsdownload'):
    """
    save fetched email's parts to files on server to be viewed in user's web 
    browser
    """
    import os
    if not os.path.exists(savedir):             # in CGI script's cwd on server
        os.mkdir(savedir)                       # will open per your browser
    for filename in os.listdir(savedir):        # clean up last message: temp!
        dirpath = os.path.join(savedir, filename)
        os.remove(dirpath)
    typesAndNames = parser.saveParts(savedir, message)
    filenames = [fname for (ctype, fname) in typesAndNames]
    for filename in filenames:
        os.chmod(filename, 0o666)           # some srvrs may need read/write
    return filenames
form = cgi.FieldStorage()
user, pswd, site = commonhtml.getstandardpopfields(form)
pswd = secret.decode(pswd)

try:
    msgnum = form['mnum'].value                                 # from URL link
    parser = mailtools.MailParser()
    fetcher = mailtools.SilentMailFetcher(site, user, pswd)
    fulltext = fetcher.downloadMessage(int(msgnum))             # don't eval!
    message = parser.parseMessage(fulltext)                     # email pkg Message
    parts = saveAttachments(message, parser)                    # for URL links
    mytype, content = parser.findMainText(message)              # first txt part
    commonhtml.viewpage(msgnum, message, content, form, parts)  # encode pswd
except:
    commonhtml.errorpage('Error loading message')