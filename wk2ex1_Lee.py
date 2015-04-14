# week 2 ex 1a Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt

def trapRule(x, y, n):
	a = x[0]
	b = x[-1]
	h = (b-a)/n
	
	ta = y[0]
	tb = y[-1]
	tSum = 0.
	tInt = 0.
	
	for k in range(1,n,1):
		tSum += y[a+k*h]
		
	tInt = 0.5*h *ta *tSum *tb
	
	return tInt
	
def simpRule(x, y, n):
	a = x[0]
	b = x[-1]
	h = (b-a)/n
	
	sa = y[0]
	sb = y[-1]
	sSum2 = 0.
	sSum4 = 0.
	sInt = 0.
	
	for k in range(1,n,2):
		sSum2 += y[a+k*h]
	sSum2 *= 2

	for k in range(2,n,2):
		sSum4 += y[a+k*h]
	sSum4 *= 4
	
	sInt = 1/3 * h* sa* sSum2* sSum4* sb
	
	return sInt	