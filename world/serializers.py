from cities.models import Country, Region, Subregion
from rest_framework import serializers

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    # subregions = serializers.SerializerMethodField('subregion_url')

    # def region_url(self, country, region):
        # request = self.context.get('request', None)

        # return "%s%d/regions/%d/subregions" % (request.build_absolute_uri(), country.pk, region.pk)

    class Meta:
        model = Region


class SubregionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subregion


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    regions = serializers.SerializerMethodField('region_url')
    alt_names = serializers.StringRelatedField(many=True)

    def region_url(self, country):
        request = self.context.get('request', None)

        return "http://%s/v1/countries/%d/regions" % (request.get_host(), country.pk)

    class Meta:
        model = Country
