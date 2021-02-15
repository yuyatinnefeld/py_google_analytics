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
from data_setup import set_daterange, set_metrics, set_dimensions
from google_analytics import(
    get_service, get_response, get_results_ga_core_reporting, 
    get_response_realtime, get_results_ga_real_time_report, print_results)


VIEW_ID = config('VIEW_ID')
KEY_FILE_LOCATION = config('KEY_FILE_LOCATION')

data_range = set_daterange('2020-01-01', '2020-02-01')
metrics = set_metrics('ga:pageviews','ga:avgSessionDuration')
dimensions = set_dimensions('ga:deviceCategory')
scope = 'https://www.googleapis.com/auth/analytics.readonly'


#### SETUP FOR GA CORE REPORTING ####
service_ga_reporting_v4 = get_service(
    api_name='analyticsreporting',
    api_version='v4',
    scopes=[scope],
    key_file_location=KEY_FILE_LOCATION)

response_1 = get_response(service_ga_reporting_v4, VIEW_ID, data_range, metrics, dimensions)
results = get_results_ga_core_reporting(response_1)
print_results(results)

#### SETUP FOR GA REAL TIME REPORTING ####
service_ga_real_time_v3 = get_service(
    api_name='analytics',
    api_version='v3',
    scopes=[scope],
    key_file_location=KEY_FILE_LOCATION)

real_time_report = get_response_realtime(service_ga_real_time_v3)
df = get_results_ga_real_time_report(real_time_report)
print_results(df)
#print_realtime_report(real_time_report)