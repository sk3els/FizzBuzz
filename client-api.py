import requests, os

requestJson = {'max_range': os.environ['MAX_RANGE']}
functionUrl = os.environ['FUNCTION_URL']

if int(requestJson['max_range']) > 999 or int(requestJson['max_range']) < 0:
   print("Error: max_range must be between [0,999]")
   quit()
   
try:
   r = requests.get(functionUrl, params=requestJson)
   print(r.json())
except:
   print("Error: Likely invalid value for FUNCTION_URL")