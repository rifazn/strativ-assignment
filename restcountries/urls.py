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
    # JSON query of neighbors of a specific country
    path('rest/neighbours/<str:name>/', views.api_neighbours, name='api_neighbours'),
    # JSON query of countries speaking the language provided
    path('rest/language/<str:language>/', views.api_same_language,
         name='same_language'),
    # JSON query by search pattern
    path('rest/search_country/<str:search_term>/', views.api_search_country,
         name='api_search_country'),
]
