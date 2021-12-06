from ..utils import readlines
from d6 import part1


def test_part1():
    input = readlines("example.txt")[0].strip().split(",")
    school = part1.School([part1.Fish(days_remaining=int(x)) for x in input])

    for i in range(80):
        school.new_day()

    assert len(school) == 5934


