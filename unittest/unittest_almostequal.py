#!/usr/bin/env python

"""Test for near equality

"""

import unittest


class AlmostEqualTest(unittest.TestCase):
    def testNotAlmostEqual(self):
        self.failIfAlmostEqual(1.1, 3.3 - 2.0, places=1)

    def testAlmostEqual(self):
        self.failUnlessAlmostEqual(1.1, 3.3 - 2.0, places=0)


if __name__ == '__main__':
    unittest.main()
