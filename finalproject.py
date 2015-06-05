# Final Project Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt
import random

amount = 1000
steps = 1000
stepsize = 1
dx = math.sqrt(steps)

route = np.zeros((steps,2))
xroute = route[:,0]
yroute = route[:,1]

for l in range (1,steps):
	m = random.randint(1,4)
	if m == 1:
		xroute[l:] += stepsize
	elif m == 2:
		xroute[l:] -= stepsize
	elif m ==3:
		yroute[l:] += stepsize
	elif m ==4:
		yroute[l:] -= stepsize

data = np.zeros((amount,2))

for i in range (amount):
	for j in range (steps):
		k = random.randint(1,4)
		if k == 1:
			data[i,1] += stepsize
		elif k == 2:
			data[i,1] -= stepsize
		elif k ==3:
			data[i,0] += stepsize
		elif k ==4:
			data[i,0] -= stepsize

fig = plt.figure()
ax0 = fig.add_subplot(221)
ax0.plot(xroute,yroute,'r')	
ax0.spines['left'].set_position('zero')
ax0.spines['bottom'].set_position('zero')
ax0.set_title('Single Random Walk')

ax1 = fig.add_subplot(222)
ax1.plot(xroute,yroute,'r')	
ax1.spines['left'].set_position('zero')
ax1.spines['bottom'].set_position('zero')
plt.xlim(-1*dx,dx)
plt.ylim(-1*dx,dx)
ax1.set_title('Single Random Walk Zoom out')			

ax2 = fig.add_subplot(223)
ax2.scatter(data[:,0],data[:,1])
plt.grid(True)
ax2.set_title('Multiple Random Walk Endpoints')

ax3 = fig.add_subplot(224, polar=True)
ax3.scatter(data[:,0],data[:,1])
ax3.set_title('Multiple Random Walk Endpoints Polar')

plt.show()