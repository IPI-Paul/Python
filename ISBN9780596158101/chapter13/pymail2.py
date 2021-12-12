#!/usr/bin/env python3

# Example 13-27
# Provides an updated version of the pymail program
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-03-03

"""
################################################################################
pymail2 - simple console email interface client in Python; this version uses the 
mailtools package, which in turn uses poplib, stmplib, and the email package for 
parsing and composing emails; displays first text part of mails, not the entire 
full text; fetches just mail headers initially, using the TOP command; fetches 
full text of just email selected to be displayed; caches already fetched mail;
caveat: no way to refresh index; uses standalone mailtools objects - they can 
also be used as superclasses;
################################################################################
"""

import sys
sys.path.append('..')
import mailconfig, chapter13 as mailtools, _thread as thread, time
from pymail import inputmessage, usingLocalPOP, delList, fetchEncoding
mailcache = {}

def progress(i, max):
    print(i, 'of', max)

def loadmessages(progress):
    mailfile = mailconfig.savemailfile
    hdrsList, msgSizes, ignore = fetcher.downloadAllHeaders(progress)
    msgList = [parser.parseHeaders(hdrtext) for hdrtext in hdrsList]
    if usingLocalPOP:
        for i in range(len(msgList)):
            delList[i+1] = msgList[i].get('File')    
    
    print('[Pymail email client]')
    showindex(msgList, msgSizes)
    toDelete = interact(msgList, msgSizes, mailfile)
    if toDelete: deletemessages(toDelete)

def fetchmessage(i):
    try:
        fulltext = mailcache[i]
    except KeyError:
        fulltext = fetcher.downloadMessage(i)
        mailcache[i] = fulltext
    return fulltext

def sendmessage():
    From, To, Subj, text = inputmessage()
    attaches = []
    while True:
        file = None
        file = input('Please give path and filename to attach: ')
        if file:
            file = os.path.abspath(file)
            if not os.path.exists(file):
                print('The file does not exist:', file)
            else:
                attaches.append(file)
        else:
            break
    sender.sendMessage(From, To, Subj, [], text, attaches)

def deletemessages(toDelete, verify=True):
    print('To be deleted:', toDelete)
    if verify and input('Delete? ')[:1] not in ['y', 'Y']:
        print('Delete cancelled.')
    else:
        print('Deleting messages from server...')
        if usingLocalPOP:
            fetcher.deleteMessages(toDelete, delList=delList)
        else:
            fetcher.deleteMessages(toDelete)

def showindex(msgList, msgSizes, chunk=5):
    count = 0
    for (msg, size) in zip(msgList, msgSizes):      # email.message.Message, int
        count += 1                                  # 3.xiter ok here
        print('%d:\t%d bytes' % (count, size))
        for hdr in ('From', 'To', 'Date', 'Subject'):
            print('\t%-8s=>%s' % (hdr, msg.get(hdr, '(unknown)')))
        if count % chunk == 0:
            input('[Press Enter Key]')              # pause after each chunk

def showmessage(i, msgList):
    if 1 <= i <= len(msgList):
        fulltext = fetchmessage(i)
        message = parser.parseMessage(fulltext)
        ctype, maintext = parser.findMainText(message)
        print('-' * 79)
        print(maintext.rstrip() + '\n')         # main text part, not entire mail
        print('-' * 79)                         # and not any attachments after
    else:
        print('Bad message number')

def savemessage(i, mailfile, msgList):
    if 1 <= i <= len(msgList):
        fulltext = fetchmessage(i)
        savefile = open(mailfile, 'a', encoding=fetchEncoding)  # 4E
        savefile.write('\n' + fulltext + '-'*80 + '\n')
    else:
        print('bad message number')

def msgnum(command):
    try:
        return int(command.split()[1])
    except:
        return -1   # assume this is bad

helptext = """
Available commands:
Available commands:
i     - index display
l n?  - list all messages (or just message n)
d n?  - mark all messages for deletion (or just message n)
s n?  - save all messages to a file (or just message n)
m     - compose and send a new mail message
r     - reload pymail
q     - quit pymail
?     - display this help text
"""

def interact(msgList, msgSizes, mailfile):
    toDelete = []
    while True:
        try:
            command = input('[Pymail] Action? (i, l, d, s, m, r, q, ?) ')
        except EOFError:
            command = 'q'
        if not command: command = '*'
        if command in ['r', 'q']:                          # quit
            break
        elif command[0] == 'i':                     # index
            showindex(msgList, msgSizes)
        elif command[0] == 'l':                     # list
            if len(command) == 1:
                for i in range(1, len(msgList)+1):
                    showmessage(i, msgList)
            else:
                showmessage(msgnum(command), msgList)
        elif command[0] == 's':                     # save
            if len(command) == 1:
                for i in range(1, len(msgList)+1):
                    savemessage(i, mailfile, msgList)
            else:
                savemessage(msgnum(command), mailfile, msgList)
        elif command[0] == 'd':                     # mark for deletion later
            if len(command) == 1:                   # 3.x needs list(): iter
                toDelete = list(range(1, len(msgList)+1))
            else:
                delnum = msgnum(command)
                if (1 <= delnum <= len(msgList)) and (delnum not in toDelete):
                    toDelete.append(delnum)
                else:
                    print('Bad message number')
        elif command == 'm':                        # send a new mail via SMTP
            try:
                sendmessage()
            except:
                print('Error - mail not sent')
        elif command[0] == 'r':
            break
        elif command[0] == '?':
            print(helptext)
        else:
            print('What? -- type "?" for commands help')
    if command[0] == 'r':
        if toDelete: 
            deletemessages(toDelete)
            toDelete = []
        loadmessages(progress)
    return toDelete

def main():
    global parser, sender, fetcher
    mailserver = mailconfig.popservername
    mailuser = mailconfig.popusername
    
    parser = mailtools.MailParser()
    sender = mailtools.MailSender(tracesize=5000)
    fetcher = mailtools.MailFetcherConsole(mailserver, mailuser)
    
    loadmessages(progress)
    
if __name__ == '__main__': main()