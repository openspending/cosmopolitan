from rest_framework import serializers

from cosmopolitan.models import Continent
from cosmopolitan.models import Currency
from cosmopolitan.models import Country
from cosmopolitan.models import City
from cosmopolitan.models import Region
from cosmopolitan.models import Postcode


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'url', 'name')


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'url', 'name')


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = ('id', 'url', 'name')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'url', 'name')


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'url', 'name')


class PostcodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Postcode
        fields = ('id',)