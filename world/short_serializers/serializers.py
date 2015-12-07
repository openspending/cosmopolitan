from rest_framework import serializers

from cities.models import Country

class CountrySerializerShort(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('url', 'code', 'name')

