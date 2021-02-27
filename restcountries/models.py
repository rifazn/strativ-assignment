from django.db import models

# Create your models here.
class Country(models.Model):
    """Country model having all attributes as specified"""
    name = models.CharField(max_length=200)
    alphacode2 = models.CharField(max_length=3)
    capital = models.CharField(max_length=200)
    population = models.BigIntegerField()
    timezone = models.CharField(max_length=20)
    flag = models.CharField(max_length=200)
    languages = models.CharField(max_length=500) # TODO: make it a choicefield
    neighbouring_countries = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return f'{self.name[:50]}'
