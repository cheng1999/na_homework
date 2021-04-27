import numpy as np
from polyFit import *
import  matplotlib.pyplot as plt
xData = np.array([-2.2,-0.3,0.8,1.9])
yData = np.array([15.180,10.962,1.920,-2.04])


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
