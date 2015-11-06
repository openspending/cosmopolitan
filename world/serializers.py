from cities.models import Country, Region, AlternativeName
from rest_framework import serializers
# from rest_framework_nested.relations import NestedHyperlinkedRelatedField

# Serializers define the API representation.
class CountrySerializer(serializers.HyperlinkedModelSerializer):
    regions = serializers.HyperlinkedIdentityField(view_name='region-detail')

    class Meta:
        model = Country

class AlternativeNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlternativeName

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('name', 'slug')
