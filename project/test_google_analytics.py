#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# PYTHON TEMPLATE
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""


import pytest
from google_analytics import set_daterange, set_metrics


class TestGoogleAnalytics:

    def test_set_datarange(self):
        assert [{'startDate': '2020-01-01', 
                'endDate': '2020-02-01'}] == set_daterange('2020-01-01', '2020-02-01')


    def test_set_metrics(self):
        assert [{"expression": 'ga:pageviews'},
                {"expression": 'ga:avgSessionDuration'}] == set_metrics('ga:pageviews','ga:avgSessionDuration')




if __name__ == '__main__':
    pytest.main()