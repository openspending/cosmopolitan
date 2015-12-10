from django.conf.urls import include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import routers

from world.views import CountryViewSet
from world.views import RegionViewSet
from world.views import SubregionViewSet
from world.views import CityViewSet
from world.views import ContinentViewSet
from world.views import CurrencyViewSet
from world.views import ExtraCountryViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'subregions', SubregionViewSet)
router.register(r'cities', CityViewSet)
router.register(r'continents', ContinentViewSet)
router.register(r'currencies', CurrencyViewSet)
router.register(r'extracountries', ExtraCountryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/', include(router.urls)),

    url(r'^v1/countries/(?P<country_id>[0-9]+)/regions/(?P<region_id>[0-9]+)/cities', CityViewSet.as_view({'get': 'list'})),
    url(r'^v1/countries/(?P<country_id>[0-9]+)/regions/(?P<region_id>[0-9]+)/subregions', SubregionViewSet.as_view({'get': 'list'})),
    url(r'^v1/countries/(?P<country_id>[0-9]+)/regions', RegionViewSet.as_view({'get': 'list'})),
]
urlpatterns += staticfiles_urlpatterns()
