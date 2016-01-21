from django.db import models


class Currency(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    countries = models.ManyToManyField('extra_countries.ExtraCountry', related_name='related_country')
    continents = models.ManyToManyField('continents.Continent')
