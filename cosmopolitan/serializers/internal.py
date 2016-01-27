from cosmopolitan.models import Continent
from cosmopolitan.models import Currency
from cosmopolitan.models import Country

from cosmopolitan.serializers.common import CountrySerializer
from cosmopolitan.serializers.common import ContinentSerializer


class CountryShortSerializer(CountrySerializer):
    class Meta:
        model = Country
        fields = ('id', 'url')


class CurrencyShortSerializer(CountrySerializer):
    class Meta:
        model = Currency
        fields = ('id', 'url')


class ContinentShortSerializer(CountrySerializer):
    class Meta:
        model = Continent
        fields = ('id', 'url')


class ContinentWithRelatedSerializer(ContinentSerializer):
    related = CountryShortSerializer(many=True, read_only=True, source='countries')

    class Meta:
        model = Continent
        fields = ('id', 'name', 'url', 'related')
