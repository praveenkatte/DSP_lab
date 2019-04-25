#DISCRETE FOURIER TRANSFORM

import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
def dft(x):
	N=len(x)
	y=[]
	for k in range(0,N,1):
		sum=0
		for n in range(0,N,1):
			sum=sum+x[n]*np.exp((-j*(2*np.pi)*n*k)/N)
		y.append(sum)
	return y
                                 
x=np.array(input('enter a sequence:'))
y=dft(x)
MM=np.angle(y)*60

print y
plt.subplot(2,1,1)
plt.title('MAGNITUDE PLOT')
plt.xlabel('FREQUENCY')
plt.ylabel('MAGNITUDE')
plt.stem(np.abs(y))
plt.subplot(2,1,2)
plt.title('PHASE PLOT')
plt.xlabel('FREQUENCY')
plt.ylabel('PHASE')
plt.stem(MM)
plt.show()

