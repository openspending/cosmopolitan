from django.db import models


class ExtraCountry(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    extra_currency = models.ForeignKey('currencies.Currency')
    extra_continent = models.ForeignKey('continents.Continent')
    country = models.OneToOneField('cities.Country')
