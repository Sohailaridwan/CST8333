"""db_meta.py: Fetches list of tables, and meta information for table 'CATEGORIES' from database."""

__author__      = "Sohaila Ridwan"
__date__   = "March 25, 2018"

from peewee import *

# SQLite Database access variable
db = SqliteDatabase("app.db")


def show_tables():
    """Shows a list containing all the tables in the database."""
    """print("\nAuthor: Sohaila Ridwan")"""
    print("Database contains following tables:")
    print(db.get_tables())


def show_primary_key_for_categories_table():
    """Shows the primary key for table 'categories'"""
    print("\nAuthor: Sohaila Ridwan")
    print("The primary key column for table 'categories':")
    print(db.get_primary_keys('categories'))


def show_table_desc_for_categories_table():
    """Shows schema definition for table 'categories'."""
    """print("\nAuthor: Sohaila Ridwan")"""
    print("The schema definition for table 'categories':")
    print(db.get_columns('categories'))


def show_primary_key(table):
    """Shows the primary key for table 'categories'"""
    """print("\nAuthor: Sohaila Ridwan")"""
    print("The primary key for table '" + table + "': ")
    print(db.get_primary_keys(table))


def show_table_desc(table):
    """Shows schema definition for table 'categories'."""
    """ print("\nAuthor: Sohaila Ridwan")"""
    print("The schema definition for table '" + table + "': ")
    print(db.get_columns(table))


if __name__ == '__main__':
    show_primary_key('categories')
    show_tables()
    # show_primary_key_for_categories_table()
    # show_table_desc_for_categories_table()
