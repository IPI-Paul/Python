#!/usr/bin/env python3

# Example 13-5
# Uses Storbinary such that the file whose name is passed in is always uploaded
# vebatim--in binary mode, without Unicode encodings or line-feed translations
# for the target machine's conventions
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-02-08

"""
Store an arbitrary file by FTP in binary mode. Uses anonymous ftp unless you pass
in a user=(name, pswd) tuple of arguments.
"""

import os
import ftplib                       # socket-based FTP tools

def putfile(file, site, dir, user=(), *, verbose=True):
    """
    store a file by ftp to a site/directory
    anonymous or real login, binary transfer
    """
    if verbose: print('Uploading', file)
    local = open(file, 'rb')                # local file of same name
    remote = ftplib.FTP(site)               # connect to FTP site
    remote.login(*user)                     # anonymous or real login
    remote.cwd(dir)
    remote.storbinary('STOR ' + os.path.basename(file), local, 1024)
    remote.quit()
    local.close()
    if verbose: print('Upload done.')

if __name__ == '__main__':
    site = 'localhost'
    dir = 'Python/ISBN9780596158101/sourceFiles/images'
    import sys, getpass
    usr = input('User Name: ')
    pswd = getpass.getpass(site + ' pswd?')             # filename on cmdline
    putfile(sys.argv[1], site, dir, user=(usr, pswd))    # nonanonymous login