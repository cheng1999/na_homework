from romberg import *
import math

def f(x):
    return math.sin(x)**-.5

def F(t):
    return 2*(1-t**4)**-.5

I,n = romberg(F,math.sin(0)**.5,math.sin(math.pi/4)**.5)
print("Integral =",I)
print("nPanels =",n)

'''
::: CODE RUN :::
cheng@Cheng:~/code/na/romberg$ python3 main.py 
Integral = 1.7911613389539645
nPanels = 64
'''

