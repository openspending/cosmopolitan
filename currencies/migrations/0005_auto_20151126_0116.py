# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from cities.models import Country


def seed_data(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Currency = apps.get_model("currencies", "Currency")

    for country in Country.objects.all():
        print("seeding currency for county: %s" % country.name)
        if not country.code:
            continue
        # trying to find a currency with the same code
        try:
            currency = Currency.objects.get(code=country.currency)
        except Currency.DoesNotExist:
            currency = Currency(code=country.currency, name=country.currency_name)
            currency.save()
        currency.countries.add(country.pk)

def reverse_data(apps, schema_editor):
    Currency = apps.get_model("currencies", "Currency")
    Currency.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0004_currency_countries'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_data)
    ]
