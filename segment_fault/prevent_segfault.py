#!/usr/bin/env python

import subprocess

# subprocess.call(["python", "test_segfault.py"])

child = subprocess.Popen(["python", "test_segfault.py"], stdout=subprocess.PIPE)

# child = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)

child.wait()

print("parent process")

# print("child.stdin: %s" % child.stdin)
if child.returncode < 0:
    print("child.returncode: %s" % child.returncode)
    print("child segment fault")
else:
    print("child.stdout: %s" % child.stdout.read())
# print("child.stderr: %s" % child.stderr.read())
