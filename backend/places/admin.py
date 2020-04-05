from django.contrib import admin
from places.models import Place


class PlacesAdmin(admin.ModelAdmin):
    search_fields = ['place_id']


# Register your models here.
admin.site.register(Place, PlacesAdmin)
