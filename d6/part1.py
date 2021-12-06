import itertools


class Fish(object):
    def __init__(self, generation=0, days_remaining=None):
        self.generation = generation
        self.offspring = []
        if generation == 0:
            self.reset(False)
        else:
            self.reset(True)

        if days_remaining:
            self.days_remaining = days_remaining

    def reset(self, newborn):
        self.days_remaining = 6 + (2 if newborn else 0)

    def new_day(self):
        if self.days_remaining == 0:
            self.reset(False)
            fry = Fish(generation=self.generation+1)
            #self.offspring.append(fry)
            return (self, fry)
        self.days_remaining -= 1
        return (self, )

    def __repr__(self):
        return f"<Fish: g#{self.generation} d#{self.days_remaining}>"


class School(object):
    def __init__(self, fish):
        self.fish = fish
        self.day = 0

    def new_day(self):
        self.day += 1
        self.fish = list(itertools.chain(*[fish.new_day() for fish in self.fish]))

    def __len__(self):
        return len(self.fish)

    def __repr__(self):
        return f"<School of {len(self)} at day {self.day}: {self.fish}>"


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    input = data.strip().split(",")

    school = School([Fish(days_remaining=int(x)) for x in input])

    for i in range(80):
        print(i)
        school.new_day()
    print()
    print(len(school))