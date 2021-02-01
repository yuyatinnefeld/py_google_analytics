#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# Google Analytics API Extractor
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""


from decouple import config
from oauth import setup_analytics
from google_analytics import (
    get_response, ga_response_dataframe, set_daterange, set_metrics, set_dimensions)

VIEW_ID = config('VIEW_ID')
data_range = set_daterange('2020-01-01', '2020-02-01')
metrics = set_metrics('ga:pageviews','ga:avgSessionDuration')
dimensions = set_dimensions('ga:deviceCategory')

analytics = setup_analytics()
response1 = get_response(analytics, VIEW_ID, data_range, metrics, dimensions)
df = ga_response_dataframe(response1)

print(df.head())

