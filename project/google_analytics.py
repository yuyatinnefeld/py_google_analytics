from decouple import config
import pandas as pd
from oauth import setup_analytics


def get_response(analytics, view_id):
    response = analytics.reports().batchGet(body={
        'reportRequests': [{
            'viewId': view_id,
            'dateRanges': [{'startDate': '2020-01-01', 'endDate': '2020-02-01'}],
            'metrics': [
                {"expression": "ga:pageviews"},
                {"expression": "ga:avgSessionDuration"}
            ], "dimensions": [
                {"name": "ga:deviceCategory"}
            ]
        }]}).execute()
    return response


def ga_response_dataframe(response):
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
