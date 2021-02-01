from decouple import config
from oauth import setup_analytics
from google_analytics import get_response, ga_response_dataframe


VIEW_ID = config('VIEW_ID')

analytics = setup_analytics()
response = get_response(analytics, VIEW_ID)
result = ga_response_dataframe(response)


print(result)

