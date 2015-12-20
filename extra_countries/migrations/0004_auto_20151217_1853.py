# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from cities.models import Country

from currencies.models import Currency

def seed_currencies_to_countries(apps, schema_editor):
    ExtraCountry = apps.get_model("extra_countries", "ExtraCountry")
    for extra_country in ExtraCountry.objects.all():
        print("seeding currency data for county: %s" % extra_country.country.name)
        try:
            currency = Currency.objects.get(code=extra_country.country.currency.lower())
            extra_country.extra_currency_id = currency.pk
            extra_country.save()
        except Currency.DoesNotExist:
            pass

def reverse_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('extra_countries', '0003_auto_20151217_1654'),
        ('currencies', '0003_auto_20151216_1906')
    ]

    operations = [
        migrations.RunPython(seed_currencies_to_countries, reverse_data)
    ]
