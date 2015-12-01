from django.db import models

class Continent(models.Model):
    code = models.CharField(max_length=2, blank=False)
    name = models.CharField(max_length=50, blank=False)
    geoNameId = models.PositiveIntegerField(blank=False)
