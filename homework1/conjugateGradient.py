import numpy as np

n=20
#b=np.asmatrix(np.append(np.ones((n-1))*0,100)).T
b=np.zeros(shape=(n,1))
b[-1]=100

x=np.random.rand(n,1)
w=1
k=10 # after k iterations with w=1, start using relaxation
p=1
tol=1e-9

def getAx(this_x):
    this_b=np.zeros(shape=(n,1))
    #this_b = np.ones((n))
    for i in range(n):
        if i==0:
            this_b[0]=this_x[0]*4+this_x[1]*-1+this_x[-1]*1
        elif i==n-1:
            this_b[-1]=this_x[0]*1+this_x[-2]*-1+this_x[-1]*4
        else:
            this_b[i]=this_x[i-1]*-1+this_x[i]*4+this_x[i+1]*-1
    return this_b
    #return np.asmatrix(this_b)

def conjugateGradient(A,x,b,tol=1e-9):
    r = b - getAx(x)
    s = r.copy()
    for c in range(1000):
        alpha = np.dot(s.T,r)
        alpha/=np.dot(s.T,getAx(s))
        x = x + alpha*s
        r = b - getAx(x)

        if np.linalg.norm(r)<tol:
            print("Number of iterations:\t", c)
            break

        beta = -np.dot(r.T, getAx(s))/np.dot(s.T,getAx(s))
        s = r + beta*s

print("x:\n", x)

"""
::: CODE RUN :::


cheng@Cheng:~/code/na$ python3 q3_2.py 
Number of iterations:	 9
x:
 [[-7.73502692e+00]
 [-2.07259421e+00]
 [-5.55349941e-01]
 [-1.48805549e-01]
 [-3.98722562e-02]
 [-1.06834753e-02]
 [-2.86164518e-03]
 [-7.63105381e-04]
 [-1.90776345e-04]
 [ 4.06575815e-20]
 [ 1.90776345e-04]
 [ 7.63105381e-04]
 [ 2.86164518e-03]
 [ 1.06834753e-02]
 [ 3.98722562e-02]
 [ 1.48805549e-01]
 [ 5.55349941e-01]
 [ 2.07259421e+00]
 [ 7.73502692e+00]
 [ 2.88675135e+01]]

"""

