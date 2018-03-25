import os
from datetime import datetime
from .context import model

def test_yearly_average():
    print(model.Stats.get_yearly_average(2015, 12))
    assert type(model.Stats.get_yearly_average(2015, 12)) is type(float), 'Invalid average value!'