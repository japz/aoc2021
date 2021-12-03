import bitarray
import numpy as np

from utils import readlines


class SensorData(object):
    def __init__(self, lines):
        self.data = np.array([np.fromstring(x, "u1") - ord("0") for x in lines])

    @property
    def num_rows(self):
        return np.shape(self.data)[0]

    @property
    def num_columns(self):
        return np.shape(self.data)[1]

    @property
    def gamma(self):
        return np.array([np.argmax(np.bincount(column)) for column in self.data.transpose()])

    @property
    def epsilon(self):
        return 1 - self.gamma

    @property
    def gamma_int(self):
        return self.gamma.dot(1 << np.arange(self.gamma.size)[::-1])

    @property
    def epsilon_int(self):
        return self.epsilon.dot(1 << np.arange(self.epsilon.size)[::-1])


if __name__ == "__main__":
    lines = readlines("input.txt")
    sensor = SensorData(lines)

    print(sensor.gamma_int * sensor.epsilon_int)

