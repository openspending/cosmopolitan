[![Build Status](https://travis-ci.org/openspending/cosmopolitan.svg?branch=master)](https://travis-ci.org/openspending/cosmopolitan) [![Coverage Status](https://coveralls.io/repos/openspending/cosmopolitan/badge.svg?branch=master&service=github)](https://coveralls.io/github/openspending/cosmopolitan?branch=master)

# Cosmopolitan
An API server for core data on places of the world.

Based on https://github.com/coderholic/django-cities

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
    python manage.py migrate currencies zero
    python manage.py migrate extra_countries zero
    
    python manage.py migrate continents
    python manage.py migrate currencies
    python manage.py migrate extra_countries