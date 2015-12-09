# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0002_auto_20151112_1900'),
        ('currencies', '0006_auto_20151207_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCountry',
            fields=[
                ('country', models.OneToOneField(to='cities.Country', serialize=False, primary_key=True)),
                ('extra_continent', models.ForeignKey(to='continents.Continent')),
                ('extra_currency', models.ForeignKey(to='currencies.Currency')),
            ],
        ),
    ]
