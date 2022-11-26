from math import pi


def vol(rad):
    volume = 4 / 3 * pi * rad ** 3
    return volume


result = vol(2)
print(result)
