import requests
from .models import Country

def get_countries():
    """
    Return a dictionary of all countries from 'https:restcountries.eu/rest' api
    as described in the specification.
    """
    url = 'https://restcountries.eu/rest/v2/all'
    fields = ['name', 'alpha2Code', 'capital','population',
              'timezones','flag','languages','borders']
    fields = ';'.join(fields)
    params = {
        'fields': fields
    }

    res = requests.get(url, params=params)

    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful')

    data = res.json()

    return data

def populate_countries_db(data):
    """
    Initialize the databse by populating with data returned from
    get_countries().
    """
    for row in data:
        country = Country()
        country.name = row['name']
        country.alphacode2 = row['alpha2Code']
        country.capital = row['capital']
        country.population = row['population']
        country.timezone = row['timezones'][0]
        country.flag = row['flag']
        country.languages = ', '.join([lang['name'] for lang in row['languages']])
        country.neighbouring_countries = ', '.join(row['borders'])

        country.save()

def print_countries_db():
    """
    Print to stdout all entries from the 'Country' model which is populated by
    the restcountries API consumption.
    """
    args = ['No.', 'name', 'alphacode2', 'capital', 'population', 'timezone', 'flag',
            'languages', 'neighbouring_countries']
    print('{:<3}  {:<7}  {:<3}  {:<10}  {:<10}  {:6}  {:<10}  {:<10}  {:<20}'.format(*args))

    countries = Country.objects.all()
    for country in countries.all().values():
        print('{:<3}  {:<7}  {:<3}  {:<10}  {:<10}  {:6}  {:<25}  {:<10}  {:<20}'
              .format(*country.values()))

