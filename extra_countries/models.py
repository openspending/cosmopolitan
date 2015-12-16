from django.db import models


class ExtraCountry(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    extra_currency = models.ForeignKey('currencies.Currency', null=True)
    extra_continent = models.ForeignKey('continents.Continent', null=True)
    country = models.OneToOneField('cities.Country')
