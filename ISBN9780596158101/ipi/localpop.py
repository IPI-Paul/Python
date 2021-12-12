#!/usr/bin/env python3

# Example by IPI-Paul.
# This script acts as a simple POP3 server. A few additional functions have been 
# added to allow safe deletes and header downloads
# Author: Daniel Miller, Paul I Ighofose
# Last modified: 2019-02-15

"""
pypopper: a file-based pop3 server

Useage:
    python pypopper.py <port> <path to message file>
"""

import logging, os, socket, sys, traceback, time, poplib
from glob import glob
poplib._MAXLINE = 204800
sys.path.append('..')
from ipi.localsmtp import saveName
import chapter13.mailconfig as mailconfig

logging.basicConfig(format='%(name)s %(levelname)s - %(message)s')
log = logging.getLogger('localpop')
log.setLevel(logging.INFO)

class LocalPOP:
    def __init__(self, mbox, trace=False, fetchEncoding=None):
        self.mbox = mbox
        self.trace = trace
        self.fetchEncoding = fetchEncoding
        self.mcount = self.msize = 0
        self.mnum = ''
        self.dtxt = ''
        self.usr = '|'

    def handleUser(self, data, msg):
        return '+OK user accepted'
    
    def handlePass(self, data, msg):
        return '+OK pass accepted'
    
    def handleStat(self, data, msg):
        return '+OK %i %i' % (self.mcount, self.msize)
    
    def handleList(self, data, msg):
        return '+OK %i messages (%i octets)\r\n%s\r\n.' % (self.mcount, 
                                                           self.msize, 
                                                           self.mnum[:-1])
    
    def handleTop(self, data, msg):
        cmd, num, lines = data.split(None, 2)
        assert int(num) <= int(self.mcount), 'unknown message number: %s' % num
        lines = int(lines.split("'")[0]) - 1        
        if b'\r\n' in msg.top:
            text = msg.top + b'\r\n\r\n' 
            if lines >= 0: 
                text += b'\r\n'.join(msg.bot[:lines])
        else:
            text = msg.top + b'\n\n'
            if lines >= 0: 
                text += b'\n'.join(msg.bot[:lines])
        if self.trace:
            log.info('TOP %i %i' % (int(num), int(lines)))
        return '+OK top of message follows\r\n%s\r\n.' % text
    
    def handleRetr(self, data, msg):
        if self.trace:
            log.info('message sent')
        if msg: 
            return '+OK %i octets\r\n%s\r\n.' % (self.msize, msg.data)
        #return '+OK 0 octets\r\n''\r\n.'
    
    def handleDele(self, data, msg):
        messages = glob(os.path.abspath(self.mbox) + '/*' + self.usr + '*')
        try:
            self.dtxt = data.split(None, 2)[2][:-2]
        except:
            self.dtxt = None

        if self.dtxt:
            try:
                for file in messages:
                    if os.path.abspath(self.dtxt) == os.path.abspath(
                        os.path.join(self.mbox, file)):
                        os.remove(os.path.join(self.mbox, file))
                        if self.trace:
                            log.info('Deleted ' + self.dtxt)
                        break
            except Exception as ex:
                print(str(ex))
            return '+OK message %s deleted' % self.dtxt # self.mcount
        return '-Err message %s not found' % self.dtxt
    
    def handleNoop(self, data, msg):
        return '+OK'
    
    def handleQuit(self, data, msg):
        return '+OK localpop POP3 sever signing off'
    
    def getComm(self, conn, mbox, messages):
        dispatch = dict(
            USER    = self.handleUser,
            PASS    = self.handlePass,
            STAT    = self.handleStat,
            LIST    = self.handleList,
            TOP     = self.handleTop,
            RETR    = self.handleRetr,
            DELE    = self.handleDele,
            NOOP    = self.handleNoop,
            QUIT    = self.handleQuit,
            )
        multi = ['TOP', 'RETR', 'DELE']
        data = conn.recvall()
        comm = data.replace("[b'", ' ').replace("']", '')
        try:
            command = comm.split(None, 1)[0]
            try:
                num = int(comm.split(None, 2)[1])
            except:
                num = 0
            try:
                self.dtxt = comm.split(None, 4)[3]
            except:
                self.dtxt = ''
        except:
            command = comm.split(None, 1)[0]
            num = 0
        try:
            cmd = dispatch[command]
        except KeyError:
            conn.sendall('-ERR unknown command')
        else:
            if command in multi:
                idx = len(messages)
                for file in messages:
                    if num in (0, idx):
                        msg = popMessage(os.path.join(mbox, file), 
                                         self.trace)                                
                        conn.sendall(cmd(data, msg))
                    idx -= 1
            else:
                conn.sendall(cmd(data, None))
        return cmd
    
    def serve(self, host, port, mbox):
        self.mbox = mbox
        assert os.path.exists(mbox)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        try:
            if host:
                hostname = host
            else:
                hostname = mailconfig.popservername
            log.info('localpop POP3 serving "%s" on %s: %s', mbox, 
                          hostname, port)
            while True:
                sock.listen(5)
                conn, addr = sock.accept()
                if self.trace:
                    log.info('localpop Connected by %s', addr)
                try:
                    conn = ChatterboxConnection(conn)
                    conn.sendall('+OK localpop file-based pop3 server ready')
                    data = conn.recvall()
                    comm = data.replace("[b'", ' ').replace("']", '')
                    if comm.split(None, 1)[0] == 'USER': 
                        self.usr = saveName(comm.split(None, 1)[1])
                        conn.sendall(self.handleUser(data, None))
                    messages = glob(os.path.abspath(mbox) + '/*' + self.usr + '*')
                    self.mcount = len(messages)
                    fcount = 0
                    for file in messages:
                        fsize = os.path.getsize(os.path.join(mbox, file))
                        fcount += 1
                        self.mnum += str(fcount) + ' ' + str(fsize) + '\n'
                        self.msize += fsize
                    while True:
                        try:
                            cmd = self.getComm(conn, mbox, messages)
                            if cmd == self.handleQuit: 
                                break
                        except:
                            break
                finally:
                    conn.close()
                    msg = None
                    self.mnum = ''
                    self.msize = 0                  
                    if self.trace:
                        log.info('localpop Closed Connection')
        except (SystemExit, KeyboardInterrupt):
            log.info('localpop stopped')
        except Exception as ex:
            log.critical('fatal error', exc_info=ex)
        finally:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()

