# week 1 ex 2 Te-En Lee 861027623
import numpy as np
import math
import matplotlib.pyplot as plt


homeWorkGrade = np.array([10., 10., 8., 9.5, 3., 9., 0., 6.])
midTermGrade = np.array([10., 10., 10., 10., 8., 5., 10., 7.])
finalProjectGrade = np.array([9., 10., 10., 6., 10., 6., 8., 9.])
numbFailedStudents = 0
numbOutstandingStudents = 0	

finalGrade = (homeWorkGrade*0.4) + (midTermGrade*0.2) + (finalProjectGrade*0.4)

for n in range(0,8,1):
	
	if finalGrade [n] <6 :
		numbFailedStudents = numbFailedStudents + 1
	
	elif finalGrade [n]>9.5 :
		numbOutstandingStudents = numbOutstandingStudents + 1

print "Final Grades: "
for n in range (0,8,1):
	print (finalGrade[n])
	
print "Number of failed students: ",numbFailedStudents
print "Number of outstanding students: ", numbOutstandingStudents

plt.hist (finalGrade)
plt.title ("Student Final Grade Histogram")
plt.xlabel ("Points")
plt.ylabel ("Number of Students")

np.savetxt('wk1ex2_Lee.txt',finalGrade)
plt.savefig ('wk1ex2_Lee.jpeg', format = "jpeg")