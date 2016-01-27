from rest_framework import viewsets
from rest_framework.response import Response

from cosmopolitan.models import Continent
from cosmopolitan.models import Currency
from cosmopolitan.models import Country

from cosmopolitan.serializers.specific import CurrencyListSerializer
from cosmopolitan.serializers.specific import CurrencyDetailSerializer

from cosmopolitan.serializers.specific import ContinentListSerializer
from cosmopolitan.serializers.specific import ContinentDetailSerializer

from cosmopolitan.serializers.specific import CountryListSerializer
from cosmopolitan.serializers.specific import CountryDetailSerializer

class ContinentViewSet(viewsets.ReadOnlyModelViewSet):
    model = Continent
    serializer_class = ContinentDetailSerializer
    queryset = Continent.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ContinentListSerializer(queryset,
                                             many=True,
                                             context={'request': request})
        return Response(serializer.data)


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    model = Currency
    serializer_class = CurrencyDetailSerializer
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
        serializer = CurrencyListSerializer(queryset,
                                            many=True,
                                            context={'request': request})
        return Response(serializer.data)


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    model = Country
    serializer_class = CountryDetailSerializer
    queryset = Country.objects.all()

    def get_queryset(self):
        queryset = Country.objects.all()
        continents = self.request.query_params.get('continents', None)
        if continents is not None:
            continents = continents.split(',')
            queryset = queryset.filter(continent_id__in=continents)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CountryListSerializer(queryset,
                                           many=True,
                                           context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CountryDetailSerializer(instance,
                                             context={'request': request})
        data = self._remove_self_from_related(serializer.data, request)
        return Response(data)

    def _remove_self_from_related(self, data, request):
        # remove retreived country from list of related Countries
        # to not show it twice
        for idx, current_country in enumerate(data['continent']['related']):
            request_country_code = request.path[-3:-1]
            if current_country['id'] == request_country_code:
                del(data['continent']['related'][idx])
        return data
