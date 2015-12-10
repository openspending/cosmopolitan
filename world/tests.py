from rest_assured.testcases import BaseRESTAPITestCase
from rest_assured.testcases import ListAPITestCaseMixin
from .factory_boys import *


class CountriesTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'extra_country'
    factory_class = ExtraCountryFactory


class RegionTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'region'
    factory_class = RegionFactory


class SubRegionTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'subregion'
    factory_class = SubregionFactory


class CityTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'city'
    factory_class = CityFactory


class ContinentTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'continent'
    factory_class = ContinentFactory


class CurrencyTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'currency'
    factory_class = CurrencyFactory