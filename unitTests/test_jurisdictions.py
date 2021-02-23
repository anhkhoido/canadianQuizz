from provinces_dictionary import canadian_provinces
from provinces_dictionary import us_states
import unittest

class TestJurisdiction(unittest.TestCase):
    def test_correct_number_of_canadian_provinces(self):
        list_canadian_provinces = list(canadian_provinces.values())
        number = len(list_canadian_provinces)
        self.assertTrue(number == 13)
    def test_correct_number_of_american_states(self):
        list_american_states = list(us_states.values())
        number = len(list_american_states)
        self.assertTrue(number == 50)
unittest.main()