from cities.models import Country, Region
from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

# Serializers define the API representation.
class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'capital', 'population', 'area', 'slug')

    regions = serializers.HyperlinkedIdentityField(
        view_name='country-regions-list'
    )

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('name', 'slug')
