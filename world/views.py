from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import generics

from rest_framework.response import Response

from cities.models import Country
from cities.models import Region
from cities.models import Subregion
from cities.models import City
# from cities.models import District

from .serializers import CountrySerializer
from .serializers import RegionSerializer
from .serializers import SubregionSerializer
from .serializers import CitySerializer
# from .serializers import DistrictSerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    model = Region
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

    def get_queryset(self):
        try:
            country_id = self.kwargs['country_id']
        except KeyError:
            return self.queryset
        return self.queryset.filter(country=country_id)


class SubregionViewSet(viewsets.ReadOnlyModelViewSet):
    model = Subregion
    serializer_class = SubregionSerializer
    queryset = Subregion.objects.all()

    def get_queryset(self):
        try:
            region_id = self.kwargs['region_id']
        except KeyError:
            return self.queryset
        return self.queryset.filter(region=region_id)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_queryset(self):
        try:
            region_id = self.kwargs['region_id']
        except KeyError:
            return self.queryset
        return self.queryset.filter(region=region_id)


# class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
#     model = District
#     serializer_class = DistrictSerializer
#     queryset = District.objects.all()
#
#     def get_queryset(self):
#         try:
#             city_id = self.kwargs['city_id']
#         except KeyError:
#             return self.queryset
#         return self.queryset.filter(city=city_id)
