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

from places.models import Category, Place



# businesses = main(csv_file=SOURCE,
#                   keys=YELP_KEYS,
#                   aliases=ALIASES,
                #   create_json=True)
f = open('./scripts/businesses.json', "r")
businesses = json.loads(f.read())

print(businesses, len(businesses))
gift_cards: Dict[str, str] = {}
instagram_handles: Dict[str, str] = {}
shop_urls: Dict[str, str] = {}

with open(SOURCE, 'r') as csv_file:
    for row in csv.reader(csv_file):
        yelp_id = row[0]
        giftcard_col = row[2]
        instagram_col = row[3]
        shopurl_col = row[4]

        if giftcard_col and giftcard_col != 'NA':
            gift_cards[yelp_id] = giftcard_col
        if instagram_col:
            instagram_handles[yelp_id] = instagram_col
        if shopurl_col:
            shop_urls[yelp_id] = shopurl_col


updated = dt.datetime.now(tz=dt.timezone.utc)

for business in businesses:
    id_ = gift_cards[business['id']] if business['id'] in gift_cards else ''
    instagram_handle = instagram_handles[business['id']] if business['id'] in instagram_handles else ''
    shop_url = shop_urls[business['id']] if business['id'] in shop_urls else ''

    try:
        business_ = Place.objects.get(yelp_id=business['id'])

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
        business_.ig_handle = instagram_handle
        business_.shop_url = shop_url
        business_.last_updated = updated

        for category in business.get('categories'):
            if category.get('title') and category.get('title') not in\
                    business_.categories.values_list('name'):
                business_.categories.create(name=category.get('title'))

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
                          ig_handle=instagram_handle,
                          shop_url=shop_url,
                          last_updated=updated,
                          created_at=updated)
        business_.save()

        for category in business.get('categories'):
            if category.get('title'):
                business_.categories.create(name=category.get('title'))
        business_.save()
