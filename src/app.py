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
    print("On {} the average for '{}' was {:.2f}".format(year, Categories.get(Categories.id==category).desc, Stats.get_yearly_average(year, category)))


if __name__ == '__main__':
    app()