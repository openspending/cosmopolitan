import factory
from factory.fuzzy import FuzzyText

from django.contrib.gis.geos import GEOSGeometry

from cosmopolitan.models import Continent
from cosmopolitan.models import Currency
from cosmopolitan.models import Country

from cities.models import Country as CitiesCountry
from cities.models import Region
from cities.models import City


class CitiesCountryFactory(factory.DjangoModelFactory):
    class Meta:
        model = CitiesCountry

    name = FuzzyText(length=6)
    population = 1


class RegionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Region

    name = FuzzyText(length=6)
    country = factory.SubFactory(CitiesCountryFactory)


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = City

    name = FuzzyText(length=6)
    location = GEOSGeometry('POINT(5 23)')
    population = 1
    country = factory.SubFactory(CitiesCountryFactory)
    region = factory.SubFactory(RegionFactory)


class ContinentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Continent

    id = FuzzyText(length=2)
    name = FuzzyText(length=6)
    geoNameId = 12


class CurrencyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Currency

    id = FuzzyText(length=2)
    name = FuzzyText(length=6)


class CountryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Country

    id = FuzzyText(length=2)
    population = 2
    continent = factory.SubFactory(ContinentFactory)
    currency = factory.SubFactory(CurrencyFactory)
