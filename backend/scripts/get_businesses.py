import json
import requests
import csv
import django
import sys
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
sys.path.append(os.path.dirname(__file__) + '/..')
django.setup()

NEIGHBORHOOD_JS_OUTPUT_TEMPLATE = """
const Neighborhoods = %s;
export default Neighborhoods;
"""

api_key = os.environ['YELP_API_KEY']
headers = {'Authorization': 'Bearer %s' % api_key}
url = "https://api.yelp.com/v3/businesses/search"
params = {'location': 'Toronto, ON', 'limit': 50, 'offset': 50}

# Making a get request to the API
req = requests.get(url, params=params, headers=headers)

# proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))

# printing the text from the response
results = json.loads(req.text)

businesses = results.get("businesses")


offset = 0
f = open('businesses.csv', 'w')

with f:
    writer = csv.writer(f)

    for row in businesses:
        info = [row.get("id"), row.get("alias"), row.get("name"), row.get("url"),
                row.get("coordinates"), row.get("location"),
                row.get("phone"), row.get("image_url")]
        writer.writerow(info)
