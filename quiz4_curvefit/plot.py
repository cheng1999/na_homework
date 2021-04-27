import numpy as np
from polyFit import *
import  matplotlib.pyplot as plt
xData = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
yData = np.array([6.008, 15.722, 27.130, 33.722, 5.257, 9.549, 11.098, 28.828])


def plotPoly(xData,yData,coeff):
    m = len(coeff)
    x1 = min(xData)
    x2 = max(xData)
    dx = (x2 - x1)/20.0
    x = np.arange(x1,x2 + dx/10.0,dx)
    y = np.zeros((len(x)))*1.0
    for i in range(m):
        y = y + coeff[i]*x**i
    return(x,y)

def plotPolys(xData,yData,coeff_s,xlab='x',ylab='y'):
    for coeff in coeff_s:
        x,y = plotPoly(xData,yData,coeff)
        plt.plot(xData,yData,'o',x,y,'-')
    plt.xlabel(xlab); plt.ylabel(ylab)
    plt.grid (True)
    plt.show()

coeff_s=[]
while True:
    try:
        m = eval(input("\nDegree of polynomial ==> "))
        coeff = polyFit(xData,yData,m)
        coeff_s.append(coeff)
        print("Coefficients are:\n",coeff)
        print("Std. deviation =",stdDev(coeff,xData,yData))
        plotPolys(xData,yData,coeff_s)
        #plotPoly(xData,yData,coeff)
    except SyntaxError: break
