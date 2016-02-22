import os
import json

from cosmopolitan.models import Country
from cosmopolitan.models import Polygon

import cosmopolitan.management.commands.service.common as common

# countrise data URL
# http://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip

COUNTRIES = {
                "file_name_without_extension": "ne_10m_admin_0_countries",
                "file_name": "ne_10m_admin_0_countries.zip",
            }

def process_countries():
    data = common.prepare_data(COUNTRIES)

    print("\n--- Seeding countries: ---")

    Polygon.objects.all().delete()

    for feature in data["features"]:
        json_country_code = feature["properties"]["ISO_A2"]
        try:
            country = Country.objects.get(pk=json_country_code.lower())
        except Country.DoesNotExist:
            print('Not found: ' + json_country_code, end='')

        country_Polygon = Polygon(id="%s:%s" % ("country", country.id))
        country_Polygon.type = "country"
        country_Polygon.type_id = country.id
        country_Polygon.polygon = json.dumps(feature["geometry"]["coordinates"])
        country_Polygon.save()

        print(".", end="", flush=True)
        print("Finish.")

CITIES = {
            "file_name_without_extension": "ne_10m_populated_places_simple",
            "file_name": "ne_10m_populated_places_simple.zip",
         }

def process_cities():
    data = common.prepare_data(CITIES)

    print("\n--- Seeding countries: ---")
