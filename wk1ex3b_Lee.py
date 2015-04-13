# week 1 ex 3.b Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt

height = input ("Enter height of tower in meters: ")
gravity = 9.81

maxVel = input ("Enter maximum velocity: ")
minVel = input ("Enter minimum velocity: ")
bin = input ("Enter number of bins: ")

dv = (maxVel-minVel)/bin

velVector = []
for n in range(10):
	velVector.append(minVel + n*dv +dv/2)
	
timeVector = []
for m in range(10):
	timeVector.append( (np.sqrt((velVector[m]**2)+(2.*gravity*height))-velVector[m])/gravity )
	

plt.plot (velVector, timeVector, 'o-', color = 'black')
plt.title ("Time vs. Velocity")
plt.xlabel ("Velocity (m/s)")
plt.ylabel ("Time (s)")

np.savetxt('wk1ex3b_Lee.txt',timeVector)
plt.savefig("wk1ex3b_Lee.jpeg", format="jpeg")

