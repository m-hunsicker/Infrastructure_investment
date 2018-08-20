#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:31:21 2018

@author: mitch
"""

import pandas as pd
from pandas.tseries.frequencies import to_offset


def is_subperiod(initial_freq, target_freq):
    """
    Test whether initial_freq has a lower duration than target_freq .This function was necessary since the pandas
    pd.tseries.frequencies.is_subperiod does not work for example for 'M' and '3M'.
    The idea was
    :param initial_freq: Pandas freq.
    :param target_freq: Pandas freq.
    :return: True when initial_freq lower than target_freq
    """
    base_dt = pd.to_datetime("2000-01-01")
    first_date = base_dt + to_offset(initial_freq)
    second_date = base_dt + to_offset(target_freq)
    return first_date < second_date


def is_superperiod(initial_freq, target_freq):
    """
    Test whether initial_freq has a higher duration than target_freq .This function was necessary since the pandas
    pd.tseries.frequencies.is_subperiod does not work for example for 'M' and '3M'.
    The idea was
    :param initial_freq: Pandas freq.
    :param target_freq: Pandas freq.
    :return: True when initial_freq higher than target_freq
    """
    base_dt = pd.to_datetime("2000-01-01")
    first_date = base_dt + to_offset(initial_freq)
    second_date = base_dt + to_offset(target_freq)
    return first_date > second_date

# class Project(object):
#     def _init_(self,name):
#         self.name = name
#         self.components = []
#
#     def get_time_series(self):
#         pass
#
# class Stage(object):
#     def _init_(self, name, period_step, duration, previous = None, ):
#         """
#         date_start: beginning of the time series
#         step: period size in months
#         duration: number of periods
#         """
#         self.name = name
#         self.previous = None
#         if previous != None:
#             self.time_series = Time_Series(previous.date_end + 1, time_step)
#
#         elif date_start != None:
#             self.time_series = Time_Series(previous.date_end + 1, time_step)
#         else:
#             raise Exception("Start date cours not be initiated")#
#
# class financial_component(object):
#     category_type_list = {1:'Physical', 2:'Financial'}
#     category_financial_list = {1:'P&L', 2:'Balance Sheet', 3:'Cash Flow Statement'}
#     def _init_(self, name, category_type, category_cash = [], children = []):
#         self.name = name
#         self.category_type = category_type
#         self.children = children
#
# class base_hypothesis(object):
#     category_type_list = {1:'Physical', 2:'Financial'}
#     category_type_list = []
#
#     def _init_(self, name, category_type):
#         self.name = name
#         self.category_type = category_type
#         self.children = children
