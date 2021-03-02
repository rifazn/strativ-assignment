# Startiv Assignment for Job application

## Phase 2

| No.   |  Function  |  API request and URL |
| :---: | :-------------------------- | :--------------------------------------- |
| 1.    | List all countries | GET `/api/countries` \* |
| 2.    | Specific country | GET `/api/countries/<pk>` \* |
| 3.    | Add a new country | Make POST request with data to `/api/countries` \* |
| 4.    | Update a country's details | PUT request with data to `/api/countries/<pk>` \* |
| 5.    | Delete a country instance | DELETE request to `/api/countries/<pk>` \* |
| 6.    | List a country's neighbours | GET request to `/api/countries/1/neighbours/` |
| 7.    | List country's who speak a specified language | GET request to `/api/language/<str:language_name>` \*\* |
| 8.    | Search and list countries by partial country name | GET `api/countries/search=<str:name>&fields=name` |


+ __\*__: Also browsable by the browser
+ __\*\*__: GET `/api/countries/search=<str:language_name>&fields=languages`

