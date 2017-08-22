"""Test latin square."""
import unittest

import src


class LatinSquareTestCase(unittest.TestCase):
    """Unit test for the latin square."""

    def test_random_test(self):
        """Test random."""
        self.assert_('message', 'message')

    def test_is_not_latin_square(self):
        """Test a given array is not a latin square."""
        self.assertFalse(src.latin_square.is_latin_square(0, [1, 2, 3]))
