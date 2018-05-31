# Partial digest problem, find x such that delta(x)=l
# only output one possible x
def pdigest(l,x):
    if l==[]:
        return
    segment = max(l)
    delta1=[abs(segment-segx) for segx in x]
    delta2=[abs(length-segment-segx) for segx in x]
    if all(y in l for y in delta1):
        for i in delta1:
            l.remove(i)
        x.append(segment)
        pdigest(l,x)
    elif all(y in l for y in delta2):
        for i in delta2:
            l.remove(i)
        x.append(length-segment)
        pdigest(l,x)
    x.sort()
    return x

l=[1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,9,9,10,11,12,15]
length=max(l)
l.remove(length)
x=[0,length]
x=pdigest(l,x)
print(x)

# Partial digest problem, find x such that delta(x)=l
# all possible x
def pdigest(l,x):
    if l==[]:
        x.sort()
        print(x)
        return
    segment = max(l)
    delta1=[abs(segment-segx) for segx in x]
    if all(y in l for y in delta1):
        for i in delta1:
            l.remove(i)
        x.append(segment)
        pdigest(l,x)
        x.remove(segment)
        l.extend(delta1)

    delta2 = [abs(length - segment - segx) for segx in x]
    if all(y in l for y in delta2):
        for i in delta2:
            l.remove(i)
        x.append(length-segment)
        pdigest(l,x)
        x.remove(length-segment)
        l.extend(delta2)

    return

l=[1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,9,9,10,11,12,15]
length=max(l)
l.remove(length)
x=[0,length]
pdigest(l,x)
