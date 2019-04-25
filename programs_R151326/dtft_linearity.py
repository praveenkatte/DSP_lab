#DTFT-PROPERTY LINEARITY

def npt_dtft(x,b):
    x=[]
    j=np.complex(0,1)
        for i in range (0,b):
            o+=x[i]*np.exp((-j*2*np.pi*i*k))
            print o
            x.append(o)
        return x
b=input ('enter no.of type of dft')
x1=np.zeros(b)
x2=np.zeros(b)
for i in range (0,b):
    x1[i]=input("enter a elemnt")
    x2[i]=input("enter a element for 2;")
x3=[]
for i in range (0,b):
    y=x1[i]+x2[i]
    x3.append(y)

x1=npt_dtft(x1,b)
x2=npt_dtft(x2,b)
x3=npt_dtft(x3,b)

m1=np.abs(x1)

m2=np.abs(x2)
x4=m1+m2
plt.subplots_adjust(left=0.125,right=0.9,bottom=0.1,top=0.9,wspace=0.5,hspace=0.8)

ax1=plt.subplot(2,1,1)
ax2=plt.subplot(2,1,2)
ax1.stem(x3)
ax2.stem(x4)
plt.show

