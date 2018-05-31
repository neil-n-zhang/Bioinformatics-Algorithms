import numpy as np
import random as random

def readdata(address):
    f=open(address,'r')
    text=f.readlines()
    f.seek(0)
    k,dim=list(map(int,f.readline().split()))
    data=np.zeros([len(text)-1,dim])
    for i in list(range(1,len(text))):
        data[i-1,:]=list(map(float,text[i].split()))
    return data,k,dim

def distance(a,b):
    dist_square=0
    for i in list(range(len(a))):
        dist_square=dist_square+(a[i]-b[i])**2
    return dist_square**0.5

def kmeanscluster(data,k,dim):
    centers=np.zeros([k,dim])
    groups=np.zeros([len(data),1])
    for i in list(range(k)):
        for j in list(range(dim)):
            centers[i,j]=random.uniform(min(data[:,j]),max(data[:,j]))

    former_totaldist=0
    for z in list(range(300)):
        totaldist=0
        for i in list(range(len(data))):
            group_dist = np.zeros([1, k])
            for j in list(range(k)):
                group_dist[0,j]=distance(data[i],centers[j])
            totaldist=totaldist+np.min(group_dist)
            groups[i]=group_dist.argmin()
        for i in list(range(k)):
            centers[i]=np.mean(data[np.where(groups==i)[0],:],axis=0)
        if totaldist-former_totaldist==0:
            break
        else:
            former_totaldist=totaldist
    return centers[centers[:,0].argsort()]

data,k,dim=readdata('D:\Bioinformatics_Algorithms\Chapter10\kmeans.txt')
for i in list(range(2)):
    centers=kmeanscluster(data,k,dim)
    print(centers)