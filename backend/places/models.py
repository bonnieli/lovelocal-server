import json
# from django.db.models import Q
from django.db import models
# from django.contrib.gis.geos import Point
# from django.contrib.gis.db.models.functions import Distance
# from django.contrib.gis.measure import D


# class EmailSubscription(models.Model):
#     email = models.EmailField()
#     place = models.ForeignKey(to='Place', on_delete=models.CASCADE)
#     processed = models.BooleanField(default=False)

#     def __str__(self):
#         return "%s to %s" % (self.email, self.place.name)


# class SubmittedGiftCardLink(models.Model):

#     link = models.URLField(max_length=1000)
#     place = models.ForeignKey(to='Place', on_delete=models.CASCADE)
#     date_submitted = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "%s to %s" % (self.link, self.place.name)


# class SubmittedPlace(models.Model):
#     gift_card_url = models.URLField(null=True, blank=True, max_length=1000)
#     email = models.EmailField(null=True, blank=True)
#     place_id = models.TextField()
#     place_name = models.TextField()
#     place_rough_location = models.TextField()
#     date_submitted = models.DateTimeField(auto_now_add=True)
#     processed = models.BooleanField(default=False)

#     def __str__(self):
#         return "%s at %s" % (self.place_name, self.place_rough_location)


# class Neighborhood(models.Model):
#     name = models.TextField()
#     key = models.TextField(primary_key=True)
#     places = models.ManyToManyField(through='NeighborhoodEntry', to='Place')
#     lat = models.FloatField()
#     lng = models.FloatField()
#     geom = models.PointField(srid=4326, null=True)
#     bounds = models.PolygonField(srid=4326, null=True, blank=True)
#     photo_url = models.URLField(blank=True, null=True, max_length=1000)
#     photo_attribution = models.TextField(blank=True, null=True)
#     area = models.ForeignKey(to='Area', on_delete=models.SET_NULL, blank=True, null=True)
#     rank = models.IntegerField(null=True, blank=True)

#     def place_list(self, limit, offset):
#         hardcoded = [x.place for x in NeighborhoodEntry.objects.filter(neighborhood=self).order_by('rank')]
#         if offset == 0:
#             to_fetch = (limit - len(hardcoded)) + 1
#         else:
#             to_fetch = limit + 1
#         if self.bounds:
#             close_by = Place.objects.filter(
#                 Q(geom__within=self.bounds)
#             ).annotate(
#                 has_card=models.Count('gift_card_url')
#             ).exclude(
#                 place_id__in=[x.place_id for x in hardcoded]
#             ).order_by('-has_card', '-num_ratings')[offset:offset + to_fetch]
#         else:
#             close_by = Place.objects.filter(
#                 Q(geom__distance_lt=(self.geom, D(m=2500)))
#             ).exclude(
#                 place_id__in=[x.place_id for x in hardcoded]
#             ).annotate(
#                 has_card=models.Count('gift_card_url')
#             ).annotate(
#                 distance=Distance('geom', self.geom)
#             ).order_by('-has_card', 'distance')[offset:offset + to_fetch]
#         more_available = len(close_by) == to_fetch
#         if offset == 0:
#             joined = (hardcoded + list(close_by))
#         else:
#             joined = list(close_by)
#         end_list = -1 if more_available else len(joined)
#         return joined[0:end_list], more_available

#     def to_json(self):
#         return {
#             "name": self.name,
#             "key": self.key,
#             "image": self.photo_url
#         }

#     def save(self, *args, **kwargs):
#         if (self.lat and self.lng):
#             self.geom = Point([float(x) for x in (self.lng, self.lat)], srid=4326)

#         super(self.__class__, self).save(*args, **kwargs)


# class NeighborhoodEntry(models.Model):
#     place = models.ForeignKey('Place', on_delete=models.CASCADE)
#     neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE)
#     rank = models.IntegerField()


# class Area(models.Model):
#     key = models.TextField(primary_key=True)
#     display_name = models.TextField()

#     @classmethod
#     def update_area_for_all_places(cls):
#         for a in cls.objects.all():
#             for n in Neighborhood.objects.filter(area=a):
#                 if n.bounds:
#                     places = Place.objects.filter(geom__within=n.bounds)
#                 else:
#                     places = Place.objects.filter(geom__distance_lt=(n.geom, D(m=5000)))
#                 places.update(area=a)

# Create your models here.


class Place(models.Model):
    yelp_id = models.TextField()
    name = models.TextField()
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

    last_updated = models.DateTimeField()
    created_at = models.DateTimeField()
    # lat = models.FloatField()
    # lng = models.FloatField()
    # address = models.TextField(blank=True)
    #
    # user_rating = models.FloatField(blank=True)
    # num_ratings = models.FloatField(blank=True)
    #
    # # area = models.ForeignKey(to='Area', null=True, blank=True, on_delete=models.SET_NULL)
    # email_contact = models.EmailField(blank=True)
    # place_url = models.URLField(blank=True, max_length=1000)
    # image_url = models.URLField(blank=True, max_length=1000)
    # image_attribution = models.TextField(blank=True)
    # gift_card_url = models.URLField(blank=True, max_length=1000)
    # takeout_url = models.URLField(blank=True, max_length=1000)
    # donation_url = models.URLField(blank=True, max_length=1000)
    # # geom = models.PointField(srid=4326, null=True, blank=True)
    # place_types = models.TextField(blank=True)

    def get_image_url(self):
        return self.image or "http://TODO/placeholder"

    def to_json(self):
        return {
            'name': self.name,
            'giftCardURL': self.giftcard_url,
            'imageURL': self.image_url,
            'placeID': self.place_id,
            'website': self.url
        }

    def to_typeahead_json(self):
        return {
            'name': self.name,
            'key': self.place_id,
            'image_attribution': self.image_attribution
        }
