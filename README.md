# Cosmopolitan

[![Gitter](https://img.shields.io/gitter/room/openspending/chat.svg)](https://gitter.im/openspending/chat)
[![Build Status](https://travis-ci.org/openspending/cosmopolitan.svg?branch=master)](https://travis-ci.org/openspending/cosmopolitan) [![Coverage Status](https://coveralls.io/repos/openspending/cosmopolitan/badge.svg?branch=master&service=github)](https://coveralls.io/github/openspending/cosmopolitan?branch=master)

An API server for core data on places of the world.

http://cosmopolitan.openspending.org/

This API provides information about countries, cities and currencies all over the world and can be used as a cataloged data for various reasons.

Just a brief summary:

* contains a list of all countries in the world with country code, country continent and list of countries on the same continent;
* contains a list of all continents in the world with a list of countries for each continent;
* contains a list of all regions in the world with a list of cities for each country;
* contains a list of all cities in the world with population over 5000;
* contains a list of all currencies in the world, each currency has a list of countries where this currency is being used.

Based on https://github.com/coderholic/django-cities

## Using the API

Add param `format=json` in every request you want to perform to get JSON responses.
For example: `GET /v1/?format=json`.

API has self-documented format, so when you request to `/` (root of the API without any params) you'll get descriptions of all endpoints and can follow them for more descriptions.

You could also use filters when using this API:

### Filter: countries by continents

* `/v1/countries/?continents={id}` - get countries of the particular continent;
* `/v1/countries/?continents={id},{id},{id}` - get countries belongs to several continents.

Example: `GET /v1/countries/?continents=an`, `GET /v1/countries/?continents=an,af`

### Filter: currencies by countries

* `/v1/currencies/?countries={id}` - get currencies of the particular country;
* `/v1/currencies/?countries={id},{id},{id}` - get currencies belongs to several countries.

Example: `GET /v1/currencies/?countries=aq`, `GET /v1/currencies/?countries=aq,af`

### Filter: cities by countries

* `/v1/cities/?countries={id}` - get cities of the particular country;
* `/v1/cities/?countries={id},{id},{id}` - get cities belong to several countries.

Example: `GET /v1/cities/?countries=gr`, `GET /v1/cities/?countries=gr,us`

### Filter: cities by regions

* `/v1/cities/?regions={id}` - get cities of the particular region;
* `/v1/cities/?regions={id},{id},{id}` - get cities belong to several regions.

Example: `GET /v1/cities/?regions=tx`, `GET /v1/cities/?countries=tx,il`

### Filter: cities by continents

* `/v1/cities/?continents={id}` - get cities of the particular continent;
* `/v1/cities/?continents={id},{id},{id}` - get cities belong to several continents.

Example: `GET /v1/cities/?continents=eu`, `GET /v1/cities/?continents=eu,af`

### Filter: cities by slug

* `/v1/cities/?slugs={slug}` - get cities matching the particular slug, ;
* `/v1/cities/?slugs={slug},{slug},{slug}` - get cities matching to several slugs.

Example: `GET /v1/cities/?slugs=athens`, `GET /v1/cities/?slugs=athens,paris`
** where slug means the name of the city in lowercase with no accents and instead of spaces,  hyphens "-"

### Filter: multiple filters

You can also define multiple filters on the city endpoint.

Example: `GET /v1/cities/?slugs=athens,paris&countries=us&regions=tx`

### Filter: countries polygons by countries

* `/v1/countrypolygons/?countries={id},{id},{id}`

### Filter: get list of countries polygons for region(s)

* `/v1/countrypolygons/?regions={id},{id},{id}`

### Filter: all polygons by countries

* `/v1/polygons/?countries={id},{id},{id}`

### Filter: get list of all polygons for region(s)

* `/v1/polygons/?regions={id},{id},{id}`

## Running locally

Under virtual env (to create virtualenv, run `python3 -m venv env`):

    source env/bin/activate

    export LOCAL_DEV=1

    export DEBUG=1

Postgres + PostGIS setup (OS X):

    brew install postgis

    createuser cosmopolitan

    createdb cosmopolitan

    psql cosmopolitan

    alter user "cosmopolitan" with password '123456';

    grant all privileges on database cosmopolitan to cosmopolitan;

    CREATE EXTENSION postgis;

If you want your user to have super privileges:

    ALTER USER cosmopolitan WITH SUPERUSER;

Tip for local development using (OS X)

Install [GDAL binaries]() for OSX, and add the following to .bash_profile:

    GDAL_LIBRARY_PATH="/Library/Frameworks/GDAL.framework/Versions/1.11/GDAL"
    GEOS_LIBRARY_PATH="/Library/Frameworks/GEOS.framework/Versions/3/GEOS"

Then add the following to your local Django settings:

    # GeoDjango fixes
    GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
    GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')

(see https://www.alextomkins.com/2017/08/fixing-gdal-geos-django-macos/ for details)

## Starting from scratch

### Requirements

* [GDAL/OGR Binaries](http://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries)

If you just pulled this repo, you need to:

* run migrations `./manage.py migrate`
* fill in cities database with `./manage.py cities --import=all`;
* import data to cosmopolitan tables: `./manage.py import`

## License

`Cosmopolitan` is opensource, licensed under a standard MIT license (included in this repository as [LICENSE](https://github.com/openspending/cosmopolitan/blob/master/LICENSE)).

Data sources licensies:

- [GeoNames](http://www.geonames.org/about.html) is under a creative commons attribution license.
- [NaturalEarthData terms of use](naturalearthdata.com/about/terms-of-use/)
