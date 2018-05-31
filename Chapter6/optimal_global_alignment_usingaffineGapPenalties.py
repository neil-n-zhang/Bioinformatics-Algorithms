#http://rosalind.info/problems/ba5j/
import numpy as np
gap_op=-11
gap_ext=-1
f=open('D:\Bioinformatics_Algorithms\Chapter6\Blosum62.txt')
f.seek(0)
aminoacid=f.readline().split()
blosum=dict()
for i in list(range(len(aminoacid))):
    score=f.readline().split()
    for j in list(range(len(aminoacid))):
        blosum[aminoacid[i]+aminoacid[j]]=int(score[j+1])

def globalalign(seq1,seq2):
    trace=np.zeros([len(seq2)+1,len(seq1)+1])
    for i in list(range(1,len(seq1)+1)):
        trace[0,i]=1
    for i in list(range(1,len(seq2)+1)):
        trace[i,0]=2
    #deletion is 1, insertion is 2, match is 3
    s_del=np.zeros([len(seq2)+1,len(seq1)+1])
    for i in list(range(1,len(seq1)+1)):
        s_del[0,i]=s_del[0,i-1]-1
    for i in list(range(1,len(seq2)+1)):
        s_del[i,0]=s_del[i-1,0]-1
    s_in=s_del.copy()
    s=s_del.copy()

    for i in list(range(1,len(seq2)+1)):
        for j in list(range(1,len(seq1)+1)):
            s_del[i,j]=max(s_del[i-1,j]+gap_ext,s[i-1,j]+gap_op)
            #s_del[i, j] = max(s_del[i - 1, j] + gap_ext, s[i - 1, j] + gap_ext + gap_op)
            s_in[i, j] = max(s_in[i, j - 1] + gap_ext, s[i, j - 1] + gap_op)
            #s_in[i, j] = max(s_in[i, j-1] + gap_ext, s[i, j-1] + gap_ext + gap_op)
            s[i,j]=max(s[i-1,j-1]+blosum[seq2[i-1]+seq1[j-1]],s_del[i,j],s_in[i, j])
            if s[i,j]==s_del[i,j]:
                trace[i,j]=1
            elif s[i,j]==s_in[i,j]:
                trace[i,j]=2
            else:
                trace[i, j] = 3
    return s[-1,-1],trace

def outputalign(seq1,seq2,i,j,trace):
    if i==0 and j==0:
        return [],[]

    if trace[i,j]==1:
        lcs1,lcs2=outputalign(seq1,seq2,i-1,j,trace)
        lcs1.append('-')
        lcs2.append(seq2[i-1])
    elif trace[i,j]==2:
        lcs1, lcs2=outputalign(seq1,seq2,i,j-1,trace)
        lcs1.append(seq1[j-1])
        lcs2.append('-')
    else:
        lcs1, lcs2 = outputalign(seq1,seq2,i-1,j-1,trace)
        lcs1.append(seq1[j-1])
        lcs2.append(seq2[i - 1])
    return lcs1,lcs2

seq1='PRTEINS'
seq2='PRTWPSEIN'

seq1='YHFDVPDCWAHRYWVENPQAIAQMEQICFNWFPSMMMKQPHVFKVDHHMSCRWLPIRGKKCSSCCTRMRVRTVWE'
seq2='YHEDVAHEDAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPIISATCARMRVRTVWE'

score,trace1=globalalign(seq1,seq2)
lcs1,lcs2=outputalign(seq1,seq2,len(seq2),len(seq1),trace1)
print(''.join(lcs1))
print(''.join(lcs2))
