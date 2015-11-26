from django.db import models
from cities.models import Country


class Currency(models.Model):
    code = models.CharField(max_length=3, null=False, unique=True)
    name = models.CharField(max_length=50, null=False)
    countries = models.ManyToManyField(Country, related_name='related_country')