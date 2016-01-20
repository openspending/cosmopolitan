from rest_framework import serializers
from cities.models import Country
from .models import ExtraCountry

from currencies.models import Currency
from continents.models import Continent


class CountryShortSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    lookup = serializers.StringRelatedField(source='pk')

    class Meta:
        model = ExtraCountry
        fields = ('url', 'lookup', 'name')


class CountryContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    lookup = serializers.StringRelatedField(source='pk')
    name = serializers.StringRelatedField(source='country.name')

    class Meta:
        model = ExtraCountry
        fields = ('url', 'lookup', 'name')


###
# Currencies
###

class CurrencyShortCountrySerializer(serializers.HyperlinkedModelSerializer):
    lookup = serializers.StringRelatedField()
    countries = CountryContinentShortSerializer(many=True, read_only=True)

    class Meta:
        model = Currency
        exclude = ('continents',)


class ContinentCurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = ('url', 'name', 'lookup')


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    lookup = serializers.StringRelatedField()
    countries = CountryShortSerializer(many=True, read_only=True)
    continents = ContinentCurrencySerializer(many=True, read_only=True)

    class Meta:
        model = Currency


class CurrencyShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ('name', 'lookup', 'url')


###
# Continents
###

class ContinentCountrySerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField()
    related = CountryShortSerializer(many=True, read_only=True, source='countries')

    class Meta:
        model = Continent
        exclude = ('countries', 'geoNameId', 'currencies')


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    lookup = serializers.StringRelatedField()
    countries = CountryContinentShortSerializer(many=True, read_only=True)

    class Meta:
        model = Continent
        exclude = ('currencies',)


class ContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = ('url', 'lookup', 'name')


class ContinentDetailedSerializer(serializers.HyperlinkedModelSerializer):
    lookup = serializers.StringRelatedField()
    countries = CountryShortSerializer(many=True, read_only=True)
    currencies = CurrencyShortSerializer(many=True, read_only=True)

    class Meta:
        model = Continent


###
# Countries
###
class ExtraCountrySerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    lookup = serializers.StringRelatedField()
    continent = ContinentCountrySerializer(source='extra_continent')
    currency = CurrencyShortSerializer(source='extra_currency')

    class Meta:
        model = ExtraCountry
        exclude = ('extra_currency', 'extra_continent', 'country')


class ExtraCountrySerializerShort(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    lookup = serializers.StringRelatedField()
    continent = ContinentShortSerializer(source='extra_continent')
    currency = CurrencyShortSerializer(source='extra_currency')

    class Meta:
        model = ExtraCountry
        exclude = ('extra_currency', 'extra_continent', 'country')
