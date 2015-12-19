from rest_framework import serializers
from cities.models import Country
from .models import ExtraCountry

from currencies.models import Currency
from continents.models import Continent


class CountryShortSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    code = serializers.StringRelatedField(source='country.code3')

    class Meta:
        model = ExtraCountry
        fields = ('url', 'code', 'name')


class CountryContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.StringRelatedField(source='country.name')

    class Meta:
        model = ExtraCountry
        fields = ('url', 'code')


###
# Currencies
###

class CurrencyShortCountrySerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.StringRelatedField()
    countries = CountryContinentShortSerializer(many=True, read_only=True)

    class Meta:
        model = Currency
        exclude = ('continents',)


class ContinentCurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = ('url', 'name', 'code')


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.StringRelatedField()
    countries = CountryShortSerializer(many=True, read_only=True)
    continents = ContinentCurrencySerializer(many=True, read_only=True)

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

class ContinentCountrySerializer(serializers.HyperlinkedModelSerializer):
    related = CountryShortSerializer(many=True, read_only=True, source='countries')

    class Meta:
        model = Continent
        exclude = ('countries', 'geoNameId', 'currencies')


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.StringRelatedField()
    countries = CountryContinentShortSerializer(many=True, read_only=True)

    class Meta:
        model = Continent
        exclude = ('currencies',)


class ContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = ('url', 'code')


class ContinentDetailedSerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.StringRelatedField()
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
    currency = CurrencyContinentShortSerializer(source='extra_currency')

    class Meta:
        model = ExtraCountry
        exclude = ('extra_currency', 'extra_continent', 'country')


class ExtraCountrySerializerShort(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    code = serializers.StringRelatedField()
    continent = ContinentShortSerializer(source='extra_continent')
    currency = CurrencyShortSerializer(source='extra_currency')

    class Meta:
        model = ExtraCountry
        exclude = ('extra_currency', 'extra_continent', 'country')



