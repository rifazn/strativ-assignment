from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from .models import Country

# Create your views here.
def api_all(request):
    countries = Country.objects.all()
    countries_list = list(countries.values())

    return JsonResponse(countries_list, safe=False)

def api_country_name(request, name):
    try:
        country = Country.objects.get(name=name.capitalize())
        return JsonResponse(model_to_dict(country))
    except Exception as er:
        print(er)
        err = {'message': 'Sorry. That country name does not exist'}
        return JsonResponse(err, status=404)

def index(request):
    return HttpResponse("Hello!")
