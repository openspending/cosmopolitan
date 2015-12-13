# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0006_auto_20151213_1507'),
        ('currencies', '0006_auto_20151207_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='continents',
            field=models.ManyToManyField(to='continents.Continent'),
        ),
    ]
