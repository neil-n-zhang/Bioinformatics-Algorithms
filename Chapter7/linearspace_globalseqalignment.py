import numpy as np

def length(v,w):
    score=np.zeros((len(v)+1,2))
    for j in list(range(1,len(w)+1)):
        score[:, 0] =score[:,1]
        for i in list(range(1,len(v)+1)):
            if v[i-1]==w[j-1]:
                score[i,1]=max(score[i-1,1],score[i,0],score[i-1,0]+1)
            else:
                score[i, 1] = max(score[i - 1, 1], score[i, 0])
    return score

def path(v,w,result_v,result_w):
    if len(v)==0:
        for i in list(range(len(w))):
            result_v.append('-')
            result_w.append(w[i])
        return

    if len(w)==1:
        score=length(v,w)
        i=np.shape(score)[0]-1
        j=1
        result1=[]
        result2 = []
        while i>0:
            if j==0:
                result1.append(v[:i:][::-1])
                for k in list(range(i)):
                    result2.append('-')
                break
            elif score[i,j]==score[i,j-1]:
                j = j - 1
                result1.append('-')
                result2.append(w)
            elif score[i,j]==score[i-1,j]:
                i=i-1
                result1.append(v[i])
                result2.append('-')
            else:
                i = i - 1
                j = j - 1
                result1.append(v[i])
                result2.append(w)
        for letter1 in result1[::-1]:
            result_v.append(letter1)
        for letter2 in result2[::-1]:
            result_w.append(letter2)
        return

    else:
        m=len(w)//2
        score1=length(v,w[0:m])
        score2=length(v[::-1],w[-1:m-1:-1])
        #score=score1[:,1]+score2[:,1]
        score=score1[:,1]+score2[:,1][::-1]
        mid=np.argmax(score)
        path(v[:mid],w[0:m],result_v,result_w)
        path(v[mid:], w[m:], result_v,result_w)

v='le'
w='e'

v='apple'
w='happe'

#problem,should be TTA-T- rather than -TTAT-

v='TTAT'
w='CTG'

a=[]
b=[]
path(v,w,a,b)
print(''.join(a))
print(''.join(b))


