# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from currencies.models import Currency

def seed_currencies_to_continents(apps, schema_editor):
    # We can't import the Continent model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Continent = apps.get_model("continents", "Continent")

    for continent in Continent.objects.all():
        print("Seeding currency data for continent: %s" % continent.name)
        for extra_country in continent.countries.all():
            try:
                currency = Currency.objects.get(name=extra_country.country.currency_name,
                                                code=extra_country.country.currency)
                if not continent.currencies.filter(pk=currency.pk).exists():
                    print("Seeding currency %s" % currency.name)
                    continent.currencies.add(currency.pk)
            except Currency.DoesNotExist:
                pass


def revert_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0004_auto_20151217_1901'),
        ('currencies', '0003_auto_20151216_1906')
    ]

    operations = [
        migrations.RunPython(seed_currencies_to_continents, revert_data)
    ]
