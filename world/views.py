from rest_framework import viewsets
from rest_framework.response import Response

from continents.models import Continent
from currencies.models import Currency

from extra_countries.models import ExtraCountry
from extra_countries.serializers import ExtraCountrySerializer
from extra_countries.serializers import ExtraCountrySerializerShort
from extra_countries.serializers import ContinentSerializer
from extra_countries.serializers import ContinentDetailedSerializer
from extra_countries.serializers import CurrencySerializer
from extra_countries.serializers import CurrencyShortCountrySerializer


class ContinentViewSet(viewsets.ReadOnlyModelViewSet):
    model = Continent
    serializer_class = ContinentSerializer
    queryset = Continent.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ContinentDetailedSerializer(instance, context={'request': request})
        return Response(serializer.data)


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    model = Currency
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

    def get_queryset(self):
        queryset = Currency.objects.all()
        countries = self.request.query_params.get('countries', None)

        if countries is not None:
            countries = countries.split(',')
            queryset = queryset.filter(countries__in=countries)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CurrencyShortCountrySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


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
