#!/usr/bin/env python3

# Example by IPI-Paul.
# This script acts as a simple STMP server
# Author: Jedi Shadow, Hasen, Paul I Ighofose
# Last modified: 2019-02-15

import asyncore, sys, os
from smtpd import SMTPServer
from datetime import datetime
sys.path.append('..')
import chapter13.mailconfig as mailconfig

def saveName(recip):
    recip = recip.split()[-1].replace('<', '').replace('>', '')
    contact = recip.split('@')[0].replace('.', ' ')
    domain = recip.split('@')[1].replace('.', '_')
    return (contact + ' ' + domain).replace("'", '').replace('"', '')

class LocalSMTP:
    def __init__(self, host, port, mbox, trace=False):
        self.server = smtpServer((host, port), mbox, trace)
        print('localsmtp SMTP Server now listening on %s port %i!' % (host, port))
        try:
            asyncore.loop()
        except Exception as ex:
            print(str(ex))

class smtpServer(SMTPServer):
    no = 0
    def __init__(self, args, mbox, trace=False):
        self.trace = trace
        self.mbox = mbox
        SMTPServer.__init__(self, args, None)
        
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        if self.trace:
            print('Receiving message from:', peer)
            print('Message Addressed From:', mailfrom)
            print('Messages Addressed To:', rcpttos)
            print('Message Length:', len(data))
        for recips in rcpttos:
            recip = saveName(recips)
            filename = '%s %s-%d.msg' % (recip, datetime.now().strftime('%Y%m%d %H%M%S'),
                                      self.no)
            f = open(os.path.join(self.mbox, filename), 'wb')
            f.write(data)
            f.close()
            if self.trace:
                print('%s saved.' % filename)
        self.no += 1
        return
    
if __name__ == '__main__': 
    host, port, mbox = mailconfig.smtpserver
    LocalSMTP(host, port, mbox, trace=True)