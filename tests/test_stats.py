"""test_stats.py: Tests the functionality of dataset.py."""

__author__      = "Sohaila Ridwan"
__date__   = "April 15, 2018"

from context import model
import unittest

class TestStats(unittest.TestCase):

    def test_yearly_average(self):
        value = model.Stats.get_yearly_average(2010, 26)
        assert type(value) is float, 'Invalid type for average value!'
