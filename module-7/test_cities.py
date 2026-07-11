# Roxanne Buenaventura
# CSD325
# Assignment 7_2
# 10 July 2026 

import unittest
from city_functions import get_city_country

class TestCityFunctions(unittest.TestCase):
    """Test for the function get_city_country()."""

    def test_city_country(self):
        """Do city and country paids return a correctly formatted string?"""
        formatted_string = get_city_country("santiago", "chile")
        self.assertEqual(formatted_string, "Santiago, Chile")   

if __name__ == '__main__':
    unittest.main()
