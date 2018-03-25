"""app.py: Implements mathematical operation on provided dataset."""

__author__      = "Sohaila Ridwan"
__date__   = "March 25, 2018"

import click
from dataset import Categories
from model import Stats

@click.group()
def app():
    pass

@app.command()
@click.option("--year", "-Y", default=2010)
@click.option("--category", '-C', default=1, type=click.IntRange(min=1, max=217))
def y_avg(year, category):
    print("\nAuthor: Sohaila Ridwan")
    print("On {} the average for '{}' was {:.2f}".format(year, Categories.get(Categories.id==category).desc, Stats.get_yearly_average(year, category)))


if __name__ == '__main__':
    app()