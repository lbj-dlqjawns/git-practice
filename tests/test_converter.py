"""Unit tests for the converter module."""

import unittest

from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
)


class ConverterTests(unittest.TestCase):
    def test_kilometers_to_miles(self):
        self.assertAlmostEqual(kilometers_to_miles(10), 6.21371)

    def test_miles_to_kilometers(self):
        self.assertAlmostEqual(miles_to_kilometers(6.21371), 10)

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)


if __name__ == "__main__":
    unittest.main()
