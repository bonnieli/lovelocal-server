from django.db import models


class Place(models.Model):
    yelp_id = models.TextField()
    name = models.TextField(db_index=True)
    image_url = models.URLField(blank=True)
    url = models.URLField(blank=True)
    phone = models.TextField(blank=True,
                             max_length=12)
    street_address = models.TextField(blank=True)
    city = models.TextField(blank=True)
    postal_code = models.TextField(blank=True,
                                   max_length=6)
    province = models.TextField(blank=True)
    country = models.TextField(blank=True)
    latitude = models.FloatField(blank=True, default=0)
    longitude = models.FloatField(blank=True, default=0)
    price = models.IntegerField(blank=True, default=0)
    giftcard_url = models.URLField(blank=True)
    contact = models.TextField(blank=True)

    last_updated = models.DateTimeField()
    created_at = models.DateTimeField()

    def get_image_url(self):
        return self.image or "http://TODO/placeholder"

    def to_json(self):
        return {
            'name': self.name,
            'giftCardURL': self.giftcard_url,
            'imageURL': self.image_url,
            'placeID': self.yelp_id,
            'website': self.url
        }

    def to_typeahead_json(self):
        return {
            'name': self.name,
            'key': self.place_id,
            'image_attribution': self.image_attribution
        }
