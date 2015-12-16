# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
        ('extra_countries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='countries',
            field=models.ManyToManyField(to='extra_countries.ExtraCountry', related_name='related_country'),
        ),
    ]
