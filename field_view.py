import numpy as np


def tan_angle(theta):
    return np.tan(np.radians(theta))

def vertical_angle(hor, dia):
    tan = np.sqrt(tan_angle(dia)**2 - tan_angle(hor)**2)
    return np.degrees(np.arctan(tan))


if __name__ == '__main__':
    print(vertical_angle(57, 71))