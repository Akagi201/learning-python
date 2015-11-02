#!/usr/bin/env python

"""Demonstrate possible test outcomes

"""

import unittest


class OutcomesTest(unittest.TestCase):
    def testPass(self):
        return

    def testFail(self):
        self.failIf(True)

    def testError(self):
        raise RuntimeError('Test error!')


if __name__ == '__main__':
    unittest.main()
