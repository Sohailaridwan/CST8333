"""db_meta.py: Fetches Database meta information."""

__author__      = "Sohaila Ridwan"
__date__   = "April 15, 2018"

from peewee import *

# SQLite Database access variable
db = SqliteDatabase("app.db")


def show_tables():
    """Shows a list containing all the tables in the database."""
    """print("\nAuthor: Sohaila Ridwan")"""
    print("Database contains following tables:")
    for table in db.get_tables():
        print("# {}".format(table))


def show_primary_key(table):
    """Shows the primary key for table 'categories'"""
    """print("\nAuthor: Sohaila Ridwan")"""
    print("The primary key for table '{}': ".format(table.__name__))
    fields = table._meta.fields
    keys = db.get_primary_keys(table.__name__)
    for key in keys:
        print("Primary Key Name: {} Type: {}".format(key, fields[key].field_type))

def show_table_desc(table):
    """Shows schema definition for table 'categories'."""
    """ print("\nAuthor: Sohaila Ridwan")"""
    print("The schema definition for table '{}': ".format(table.__name__))
    fields = table._meta.fields
    for k in fields:
        print("Column '{}': Type '{}'".format(k, fields[k].field_type))


if __name__ == '__main__':
    show_primary_key('categories')
    show_tables()
    # show_primary_key_for_categories_table()
    # show_table_desc_for_categories_table()
