import math
from gaussQuad import *

def f(x): return 2(1+(x**2)/(4-x**2))**(0.5)

a = -2; b = 11
Iexact = 1.41815
for m in range(2,12):
    I = gaussQuad(f,a,b,m)
    if abs(I - Iexact) < 0.00001:
        print("Number of nodes =",m)
        print("Integral =", gaussQuad(f,a,b,m))
        break
input("\nPress return to exit")
