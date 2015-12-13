# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from continents.models import Continent

def seed_data(apps, schema_editor):
    # We can't import the Continent model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Currency = apps.get_model("currencies", "Currency")

    for currency in Currency.objects.all():
        for country in currency.countries.all():
            continent = Continent.objects.get(code=country.continent)
            if not currency.continents.filter(pk=continent.pk).exists():
                print("Seeding continent %s" % continent.name)
                currency.continents.add(continent.pk)


def revert_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0007_currency_continents'),
        ('continents', '0006_auto_20151213_1507')
    ]

    operations = [
        migrations.RunPython(seed_data, revert_data)
    ]
