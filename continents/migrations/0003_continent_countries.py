# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0002_auto_20151112_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='countries',
            field=models.ManyToManyField(related_name='related_continent_country', to='cities.Country'),
        ),
    ]
