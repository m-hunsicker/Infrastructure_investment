# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:09:16 2018

@author: michel_hunsicker@yahoo.fr
"""

import unittest

from utils import is_subperiod, is_superperiod


class TestAggregator(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_subperiod(self):
        self.assertFalse(is_subperiod('3M', 'M'))
        self.assertTrue(is_subperiod('M', '3M'))
        self.assertTrue(is_subperiod('Y', '2Y'))
        self.assertFalse(is_subperiod('T', 'S'))

    def test_is_superperiod(self):
        self.assertTrue(is_superperiod('3M', 'M'))
        self.assertFalse(is_superperiod('M', '3M'))
        self.assertFalse(is_superperiod('Y', '2Y'))
        self.assertTrue(is_superperiod('T', 'S'))


if __name__ == '__main__':
    unittest.main()
