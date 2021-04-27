import numpy as np
from polyFit import *
import  matplotlib.pyplot as plt
xData = np.array([-2.2, -0.3, 0.8, 1.9])
yData = np.array([15.18, 10.962, 1.92, -2.04])


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

def findDifferentiation(x, degree, coeff):
    def factorial_n(i,n):
        fac=i
        for j in range(1,n):
            fac*=(i-j)
        return fac

    differentiation=0
    for i in range(degree, len(coeff)):
        differentiation += coeff[i]*factorial_n(i,degree)*(x**(i-degree))
    return round(differentiation,10)

coeff_s=[]
while True:
    try:
        m = eval(input("\nDegree of polynomial ==> "))
        x = eval(input("Value of X ==> "))
        coeff = polyFit(xData,yData,m)
        coeff_s.append(coeff)

        print("\nPolynomial = "+' + '.join([(lambda i: "{}x^{}".format(round(coeff[i],10),i))(i) for i in range(len(coeff))]))
        print("Coefficients are: ",coeff)
        print("Std. deviation = ",stdDev(coeff,xData,yData))
        print("f\' = ",findDifferentiation(x,1,coeff))
        print("f\'\' = ",findDifferentiation(x,2,coeff))

        #plotPolys(xData,yData,coeff_s)
        #plotPoly(xData,yData,coeff)
    except SyntaxError: break
