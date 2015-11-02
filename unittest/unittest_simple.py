#!/usr/bin/env python

"""Simplistic examples of unit tests.

"""

import unittest
import time


class SimplisticTest(unittest.TestCase):
    def test(self):
        time.sleep(3)
        self.failUnless(True)


if __name__ == '__main__':
    unittest.main()
