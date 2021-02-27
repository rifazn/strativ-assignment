"""Defines URL patterns for 'restcountries'"""

from django.urls import path

from . import views

app_name = 'restcountries'
urlpatterns = [
    path('', views.index, name='index'),
    # Paths for exposing the REST API
    path('rest/all', views.api_all, name='api_all'),
]
