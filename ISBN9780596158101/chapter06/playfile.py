#!/usr/bin/env python3

# Example 6-23
# Puts into code how operating systems map file extension types to handler programs
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
Try to play an arbitrary media file. Allows for specific players instead of 
always using general web browser scheme. May not work on your system as is; 
audio files use filters and command lines on Unix, and filename associations on 
Windows via the start command(i.e., whatever you have on your machine to run .au 
files--an audio player, or perhaps aweb brower). Configure and extend as needed. 
playknownfile assumes you know what sort of media you wish to open, and playfile 
tries to determine media type automatically using Python mimetypes module; both 
try to launch a web browser with Python webbrowser module as a last resort when 
mimetype or platform unknown
################################################################################
"""

import os, sys, mimetypes, webbrowser

helpmsg = """
Sorry: can't find a media player for '%s' on your system!
Add an entry for your system to the media player dictionary
for this type of file in playfile.py, or play the file manually.
"""

def trace(*args): print(*args)          # with specs between

################################################################################
# player techniques: generic and otherwise
################################################################################

class MediaTool:
    
    def __init__(self, runtext=''):
        self.runtext = runtext
        
    def run(self, mediafile, **options):            # most ignore options
        fullpath = os.path.abspath(mediafile)       # cwd may be anything
        self.open(fullpath, **options)

class Filter(MediaTool):
    
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w')        # spwan shell tool
        player.write(media.read())                  # send to its stdin

class Cmdline(MediaTool):
    
    def open(self, mediafile, **ignored):
        cmdline = self.runtext % mediafile          # run any cmd line
        os.system(cmdline)                          # use %s for filename

class Winstart(MediaTool):                         # use Windows registry
    def open(self, mediafile, wait=False, **other):# or os.system('start file')
        if not wait:                               # allow wait for curr media
            os.startfile(mediafile)
        else:
            os.system('start /WAIT ' + mediafile)

class Webbrowser(MediaTool):
    
    # file::// requires abs path
    def open(self, mediafile, **options):
        webbrowser.open_new('file://%s' % mediafile, **options)
        
################################################################################
# media- and platform-specific policies: change me, or pass one in
################################################################################

# map platform to player: change me!

audiotools = {
    'cygwin':    Cmdline('xplayer %s'),
    'sun0s5':  Filter('/usr/bin/audioplay'),       # os.popen().write()
    'linux2':   Cmdline('cat %s > /dev/audio'),     # on zaurus, at least
    'sunos4':   Filter('/usr/demo/SOUND/play'),     # yes, this is that old!
    'win32':     Winstart(),                         # startfile or system
    #'win32':    Cmdline('start %s')
    }

videotools = {
    'cygwin':   Cmdline('xplayer %s'),  
    'linux2':   Cmdline('tkcVideo_c700 %s'),           # zaurus pda
    'win32':    Winstart()
    }

imagetools = {
    'cygwin':   Cmdline('lximage-qt %s'),  
    'linux2':   Cmdline('zimager %s'),                   # zaurus pda
    'win32':    Winstart()
    }

texttools = {
    'cygwin':   Cmdline('ted %s'),  
    'linux2':   Cmdline('vi %s'),                   # zaurus pda
    'win32':    Cmdline('notepad %s')    
    }

apptools = {
    'cygwin':   Cmdline('gio open %s'),  
    'win32':    Winstart()          # doc, xls, etc: use at your own risk!
    }

calctools = {
    'cygwin':   Cmdline('gnumeric %s'),  
    'win32':    Winstart()          # doc, xls, etc: use at your own risk!
    }

doctools = {
    'cygwin':   Cmdline('focuswriter %s'),  
    'win32':    Winstart()          # doc, xls, etc: use at your own risk!
    }

# map mimetype of filenames to player tables

mimetable = {
    'audio':        audiotools,
    'video':        videotools,
    'image':        imagetools,
    'text':         texttools,                  # not html text: browser
    'application':   apptools
    }

################################################################################
# top-level interfaces
################################################################################

def trywebbrowser(filename, helpmsg=helpmsg, **options):
    """
    try to open a file in a web browser
    last resort if unkwnown mimetype or platform, and for text/html
    """
    trace('trying browser', filename)
    try:
        player = Webbrowser()                   # open in local browser
        player.run(filename, **options)
    except:
        print(helpmsg % filename)               # else nothing worked

def playknownfile(filename, playertable={}, **options):
    """
    play media file of known type: uses platform-specific player objects, or 
    spawns a web browser if nothing for this platform; accepts a media-specific
    player table
    """
    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options)      # specific tool
    else:
        trywebbrowser(filename, **options)                      # general scheme

def playfile(filename, mimetable=mimetable, **options):
    """
    play media file of any type: uses mimetypes to guess media type and map to 
    platform-specific player tables; spawn web browser if text/html, media type
    unknown, or has no table
    """
    contenttype, encoding = mimetypes.guess_type(filename)       # check name
    if contenttype == None or encoding is not None:             # can't guess
        contenttype = '?/?'                                     # poss .txt.gz
    maintype, subtype = contenttype.split('/', 1)               # 'image/jpeg'
    if maintype == 'text' and subtype == 'html':
        trywebbrowser(filename, **options)                      # special case
    elif maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options) # try table
    else:
        trywebbrowser(filename, **options)                      # other types

################################################################################
# self-test code
################################################################################

if __name__ == '__main__':
    # media type known
    src = '../sourcefiles/'
    playknownfile(src + 'audio/ofthepeople.au', audiotools, wait=True)
    playknownfile(src + 'images/tk.gif', imagetools, wait=True)
    playknownfile(src + 'images/queen-of-hearts.jpg', imagetools)
    playknownfile(src + 'app/spam.docx', doctools)
    playknownfile(src + 'app/spam.xlsx', calctools)
    
    # media type guessed
    input('stop players and press Enter')
    playfile(src + 'images/queen-of-hearts.jpg')        # image/jpeg
    playfile(src + 'images/tk.gif')                     # image/gif
    playfile(src + 'html/ch01-cgi101.html')             # text/html
    playfile(src + 'html/ch01-peoplecgi.html')          # text/html
    playfile(src + 'text/ch04-hillbillies.txt')         # text/plain
    playfile(src + 'app/spam.docx')                     # app
    playfile(src + 'app/spam.xlsx')                     # app
    playfile(src + 'audio/ofthepeople.au', wait=True)  # audio/basic
    input('Done')                                       # stay open if clicked