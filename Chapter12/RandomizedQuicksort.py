import random
def quicksort(num):
    if len(num)<=1:
        return num
    else:
        m=random.choice(num)
        num_small=[]
        num_large=[]
        num.remove(m)
        for n in num:
            if n<m:
                num_small.append(n)
            else:
                num_large.append(n)
        num_small=quicksort(num_small)
        num_large=quicksort(num_large)
        num_sorted=num_small+[m]+num_large
    return num_sorted


quicksort([1,5,6,2,4,3])
