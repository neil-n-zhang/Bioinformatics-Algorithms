import numpy as np
f=open('D:\ComparingGenesProteinsandGenomes\Manhattan_tourist.txt','r')
data=f.readlines()
f.seek(0)
dim=f.readline().split()
dim=list(map(int,dim))
col=[]
for i in range(dim[0]):
    col.append(list(map(int,f.readline().split())))
f.readline()
row=[]
for i in range(dim[0]+1):
    row.append(list(map(int,f.readline().split())))
s=np.zeros((dim[0]+1,dim[1]+1))
for i in range(1,dim[0]+1):
    s[i,0]=s[i-1,0]+col[i-1][0]
for j in range(1,dim[1]+1):
    s[0,j]=s[0,j-1]+row[0][j-1]

for i in range(1,dim[0]+1):
    for j in range(1,dim[1]+1):
        s[i,j]=max(s[i-1,j]+col[i-1][j],s[i,j-1]+row[i][j-1])

print(s[-1,-1])