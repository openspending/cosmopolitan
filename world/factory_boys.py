import factory

from django.contrib.gis.geos import GEOSGeometry

from continents.models import Continent
from currencies.models import Currency

from cities.models import Country
from cities.models import Region
from cities.models import Subregion
from cities.models import City


class CountryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Country

    name = 'TestCountry1'
    population = 1


class RegionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Region

    name = 'TestRegion1'
    country = factory.SubFactory(CountryFactory)


class SubregionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Subregion

    name = 'TestSubRegion1'
    region = factory.SubFactory(RegionFactory)


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = City

    name = 'TestCity1'
    location = GEOSGeometry('POINT(5 23)')
    population = 1
    country = factory.SubFactory(CountryFactory)
    region = factory.SubFactory(RegionFactory)


class ContinentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Continent

    code = 'EU'
    name = 'Alabama'
    geoNameId = 12


class CurrencyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Currency

    code = 'EU'
    name = 'EuroCent'
