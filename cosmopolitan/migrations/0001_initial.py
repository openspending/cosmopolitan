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
                ('id', models.CharField(primary_key=True, max_length=2, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('geoNameId', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=2, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='ascii name')),
                ('slug', models.CharField(max_length=200)),
                ('population', models.IntegerField()),
                ('code3', models.CharField(max_length=3)),
                ('continent', models.ForeignKey(to='cosmopolitan.Continent', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=3, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('continents', models.ManyToManyField(to='cosmopolitan.Continent')),
                ('countries', models.ManyToManyField(to='cosmopolitan.Country', related_name='related_country')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ForeignKey(to='cosmopolitan.Currency', null=True),
        ),
        migrations.AddField(
            model_name='continent',
            name='countries',
            field=models.ManyToManyField(to='cosmopolitan.Country', related_name='related_continent_country'),
        ),
        migrations.AddField(
            model_name='continent',
            name='currencies',
            field=models.ManyToManyField(to='cosmopolitan.Currency'),
        ),
    ]
