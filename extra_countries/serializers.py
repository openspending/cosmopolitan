from rest_framework import serializers

from .models import ExtraCountry

from world.serializers import ContinentSerializer
from world.serializers import CurrencySerializer

class ExtraCountrySerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.StringRelatedField(source='country.name')
    code = serializers.StringRelatedField(source='country.code3')
    continent = ContinentSerializer(source='extra_continent')
    currency = CurrencySerializer(source='extra_currency')

    class Meta:
        model = ExtraCountry
        exclude = ('extra_currency', 'extra_continent')
