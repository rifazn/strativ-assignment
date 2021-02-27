from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Country

# Create your views here.
def api_all(request):
    countries = Country.objects.all()
    countries_list = list(countries.values())

    return JsonResponse(countries_list, safe=False)

def index(request):
    return HttpResponse("Hello!")
