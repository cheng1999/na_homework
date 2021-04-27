import numpy as np

n=20
b=np.append(np.ones((n-1))*0,100)

b=np.zeros(shape=(n,1))
b[-1]=100

x=np.random.rand(n,1)
w=1
k=10 # after k iterations with w=1, start using relaxation
p=1
tol=1e-9

def getA(i,j):
    if i>=n or i<0 or j >=n or j <0: return None
    if i==j:
        return 4 
    elif abs(i-j)==1:
        return -1
    elif (i==n-1 and j==0) or (i==0 and j==n-1):
        return 1
    else: return 0
def getb(i):
    if i==n-1: return 100
    else: return 0


A = np.ones((n,n))
for i in range(n):
    for j in range(n):
        A[i][j]=getA(i,j)

for c in range(1000):
    xold=x.copy()
    
    for i in range(n):
        sum_Ax_i=0
        for j in range(n):
            if i==j:continue
            sum_Ax_i+=getA(i,j)*x[j]

        x[i]=w/getA(i,i)*(getb(i)-sum_Ax_i)+(1-w)*x[i]

    dx = np.linalg.norm(xold-x) 

    if dx<tol:
        print("Number of iterations:\t", c)
        break
    if c == k: dx1=dx
    elif c == k+p:
        dx2=dx
        w = 2/(1+np.sqrt(1-dx2/dx1)**(1/p))
print('Relaxation factor:\t', w)
print("x:\n", x)
print("Iterations number to this matrix A is less than Example 2.17.")
#print("Error:\n\t", np.dot(A,x)-b)

"""
::: CODE RUN :::

cheng@Cheng:~/code/na$ python3 q3_1.py 
Number of iterations:	 20
relaxation factor:	 1.0978447860565292
x:
 [[-7.73502692e+00]
 [-2.07259421e+00]
 [-5.55349941e-01]
 [-1.48805549e-01]
 [-3.98722562e-02]
 [-1.06834753e-02]
 [-2.86164518e-03]
 [-7.63105382e-04]
 [-1.90776346e-04]
 [-8.21111567e-13]
 [ 1.90776344e-04]
 [ 7.63105381e-04]
 [ 2.86164518e-03]
 [ 1.06834753e-02]
 [ 3.98722562e-02]
 [ 1.48805549e-01]
 [ 5.55349941e-01]
 [ 2.07259421e+00]
 [ 7.73502692e+00]
 [ 2.88675135e+01]]
Iterations number to this matrix A is less than Example 2.17.
"""

