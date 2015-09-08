#!/usr/bin/env python2

# -*- coding: utf-8 -*-

import pexpect

# (current) UNIX password:
def change_password(old_passwd, new_passwd):
    child = pexpect.spawn('passwd')
    child.expect('(current).*:')
    child.sendline(old_passwd)
    child.expect('New password.*:')
    child.sendline(new_passwd)
    child.expect('Retype new password.*:')
    child.sendline(new_passwd)

def change_password2(old_passwd, new_passwd):
    child = pexpect.spawn('passwd')
    i = child.expect(['[Oo]ld [Pp]assword', '.current.*password', '[Nn]ew [Pp]assword'])

    # Root does not require old password, so it gets to bypass the next step.
    if i == 0 or i == 1:
        child.sendline(old_passwd)
        child.expect('[Nn]ew [Pp]assword')

    child.sendline(new_passwd)
    i = child.expect(['[Nn]ew [Pp]assword', '[Rr]etype', '[Rr]e-enter'])

    if i == 0:
        print('Host did not like new password. Here is what it said...')
        print(child.before)
        child.send(chr(3)) # Ctrl-C
        child.sendline('') # This should tell remote passwd command to quit.
        return
    child.sendline(new_passwd)
    child.expect(pexpect.EOF)

def main():
    change_password2('howcute121', 'howcute222')

if __name__ == '__main__':
    main()
