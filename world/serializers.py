from cities.models import Country, Region, AlternativeName
from rest_framework import serializers

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    regions = serializers.SerializerMethodField('region_url')
    alt_names = serializers.StringRelatedField(many=True)

    def region_url(self, country):
        request = self.context.get('request', None)

        return "%s%d/regions" % (request.build_absolute_uri(), country.pk)

    class Meta:
        model = Country


class AlternativeNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlternativeName
