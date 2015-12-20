# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from extra_countries.models import ExtraCountry

def seed_countries_to_continents(apps, schema_editor):
    # We can't import the Continent model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Continent = apps.get_model("continents", "Continent")

    for extra_country in ExtraCountry.objects.all():
        continent = Continent.objects.get(code=extra_country.country.continent.lower())
        if not continent.countries.filter(pk=extra_country.pk).exists():
            print("Seeding country data for continent: %s" % continent.name)
            continent.countries.add(extra_country.pk)


def revert_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0003_auto_20151216_1903'),
        ('extra_countries', '0002_auto_20151216_1902')
    ]

    operations = [
        migrations.RunPython(seed_countries_to_continents, revert_data)
    ]
