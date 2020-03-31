import django
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
django.setup()
from places.models import Place
import pandas as pd
import sys
import json

fl = sys.argv[1]

df = pd.read_csv(fl)

for _, row in df.iterrows():

    name = row[2]
    print(name)
    coord = row[4]
    coord = coord.replace("\'", "\"")
    coord = json.loads(coord)
    image = row[7]
    gc_url = row[8]

    try:
        p = Place.objects.get(place_id=name)
    except Place.DoesNotExist:
        print("Something new...", name)
        p = Place(place_id=name)

    p.lat = coord.get("latitude")
    p.lng = coord.get("longitude")
    p.image = image

    if gc_url == gc_url: # checks if its NaN value 
        p.gift_card_url = gc_url

    p.save()
