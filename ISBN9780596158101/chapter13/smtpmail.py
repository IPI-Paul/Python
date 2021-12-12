#!/usr/bin/env python3

# Example 13-19
# Is intended to be used from an interactive command line; it reads a new mail 
# message from the user and sends the new mail by SMTP using Python's smtplib 
# module
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-02-17

"""
################################################################################
use the Python SMTP mail interface module to send email messages; this is just a 
simple one-shot send script--see pymail, PyMailGUI, and PyMailCGI for clients 
with more user interaction features; also see popmail.py for a script that 
retrieves mail, and the mailtools pkg for attachments and formatting with the 
standard library emnail package;
################################################################################
"""

import smtplib, sys, email.utils, mailconfig, _thread as thread, time 
mailserver = mailconfig.smtpservername              # ex: smtp.rmi.net

def initiateSMTP():
    """
    Adds SMTP mail server on localhost to test SMTP mail
    """
    print('Initiating SMTP mail server...')
    host, port, mbox = mailconfig.smtpserver
    smtp = LocalSMTP(host, port, mbox)
    
if input('Do you want to start the localhost SMTP Server? ') in ['y', 'Y']:
    sys.path.append('..')
    from ipi.localsmtp import *
    thread.start_new_thread(initiateSMTP,())
    time.sleep(2)

From = input('From? ').strip()                      # or import from mailconfig
To = input('To? ').strip()                          # ex: python-list@python.org
Tos = To.split(';')                                 # allow a list of recipients
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()                     # curr datetime, rfc2822

# standard headers, followed by blank line, followed by text
text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Date, Subj))

print('Type message text, end with [END] or line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
while True:
    line = sys.stdin.readline()
    if not line:
        break                               # exit onb ctrl-d/z
    # if line[:4] == 'From':
    #     line = '>' + line                 # servers may escape
    text += line
    if 'END' in text:
        text = text.replace('END', '')
        break

print('Connecting...')
server = smtplib.SMTP(mailserver)           # connect, no log-in step
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:                                  # smtplib may raise exceptions
    print('Failed recipients:', failed)     # too, but let them pass here#
else:
    print('No errors.')
print('Bye')