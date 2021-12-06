from ..utils import readlines
from d6 import part1, part2


def test_part1():
    input = readlines("example.txt")[0].strip().split(",")
    school = part1.School([part1.Fish(days_remaining=int(x)) for x in input])

    for i in range(80):
        school.new_day()

    assert len(school) == 5934


def test_part2():
    input = readlines("example.txt")[0].strip().split(",")
    school = part2.School([int(x) for x in input])

    for i in range(80):
        school.new_day()

    assert school.total == 5934