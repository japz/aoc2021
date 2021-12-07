import itertools


class School(object):
    def __init__(self, initial):
        self.day = 0
        self.buckets = [0] * 9
        for i in initial:
            self.buckets[i] += 1

    def new_day(self):
        this_many_reproduce = self.buckets.pop(0)
        self.buckets[6] += this_many_reproduce
        self.buckets.append(this_many_reproduce)


    @property
    def total(self):
        return sum(self.buckets)

    def __repr__(self):
        return f"<School of {self.total} at day {self.day}>"


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    input = data.strip().split(",")

    school = School([int(x) for x in input])

    for i in range(256):
        school.new_day()
    print(school.total)
