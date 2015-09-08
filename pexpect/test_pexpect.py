#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: test_pexpect.py

import pexpect

if __name__ == '__main__':
    user = 'mm'
    ip = '192.168.2.8'
    mypassword = 'xxxx'

    # print user
    # child = pexpect.spawn('ssh %s@%s' % (user, ip))
    # child.expect('password:')
    # child.sendline(mypassword)

    # child.expect('$')
    # child.sendline('sudo -s')
    # child.expect(':')
    # child.sendline(mypassword)
    # child.expect('#')
    # child.sendline('ls -la')
    # child.expect('#')
    child = pexpect.spawn("ls -al")
    # child.sendline('ls -al')
    child.expect(pexpect.EOF)
    print child.before  # Print the result of the ls command.
    # child.sendline("echo '112' >> /home/mm/1.txt ")
    child.interact()  # Give control of the child to the user.

    print("lost")
