from rest_framework import serializers

from currencies.models import Currency

from world.short_serializers.serializers import CountrySerializerShort


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    countries = CountrySerializerShort(many=True, read_only=True)

    class Meta:
        model = Currency


class CurrencyShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ('code', 'url')
