from ..utils import readlines
from d3 import part1


def test_part1():
    s = part1.SensorData(readlines("example.txt"))
    assert s.gamma_int == 22
    assert s.epsilon_int == 9