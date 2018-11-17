import unittest
from city_function import country_city_total_information

class TestCountryFunction(unittest.TestCase):
    def test_country_city_function(self):
        city_total_information = country_city_total_information('france', 'paris')
        self.assertEqual(city_total_information, 'France, Paris')

    def test_country_city_population(self):
        city_total_information = country_city_total_information('france', 'paris', '5 000 000')
        self.assertEqual(city_total_information, 'France, Paris - 5 000 000')

unittest.main()