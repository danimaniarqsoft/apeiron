# -*- coding: utf-8 -*-

from .context import apeiron

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(apeiron.forTest())


if __name__ == '__main__':
    unittest.main()
