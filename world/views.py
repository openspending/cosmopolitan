from cities.models import Country, Region
from rest_framework import serializers, viewsets, generics
from rest_framework.response import Response
from .serializers import CountrySerializer, RegionSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionViewSet(viewsets.ModelViewSet):
    model = Region
    serializer_class = RegionSerializer

    def get_queryset(self):
        queryset = Region.objects.all()
        try:
            country_id = self.kwargs['country_id']
        except KeyError:
            return queryset
        return queryset.filter(country=country_id)
