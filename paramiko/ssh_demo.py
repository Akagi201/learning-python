#!/usr/bin/env python

import sys, paramiko

if len(sys.argv) < 5:
    print "args missing"
    sys.exit(1)

hostname = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]

port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())

    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print stdout.read()

finally:
    client.close()
