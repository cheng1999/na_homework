import numpy as np

def gaussSeidel(A,x,b,relaxation=True,w=1,k=10,p=1,tol=1e-9):
	for c in range(1000):
	    xold=x.copy()
	    
	    for i in range(len(b)):
	        sum_Ax_i=0
	        for j in range(len(b)):
	            if i==j:continue
	            sum_Ax_i+=A.item(i,j)*x[j]
	
	        #x[i]=w/getA(i,i)*(getb(i)-sum_Ax_i)+(1-w)*x[i]
	        x[i]=w/A.item(i,i)*(b[i]-sum_Ax_i)+(1-w)*x[i]
	
	    dx = np.linalg.norm(xold-x) 
	
	    if dx<tol:
	        #print("Number of iterations:\t", c)
	        break
	    if c == k: dx1=dx
	    elif c == k+p:
	        dx2=dx
	        if relaxation: w = 2/(1+np.sqrt(1-dx2/dx1)**(1/p))
	return {'x':x,'relaxationFactor':w,'iterNum':c}
