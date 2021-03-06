#AUDIO SLOW
import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt

fs,d8k=wav.read('myvoice.wav')  
wav.write('myvoiceslow.wav',0.5*fs,d8k)
fs1,d8k1=wav.read('myvoiceslow.wav')  

print("sampling rate=",fs1)
print("length of data=",len(d8k1))
print("data read from the file=",d8k1)   
                                  
t=np.arange (0,(len(d8k1))/fs1,1.0/(fs1))
print ((len(d8k1))/fs1)

plt.xlabel('------>time(ms)')
plt.ylabel('----->data read fom the file')
plt.title('Expansion of Audio file')
plt.plot(t,d8k1)
plt.show()
