# compute the determinant and inverse of matrix a


import numpy as np

a = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

print("Determinant:", np.linalg.det(a))
print("Inverse:")
print(np.linalg.inv(a))