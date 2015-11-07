from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import generics

from rest_framework.response import Response

from cities.models import Country
from cities.models import Region
from cities.models import Subregion
from cities.models import City
from cities.models import District

from .serializers import CountrySerializer
from .serializers import RegionSerializer
from .serializers import SubregionSerializer
from .serializers import CitySerializer
from .serializers import DistrictSerializer


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


class CityViewSet(viewsets.ModelViewSet):
    model = City
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.all()
        try:
            region_id = self.kwargs['region_id']
        except KeyError:
            return queryset
        return queryset.filter(region=region_id)


class DistrictViewSet(viewsets.ModelViewSet):
    model = District
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        try:
            city_id = self.kwargs['city_id']
        except KeyError:
            return queryset
        return queryset.filter(city=city_id)
