from django.db import models

class Continent(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    geoNameId = models.PositiveIntegerField(blank=False)
    countries = models.ManyToManyField('cosmopolitan.Country', related_name='related_continent_country')
    currencies = models.ManyToManyField('cosmopolitan.Currency')


class Country(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="ascii name")
    slug = models.CharField(max_length=200)
    population = models.IntegerField()
    code3 = models.CharField(max_length=3)
    currency = models.ForeignKey('cosmopolitan.Currency', null=True)
    continent = models.ForeignKey('cosmopolitan.Continent', null=True)


class Currency(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    countries = models.ManyToManyField('cosmopolitan.Country', related_name='related_country')
    continents = models.ManyToManyField('cosmopolitan.Continent')
