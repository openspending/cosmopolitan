from django.db import models

from cities.models import Country

from currencies.models import Currency
from continents.models import Continent

class ExtraCountry(models.Model):
    extra_currency = models.ForeignKey(Currency)
    extra_continent = models.ForeignKey(Continent)
    country = models.OneToOneField(Country, primary_key=True)
    code = models.CharField(max_length=3, db_index=True, default='')
