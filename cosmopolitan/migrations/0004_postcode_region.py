# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmopolitan', '0003_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcode',
            name='region',
            field=models.ForeignKey(to='cosmopolitan.Region', null=True, blank=True),
        ),
    ]
