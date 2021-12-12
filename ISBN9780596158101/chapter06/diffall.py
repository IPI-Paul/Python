#!/usr/bin/env python3

# Example 6-12
# Is a tree walker that applies dirdiff at each level to report unique items, 
# explicitly compares the contents of files in common, and decends through 
# directories in common
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-08

"""
################################################################################
Usage: 'python diffall.py dir1 dir2'.
Recursive directory tree comparison: report unique files that exist in only dir1 
or dir2, report files of same name in dir1 and dir2 with differing contents, 
report instances of same name but different type in dir1 and dir2, and do the 
sames for all subdirectories of the same names in and below dir1 and dir2. A 
summary of diffs appears at end of output, but search redirected output for 'DIFF'
and 'unique' strings for further details. New: (3E) limit reads to 1M for large 
files, (3E) catch same name=file/dir, (4E) avoid extra os.listdir() calls in 
dirdiff.comparedirs() by passing results here along.
################################################################################
"""

import os, dirdiff, sys
sys.path.append('..')
blocksize = 1024 * 1024                 # up to 1M per read

def intersect(seq1, seq2):
    """
    Return all items in both seq1 and seq2; a set(seq1) & set(seq2) would work 
    too, but seta are randomly oredered, so any platform-dependent directory 
    order would be lost
    """
    return [item for item in seq1 if item in seq2]

def comparetrees(dir1, dir2, diffs, verbose=False):
    """
    Compare all subdirectories and files in two directory trees; uses binary 
    files to prevent Unicode decoding and endline transforms, as trees might 
    contain arbitrary binary files as well as arbitrary test; may need bytes 
    listdir arg for undecodable filenames on some platforms
    """
    # compare file name lists
    print('-' * 20)
    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)
    if not dirdiff.comparedirs(dir1, dir2, names1, names2):
        diffs.append('unique files at %s - %s' % (dir1, dir2))
    
    print('Comparing contents')
    common = intersect(names1, names2)
    missed = common[:]
    
    # compare contents of files in common
    for name in common:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)
        if os.path.isfile(path1) and os.path.isfile(path2):
            missed.remove(name)
            file1 = open(path1, 'rb')
            file2 = open(path2, 'rb')
            while True:
                bytes1 = file1.read(blocksize)
                bytes2 = file2.read(blocksize)
                if (not bytes1) and not(bytes2):
                    if verbose: print(name, 'matches')
                    break
                if bytes1 != bytes2:
                    diffs.append('files differ at %s - %s' % (path1, path2))
                    print(name, 'DIFFERS')
                    break
    # recur to compare directories in common
    for name in common:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)
        if os.path.isdir(path1) and os.path.isdir(path2):
            missed.remove(name)
            comparetrees(path1, path2, diffs, verbose)
    # same name but not both files or dirs?
    for name in missed:
        diffs.append('files missed at %s - %s: %s' % (dir1, dir2, name))
        print(name, 'DIFFERS')

if __name__ == '__main__':
    """
    locate ipi modules folder and import backup utility
    """
    from ipi.runtime_backup import backup, removeBackup, runtimeBackup  
    # backup(sys.argv[0])
    runtimeBackup('b', sys.argv[0])
    dir1, dir2 = dirdiff.getargs()
    diffs = []
    comparetrees(dir1, dir2, diffs, True)           # changes diffs in-place
    print('=' * 40)                                 # walk, report diffs list
    if not diffs:
        print('No diffs found.')
    else:
        print('Diffs found:', len(diffs))
        for diff in diffs: print('-', diff)
    # removeBackup(sys.argv[0])
    runtimeBackup('r', sys.argv[0])
