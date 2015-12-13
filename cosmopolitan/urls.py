from django.conf.urls import include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import routers

from world.views import ContinentViewSet
from world.views import CurrencyViewSet
from world.views import ExtraCountryViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

countries = ExtraCountryViewSet.as_view({'get': 'list'})
country_detail = ExtraCountryViewSet.as_view({'get': 'retrieve'})

router.register(r'countries', ExtraCountryViewSet)
router.register(r'continents', ContinentViewSet)
router.register(r'currencies', CurrencyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/', include(router.urls)),

    url(r'^countries/$', countries, name='country-list'),
    url(r'^countries/(?P<pk>[0-9]+)/$', country_detail, name='country-detail'),
]
urlpatterns += staticfiles_urlpatterns()
