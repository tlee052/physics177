# week 3 ex 1 Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt

pi = 3.1159
epsilon = 8.854187817
q1 = 1.
q2 = -1.
separation = 10.
size = 100. 
npixel = 500.
dx = size / npixel

x1c = size / 2. - separation / 2. 
y1c = size / 2. 
x2c = size / 2. + separation / 2. 
y2c = size / 2. 

sum = np.zeros(shape=(npixel,npixel)).astype('float')

for m in range(npixel):
	y = dx * float(m)
		for n in range(npixel):
			x = dx * float(n)
			r1 = np.sqrt( (x - x1c)**2 + (y - y1c)**2)
			r2 = np.sqrt( (x - x2c)**2 + (y - y2c)**2)
			phi1 = q1 /(4.*pi*epsilon*r1)
			phi2 = q2 /(4.*pi*epsilon*r2)
			sum[m,n] = phi1 + phi2

ax1 = plt.subplot(211)			
plt.imshow(sum, origin= 'lower', extent= ([0, size, 0, size]))
ax1.set_xlabel ('x-dir. (cm)')
ax1.set_ylabel ('y-dir. (cm)')


parDeriv = np.gradient(sum)
parDerivx = parDeriv[1]
parDerivy = parDeriv[0]
magnitude = parDerivx + parDerivy

ax2 = plt.subplot(212)
plt.imshow(magnitude, origin= 'lower', extent= ([0, size, 0, size]))
ax2.set_xlabel ('x-dir. (cm)')
ax2.set_ylabel ('y-dir. (cm)')


