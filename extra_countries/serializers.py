from rest_framework import serializers

from .models import ExtraCountry

from continents.serializers import ContinentSerializer
from continents.serializers import ContinentShortSerializer

from currencies.serializers import CurrencySerializer
from currencies.serializers import CurrencyShortSerializer


class ExtraCountrySerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    code = serializers.StringRelatedField(source='country.code3')
    continent = ContinentSerializer(source='extra_continent')
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
