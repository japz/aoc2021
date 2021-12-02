class Submarine(object):
    aim: int
    pos_x: int
    pos_z: int

    def __init__(self):
        self.aim = 0
        self.pos_x = 0
        self.pos_z = 0

    def forward(self, n: int):
        self.pos_x += n
        self.pos_z += n * self.aim

    def down(self, n: int):
        self.aim += n

    def up(self, n: int):
        self.aim -= n

    def command(self, command: str):
        match command.split():
            case [action, n]:
                getattr(self, action)(int(n))

    @property
    def product(self):
        return self.pos_x * self.pos_z


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    sub = Submarine()

    for command in lines:
        sub.command(command)

    print(sub.product)