from django.db import models


class ExtraCountry(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    code3 = models.CharField(max_length=3)
    extra_currency = models.ForeignKey('currencies.Currency', null=True)
    extra_continent = models.ForeignKey('continents.Continent', null=True)
    country = models.OneToOneField('cities.Country')
