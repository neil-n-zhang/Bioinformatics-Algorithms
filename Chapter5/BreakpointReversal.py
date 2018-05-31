def makePermutation(n):
    import random
    middle=list(range(1,n))
    random.shuffle(middle)
    seq=[0]+middle+[n]
    return seq

def hasBreakpoints(seq):
    for i in list(range(1,len(seq))):
        if seq[i]!=1+seq[i-1]:
            return True
    return False

def getStrips(seq):
    increase=[]
    decrease=[]
    deltas=[seq[i]-seq[i-1] for i in list(range(1,len(seq)))]
    start=1
    for i in list(range(1,len(deltas))):
        if abs(deltas[i])==1 and i!=len(deltas)-1:
            continue
        elif abs(deltas[i-1])!=1:
            start=i
        end=i+1

        if deltas[i-1]==1 and i!=1:
            increase.append((start,end))
            start=end
        else:
            decrease.append((start,end))
            start = end
    return increase,decrease

def pickReversal(seq, strips):
    reversal=[0,(0,0)]
    left=[i for i,j in strips]
    right = [j for i, j in strips]
    maxrevbreakpoint = 0
    for i in left:
        for j in right:
            revbreakpoint = 0
            if j-i<=1:
                continue
            if abs(seq[i-1]-seq[j-1])==1:
                revbreakpoint+=1
            if abs(seq[i]-seq[j])==1:
                revbreakpoint += 1
            if revbreakpoint>maxrevbreakpoint:
                maxrevbreakpoint=revbreakpoint
                reversal[0]=maxrevbreakpoint
                reversal[1]=(i,j)
    return reversal

def doReversal(seq,i,j):
    return seq[:i] + list(reversed(seq[i:j])) + seq[j:]

seq=makePermutation(5)
print(seq)
while hasBreakpoints(seq):
    increase,decrease=getStrips(seq)
    if decrease!=[]:
        strips=increase+decrease
        reversal=pickReversal(seq, strips)
        seq=doReversal(seq, reversal[1][0], reversal[1][1])
        print(seq)
    else:
        seq = doReversal(seq, increase[0][0], increase[0][1])