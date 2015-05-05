# week 5 ex 1 Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize as opt

def p(x):
	return 924* x**6 - 2772* x**5 + 3150* x**4 - 1680* x**3 + 420* x**2 - 42* x + 1

x = np.linspace(0, 1, 1000)

plt.plot (x, p(x),'r')
plt.show()
plt.savefig('wk5ex1.png', format = 'png')

# 0~.05 0.1~0.2 0.3~0.4 0.6~0.7 0.8~0.9 0.95~1

estimate = np.array([0.05, 0.2, 0.4, 0.7, 0.8, 0.95])
N = len(estimate)
solution = np.zeros(6)
for n in range(N)
	x0 = estimate[n]
	solution[n] = opt.newton(p, x0, tol=1.e-04, maxiter=50)
	
print('solutions = ', solution[0], solution[1], solution[2], solution[3], solution[4], solution[5], solution[6])
