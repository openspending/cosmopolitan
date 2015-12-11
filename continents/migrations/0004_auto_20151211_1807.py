# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from cities.models import Country

def seed_data(apps, schema_editor):
    # We can't import the Continent model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Continent = apps.get_model("continents", "Continent")

    for country in Country.objects.all():
        continent = Continent.objects.get(code=country.continent)
        continent.countries.add(country.pk)

def revert_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0003_continent_countries'),
    ]

    operations = [
        migrations.RunPython(seed_data, revert_data)
    ]
