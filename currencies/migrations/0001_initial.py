# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', models.CharField(serialize=False, primary_key=True, max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('continents', models.ManyToManyField(to='continents.Continent')),
            ],
        ),
    ]
