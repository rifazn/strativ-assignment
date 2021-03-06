# Startiv Assignment for Job application

## Description

This is the task that was assigned to me for my job application at Strativ.se
as a Python Developer. The task requires consuming and exposing REST APIs.

Prior to applying for the job, I had used the `requests` module to consume
APIs, and returned `JsonResponse` objects for exposing APIs from within the
default django views. Therefore, I very soon reached my limitations when I had
to design `POST, PUT, DELETE` API requests using the default methods provided
by Django. Authenticating the APIs started becoming a tremendous challenge too.
This is when I found out about the `Django REST Framework` module. This is a
framework that enhances the default Django experience by making creation of
REST APIs using Django much more powerful and easier.

I had to learn the `Django REST Framework` while working for the assignment
and I found out that, since the level of abstraction is very high here, doing
something that reasonably looks very "basic" required me to learn the framework
quite well. I had to use StackOverflow and the official tutorial pages to really
be able to complete my tasks for the assignment. Now that I have learned the
framework, doing the same "basic" things should become much easier for me.

## Project structure

The name of the project is `interview-assignment` and the main app is called
`restcountries`.

## Instructions

1. Initialize a virtual environment

```sh
$ python -m venv venv
$ source venv/bin/activate
```

2. Install the requirements: `pip install -r requirements`
3. Run the server: `python manage.py runserver`

## Admin user

I created the admin user `admin` with password `1` that can be used to test
project initially. New users can be made by browsing the root url of the
project and click "Register" on the left side of the page.

## Phase 1

This phase required me to consume data from the restcountries.eu site. Then
save the data on the project's local database.

The `restcountries.utils.get_countries()` can be used to fetch data from
`restcountries.eu`. This function uses the `requests` module to send the GET
request.

The `restcountries.utils.populate_database(data)` method has been used to
populate the local database.

The `restcountries.utils.print_countries_db()` prints all the data from the
local database to the stdout. This can be used to verify that the database has
been populated succesfully after running the populate_database(data) method.

### Some shortcuts used to complete this phase

The `languages` field and the `borders` field of a country fetched from
restcountries.eu are of type `list`. I converted the lists to `str` type (with
comma seperated values) before storing to the local database to simplify
interacting with the database.

## Phase 2

To verify the tasks, this table can be used.

| No.   |  Function  |  API request and URL |
| :---: | :-------------------------- | :--------------------------------------- |
| 1.    | List all countries | GET `/api/countries` \* |
| 2.    | Specific country | GET `/api/countries/<pk>` \* |
| 3.    | Add a new country | Make POST request with data to `/api/countries` \* |
| 4.    | Update a country's details | PUT request with data to `/api/countries/<pk>` \* |
| 5.    | Delete a country instance | DELETE request to `/api/countries/<pk>` \* |
| 6.    | List a country's neighbours | GET request to `/api/countries/<pk>/neighbours/` |
| 7.    | List country's who speak a specified language | GET request to `/api/language/<str:language_name>` \*\* |
| 8.    | Search and list countries by partial country name | GET `api/countries/search=<str:name>&fields=name` |


+ __\*__: Also browsable by the browser
+ __\*\*__: GET `/api/countries/search=<str:language_name>&fields=languages`

### Some context (my experience in the phase)

You may find urls prefixed with `rest/` in the URLconf. Please use the urls
prefixed with `api/` to judge me.

I have littered the `restcountries.views` with views named with `api_`
prefixes. This is when I thought I could just return JsonResponses to expose
the project's API. This was before I had learned about the `Django Rest
Framework`. Therefore, the url config is also littered with `rest/` prefixed
urls. This is also why I did not include the `rest/` urls in the table above.

When I finally learned `Django Rest Framework` I used the
`restcountries/api-views.py` file to define `ViewSets` that correctly get
called with `api/` urls.

## Phase 3

Search countries ny name: use the search bar on the left hand side.

To browse a country in detail view, click on Details beside the country in the
table from the root directory.

## Phase 4

To browse the APIs, a user needs to be logged in. You can use (user,pass)
(`admin`,`1`) to log in from the root directory of the website, or register a
user using the 'Register' link on the website.

Thank you for giving me a chance here in Strativ and giving such a task to
complete. _The task was really interesting_ and I learned a lot of new things
while doing the assignment. I think I have completed all the tasks and I hope
that my work will be favorable.

Thanks to the Strativ team so very much again.
