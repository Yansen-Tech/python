import numpy as np
import math as ma 
import sklearn
import pandas
import scipy
from numpy import random
from numpy.core.fromnumeric import mean
from numpy.random.mtrand import rand
import matplotlib.pyplot as plt
arrays=np.array([[1,8],[12,4],[5,6]])
print(arrays)
print(np.sum(arrays))
print()
print(np.sum(arrays,axis=1))
print()
print(np.sum(arrays,axis=0))
print()
print(arrays.T)

print(np.mean(arrays))
print()
print(np.median(arrays))
print()
print(np.std(arrays))
print()
print(np.min(arrays))
print(np.max(arrays))
print(arrays.shape)

modifikasi=np.array([12,41,512,14,141,61])
print(modifikasi.reshape(2,3))
print(modifikasi.ndim)
modifikasi[2:6]=100
print(modifikasi[2:7])
print(modifikasi)

numu=random.rand (8,5)
for j in range(8):
    numu[j]=j

print(numu)
print()

print(numu[2,1])
print()

nan=np.arange(20)
print(nan.reshape(4,5))

sinrad=ma.sin(0.5)
print("Sinus dalam radian ",sinrad)
print('sinrad',sinrad,'dibulatkan',round)

t=np.linspace(0,3,7)
print(t)
y=np.array([0,2,3.5,7,8,10,12])
print(y)
plt.plot(t,y)
plt.show()