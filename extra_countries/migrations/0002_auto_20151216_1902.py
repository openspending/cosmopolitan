# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from cities.models import Country

from continents.models import Continent

def seed_data(apps, schema_editor):
    ExtraCountry = apps.get_model("extra_countries", "ExtraCountry")
    for country in Country.objects.all():
        print("seeding data for county: %s" % country.name)
        ex = ExtraCountry(country_id=country.pk,
                          code=country.code.lower(),
                          code3=country.code3.lower())
        ex.save()

def reverse_data(apps, schema_editor):
    for continent in Continent.objects.all():
        continent.countries.all().delete()

    ExtraCountry = apps.get_model("extra_countries", "ExtraCountry")
    ExtraCountry.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('extra_countries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_data)
    ]
