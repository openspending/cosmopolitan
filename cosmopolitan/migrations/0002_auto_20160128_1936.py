# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cosmopolitan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='ascii name')),
                ('name_std', models.CharField(db_index=True, max_length=200, verbose_name='standard name')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('population', models.IntegerField()),
                ('elevation', models.IntegerField(null=True)),
                ('kind', models.CharField(max_length=10)),
                ('timezone', models.CharField(max_length=40)),
                ('country', models.ForeignKey(to='cosmopolitan.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='ascii name')),
                ('name_std', models.CharField(db_index=True, max_length=200, verbose_name='standard name')),
                ('country', models.ForeignKey(to='cosmopolitan.Country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(blank=True, null=True, to='cosmopolitan.Region'),
        ),
    ]
