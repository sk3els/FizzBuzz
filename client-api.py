import requests, os

# grabs ENV vars specified in Docker file or otherwise overridden
requestJson = {'max_range': os.environ['MAX_RANGE']}
functionUrl = os.environ['FUNCTION_URL']

# validate max_range is in acceptable range
if int(requestJson['max_range']) > 999 or int(requestJson['max_range']) < 0:
   print("Error: max_range must be between [0,999]")
   quit()

# make GET request to Google Cloud API service or otherwise specified function_url
try:
   r = requests.get(functionUrl, params=requestJson)
   print(r.json())
except:
   print("Error: Likely invalid value for FUNCTION_URL")
