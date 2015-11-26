from rest_framework import serializers

from cities.models import Country
from cities.models import Region
from cities.models import Subregion
from cities.models import City

from continents.models import Continent
from currencies.models import Currency


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    regions = serializers.SerializerMethodField('region_url')
    alt_names = serializers.StringRelatedField(many=True)

    def region_url(self, country):
        request = self.context.get('request', None)

        return "http://%s/v1/countries/%d/regions" % (request.get_host(), country.pk)

    class Meta:
        model = Country


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    subregions = serializers.SerializerMethodField('subregion_url')
    cities = serializers.SerializerMethodField('city_url')
    alt_names = serializers.StringRelatedField(many=True)

    def subregion_url(self, region):
        request = self.context.get('request', None)

        return "http://%s/v1/countries/%d/regions/%d/subregions" % (request.get_host(), region.country.pk, region.pk)

    def city_url(self, region):
        request = self.context.get('request', None)

        return "http://%s/v1/countries/%d/regions/%d/cities" % (request.get_host(), region.country.pk, region.pk)

    class Meta:
        model = Region


class SubregionSerializer(serializers.HyperlinkedModelSerializer):
    alt_names = serializers.StringRelatedField(many=True)

    class Meta:
        model = Subregion


class CitySerializer(serializers.HyperlinkedModelSerializer):
    alt_names = serializers.StringRelatedField(many=True)
    districts = serializers.SerializerMethodField('city_url')

    def city_url(self, city):
        request = self.context.get('request', None)

        return "http://%s/v1/countries/%d/regions/%d/cities/%d/districts" % (request.get_host(), city.country.pk, city.region.pk, city.pk)

    class Meta:
        model = City


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
