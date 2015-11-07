from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from world.views import CountryViewSet, RegionViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/', include(router.urls)),

    url(r'^v1/countries/(?P<country_id>[0-9]+)/regions', RegionViewSet.as_view({'get': 'list'}), name='country-regions'),
]
