#!/usr/bin/env python

"""Test for equality

"""

import unittest


class EqualityTest(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(1, 3 - 2)

    def testNotEqual(self):
        self.failIfEqual(2, 3 - 2)


if __name__ == '__main__':
    unittest.main()
