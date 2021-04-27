import math
from gaussQuad import *

a=2;b=1
#def f(x): return 2*(1+(x**2)/(a**2-x**2)*(b**2/a**2))**(0.5)
def f(t): 
    x = a*math.cos(t)
    y = b*math.sin(t)
    return 2*(x**2+y**2)**.5
I = gaussQuad(f,0,math.pi,17)
I_exact = 9.688448216
print("Integral =", round(I,5))

"""
::: CODE RUN :::

cheng@Cheng:~/code/na/quiz8_gaussintegral$ python3 main.py 
Integral = 9.68845

"""
