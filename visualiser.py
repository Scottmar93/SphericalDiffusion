import numpy as np
import matplotlib.pyplot as plt
def visualiser(c,r_out,t_out):
	n=2
	plt.figure(0)
	for i in range (0,n):
		plt.plot(r_out,c[i,:],linewidth=2.0,label='t=%s s' \
		% t_out[i])
	plt.xlabel("r/R")
	plt.ylabel("c/c_max")
	plt.legend()
	plt.show()
	return 

	#import numpy
	#c=numpy.array([[1,2,3,4],[1,3,3,1]])
	#visualiser.visualiser(c,[1,2,3,4],[1,2])