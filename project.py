#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:31:21 2018

@author: mitch
"""


class Project(object):
    def __init__(self, name):
        self.name = name
        self.phase_list = []

    def get_time_series(self):
        pass

    def get_PnL(self):
        pass

    def get_BalanceSheet(self):
        pass

    def get_CFS(self):
        pass


class Time_Series(object):
    def __init__(self, date_start, step, duration):
        data = []
        date_end = date_start + duration


class PNL(object):
    pass


class financial_component(object):
    category_type_list = []
    level = []
    category_financial_list = [{1: 'P&L'}, {2: 'Balance Sheet'},
                               {3: 'Cash Flow Statement'}]

    def _init_(self, name, category_type, category_cash=[], children=[]):
        self.name = name
        self.category_type = category_type
        self.children = children


class base_hypothesis(object):
    category_type_list = []

    def _init_(self, name, category_type):
        self.name = name
        self.category_type = category_type
        self.children = children


print("Ca marche")
