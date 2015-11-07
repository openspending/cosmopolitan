from cities.models import Country, Region, Subregion
from rest_framework import serializers, viewsets, generics
from rest_framework.response import Response
from .serializers import CountrySerializer, RegionSerializer, SubregionSerializer


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


class SubregionViewSet(viewsets.ModelViewSet):
    model = Subregion
    serializer_class = SubregionSerializer

    def get_queryset(self):
        queryset = Subregion.objects.all()
        try:
            region_id = self.kwargs['region_id']
        except KeyError:
            return queryset
        return queryset.filter(region=region_id)
