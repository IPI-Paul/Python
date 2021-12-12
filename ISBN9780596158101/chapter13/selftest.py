#!/usr/bin/env python3

# Example 13-26
# Lists the self-test code for the mailtools package.
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-03-03

"""
################################################################################
self-test when this file is run as a program
################################################################################
"""

#
# mailconfig normally comes from the client's source directory or
# sys.path; for testing, get it from Email directory one level up
#
import sys, _thread as thread, time
sys.path.append('..')
import mailconfig
print('config:', mailconfig.__file__)

fetchEncoding = mailconfig.fetchEncoding
usingLocalPOP = False

def initiatePOP3():
    """
    Adds POP3 mail server on localhost to test POP mail
    """
    print('Initiating POP3 mail server...')
    host, port, mbox = mailconfig.popserver
    pop3 = LocalPOP(mbox, fetchEncoding=fetchEncoding)
    pop3.serve(host, port, mbox)

def initiateSMTP():
    """
    Adds SMTP mail server on localhost to test SMTP mail
    """
    print('Initiating SMTP mail server...')
    host, port, mbox = mailconfig.smtpserver
    smtp = LocalSMTP(host, port, mbox)
    
if input('Do you want to start the localhost POP3 Server? ') in ['y', 'Y']:
    from ipi.localpop import *
    thread.start_new_thread(initiatePOP3,())
    usingLocalPOP = True
    time.sleep(2)
if input('Do you want to start the localhost SMTP Server? ') in ['y', 'Y']:
    from ipi.localsmtp import *
    thread.start_new_thread(initiateSMTP,())
    time.sleep(2)

# get these from __init__
from chapter13 import (MailFetcherConsole,
                       MailSender, MailSenderAuthConsole,
                       MailParser)

if not mailconfig.smtpuser:
    sender = MailSender(tracesize=5000)
else:
    sender = MailSenderAuthConsole(tracesize=5000)

sender.sendMessage(From         = mailconfig.myaddress,
                   To           = [mailconfig.myaddress],
                   Subj         = 'testing mailtools package',
                   extrahdrs    = [('X-Mailer', 'mailtools')],
                   bodytext     = 'Here is my source code\n',
                   attaches     = ['selftest.py', 
                                   os.path.abspath('../sourceFiles/images/face.gif'),
                                   os.path.abspath('../sourceFiles/audio/ofthepeople.au'),
                                   os.path.abspath('../sourceFiles/app/spam.xlsx')],
                   )
                    # bodytextEncoding='utf-8',             # other tests to try
                    # attachesEncodings=['latin-1'],        # inspect text headers
                    # attaches=['monkeys.jpg')              # verify Base64 encoded
                    # to='i18n addr list...',               # test mime/unicode headers

# change mailconfig to test fetchlimit
fetcher = MailFetcherConsole()
def status(*args): print(args)

hdrs, sizes, loadedall = fetcher.downloadAllHeaders(status)
for num, hdr in enumerate(hdrs[:5]):
    print(hdr)
    if input('load mail? ') in ['y', 'Y']:
        print(fetcher.downloadMessage(num+1).rstrip(), '\n', '-'*70)

last5 = ((len(hdrs)-4) > 0 and len(hdrs)-4) or 1
msgs, sizes, loadedall = fetcher.downloadAllMessages(status, loadfrom=last5)
for msg in msgs:
    print(msg[:200], '\n', '-'*70)

parser = MailParser()
for i in range(0, len(msgs)):                       # try [0, len(msgs)]
    fulltext = msgs[i]
    message = parser.parseMessage(fulltext)
    ctype, maintext = parser.findMainText(message)
    print('Parsed:', message['Subject'])
    print(maintext)
input('Press Enter to exit')    # pause if clicked on Windows