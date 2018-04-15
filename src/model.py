"""model.py: Calculates the average price for a category."""

__author__      = "Sohaila Ridwan"
__date__   = "April 15, 2018"

from peewee import fn
from datetime import datetime
from dataset import PriceIndex, GeoCodes, Categories

class Stats(object):

    @staticmethod
    def get_yearly_average(year, category_code):
        """Returns the average price for a category."""
        result = PriceIndex.select(fn.Sum(PriceIndex.price).alias('sum'), fn.Count(PriceIndex.price).alias('count')).where((PriceIndex.category == category_code) & (PriceIndex.date.year == year)).scalar(as_tuple=True)

        if result[0]:
            return result[0]/result[1]
        else:
            return 0
