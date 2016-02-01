# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cosmopolitan', '0002_auto_20160128_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('region_name', models.CharField(max_length=100, db_index=True)),
                ('subregion_name', models.CharField(max_length=100, db_index=True)),
                ('district_name', models.CharField(max_length=100, db_index=True)),
                ('country', models.ForeignKey(to='cosmopolitan.Country', related_name='postal_codes')),
            ],
        ),
    ]
