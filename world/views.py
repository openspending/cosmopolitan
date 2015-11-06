from cities.models import Country, Region, AlternativeName
from rest_framework import serializers, viewsets
from .serializers import CountrySerializer, RegionSerializer, AlternativeNameSerializer

# ViewSets define the view behavior.
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class AlternativeNameViewSet(viewsets.ModelViewSet):
    queryset = AlternativeName.objects.all()
    serializer_class = AlternativeName
