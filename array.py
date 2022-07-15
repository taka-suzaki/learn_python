import numpy as np


arr = np.array([1, 2, 3,4, 5])


if __name__ == "__main__":
    print(arr.reshape([-1, 1]))
    print(arr.reshape([1, -1]))


