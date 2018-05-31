def merge(left,right):
    if isinstance(left,int):
        left=[left]
    if isinstance(right, int):
        right=[right]
    c=[]
    left.append(float('inf'))
    right.append(float('inf'))
    while len(left)>1 or len(right)>1:
        if left[0]<right[0]:
            c.append(left[0])
            left.remove(left[0])
        else:
            c.append(right[0])
            right.remove(right[0])
    return c

def mergesort(numlist):
    if isinstance(numlist,int):
        numlist=[numlist]
    if len(numlist)==1:
        return numlist
    else:
        left=mergesort(numlist[0:len(numlist)//2])
        right=mergesort(numlist[len(numlist)//2:])
        return merge(left,right)