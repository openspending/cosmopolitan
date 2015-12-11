from rest_framework import serializers

from continents.models import Continent

from world.short_serializers.serializers import CountrySerializerShort


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    related = CountrySerializerShort(many=True, read_only=True, source='countries')

    class Meta:
        model = Continent
        exclude = ('countries',)


class ContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = ('url', 'code')
