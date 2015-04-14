# week 2 ex 2 Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt

import wk2ex1_Lee as func

data = np.loadtxt('velocities.txt')
time = data[:,0]
velocity = data[:,1]
n = 100

trapInt = func.trapRule(time, velocity, n)

simpInt = func.simpRule(time, velocity, n)

print trapInt
print simpInt

intValues = np.array([trapInt, simpInt])
np.savetxt('wk2ex2_Lee.txt', intValues)

plt.plot(time, velocity)
plt.title("Velocity Curve")
plt.xlabel("Time")
plt.ylabel("Velocity")

plt.show()
