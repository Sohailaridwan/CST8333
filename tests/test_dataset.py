"""test_dataset.py: Tests the functionality of dataset.py."""

__author__      = "Sohaila Ridwan"
__date__   = "April 15, 2018"


"""//from context import dataset.*"""
import dataset
import unittest

class TestDataset(unittest.TestCase):

    def test_inheritance(self):
        new_category = dataset.Categories.create(desc="Test Category")
        new_category.save()

        assert isinstance(new_category, dataset.BaseModel) is True,\
            "Error: super and sub-class relationship"


    def test_database_insertion(self):
        new_category = dataset.Categories.create(desc="Test Category")
        new_category.save()

        assert isinstance(new_category, dataset.BaseModel) is True, \
            "Error: super and sub-class relationship"

        assert type(new_category) is dataset.Categories, \
            "Could not insert data!"


    def test_database_delete(self):
        new_category = dataset.Categories.create(desc="Test Category")
        new_category.save()

        assert type(new_category) is dataset.Categories, \
            "Could not insert data!"

        new_category.delete_instance()

        y = None

        try:
            y = dataset.Categories.get(dataset.Categories.id == new_category.id)
        except Exception:
            pass

        assert y is None, "Could not remove dummy test row!"
