import numpy as np
A = np.array([\
    (3.50,  2.77,  -0.76, 1.80),\
    (-1.80, 2.68,  3.44, -0.09),\
    (0.27,  5.07,  6.90,  1.61),\
    (1.71,  5.45,  2.68,  1.71)\
    ])

A_copy=A.copy()
b = np.array([(7.31, 4.23, 13.85, 11.55)]).T
b_copy=b.copy()
n = len(b)

for y in range(n-1):
    for x in range(y+1):
        if A[y-x+1][-x-1]!=0:
          coe=A[y-x][-x-1]/A[y-x+1][-x-1]
          A[y-x]=A[y-x]-coe*A[y-x+1]
          b[y-x]=b[y-x]-coe*b[y-x+1]
        if A[-y+x-2][x]!=0:
          coe=A[-y+x-1][x]/A[-y+x-2][x]
          A[-y+x-1]=A[-y+x-1]-coe*A[-y+x-2]
          b[-y+x-1]=b[-y+x-1]-coe*b[-y+x-2]

x=b.T/A.diagonal().T
Ax=np.dot(A_copy,x.T)

print('x:\n',x.T)
print('\nAx=\n',Ax)
print('\nError:\n',Ax-b_copy)

"""
Calculate determinant
"""
def recur(coe,matrix):
    det=0
    if len(matrix)==2:
        x= matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return(coe*x)
    for i in range(len(matrix)):
        matrix_tocur=[]
        for j in range(len(matrix)):
            if j==i:continue
            matrix_tocur.append(matrix.T[j][1:])
        coe_tocur=1
        if i%2==1:coe_tocur=-1
        coe_tocur*=coe
        matrix_tocur=np.array(matrix_tocur).T
        det+=recur(coe_tocur*matrix[0][i],matrix_tocur)
    return(det)

print("\nDeterminant of A:\n",recur(1,A_copy))
#print(np.linalg.det(A_copy))

"""
::: CODE RUN :::

cheng@Cheng:~/code/na$ python3 q2.py 
x:
 [[1.]
 [1.]
 [1.]
 [1.]]

Ax=
 [[ 7.31]
 [ 4.23]
 [13.85]
 [11.55]]

Error:
 [[-4.97379915e-14]
 [ 2.66453526e-15]
 [-3.90798505e-14]
 [-3.01980663e-14]]

Determinant of A:
 -0.22579734000001395

"""
