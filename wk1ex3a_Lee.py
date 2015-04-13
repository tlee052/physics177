# week 1 ex 3.a Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt

height = input ("Enter height of tower in meters: ")
initialVel = input ("Enter initial Velocity: ")
gravity = 9.81
time = (np.sqrt((initialVel**2)+(2.*gravity*height))-initialVel)/gravity
time = round(time, 3)

print time
