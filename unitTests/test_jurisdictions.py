from provinces_dictionary import canadian_provinces
from provinces_dictionary import us_states
import unittest

class TestJurisdiction(unittest.TestCase):
    def setUp(self):
        self.list_of_canadian_provinces_and_territories = list(canadian_provinces.keys())
        self.list_of_american_states = list(us_states.keys())

    def test_correct_number_of_canadian_provinces(self):
        number = len(self.list_of_canadian_provinces_and_territories)
        self.assertTrue(number == 13)

    def test_correct_number_of_american_states(self):
        number = len(self.list_of_american_states)
        self.assertTrue(number == 50)

if __name__ == "__main__":
    unittest.main()