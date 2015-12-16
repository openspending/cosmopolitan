# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0001_initial'),
        ('currencies', '0001_initial'),
        ('cities', '0002_auto_20151112_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCountry',
            fields=[
                ('code', models.CharField(serialize=False, primary_key=True, max_length=3)),
                ('country', models.OneToOneField(to='cities.Country')),
                ('extra_continent', models.ForeignKey(to='continents.Continent', null=True)),
                ('extra_currency', models.ForeignKey(to='currencies.Currency', null=True)),
            ],
        ),
    ]
