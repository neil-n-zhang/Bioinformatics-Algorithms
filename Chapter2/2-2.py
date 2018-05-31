#print every index from (0,0, ..., 0) to (n1,n2, ..., nd# ) iterate
import numpy as np
def nextindex(start,end):
    l=len(start)
    for i in list(reversed(range(l))):
        if start[i]<end[i]:
            start[i]=start[i]+1
            return start
        else:
            start[i] = 0
    return start

def allindex(end):
    l=len(end)
    start=np.zeros(l)
    while 1==1:
        print(start)
        start=nextindex(start,end)
        if all(start==np.zeros(l)):
            return

allindex([3,2,3])


#print every index from (0,0, ..., 0) to (n1,n2, ..., nd# ) recursive