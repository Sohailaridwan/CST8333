"""categories_crud.py: Does CRUD opeation on table 'CATEGORIES'."""
__author__      = "Sohaila Ridwan"
__date__   = "March 25, 2018"

from peewee import *
from dataset import *

"""SQLite Database access variable"""
db = SqliteDatabase("app.db")

def read_from_table(table):
    """"Does 'Read' from a table"""
    table.display()


def add_new_record(table):
    if table in [Categories, GeoCodes]:
        return add_new_record_v1(table)
    elif table in [PriceIndex]:
        return add_new_record_v2(table)
    else:
        print("Invalid table name.")

def add_new_record_v1(table):
    """"Does 'Insert' record in a table"""
    value = input("Enter value: ")
    result = table.create(desc=value)
    return result

def add_new_record_v2(table):
    """"Does 'Insert' record in priceindex table"""
    in_date = input("Enter Date (Format YYYY-MM-DD HH:MM:SS): ")
    in_geocode = input("Enter Geocode (Integer): ")
    in_cat_id = input("Enter Category ID (Integer): ")
    in_vector = input("Enter Vector Value (Format: vXXXXXXX): ")
    in_price = input("Enter Price (Fraction): ")

    result = table.create(date=in_date,
                 geocode=in_geocode,
                 category=in_cat_id,
                 vector=in_vector,
                 price=float(in_price))

    return result

def update_record(table):
    if table in [Categories, GeoCodes]:
        return update_record_v1(table)
    elif table in [PriceIndex]:
        return update_record_v2(table)
    else:
        print("Invalid table name.")

def update_record_v1(table):
    value = input("Enter id: ")
    row = table.get(table.id == value)

    if row:
        desc = input("Enter new name: ")
        row.desc = desc
        row.save()

def update_record_v2(table):
    value = input("Enter id: ")
    row = table.get(table.id == value)

    row.date = input("Enter new Date (Format YYYY-MM-DD HH:MM:SS): ")
    row.geocode = input("Enter new Geocode (Integer): ")
    row.category = input("Enter new Category ID (Integer): ")
    row.vector = input("Enter new Vector Value (Format: vXXXXXXX): ")
    row.price = input("Enter new Price (Fraction): ")

    row.save()

def delete_a_record_with_id(table):
    """"Does 'Delete' from table"""
    value = input("Enter id: ")
    row = table.get(table.id==value)
    if row:
        row.delete_instance()

if __name__ == '__main__':
    # read_from_categories_table()
    # add_new_record_in_categories_table()
    # update_a_record_in_categories_table(("new category zero", 218))
    # delete_a_record_in_categories_table()
    pass
