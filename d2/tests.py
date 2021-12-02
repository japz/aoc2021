from ..utils import readlines


def test_part1():
    from .part1 import Submarine
    lines = readlines("example.txt")

    sub = Submarine()

    for command in lines:
        sub.command(command)

    assert sub.product == 150


def test_part2():
    from .part2 import Submarine
    lines = readlines("example.txt")

    sub = Submarine()

    for command in lines:
        sub.command(command)

    assert sub.product == 900
