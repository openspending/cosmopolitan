# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0006_auto_20151207_1445'),
        ('continents', '0004_auto_20151211_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='currencies',
            field=models.ManyToManyField(to='currencies.Currency'),
        ),
    ]
