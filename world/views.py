from cities.models import Country, Region
from rest_framework import serializers, viewsets
from .serializers import CountrySerializer, RegionSerializer

# ViewSets define the view behavior.
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = RegionSerializer

    def list(self, request, country_pk=None):
        regions = self.queryset.filter(domain=domain_pk)
        return Response
