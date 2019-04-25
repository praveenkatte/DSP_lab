import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt

fs,d8k=wav.read('myvoice.wav')  
print("sampling rate=",fs)
print("length of data=",len(d8k))
print("data read from the file=",d8k)   
                                  
t=np.arange (0,len(d8k)/fs,1.0/fs)

plt.xlabel('------>time(ms)')
plt.ylabel('----->data read from the file')
plt.title('Audio file')
plt.plot(t,d8k)
plt.show()


