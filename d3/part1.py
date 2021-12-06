from d3.sensor import SensorData
from utils import readlines
import numpy as np

if __name__ == "__main__":
    lines = readlines("example.txt")
    sensor = SensorData(lines)
    print(sensor.gamma)
    print(sensor.gamma_int * sensor.epsilon_int)

    #print([np.bincount(column) for column in sensor.data.transpose()])