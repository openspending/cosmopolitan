[![Build Status](https://travis-ci.org/openspending/cosmopolitan.svg?branch=master)](https://travis-ci.org/openspending/cosmopolitan) [![Coverage Status](https://coveralls.io/repos/openspending/cosmopolitan/badge.svg?branch=master&service=github)](https://coveralls.io/github/openspending/cosmopolitan?branch=master)

# Cosmopolitan
An API server for core data on places of the world.

Based on https://github.com/coderholic/django-cities

## Using the API

Add param `format=json` in every request you want to perform to get JSON responses.
For example: `GET /v1/?format=json`.

API has self-documented format, so when you request to `/` (root of the API without any params) you'll get descriptions of all endpoints and can follow them for more descriptions.

You could also use filters when using this API:

### Filter countries by continents

* `/v1/countries/?continents={code}` - get countries of the particular continent;
* `/v1/countries/?continents={code},{code},{code}` - get countries belongs to several continents.

Example: `GET /v1/countries/?continents=an`, `GET /v1/countries/?continents=an,af`

### Filter currencies by countries

* `/v1/currencies/?countries={code}` - get currencies of the particular country;
* `/v1/currencies/?countries={code},{code},{code}` - get currencies belongs to several countries.

Example: `GET /v1/currencies/?countries=aq`, `GET /v1/currencies/?countries=aq,af`


## Running locally

Under virtual env:

    . env/bin/activate

    export LOCAL_DEV=1

    export DEBUG=1

## Starting from scratch

if you just pulled this repo, you need to:

* fill in cities database with ```python manage.py cities --import=all```;
* re-migrate all models on top with

    python manage.py migrate continents zero

    python manage.py migrate
