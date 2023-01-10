import numpy as np


def solve():
    A = np.array([[20, 10], [17, 22]])
    B = np.array([350, 500])
    X = np.linalg.solve(A, B)
    return X
