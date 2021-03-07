<h1 align="center">Google Analytics API Extractor</h1> <br>
<h2>🐍 Table of Contents 🐍</h2>

- [About](#about)
- [Benefit](#benefit)
- [Info](#info)
- [Setup](#setup)

<h2>⚡ About ⚡ </h2>
The Google Analytics Reporting API v4 is the most advanced programmatic method to access report data in Google Analytics. With the Google Analytics Reporting API, you can:

- Build custom dashboards to display Google Analytics data.
- Automate complex reporting tasks to save time.
- Integrate your Google Analytics data with other business applications.
## Benefit
Google Analytics is built upon a powerful data reporting infrastructure. The Google Analytics Reporting API v4 gives you access to the power of the Google Analytics platform. The API provides these key features:

- Metric expressions: The API allows you to request not only built-in metrics but also combination of metrics expressed in mathematical operations. For example, you can use the expression ga:goal1completions/ga:sessions to request the goal completions per number of sessions.

- Multiple date ranges: The API allows you in a single request to get data in two date ranges.

- Cohorts and Lifetime value: The API has a rich vocabulary to request Cohort and Lifetime value reports.

- Multiple segments: The API enables you to get multiple segments in a single request.

## Info
https://developers.google.com/analytics/devguides/reporting/core/v4
## Setup
### 0. activate venv
```bash
python -m venv venv
source ./venv/bin/activate (Mac) or venv\Scripts\activate (Windows)
```

### 1. install the packages

```bash
pip install -r requirements.txt
```

### 2. create the service account in GCP for the Google Analytics API
https://console.cloud.google.com/

### 3. download the json file of the service account

### 4. create conf repository and locate client_secrets.json into this repository

```bash
mkdir conf
mv xxxxx-xxxxx.json client_secrets.json
```

### 5. create .env and save there private keys and secret information

```bash
touch .env
```

### 6. setup the .env
```bash
KEY_FILE_LOCATION='PATH_OF_YOUR_CLIENT_SECRETS.JSON'
VIEW_ID='YOUR_GA_ID'

```

### 7. setup GA analyse info

```python
VIEW_ID = config('VIEW_ID')
data_range = set_daterange('2020-01-01', '2020-02-01')
metrics = set_metrics('ga:pageviews','ga:avgSessionDuration')
dimensions = set_dimensions('ga:deviceCategory')
```

### 8. run the main.py
```bash
python project/main.py
```
