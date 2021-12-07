import numpy as np


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    input = data.strip().split(",")
    array = np.array([int(x) for x in input])

    max_value = np.max(array)
    out = [0] * max_value

    func = np.vectorize(lambda x: (x * (x + 1)) / 2)
    for i in range(max_value):
        x = np.array([i] * array.size)
        print(x)
        out[i] = sum(func(np.abs(np.subtract(array, x))))

    print(np.min(out))

