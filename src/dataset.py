import csv
import os
from peewee import *
from datetime import datetime

# SQLite Database access variable
db = SqliteDatabase("app.db")

def load_dataset():
    """Loads the dataset from CSV file and converts to python list.

    :return: list object.
    """
    with open(os.path.abspath("./data.csv"), "r") as datafile:
        reader = csv.reader(datafile)
        return list(reader)

def create_tables():
    """Creates the database based on the orm models.
    """
    db.create_tables([Categories, GeoCodes, PriceIndex], safe=True)

def populate_geocodes():
    """Populates the SQLiteDB GeoCodes table with the data from the CSV file.

    Must be called after tables has been created.
    """
    codes = [(1, 'Canada'),
             (2, 'Newfoundland and Labrador'),
             (3, 'Prince Edward Island'),
             (4, 'Nova Scotia'),
             (5, 'New Brunswick'),
             (6, 'Quebec'),
             (7, 'Ontario'),
             (8, 'Manitoba'),
             (9, 'Saskatchewan'),
             (10, 'Alberta'),
             (11, 'British Columbia')]
    for code in codes:
        GeoCodes.get_or_create(desc=code[1])

def populate_categories():
    """Populates the SQLiteDB Categories table with the data from the CSV file.

    Must be called after tables has been created.
    """
    dataset = load_dataset()
    categories = []
    for i in dataset:
        categories.append((i[2], i[-2].split('.')[-1]))
    categories = set(categories)
    for cat in categories:
        Categories.get_or_create(desc=cat[0])

def populate_price_indexes():
    """Populates the SQLite Database with the data from CSV file.

    Must be called after calling `populate_geocodes` and `populate_categories`.
    """
    dataset = load_dataset()

    geocodes = {}
    for gcode in GeoCodes.select():
        geocodes[gcode.desc] = gcode
    print(geocodes)
    cats = {}
    for cat in Categories.select():
        cats[cat.desc] = cat
    print(cats)
    for row in dataset:
        date = datetime.strptime(row[0], "%Y/%m")
        # geocode = GeoCodes.get(GeoCodes.desc==row[1])
        # category = Categories.get(Categories.desc==row[2])
        vector = row[3]
        price = row[-1]

        try:
            PriceIndex.get_or_create(date=date,
                              geocode=geocodes[row[1]],
                              category=cats[row[2]],
                              vector=vector,
                              price=float(price))
        except Exception as e:
            print("Error: {}".format(e))

def show_tables():
    """Shows a list containing all the tables in the database."""
    print(db.get_tables())

def display_geocodes():
    """Displays all the rows from the GeoCodes table."""
    for geocode in GeoCodes.select():
        print("{:2}| {}".format(geocode.id, geocode.desc))

def display_categories():
    """Displays all the rows from the Categories table."""
    for cat in Categories.select():
        print("{:3}| {}".format(cat.id, cat.desc))

def display_price_indexes():
    """Displays all the rows from the PriceIndex table."""
    for index in PriceIndex.select():
        print("{}|{}|{}|{}|{}".format(index.date,
                                      index.geocode.id,
                                      index.category.id,
                                      index.vector,
                                      index.price))

class BaseModel(Model):
    """Base ORM."""
    class Meta:
        database = db

class Categories(BaseModel):
    desc = CharField()

class GeoCodes(BaseModel):
    desc = CharField()

class PriceIndex(BaseModel):
    """ORM for PriceIndex."""
    date = DateField()
    geocode = ForeignKeyField(GeoCodes, to_field='id', related_name='indexes')
    category = ForeignKeyField(Categories, to_field='id', related_name="indexes")
    vector = CharField()
    price = DoubleField()


    class Meta:
        coordinate = CompositeKey(GeoCodes, Categories)

if __name__ == '__main__':
    """Creates the database and populates it from the provided data file."""
    # show_tables()
    # create_tables()
    # populate_geocodes()
    # display_geocodes()
    # populate_categories()
    # display_categories()
    # populate_price_indexes()
    display_price_indexes()
    show_tables()