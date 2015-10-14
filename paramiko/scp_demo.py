#!/usr/bin/env python

import sys, paramiko

if len(sys.argv) < 6:
    print "args missing"
    sys.exit(1)

hostname = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
source = sys.argv[4]
dest = sys.argv[5]

port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(source, dest)

finally:
    t.close()
