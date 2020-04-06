SOURCE = 'scripts/businesses_v2.csv'
YELP_KEYS = [
    'name',
    'image_url',
    'url',
    'phone',
    'categories',
    'address1',
    'city',
    'zip_code',
    'country',
    'state',
    'latitude',
    'longitude',
    'price',
]
ALIASES = {
    'url': 'yelp_url',
    'address1': 'street_address',
    'zip_code': 'postal_code',
    'state': 'province',
}
