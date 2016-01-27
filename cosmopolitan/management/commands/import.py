from __future__ import print_function

from optparse import make_option

from django.core.management.base import BaseCommand

from cities.models import Country as DjangoCitiesCountry

from cosmopolitan.models import Continent
from cosmopolitan.models import Country
from cosmopolitan.models import Currency

# more stuff could be added here
IMPORT_OPTS = [
    "all",
    "django_cities",
]

def process_continents():
    continents_data = [
        {'id': 'af', 'name': 'Africa', 'geoNameId': 6255146},
        {'id': 'as', 'name': 'Asia', 'geoNameId': 6255147},
        {'id': 'eu', 'name': 'Europe', 'geoNameId': 6255148},
        {'id': 'na', 'name': 'North America', 'geoNameId': 6255149},
        {'id': 'oc', 'name': 'Oceania', 'geoNameId': 6255151},
        {'id': 'sa', 'name': 'South America', 'geoNameId': 6255150},
        {'id': 'an', 'name': 'Antarctica', 'geoNameId': 6255152},
    ]

    Continent.objects.all().delete()

    print("\n--- Seeding continents: ---")

    for continent in continents_data:
        c = Continent(id=continent['id'], name=continent['name'], geoNameId=continent['geoNameId'])
        c.save()
        print(".", end="")

def process_countries():
    Country.objects.all().delete()

    print("\n--- Seeding countries: ---")

    for country in DjangoCitiesCountry.objects.all():
        ex = Country(pk=country.code.lower(),
                          code3=country.code3.lower(),
                          name=country.name,
                          slug=country.slug,
                          population=country.population)
        ex.save()
        print(".", end="")

def process_currencies():
    Currency.objects.all().delete()

    print("\n--- Seeding currencies for countries ---")

    for dc_country in DjangoCitiesCountry.objects.all():
        if (str(dc_country.currency) == '') or (str(dc_country.currency_name) == ''):
            continue
        # trying to find a currency with the same code first
        try:
            currency = Currency.objects.get(pk=dc_country.currency.lower())
        except Currency.DoesNotExist: # no such currency yet
            currency = Currency(pk=dc_country.currency.lower(),
                                name=dc_country.currency_name)
        currency.save()
        country = Country.objects.get(pk=dc_country.code.lower())
        currency.countries.add(country.pk)
        print(".", end="")

def process_relations():
    process_continents_to_countries()
    process_continents_to_currencies()
    process_currencies_to_countries()
    process_countries_to_continents()
    process_currencies_to_continents()

def process_continents_to_countries():
    for country in Country.objects.all():
        if country.continent:
            country.continent.delete()

    print("\n--- Adding continents to countries ---")

    for country in Country.objects.all():
        dc_country = DjangoCitiesCountry.objects.get(code=country.pk.upper())
        continent = Continent.objects.get(pk=dc_country.continent.lower())
        country.continent_id = continent.pk
        country.save()
        print(".", end="")

def process_continents_to_currencies():
    for continent in Continent.objects.all():
        continent.currencies.all().delete()

    print("\n--- Adding continents to currencies ---")

    for currency in Currency.objects.all():
        for country in currency.countries.all():
            continent = country.continent

            if not currency.continents.filter(pk=continent.pk).exists():
                currency.continents.add(continent.pk)
                print(".", end="")

def process_currencies_to_countries():
    for country in Country.objects.all():
        if country.currency:
            country.currency.delete()

    print("\n--- Adding currencies to countries ---")

    for dc_country in DjangoCitiesCountry.objects.all():
        try:
            currency = Currency.objects.get(pk=dc_country.currency.lower())
            country = Country.objects.get(pk=dc_country.code.lower())
            country.currency_id = currency.pk
            country.save()
            print(".", end="")
        except Currency.DoesNotExist:
            pass

def process_currencies_to_continents():
    for continent in Continent.objects.all():
        continent.currencies.all().delete()

    print("\n--- Adding currencies to continents ---")

    for continent in Continent.objects.all():
        for country in continent.countries.all():
            try:
                dc_country = DjangoCitiesCountry.objects.get(code=country.pk.upper())
                currency = Currency.objects.get(pk=dc_country.currency.lower())
                if not continent.currencies.filter(pk=currency.pk).exists():
                    continent.currencies.add(currency.pk)
                    print(".", end="")
            except Currency.DoesNotExist:
                pass

def process_countries_to_continents():
    for continent in Continent.objects.all():
        continent.countries.all().delete()

    print("\n--- Adding countries to continents ---")

    for continent in Continent.objects.all():
        for country in Country.objects.all():
            if not continent.countries.filter(pk=country.pk).exists():
                if country.continent.pk == continent.pk:
                    continent.countries.add(country.pk)
                    print(".", end="")



class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("--from", metavar="IMPORT_SOURCE", default='all',
                    help="Selectively import data. Comma separated list of import sources: "
                    + str(IMPORT_OPTS).replace("'", "")
                   ),
    )

    def handle(self, *args, **options):
        self.options = options
        self.data_sources = [e for e in self.options["from"].split(",") if e]

        if not set(self.data_sources).issubset(set(IMPORT_OPTS)):
            raise ValueError("Invalid option")

        for data_source in self.data_sources:
            func = getattr(self, "_import_" + data_source)
            func()

    def _import_django_cities(self):
        process_continents()
        process_countries()
        process_currencies()
        process_relations()

    def _import_all(self):
        self._import_django_cities()
        print("\nImport finished")
