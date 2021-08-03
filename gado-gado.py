import numpy as np
from numpy import random
matrix=np.arange(15)
q=matrix
print("Q",q)
x,y=np.meshgrid(matrix,matrix)

print("Nilai matrix y : {} ".format(y))

print("Nilai matrix x  : {}".format(x))

na=np.random.rand(5,5)
print(na)
print(np.where(na>0,1,-1))
