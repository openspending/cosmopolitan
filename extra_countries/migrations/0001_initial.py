# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
        ('continents', '0001_initial'),
        ('cities', '0002_auto_20151112_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCountry',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('country', models.OneToOneField(to='cities.Country')),
                ('extra_continent', models.ForeignKey(to='continents.Continent')),
                ('extra_currency', models.ForeignKey(to='currencies.Currency')),
            ],
        ),
    ]
