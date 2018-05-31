#pairwise distances between points in X
import numpy as np
x=[0, 3, 4, 5, 6, 9, 15]

deltax=[]
for j in list(range(1,len(x))):
    for i in list(range(0,j)):
        deltax.append(abs(x[j]-x[i]))
deltax.sort()
print(deltax)