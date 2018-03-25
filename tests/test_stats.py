"""test_stats.py: Tests the functionality of dataset.py."""

__author__      = "Sohaila Ridwan"
__date__   = "March 25, 2018"

from .context import model

def test_yearly_average():
    value = model.Stats.get_yearly_average(2010, 26)
    assert type(value) is float, 'Invalid type for average value!'