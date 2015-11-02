#!/usr/bin/env python

"""Test for inequality

"""

import unittest


class InequalityTest(unittest.TestCase):
    def testEqual(self):
        self.failIfEqual(1, 3 - 2)

    def testNotEqual(self):
        self.failUnlessEqual(2, 3 - 2)


if __name__ == '__main__':
    unittest.main()
