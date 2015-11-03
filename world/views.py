from cities.models import Country
from rest_framework import serializers, viewsets
from .serializers import CountrySerializer

# ViewSets define the view behavior.
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
