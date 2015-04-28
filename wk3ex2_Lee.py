# week 3 ex 2 Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt

eq1 = np.array([4., -1., -1., -1.])
eq2 = np.array([-1., 3., 0., -1.])
eq3 = np.array([-1., 0., 3., -1.])
eq4 = np.array([-1., -1., -1., 4.])

A = np.array([[eq1],[eq2],[eq3],[eq4]])
V = np.array([5., 0., 5., 0.]) 

N = len(V)

for m in range(N):
	val = A[m,m]
	A[m,:] /= val
	V[m] /= val
	
	for n in range(m+1,N):
		mult = A[n,m]
		A[n,:] -=mult* A[m,:]
		V[n] -= V[m]* mult

x = np.array([0., 0., 0., 0.])
for o in range(N-1,-1,-1):
	x[o] = V[o]
	
	for p in range(o+1,N):
		x[o] -= A[o,p]* x[p]

print('Gaussian elimination solutions= ', x)

lu = np.linalg.solve(A,V)

print('LU method solutions= ', lu)
