# n + m → Matrix addition
# n - m → Matrix subtraction
# n * m → Element-wise multiplication

import numpy as np

n = np.array([[1,2,3],[4,5,6],[7,8,9]])
m = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(n+m)
print(n-m)
print(n*m)