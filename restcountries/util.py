import requests

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

def populate_countries_db():
    pass
