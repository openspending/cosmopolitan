from rest_assured.testcases import BaseRESTAPITestCase
from rest_assured.testcases import ListAPITestCaseMixin
from .factory_boys import *


class CountriesTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'country'
    factory_class = ExtraCountryFactory


class ContinentTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'continent'
    factory_class = ContinentFactory


class CurrencyTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'currency'
    factory_class = CurrencyFactory
