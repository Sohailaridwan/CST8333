"""categories_crud.py: Does CRUD opeation on table 'CATEGORIES'."""
__author__      = "Sohaila Ridwan"
__date__   = "March 25, 2018"

from peewee import *

"""SQLite Database access variable"""
db = SqliteDatabase("app.db")

def read_from_table(table):
    """"Does 'Read' from a table"""
    cur = db.cursor()
    cur.execute("SELECT * FROM " + table)
    rows = cur.fetchall()
    print("\nReading records from table '" + table + "'")
    for row in rows: print(row)

def add_new_record(table):
    if table in ['categories', 'geocodes']:
        return add_new_record_v1(table)
    elif table in ['priceindex']:
        return add_new_record_v2(table)
    else:
        print("Invalid table name.")

def add_new_record_v1(table):
    """"Does 'Insert' record in a table"""
    cur = db.cursor()
    sql = "INSERT INTO " + table + "(desc) VALUES(?)"
    value = input("Enter value: ")
    cur.execute(sql, (value,))
    return cur.lastrowid

def add_new_record_v2(table):
    """"Does 'Insert' record in priceindex table"""
    cur = db.cursor()
    in_date = input("Enter Date (Format YYYY-MM-DD HH:MM:SS): ")
    in_geocode = input("Enter Geocode (Integer): ")
    in_cat_id = input("Enter Category ID (Integer): ")
    in_vector = input("Enter Vector Value (Format: vXXXXXXX): ")
    in_price = input("Enter Price (Fraction): ")
    sql = "INSERT INTO priceindex (desc) VALUES(?)"
    value = input("Enter value: ")
    cur.execute(sql, (value,))
    return cur.lastrowid

def update_a_record_in_categories_table(desc):
    """"Does 'Update' into categories table"""
    cur = db.cursor()
    sql = "UPDATE CATEGORIES SET DESC = ? , WHERE ID = ?"
    cur.execute(sql, desc)
    return cur.lastrowid

def delete_a_record_in_categories_table():
    """"Does 'Delete' from categories table"""
    cur = db.cursor()
    del_row = cur.lastrowid
    sql = "DELETE FROM CATEGORIES WHERE ID = ?"
    cur.execute(sql, (del_row,))

if __name__ == '__main__':
    # read_from_categories_table()
    add_new_record_in_categories_table()
    # update_a_record_in_categories_table(("new category zero", 218))
    # delete_a_record_in_categories_table()
