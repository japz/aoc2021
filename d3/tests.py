from ..utils import readlines
from d3 import part1
from d3 import sensor

def test_part1():
    s = part1.SensorData(readlines("example.txt"))
    assert s.gamma_int == 22
    assert s.epsilon_int == 9

def test_most_dominant():
    s = sensor.SensorData(readlines("example.txt"))
    x = sensor.filter_rows(s.data,)