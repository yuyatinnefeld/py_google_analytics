#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# PYTHON TEMPLATE
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""


from decouple import config
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def setup_analytics():
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    KEY_FILE_LOCATION = config('KEY_FILE_LOCATION')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics