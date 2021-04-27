import math
def taylor_expand(coe=4, x=1, error=10e-4):
  n=0
  y=0.0
  while abs(1-coe*y/math.pi)>error:
    y+=((-1)**n)*(x**(2*n+1))/(2*n+1)
    n+=1
  return({'result':coe*y, 'round':n})

print('pi: ',math.pi)
print('with atan 1      : ', taylor_expand(coe=4,x=1))
print('with atan 1/sqrt3: ', taylor_expand(coe=6,x=1/3**.5))
print('\nTaylor expansion used is expand from point 0.\n\
  Which means closer the x to 0, faster the convergence.\n\
  Thus, 1/sqrt3 converges faster than 1')

"""
:::CODE RUN:::
~/code/na$ python na_quiz1.py 

3.141592653589793
with atan 1      :  {'result': 3.1447274421267646, 'round': 319}
with atan 1/sqrt3:  {'result': 3.1426047456630846, 'round': 5}

Taylor expansion used is expand from point 0.
  which means closer the x to 0, faster the convergence.
  Thus, 1/sqrt3 converges faster than 1
"""
