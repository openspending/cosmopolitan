# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0003_auto_20151126_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='countries',
            field=models.ManyToManyField(related_name='related_country', to='cities.Country'),
        ),
    ]
