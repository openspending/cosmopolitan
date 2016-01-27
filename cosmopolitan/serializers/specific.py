from cosmopolitan.models import Continent
from cosmopolitan.models import Currency
from cosmopolitan.models import Country

from cosmopolitan.serializers.common import CurrencySerializer
from cosmopolitan.serializers.common import CountrySerializer
from cosmopolitan.serializers.common import ContinentSerializer

from cosmopolitan.serializers.internal import CountryShortSerializer
from cosmopolitan.serializers.internal import ContinentShortSerializer
from cosmopolitan.serializers.internal import CurrencyShortSerializer
from cosmopolitan.serializers.internal import ContinentWithRelatedSerializer

class CurrencyListSerializer(CurrencySerializer):
    countries = CountryShortSerializer(many=True, read_only=True)
    class Meta:
        model = Currency
        fields = ('id', 'url', 'name', 'countries')


class CurrencyDetailSerializer(CurrencySerializer):
    countries = CountrySerializer(many=True, read_only=True)
    continents = ContinentSerializer(many=True, read_only=True)
    class Meta:
        model = Currency
        fields = ('id', 'url', 'name', 'countries', 'continents')


class ContinentListSerializer(ContinentSerializer):
    countries = CountryShortSerializer(many=True, read_only=True)
    class Meta:
        model = Continent
        fields = ('id', 'url', 'name', 'countries')


class ContinentDetailSerializer(ContinentSerializer):
    countries = CountrySerializer(many=True, read_only=True)
    currencies = CurrencySerializer(many=True, read_only=True)
    class Meta:
        model = Continent
        fields = ('id', 'url', 'name', 'countries', 'currencies')


class CountryListSerializer(CountrySerializer):
    currency = CurrencyShortSerializer()
    continent = ContinentShortSerializer()
    class Meta:
        model = Country
        fields = ('id', 'url', 'name', 'continent', 'currency')


class CountryDetailSerializer(CountrySerializer):
    currency = CurrencySerializer()
    continent = ContinentWithRelatedSerializer()
    class Meta:
        model = Country
        fields = ('id', 'url', 'name', 'continent', 'currency')
