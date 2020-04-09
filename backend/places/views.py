import json
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse


from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

import logging
import urllib.request
import os

# from django.contrib.gis.db.models.functions import Distance
# from django.contrib.gis.measure import D
from places.models import (Place)


@csrf_protect
def neighborhood_detail(request):
    search = request.GET.get('search')
    more_available = True
    offset = int(request.GET.get('offset', 0))
    per_page = 15
    max_offset = per_page + offset

    if search:
        place_list = Place.objects.filter(name__icontains=search)
    else:
        place_list = Place.objects.all()[offset:max_offset]

    if len(place_list) < per_page:
        more_available = False

    return JsonResponse({
        'suggestedPlaces': [x.to_json() for x in place_list],
        'moreAvailable': more_available
    })


@csrf_exempt
def check_url(request):
    try:
        url_status = urllib.request.urlopen(request.body.decode("utf-8")).getcode()
    except:
        return HttpResponse(":( Url is Not Working")
    if (url_status == 200):
        return HttpResponse("Yey! URL is Working")
    return HttpResponse(":( Url is Not Working")


class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        print("getting here...")
        print(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html'))
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            print("oops")
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                    This URL is only used when you have built the production
                    version of the app. Visit http://localhost:3000/ instead, or
                    run `yarn run build` to test the production version.
                    """,
                status=501,
            )


@csrf_exempt
def test(request):
    return JsonResponse({'status': 'ok'})
