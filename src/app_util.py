"""app_util.py: Implements mathematical operation on provided dataset."""

__author__      = "Sohaila Ridwan"
__date__   = "April 15, 2018"

import click
from dataset import Categories
from model import Stats
from peewee import *

# SQLite Database access variable
db = SqliteDatabase("app.db")

@click.group()
def app():
    pass

@app.command()
@click.option("--year", "-Y", default=2010)
@click.option("--category", '-C', default=1, type=click.IntRange(min=1, max=217))
def y_avg(year, category):
    """"Shows average price for user chosen category"""
    print("\nAuthor: Sohaila Ridwan")
    print("On {} the average for '{}' was {:.2f}".format(year, Categories.get(Categories.id==category).desc, Stats.get_yearly_average(year, category)))


def show_sorted_list_of_categories():
    """Fetches category data from DB, generates List; then sorts the List, and displays it."""
    print("\nAuthor: Sohaila Ridwan\n")
    cur = db.cursor()
    query = "SELECT DESC FROM CATEGORIES"
    cur.execute(query)
    result = cur.fetchall()

    list_categories = [list(i) for i in result]
    list_categories.sort()

    for p in list_categories:
        print(p)


if __name__ == '__main__':
    # app()
    show_sorted_list_of_categories()