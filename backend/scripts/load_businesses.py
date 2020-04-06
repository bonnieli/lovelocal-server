import django
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
django.setup()
from places.models import Place
import sys
import json
from scripts.config import SOURCE, YELP_KEYS, ALIASES
from scripts.get_businesses_V2 import main
import csv
from typing import Dict

businesses = main(csv_file=SOURCE,
                  keys=YELP_KEYS,
                  aliases=ALIASES,
                  create_json=False)

gift_cards: Dict[str, str] = {}

with open(SOURCE, 'r') as csv_file:
    for row in csv.reader(csv_file):
        if row[8] and row[8] != 'NA':
            gift_cards[row[0]] = row[8]

for business in businesses:
    try:
        business_ = Place.objects.get(name=business['name'])
    except Place.DoesNotExist:
        if business['id'] in gift_cards:
            id_ = gift_cards[business['id']]
        else:
            id_ = ''
        business_ = Place(yelp_id=business['id'],
                          name=business['name'],
                          iamge_url=business['image_url'],
                          yelp_url=business['yelp_url'],
                          phone=business['phone'],
                          street_address=business['street_address'],
                          city=business['city'],
                          postal_code=business['postal_code'].replace(' ', ''),
                          country=business['country'],
                          province=business['province'],
                          latitude=business['latitude'],
                          longitude=business['longitude'],
                          price=business['price'].count('$'),
                          url=business['url'],
                          giftcard_url=id_)
        business_.save()

# fl = sys.argv[1]
#
# df = pd.read_csv(fl)
#
# for _, row in df.iterrows():
#
#     name = row[2]
#     print(name)
#     coord = row[4]
#     coord = coord.replace("\'", "\"")
#     coord = json.loads(coord)
#     image = row[7]
#     gc_url = row[8]
#
#     try:
#         p = Place.objects.get(place_id=name)
#     except Place.DoesNotExist:
#         print("Something new...", name)
#         p = Place(place_id=name)
#
#     p.lat = coord.get("latitude")
#     p.lng = coord.get("longitude")
#     p.image = image
#
#     if gc_url == gc_url: # checks if its NaN value
#         p.gift_card_url = gc_url
#
#     p.save()