class ChatterboxConnection(object):
    END = '\r\n'    

    def __init__(self, conn):
        self.conn = conn
    
    def __getattr__(self, name):
        return getattr(self.conn, name)
    
    def sendall(self, data, END=END):
        if len(data) < 50:
            log.debug('send: %r...', data)
        else:
            log.debug('send: %r...', data[:50])
        data += END
        self.conn.sendall(data.encode())
    
    def recvall(self, END=END.encode()):
        data = []
        while True:
            chunk = self.conn.recv(4096)
            if END in chunk:
                data.append(chunk[:chunk.index(END)])
                break
            data.append(chunk)
            if len(data) > 1:
                pair = data[-2] + data[-1]
                if END in pair:
                    data[-2] = pair[:pair.index(END)]
                    data.pop()
                    break
        log.debug('recv: %r', ''.join(str(data)))
        return ''.join(str(data))

class popMessage(object):
    def __init__(self, file, trace):
        if os.path.exists(file):
            msg = open(file, 'rb')
            try:
                self.data = data = msg.read()
                if b'\r\n' in self.data:
                    self.data = b'File: ' + file.encode()  + b'\r\n' + self.data
                else:
                    self.data = b'File: ' + file.encode()  + b'\n' + self.data
                if trace: 
                    print(data)
                try:
                    self.top, bot = data.split(b'\r\n\r\n', 1)
                    self.top = b'File: ' + file.encode() + b'\r\n' + self.top
                    self.bot = bot.split(b'\r\n')
                except:
                    self.top, bot = data.split(b'\n\n', 1)
                    self.top = b'File: ' + file.encode() + b'\n' + self.top
                    self.bot = bot.split(b'\n')
            finally:
                msg.close()
        else:
            print('File Deleted!')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        host, port, mbox = mailconfig.popserver
    else:
        _, port, mbox = sys.argv
        if ':' in port:
            host = port[:port.index(':')]
            port = port[port.index(':')+1:]
        else:
            host = mailconfig.mailbox
    try:
        port = int(port)
    except Exception:
        print('Unknown port:', port)
    else:
        if os.path.exists(mbox):
            popsvr = LocalPOP(mbox, trace=True)
            popsvr.serve(host, port, mbox)
        else:
            print('Mailbox not found:', mbox)
            