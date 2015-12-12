# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def seed_data(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    ExtraCountry = apps.get_model("extra_countries", "ExtraCountry")

    for country in ExtraCountry.objects.all():
        print("seeding code for county: %s" % country.country.name)
        country.code = country.country.code3
        country.save()

def reverse_data(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('extra_countries', '0003_extracountry_code'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_data)
    ]
