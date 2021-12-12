#!/usr/bin/env python3

# Example by IPI-Paul.
# Used to intiate POP3 and SMTP local host servers 
# Author: Paul I Ighofose
# Last modified: 2019-03-18 

import os, sys, _thread as thread, time
sys.path.append('../chapter13')
import mailconfig
from localpop import *
from localsmtp import *

def initiatePOP3():
    """
    Adds POP3 mail server on localhost to test POP mail
    """
    print('Initiating POP3 mail server...')
    host, port, mbox = mailconfig.popserver
    pop3 = LocalPOP(mbox, trace=False)
    pop3.serve(host, port, mbox)

def initiateSMTP():
    """
    Adds SMTP mail server on localhost to test SMTP mail
    """
    print('Initiating SMTP mail server...')
    host, port, mbox = mailconfig.smtpserver
    smtp = LocalSMTP(host, port, mbox, trace=False)


if __name__ == '__main__':
    print('Initiating POP3 and SMTP mail servers')
    child = []
    if sys.platform[:3] == 'win':
        thread.start_new_thread(initiatePOP3,())
        thread.start_new_thread(initiateSMTP,())
    else:
        pid = os.fork()
        if pid == 0:
            initiatePOP3()
        child.append(pid)
        pid = os.fork()
        if pid == 0:
            smtp = initiateSMTP()
        child.append(pid)
    time.sleep(3)
    input('Press any key to quit:\n')
    if not sys.platform[:3] == 'win': 
        for pid in child:
            os.system('kill -9 %i' % pid)