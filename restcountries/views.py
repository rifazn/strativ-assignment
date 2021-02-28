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
        country = Country.objects.get(name__iexact=name)
        return JsonResponse(model_to_dict(country))
    except Exception as er:
        print(er)
        err = {'message': 'Sorry. That country name does not exist'}
        return JsonResponse(err, status=404)

def api_search_country(request, search_term):
    """
    JSON response returning all countries where names contain 'search_term'
    """
    countries = Country.objects.filter(name__icontains=search_term)
    if countries.count() > 0:
        countries_list = list(countries.values())
        return JsonResponse(countries_list, safe=False)
    else:
        err = {'message': 'Your search term matched no country names'}
        return JsonResponse(err, status=404)

def api_neighbours(request, name):
    """
    Return as strings alpha3Code encoded list of neighbours of the specified
    country.
    """
    try:
        country = Country.objects.get(name__iexact=name)
        neighbours = country.neighbouring_countries
        return JsonResponse({'neighbours': neighbours})
    except Exception as er:
        print(er)
        err = {'message': 'Sorry. That country name does not exist'}
        return JsonResponse(err, status=404)

def api_same_language(request, language):
    """
    JSON Response list of all countries speaking 'language'
    """
    # Some sanity checks
    if len(language) < 1:
        err = {'message': 'Language cannot be of zero length.'}
        return JsonResponse(err, status=400)
    else:
        # Check if language name has digits in it
        # Could be easier using regex
        chars = list(language)
        hasDigits = True

        for digit in range(10):
            if digit in chars:
                break
        else:
            hasDigits = False

        if hasDigits:
            err = {
                'message': 'Your language name has digits. Sorry, robot \
                languages not supported yet.'
            }
            return JsonResponse(err, 404)

    same_lang_countries = Country.objects.filter(languages__icontains=language)
    countries_list = list(same_lang_countries.values())

    return JsonResponse(countries_list, safe=False)

def index(request):
    return HttpResponse("Hello!")
