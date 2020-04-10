import json
import requests
import csv
import django
import sys
import os

api_key = os.environ['YELP_API_KEY']
headers = {'Authorization': 'Bearer %s' % api_key}
url = "https://api.yelp.com/v3/businesses/search"
params = {'term': 'Coffee Shop', 'location': 'Toronto, ON', 'limit': 50, 'offset': 50}

# Making a get request to the API
req = requests.get(url, params=params, headers=headers)

# proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))

# printing the text from the response
results = json.loads(req.text)

businesses = results.get("businesses")


offset = 0
f = open('yelp_businesses.csv', 'w')

with f:
    writer = csv.writer(f)

    for row in businesses:
        info = [row.get("id"), row.get("name")]
        writer.writerow(info)
