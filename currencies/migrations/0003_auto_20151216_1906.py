# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from extra_countries.models import ExtraCountry
from continents.models import Continent


def add_currencies_with_countries(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Currency = apps.get_model("currencies", "Currency")

    for extra_country in ExtraCountry.objects.all():
        print("seeding currency for county: %s" % extra_country.country.name)
        # trying to find a currency with the same code first
        try:
            currency = Currency.objects.get(code=extra_country.country.currency.lower())
        except Currency.DoesNotExist: # no such currency yet
            currency = Currency(code=extra_country.country.currency.lower(),
                                name=extra_country.country.currency_name)
        if (str(extra_country.country.currency) == '') or (str(extra_country.country.currency_name) == ''):
            pass
        else:
            currency.save()
            currency.countries.add(extra_country.pk)

def reverse_data(apps, schema_editor):
    for continent in Continent.objects.all():
        continent.currencies.all().delete()

    Currency = apps.get_model("currencies", "Currency")
    Currency.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('extra_countries', '0002_auto_20151216_1902'),
        ('currencies', '0002_currency_countries'),
    ]

    operations = [
        migrations.RunPython(add_currencies_with_countries, reverse_data)
    ]
