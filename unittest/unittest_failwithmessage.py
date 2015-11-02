#!/usr/bin/env python

"""A test that fails with a custom message.

"""

import unittest


class FailureMessageTest(unittest.TestCase):
    def testFail(self):
        self.failIf(True, 'failure message goes here')


if __name__ == '__main__':
    unittest.main()
