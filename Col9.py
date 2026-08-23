# solve system of linear equations using matrix method : x+y+z=6, 2y+5+z= -4, 2x+5y-z = 27

import numpy as np

l = np.array([[1,1,1],[0,2,1],[2,5,-1]])
k = np.array([6, -9, 27])
x = np.linalg.solve(l,k)
print("x= :",x[0])
print("y= :",x[1])
print("z= ",x[2])