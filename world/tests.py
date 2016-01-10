from rest_assured.testcases import BaseRESTAPITestCase
from rest_assured.testcases import ListAPITestCaseMixin

from .factory_boys import ExtraCountryFactory
from .factory_boys import ContinentFactory
from .factory_boys import CurrencyFactory


class CountriesTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'extracountry'
    factory_class = ExtraCountryFactory


class ContinentTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'continent'
    factory_class = ContinentFactory


class CurrencyTest(BaseRESTAPITestCase, ListAPITestCaseMixin):
    base_name = 'currency'
    factory_class = CurrencyFactory
