"""Defines URL patterns for 'restcountries'"""

from django.urls import path

from . import views

app_name = 'restcountries'
urlpatterns = [
    path('', views.index, name='index'),

    # Paths for exposing the REST API

    # JSON response containing all countries in a list
    path('rest/all/', views.api_all, name='api_all'),
    # JSON response of a single country
    path('rest/country/<str:name>/', views.api_country_name, name='api_country_name'),
]
