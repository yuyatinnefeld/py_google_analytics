#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# Google Analytics API Extractor
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""


import pytest
from oauth import setup_analytics
from google_analytics import (
    set_daterange, set_metrics, set_dimensions, ga_response_dataframe, get_response)


class TestGoogleAnalytics:

    def test_set_datarange(self):
        assert [{'startDate': '2020-01-01', 
                'endDate': '2020-02-01'}] == set_daterange('2020-01-01', '2020-02-01')

    def test_set_metrics(self):
        assert [{'expression': 'ga:zzzz'},
                {'expression': 'ga:yyyy'}] == set_metrics('ga:zzzz','ga:yyyy')

    def test_set_dimensions(self):
        assert [{'name': 'ga:xxxx'}] == set_dimensions('ga:xxxx')


    def test_setup_analytics(self):
        assert str(setup_analytics()).__contains__('googleapiclient')




if __name__ == '__main__':
    pytest.main()