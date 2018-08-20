#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:09:16 2018

@author: michel_hunsicker@yahoo.fr
"""

import unittest

import pandas as pd

from aggregator import Aggregator, Operator
from component import Component, Type1, Type2, Category


class TestAggregator(unittest.TestCase):

    def setUp(self):
        self.idx_1 = pd.period_range('2017-07-01', periods=5, freq='M')

        self.comp_1 = Component("Comp_1", Type1.QUANTITY, Type2.FINANCIAL, Category.HYPOTHESIS, "$")
        self.comp_1.data = pd.Series([1, 2, 3, 4, 5], index=self.idx_1)

        self.comp_2 = Component("Comp_2", Type1.QUANTITY, Type2.FINANCIAL, Category.COMPUTED, "$")
        self.comp_2.data = pd.Series([5, 4, 3, 2, 1], index=self.idx_1)

        self.comp_3 = Component("Comp_3", Type1.QUANTITY, Type2.FINANCIAL, Category.HYPOTHESIS, "$")
        self.comp_3.data = pd.Series([2, 2, 2, 2, 2], index=self.idx_1)

        self.comp_parent = Component("Parent", Type1.QUANTITY, Type2.FINANCIAL, Category.COMPUTED, "$")

    def test_add(self):
        print("Operator est de type: ", type(Operator))
        agg = Aggregator(self.comp_parent, [self.comp_1, self.comp_2, self.comp_3], Operator.ADD)
        agg.aggregate()
        self.assertEqual(self.comp_parent.data.equals(pd.Series([8, 8, 8, 8, 8], index=self.idx_1)), True)

    def test_sub(self):
        agg = Aggregator(self.comp_parent, [self.comp_2, self.comp_3], Operator.SUB)
        agg.aggregate()
        self.assertEqual(self.comp_parent.data.equals(pd.Series([3, 2, 1, 0, -1], index=self.idx_1)), True)

    def test_mul(self):
        agg = Aggregator(self.comp_parent, [self.comp_1, self.comp_2, self.comp_3], Operator.MULT)
        agg.aggregate()
        self.assertEqual(self.comp_parent.data.equals(pd.Series([10, 16, 18, 16, 10], index=self.idx_1)), True)

    def test_div(self):
        agg = Aggregator(self.comp_parent, [self.comp_1, self.comp_3], Operator.DIV)
        agg.aggregate()
        self.assertEqual(self.comp_parent.data.equals(pd.Series([0.5, 1, 1.5, 2, 2.5], index=self.idx_1)), True)

    def test_check_operator(self):
        """
        This test is not working because the Exception is not caught by the context : TO BE CORRECTED
        :return: None
        """
        with self.assertRaises(ValueError): Aggregator(self.comp_parent, [self.comp_1, self.comp_3], 'Invalid_Code')


if __name__ == '__main__':
    unittest.main()
