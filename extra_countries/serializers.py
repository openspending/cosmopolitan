from rest_framework import serializers
from cities.models import Country
from .models import ExtraCountry


class CountryShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('url', 'code', 'name')


class CountryContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('url', 'code')


###
# Currencies
###
from currencies.models import Currency


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    countries = CountryShortSerializer(many=True, read_only=True)

    class Meta:
        model = Currency


class CurrencyShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ('code', 'url')


class CurrencyContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ('name', 'code', 'url')


###
# Continents
###

from continents.models import Continent


class ContinentCountrySerializer(serializers.HyperlinkedModelSerializer):
    related = CountryShortSerializer(many=True, read_only=True, source='countries')

    class Meta:
        model = Continent
        exclude = ('countries', 'geoNameId')


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    countries = CountryContinentShortSerializer(many=True, read_only=True)

    class Meta:
        model = Continent


class ContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = ('url', 'code')


class ContinentDetailedSerializer(serializers.HyperlinkedModelSerializer):
    countries = CountryShortSerializer(many=True, read_only=True)
    currencies = CurrencyContinentShortSerializer(many=True, read_only=True)

    class Meta:
        model = Continent


###
# Countries
###
class ExtraCountrySerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    code = serializers.StringRelatedField(source='country.code3')
    continent = ContinentCountrySerializer(source='extra_continent')
    currency = CurrencySerializer(source='extra_currency')

    class Meta:
        model = ExtraCountry
        exclude = ('extra_currency', 'extra_continent')


class ExtraCountrySerializerShort(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    continent = ContinentShortSerializer(source='extra_continent')
    currency = CurrencyShortSerializer(source='extra_currency')

    class Meta:
        model = ExtraCountry
        exclude = ('extra_currency', 'extra_continent')



