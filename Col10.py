# write a function to check wheather a given matrix is symmetric or skew symmetric

import numpy as np

def check(a):
    if np.all(a == a.T):
        print("Symmetric")
    elif np.all(a == -a.T):
        print("Skew Symmetric")
    else:
        print("Neither")

a = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])

check(a)