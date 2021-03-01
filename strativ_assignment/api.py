from rest_framework import routers
from restcountries import api_views

router = routers.DefaultRouter()
router.register('countries', api_views.CountryViewset)

