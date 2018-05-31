def lcsbacktrack(v, w):
    import numpy as np
    s=np.zeros((len(v)+1,len(w)+1))
    backtrack=np.zeros((len(v)+1,len(w)+1))
    #1 stands for deletion, 2 stands for insertion, 3 stands for match
    backtrack[1:len(v)+1,0]=1
    backtrack[0, 1:len(w)+1] = 2

    for i in range(len(v)):
        for j in range(len(w)):
            s[i + 1, j + 1] = max(s[i, j + 1]-1, s[i + 1, j]-1,s[i, j]+scorematrix[''.join([v[i],w[j]])])
            if s[i+1,j+1]==s[i,j+1]-1:
                backtrack[i+1,j+1]=1
            elif s[i+1,j+1]==s[i+1,j]-1:
                backtrack[i+1,j+1] = 2
            else:
                backtrack[i+1,j+1] = 3
    return backtrack

def outputlcs(backtrack1,v,w,i,j,result_v,result_w):
    if i==0 or j==0:
        return
    if backtrack1[i,j]==1:
        outputlcs(backtrack1,v,w,i-1,j,result_v,result_w)
        result_v.append(v[i - 1])
        result_w.append('-')
    elif backtrack1[i,j]==2:
        outputlcs(backtrack1,v,w,i,j-1,result_v,result_w)
        result_v.append('-')
        result_w.append(w[j - 1])
    else:
        outputlcs(backtrack1, v,w, i - 1, j - 1,result_v,result_w)
        result_v.append(v[i-1])
        result_w.append(w[j - 1])

scorematrix={'aa':1,'ab':-1,'ba':-1,'am':-1,'ma':-1,'ao':-2,'oa':-2,'as':-2,'sa':-2,'at':-3,'ta':-3,'bb':1,'bm':-1,'mb':-1,'bo':-1,'ob':-1,'bs':-2,'sb':-2,'bt':-2,'tb':-2,'mm':2,'mo':-1,'om':-1,'ms':-1,'sm':-1,'mt':-2,'tm':-2,'oo':1,'os':-1,'so':-1,'ot':-1,'to':-1,'ss':1,'st':-1,'ts':-1,'tt':2}

v='moat'
w='boast'

backtrack=lcsbacktrack(v, w)
result1=[]
result2=[]
outputlcs(backtrack,v,w,len(v),len(w),result1,result2)
print(''.join(result1))
print(''.join(result2))
