# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=2)),
                ('name', models.CharField(max_length=50)),
                ('geoNameId', models.PositiveIntegerField()),
            ],
        ),
    ]
