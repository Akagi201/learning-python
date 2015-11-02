#!/usr/bin/env python

"""Test for truth

"""

import unittest


class TruthTest(unittest.TestCase):
    def testFailUnless(self):
        self.failUnless(True)

    def testAssertTrue(self):
        self.assertTrue(True)

    def testFailIf(self):
        self.failIf(False)

    def testAssertFalse(self):
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
