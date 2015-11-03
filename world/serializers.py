from cities.models import Country
from rest_framework import serializers

# Serializers define the API representation.
class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'capital', 'population', 'area')
