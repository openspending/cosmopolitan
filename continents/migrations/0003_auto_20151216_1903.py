# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def seed_data(apps, schema_editor):
    # We can't import the Continent model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Continent = apps.get_model("continents", "Continent")

    continents_data = [
                        {'lookup': 'af', 'name': 'Africa', 'geoNameId': 6255146},
                        {'lookup': 'as', 'name': 'Asia', 'geoNameId': 6255147},
                        {'lookup': 'eu', 'name': 'Europe', 'geoNameId': 6255148},
                        {'lookup': 'na', 'name': 'North America', 'geoNameId': 6255149},
                        {'lookup': 'oc', 'name': 'Oceania', 'geoNameId': 6255151},
                        {'lookup': 'sa', 'name': 'South America', 'geoNameId': 6255150},
                        {'lookup': 'an', 'name': 'Antarctica', 'geoNameId': 6255152},
                      ]

    for continent in continents_data:
        print("seeding %s" % continent['name'])
        c = Continent(lookup=continent['lookup'], name=continent['name'], geoNameId=continent['geoNameId'])
        c.save()

def revert_data(apps, schema_editor):
    Continent = apps.get_model("continents", "Continent")
    Continent.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0002_auto_20151216_1902'),
    ]

    operations = [
        migrations.RunPython(seed_data, revert_data),
    ]
