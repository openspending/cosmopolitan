# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0001_initial'),
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCountry',
            fields=[
                ('lookup', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('code3', models.CharField(max_length=3)),
                ('country', models.OneToOneField(to='cities.Country')),
                ('extra_continent', models.ForeignKey(null=True, to='continents.Continent')),
                ('extra_currency', models.ForeignKey(null=True, to='currencies.Currency')),
            ],
        ),
    ]
