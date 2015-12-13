from rest_framework import viewsets
from rest_framework.response import Response

from cities.models import Region
from cities.models import Subregion
from cities.models import City

from continents.models import Continent
from continents.serializers import ContinentSerializer

from currencies.models import Currency
from currencies.serializers import CurrencySerializer

from .serializers import RegionSerializer
from .serializers import SubregionSerializer
from .serializers import CitySerializer

from extra_countries.models import ExtraCountry
from extra_countries.serializers import ExtraCountrySerializer
from extra_countries.serializers import ExtraCountrySerializerShort


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


class ContinentViewSet(viewsets.ReadOnlyModelViewSet):
    model = Continent
    serializer_class = ContinentSerializer
    queryset = Continent.objects.all()


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    model = Currency
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class ExtraCountryViewSet(viewsets.ReadOnlyModelViewSet):
    model = ExtraCountry
    serializer_class = ExtraCountrySerializer
    queryset = ExtraCountry.objects.all()

    def get_queryset(self):
        queryset = ExtraCountry.objects.all()
        continents = self.request.query_params.get('continents', None)
        if continents is not None:
            continents = continents.split(',')
            queryset = queryset.filter(extra_continent_id__in=continents)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ExtraCountrySerializerShort(queryset, many=True, context={'request': request})
        return Response(serializer.data)
