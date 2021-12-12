#!/usr/bin/env python3

# Example 13-17
# This module is used to configure email parameters appropriately for a 
# particular user. 
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-02-16

"""
user configurtion settings for various email programs (pymail/mailtools version);
email scripts get their server names and other email config options from this 
module: change me to reflect your server names and mail preferences;
"""

#-------------------------------------------------------------------------------
# (required for load, delete: all) POP3 email server machine, user
#-------------------------------------------------------------------------------

popservername = 'localhost'                         # 'pop.secureserver.net'
popusername = 'paul@ipi-international.co.uk'        # 'PP4E@learning-python.com'

#-------------------------------------------------------------------------------
# (required for send: all) SMTP email sever machine name
# see Python smtpd module for a SMTP server class to run locally;
#-------------------------------------------------------------------------------

smtpservername = 'localhost'   # 'smtpout.secureserver.net'

#-------------------------------------------------------------------------------
# (optional: all) personale information used by clients to fill in mail if set;
# signature -- can be a triple-quoted block, ignored if empty string;
# address-- used for initial value of 'From' field if not empty,
# no longer tries to guess From for replies: this had varying success;
#-------------------------------------------------------------------------------

myaddress = 'paul@ipi-international.co.uk'
mysignature = 'Best Regards,\n\n' \
               'Paul I Ighofose\n' \
               'SQL Projects <a href="http://www.ipi-international.me.uk">' + \
               'http://www.ipi-international.me.uk</a>\n' \
               'Office Projects <a href="http://www.ipi-international.co.uk">' +\
               'http://www.ipi-international.co.uk</a>'


#-------------------------------------------------------------------------------
# (optional: mailtools) may be required for send; SMTP user/password if 
# authenticated; set user to None or '' if no login/authentication is 
# required; set pswd to name of a file holding your SMWP password, or an empty
# string to force programs to ask (in a console, or GUI);
#-------------------------------------------------------------------------------

smtpuser = None                             # per your ISP
smtppasswdfile = ''                         # set to '' to be asked

#-------------------------------------------------------------------------------
# (optional: mailtools) name of local one-line text file with your pop
# password; if empty or file cannot be read, pswd is requested when first
# connecting; pswd not encrypted; leave this empty on shared machines;
#-------------------------------------------------------------------------------

propfld = '../sourceFiles/mail settings/'
poppasswdfile = propfld + 'pymailgui.txt'           # set to '' to be asked

#-------------------------------------------------------------------------------
# (required: mailtools) local file where sent messages are saved by some clients;
#-------------------------------------------------------------------------------

sentmailfile = propfld + 'sentmail.txt'     # . means in current working dir

#-------------------------------------------------------------------------------
# (required: pymail, pymail2) local file where pymail saves pop mail on request;
#-------------------------------------------------------------------------------

savemailfile = propfld + 'savemail.txt'     # not used in PyMailGUI: dialog

#-------------------------------------------------------------------------------
# (required: pymail, mailtools) fetchEncoding is the Unicode encoding used to 
# decode fetched full message bytes, and to encode and decode message text if
# stored in text-mode save files; see Chapter 13 for details: this is a limited 
# and temporary approach to Unicode encodings until a new bytes-friendly email
# package is developed; headersEncodeTo is for sent headers: see chapter13;
#-------------------------------------------------------------------------------

fetchEncoding = 'utf8'      # 4E: how to decode and store message text (or latin1?)
headersEncodeTo = None      # 4E: how to encode non-ASCII headers sent (None=utf8)

#-------------------------------------------------------------------------------
# (optional: mailtools) the maximum number of mail headers or messages to 
# download on each load request; given this setting N, mailtools fetches at 
# most N of the most recently arrived mails; older mails outside this set are 
# not fetched from the server, but are returned as empty/dummy emails; if this 
# is assigned to None (or 0), loads will have no such limit; use this if you 
# have very many mails in your inbox, and your Internet or mail server speed 
# makes full loads too slow to be practical; some clients also load only
# newly-arrived emails, but this setting is independent of that feature;
#-------------------------------------------------------------------------------

fetchlimit = 25         # 4E: maximum number headers/emails to fetch on loads

"""
Additional settings for use with servers
"""
mailbox = '../sourceFiles/mailbox'
popserverport = 110
smtpserverport = 25
popserver = (popservername, popserverport, mailbox)
smtpserver = (smtpservername, smtpserverport, mailbox)