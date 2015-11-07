from cities.models import Country, Region, Subregion
from rest_framework import serializers

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    subregions = serializers.SerializerMethodField('subregion_url')
    alt_names = serializers.StringRelatedField(many=True)

    def subregion_url(self, region):
        request = self.context.get('request', None)

        return "http://%s/v1/countries/%d/regions/%d/subregions" % (request.get_host(), region.country.pk, region.pk)

    class Meta:
        model = Region


class SubregionSerializer(serializers.HyperlinkedModelSerializer):
    alt_names = serializers.StringRelatedField(many=True)
    
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
