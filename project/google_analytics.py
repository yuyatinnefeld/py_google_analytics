#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# PYTHON TEMPLATE
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd

def get_service(api_name, api_version, scopes, key_file_location):

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)

    service = build(api_name, api_version, credentials=credentials)

    return service

def get_response(service, view_id, data_range, metrics, dimensions):
    response = service.reports().batchGet(body={
        'reportRequests': [{
            'viewId': view_id,
            'dateRanges': data_range,
            'metrics': metrics, 
            "dimensions": dimensions
        }]}).execute()
    return response


def get_response_realtime(service):
    response = service.data().realtime().get(
        ids='ga:170783167',
        metrics='rt:activeUsers',
        dimensions='rt:medium'
        ).execute()
    return response

def get_results_ga_core_reporting(response):
    row_list = []
    # Get each collected report
    for report in response.get('reports', []):
        # Set column headers
        column_header = report.get('columnHeader', {})
        dimension_headers = column_header.get('dimensions', [])
        metric_headers = column_header.get('metricHeader', {}).get('metricHeaderEntries', [])
    
        # Get each row in the report
        for row in report.get('data', {}).get('rows', []):
            # create dict for each row
            row_dict = {}
            dimensions = row.get('dimensions', [])
            date_range_values = row.get('metrics', [])

            # Fill dict with dimension header (key) and dimension value (value)
            for header, dimension in zip(dimension_headers, dimensions):
                row_dict[header] = dimension

            # Fill dict with metric header (key) and metric value (value)
            for i, values in enumerate(date_range_values):
                for metric, value in zip(metric_headers, values.get('values')):
                # Set int as int, float a float
                    if ',' in value or '.' in value:
                        row_dict[metric.get('name')] = float(value)
                    else:
                        row_dict[metric.get('name')] = int(value)

            row_list.append(row_dict)
    return pd.DataFrame(row_list)

def get_results_ga_real_time_report(response):
    columns = response.get('columnHeaders',{})
    dimension_header = columns[0].get('name', [])
    metric_header = columns[1].get('name', [])

    col = [dimension_header, metric_header]
    df = pd.DataFrame(columns=col)
    rows = response.get('rows', [])

    for row in rows:
      df = df.append({dimension_header: row[0] , metric_header: int(row[1])}, ignore_index=True)  
    return df


def print_results(results):
    print ('** GA Report **')
    print(results)


