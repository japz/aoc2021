import numpy as np


def counts(input):
    return [np.bincount(column) for column in input.transpose()]

def most_dominant0(input):
    return np.array([int(a >= b) for a, b in counts(input)])

def most_dominant1(input):
    return np.array([int(b >= a) for a, b in counts(input)])

def filter_rows_oxygen(input, c):
    most_dom = most_dominant1(input, n)
    return [x for x in input if x[c] == most_dom[c]]


class SensorData(object):
    def __init__(self, lines):
        self.data = np.array([np.fromstring(x, "u1") - ord("0") for x in lines])

    @property
    def num_rows(self):
        return np.shape(self.data)[0]

    @property
    def num_columns(self):
        return np.shape(self.data)[1]

    def is_n_dominant(self, n):
        return np.array([int(np.bincount(column)[n] >= len(column) / 2)
             for column in self.data.transpose()])


    @property
    def gamma(self):
        return most_dominant1(self.data)
        return self.is_n_dominant(1)



    @property
    def gammaold(self):
        return np.array([np.argmax(np.bincount(column)) for column in self.data.transpose()])

    @property
    def gammanew(self):
        return np.array([np.argmax(np.bincount(column)) for column in self.data.transpose()])


    @property
    def epsilon(self):
        return most_dominant0(self.data)
        #return 1 - self.gamma

    @property
    def gamma_int(self):
        return self.gamma.dot(1 << np.arange(self.gamma.size)[::-1])

    @property
    def epsilon_int(self):
        return self.epsilon.dot(1 << np.arange(self.epsilon.size)[::-1])
