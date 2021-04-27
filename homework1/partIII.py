import numpy as np

"""
Part I
"""
from gaussSeidel import *
A = np.matrix('\
        -5 3 0 0 0;\
        3 -6 3 0 0;\
        0 3 -6 3 0;\
        0 0 3 -6 3;\
        0 0 0 3 -5\
    ')
b = np.array([-80,0,0,60,0])
x = np.array([0]*5)
print(gaussSeidel(A,x.copy(),b,relaxation=False))
print(gaussSeidel(A,x.copy(),b))
"""
Part III
"""
from polyRoots import *

c_m = 12
k_m = 1500

c = np.array([1,2*c_m,3*k_m,c_m*k_m,k_m**2])
print(polyRoots(c))
