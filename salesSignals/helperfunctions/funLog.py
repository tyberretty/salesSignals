import numpy as np


def funLog(row):
    row = np.log(float(row))
    if np.isinf(row) is True:
        row = 0

    return row
