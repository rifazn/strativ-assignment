from rest_framework import serializers
from . import models

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Country
        fields = ('url', 'name', 'alphacode2', 'capital', 'population',
                  'timezone', 'flag', 'languages', 'neighbouring_countries')
