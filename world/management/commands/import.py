from __future__ import print_function

from optparse import make_option

from django.core.management.base import BaseCommand
from django.db import transaction

from cities.models import Country

from continents.models import Continent
from extra_countries.models import ExtraCountry
from currencies.models import Currency

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
    ExtraCountry.objects.all().delete()
    print("\n--- Seeding countries: ---")
    for country in Country.objects.all():
        ex = ExtraCountry(country_id=country.pk,
                          pk=country.code.lower(),
                          code3=country.code3.lower())
        ex.save()
        print(".", end="")

def process_currencies():
    Currency.objects.all().delete()

    print("\n--- Seeding currencies for countries ---")
    for extra_country in ExtraCountry.objects.all():
        # trying to find a currency with the same code first
        try:
            currency = Currency.objects.get(pk=extra_country.country.currency.lower())
        except Currency.DoesNotExist: # no such currency yet
            currency = Currency(pk=extra_country.country.currency.lower(),
                                name=extra_country.country.currency_name)
        if (str(extra_country.country.currency) == '') or (str(extra_country.country.currency_name) == ''):
            pass
        else:
            currency.save()
            currency.countries.add(extra_country.pk)
            print(".", end="")

def process_relations():
    process_continents_to_currencies()
    process_continents_to_countries()
    process_currencies_to_countries()
    process_currencies_to_continents()

def process_continents_to_currencies():
    for continent in Continent.objects.all():
        continent.currencies.all().delete()

    print("\n--- Adding continents to currencies ---")

    for currency in Currency.objects.all():
        for extra_country in currency.countries.all():
            continent = Continent.objects.get(pk=extra_country.country.continent.lower())
            if not currency.continents.filter(pk=continent.pk).exists():
                currency.continents.add(continent.pk)
                print(".", end="")

def process_continents_to_countries():
    for country in ExtraCountry.objects.all():
        if country.extra_continent:
            country.extra_continent.delete()

    print("\n--- Adding continents to countries ---")

    for country in Country.objects.all():
        ex = ExtraCountry.objects.get(country_id=country.pk)
        continent = Continent.objects.get(pk=country.continent.lower())
        ex.extra_continent_id = continent.pk
        ex.save()
        print(".", end="")

def process_currencies_to_countries():
    for country in ExtraCountry.objects.all():
        if country.extra_currency:
            country.extra_currency.delete()

    print("\n--- Adding currencies to countries ---")

    for extra_country in ExtraCountry.objects.all():
        try:
            currency = Currency.objects.get(pk=extra_country.country.currency.lower())
            extra_country.extra_currency_id = currency.pk
            extra_country.save()
            print(".", end="")
        except Currency.DoesNotExist:
            pass

def process_currencies_to_continents():
    for continent in Continent.objects.all():
        continent.currencies.all().delete()

    print("\n--- Adding currencies to continents ---")

    for continent in Continent.objects.all():
        for extra_country in continent.countries.all():
            try:
                currency = Currency.objects.get(name=extra_country.country.currency_name,
                                                pk=extra_country.country.currency.lower())
                if not continent.currencies.filter(pk=currency.pk).exists():
                    continent.currencies.add(currency.pk)
                    print(".", end="")
            except Currency.DoesNotExist:
                pass


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("--from", metavar="IMPORT_SOURCE", default='all',
                    help="Selectively import data. Comma separated list of import sources: "
                    + str(IMPORT_OPTS).replace("'", "")
                   ),
    )

    @transaction.atomic
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
        print("Import finished")
