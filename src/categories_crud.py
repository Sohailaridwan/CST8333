"""categories_crud.py: Does CRUD opeation on table 'CATEGORIES'."""

__author__      = "Sohaila Ridwan"
__date__   = "March 25, 2018"


from peewee import *

# SQLite Database access variable
db = SqliteDatabase("app.db")


def read_from_categories_table():
    """"Does 'Read' from categories table"""
    cur = db.cursor()
    cur.execute("SELECT * FROM CATEGORIES")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def add_new_record_in_categories_table():
    """"Does 'Insert' into categories table"""
    cur = db.cursor()
    sql = "INSERT INTO CATEGORIES (desc) VALUES(?)"
    cur.execute(sql, ("new category one",))
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
    # add_new_record_in_categories_table()
    # update_a_record_in_categories_table(("new category zero", 218))
    read_from_categories_table()
    # delete_a_record_in_categories_table()
