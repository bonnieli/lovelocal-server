from typing import Dict
import csv
from get_businesses_V2 import main
from config import SOURCE, YELP_KEYS, ALIASES
import json
import django
import sys
import os
import datetime as dt

sys.path.append(os.path.dirname(__file__) + '/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
django.setup()

from places.models import Place


# businesses = main(csv_file=SOURCE,
#                   keys=YELP_KEYS,
#                   aliases=ALIASES,
#                   create_json=True)
f = open('./scripts/businesses.json', "r")
businesses = json.loads(f.read())

print(businesses, len(businesses))
gift_cards: Dict[str, str] = {}

with open(SOURCE, 'r') as csv_file:
    for row in csv.reader(csv_file):
        if row[8] and row[8] != 'NA':
            gift_cards[row[0]] = row[8]

updated = dt.datetime.now(tz=dt.timezone.utc)

for business in businesses:
    if business['id'] in gift_cards:
        id_ = gift_cards[business['id']]
    else:
        id_ = ''

    try:
        business_ = Place.objects.get(yelp_id=business['yelp_id'])

        business_.name = business['name']
        business_.image_url = business['image_url']

        business_.city = business['city']
        business_.country = business['country']
        business_.latitude = business['latitude']
        business_.longitude = business['longitude']
        business_.phone = business['phone']

        business_.postal_code = business['postal_code'].replace(' ', '')
        business_.price = business.get('price', []).count('$')
        business_.province = business['province']
        business_.street_address = business['street_address']
        business_.url = business['url'] if business['url'] else ""
        business_.yelp_id = business['id']

        business_.giftcard_url = id_
        business_.updated = updated
        business_.save()
    except Place.DoesNotExist:
        print("does not exist", business)

        business_ = Place(yelp_id=business['id'],
                          name=business['name'],
                          image_url=business['image_url'],
                          phone=business['phone'],
                          street_address=business['street_address'],
                          city=business['city'],
                          postal_code=business['postal_code'].replace(' ', ''),
                          country=business['country'],
                          province=business['province'],
                          latitude=business['latitude'],
                          longitude=business['longitude'],
                          price=business.get('price', []).count('$'),
                          url=business['url'] if business['url'] else "",
                          giftcard_url=id_,
                          date_added=updated)
        business_.save()

