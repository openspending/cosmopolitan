from rest_framework import serializers

from continents.models import Continent

class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent

class ContinentShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = ('url', 'code')
