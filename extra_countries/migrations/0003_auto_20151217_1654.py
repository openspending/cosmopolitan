# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from cities.models import Country

from continents.models import Continent

def seed_continents_to_countries(apps, schema_editor):
    ExtraCountry = apps.get_model("extra_countries", "ExtraCountry")
    for country in Country.objects.all():
        print("seeding data for county: %s" % country.name)
        ex = ExtraCountry.objects.get(country_id=country.pk)
        continent = Continent.objects.get(code=country.continent)
        ex.extra_continent_id = continent.pk
        ex.save()

def reverse_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('extra_countries', '0002_auto_20151216_1902'),
    ]

    operations = [
        migrations.RunPython(seed_continents_to_countries, reverse_data)
    ]
