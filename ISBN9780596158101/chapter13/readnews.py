#!/usr/bin/env python3

# Example 13-28
# By default fetches and displays the last 0 articles from Python's Internet 
# newsgroup, comp.lang.python, from the news.rmi.net NNTP server
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-03-12

"""
fetch and print usenet newsgroup posting from comp.lang.python via the nntplib
module, which really runs on top of sockets; nntplib also supports posting new
messages, etc.; note: posts not deleted after they are read;
"""

class nntpconfig:
    def __init__(self):
        pass
    servername = 'localhost'

listonly = False
showhdrs = ['From', 'Subject', 'Date', 'Newsgroups', 'Lines']
try:
    import sys
    servername, groupname, showcount = sys.argv[1:]
    showcount = int(showcount)
except:
    servername = nntpconfig.servername      # assign this to your server
    groupname = 'comp.lang.python'          # cmd line args or defaults
    showcount = 10                          # show last showcount posts

# connect to nntp server
from nntplib import NNTP
import nntplib, time
from io import StringIO

if input('Do you want to start the localhost NNTP Server? ') in ['y', 'Y']:
    import os
    pypath = sys.executable
    pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python3'
    cmdline = '../servers/pnntprss/nntpserver.py'
    os.spawnv(os.P_NOWAIT, pypath, (pyfile, cmdline))
    time.sleep(3)

print('Connecting to', servername, 'for', groupname)
connection = NNTP(servername, 4321)

if input('Do you want to post an article? ') in ['y', 'Y']:
    Name = input('Name: ') or ''
    Email = input('Email: ') or ''
    Link = input('Link: ') or ''
    Title = input('Title: ') or ''
    Summary = input('Summary: ') or ''
    Body = input('Main Text: ') or ''
    article = "'message_id': 0, "
    article += "'published_parsed': (%i, %i, %i, %i, %i, %i, %i, %i, %i), " % \
        time.localtime()
    article += "'author_detail': {'name': '%s', 'email': '%s'}, " % (Name, Email)
    article += "'link': '%s', 'title_detail': {'type': 'text/plain', " % Link
    article += "'value': '%s'}, 'summary_detail': '%s', " % (Title, Summary)
    article += "'content': [{'type': 'text/plain', 'value': '%s'},]" % Body
    f = StringIO("'Group': '%s'\n'Article': {%s}" % (groupname, article))
    resp = connection.post(f.read().encode())
    print(resp)

(reply, count, first, last, name) = connection.group(groupname)
print('%s has %s articles: %s-%s' % (name, count, first, last))

# get request headers only
if last > 0:
    fetchfrom = str(int(last) - ((showcount-1 < last and showcount-1) or last - 1))
    (reply, subjects) = connection.xhdr('subject', (fetchfrom + '-' + str(last)))
 
    # show headers, get message hdr+body
    for (id, subj) in subjects:                     # [-showcount:] if fetch all
        print('Article %s [%s]' % (id, subj))
        if not listonly and input('=> Display? ')in ['y', 'Y']:
            reply, art = connection.head(id)
            num, tid, list = art
            for line in list:
                for prefix in showhdrs:
                    if line.decode()[:len(prefix)] == prefix:
                        print(line.decode()[:80])
                        break
            if input('=> Show body? ') in ['y', 'Y']:
                reply, art = connection.body(id)
                num, tid, list = art
                for line in list:
                    print(line.decode()[:80])
        print()
print(connection.quit())
