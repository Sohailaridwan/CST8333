from .context import model

def test_yearly_average():
    value = model.Stats.get_yearly_average(2010, 26)
    assert type(value) is float, 'Invalid type for average value!'