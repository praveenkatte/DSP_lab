####AUTO CORRELATION
import numpy as np
from matplotlib import pyplot as plt
def convolute(x,h):
       	n1=len(x)
      	n2=len(x)
       	y=[ ]
	for n in range(n1+n2-1):
		sum=0
		for k in range(n1):
 			if n-k>=0  and  n-k<=n2-1:
				sum=sum+x[k]*x[n-k]
		y=np.append(y,sum)
	return y
x=np.array(input('enter sequence='))
h1=np.zeros(len(x))
t=0
for p in range (len(x)-1,-1,-1):
	h1[t]=x[p]
	t=t+1
l=convolute(x,h1)
print("Auto correlation=",l)
n1=np.arange(0,len(x),1)
n2=np.arange(0,len(l),1)

plt.subplot(3,1,1)
plt.xlabel('------->n')
plt.ylabel('------->amplitude')
plt.title('sequence1')
plt.stem(n1,x)
plt.subplot(3,1,2)
plt.xlabel('------->n')
plt.ylabel('------->amplitude')
plt.title('sequence2')
plt.stem(n1,x)
plt.subplot(3,1,3)
plt.xlabel('------->n')
plt.ylabel('------->amplitude')
plt.title('Auto correlation of two sequences')
plt.stem(n2,l)
plt.show()

