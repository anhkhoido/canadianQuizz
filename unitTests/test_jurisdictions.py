from provinces_dictionary import canadian_provinces
from provinces_dictionary import us_states
import logging
import random
import unittest

logging.basicConfig(filename="unitTests/test_jurisdictions.log", format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TestJurisdiction(unittest.TestCase):
    def setUp(self):
        self.list_of_canadian_provinces_and_territories = list(canadian_provinces.keys())
        self.list_of_american_states = list(us_states.keys())
        self.list_of_canadian_capital_cities = list(canadian_provinces.values())

    def test_correct_number_of_canadian_provinces(self):
        logger.info("test_jurisdictions.py::TestJurisdiction.test_correct_number_of_canadian_provinces(self)")
        number = len(self.list_of_canadian_provinces_and_territories)
        self.assertTrue(number == 13)

    def test_correct_number_of_american_states(self):
        logger.info("test_jurisdictions.py::TestJurisdiction.test_correct_number_of_american_states(self)")
        number = len(self.list_of_american_states)
        self.assertTrue(number == 50)
    
    def test_correct_capital_city_for_quebec_without_shuffle(self):
        logger.info("test_jurisdictions.py::TestJurisdiction.test_correct_capital_city_for_quebec_without_shuffle(self)")
        quebec_city = self.list_of_canadian_capital_cities[0]
        expected_city = canadian_provinces['Quebec']
        self.assertEqual(quebec_city, expected_city)

if __name__ == "__main__":
    unittest.main()