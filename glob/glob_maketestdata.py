#!/usr/bin/env python

"""Create test data for the glob examples.

"""
import os


def mkfile(filename):
    print filename
    f = open(filename, 'wt')
    try:
        f.write('\n')
    finally:
        f.close()


print 'dir'
os.mkdir('dir')

mkfile('dir/file.txt')
mkfile('dir/file1.txt')
mkfile('dir/file2.txt')
mkfile('dir/filea.txt')
mkfile('dir/fileb.txt')

print 'dir/subdir'
os.mkdir('dir/subdir')

mkfile('dir/subdir/subfile.txt')
