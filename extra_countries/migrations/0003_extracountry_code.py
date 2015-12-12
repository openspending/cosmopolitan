# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_countries', '0002_auto_20151208_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='extracountry',
            name='code',
            field=models.CharField(max_length=3, default='', db_index=True),
        ),
    ]
