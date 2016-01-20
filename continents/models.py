from django.db import models


class Continent(models.Model):
    lookup = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    geoNameId = models.PositiveIntegerField(blank=False)
    countries = models.ManyToManyField('extra_countries.ExtraCountry', related_name='related_continent_country')
    currencies = models.ManyToManyField('currencies.Currency')
