"""test_dataset.py: Tests the functionality of dataset.py."""

__author__      = "Sohaila Ridwan"
__date__   = "March 25, 2018"


import os
from datetime import datetime
from .context import dataset

def test_load_dataset():
    """Validate that data is loaded"""
    data = dataset.load_dataset()
    assert len(data) > 0, "No data is loaded."

def test_dataset_column_count():
    """Validate each record in provided data (their format)"""
    data = dataset.load_dataset()
    c = 0
    for row in data:
        if len(row) == 6:
            c+=1
    assert c == len(data), "Mismatched columns in {} row.".format(len(data)-c)

def test_last_column_is_float():
    """Validate that price is a float for all records"""
    data = dataset.load_dataset()
    f = 0
    for row in data:
        try:
            price = float(row[-1])
            if type(price) is float:
                f+=1
        except Exception as e:
            pass
    assert f == len(data), "Invalid type for price in {} rows.".format(len(data)-f)


def test_first_column_is_date():
    """Validate that the first column is a date for each record"""
    data = dataset.load_dataset()
    d = 0
    for row in data:
        try:
            date = datetime.strptime(row[0], "%Y/%m")
            if type(date) is datetime:
                d+=1
        except Exception as e:
            pass
    assert len(data) == d, "Invalid date format in {} rows.".format(len(data)-d)
