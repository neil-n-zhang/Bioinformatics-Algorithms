#Karatsuba algorithm

def fastmultiple(x,y):
    if len(str(abs(x)))<=3 or len(str(abs(y)))<=3:
        return x*y
    else:
        e=min(len(str(abs(x)))//2,len(str(abs(y)))//2)
        a=x//10**e
        b=x-a*10**e
        c = y // 10 ** e
        d = y - c * 10 ** e
        ac=fastmultiple(a,c)
        bd = fastmultiple(b, d)
        result=ac*10**(2*e)+(ac+bd-fastmultiple((a-b),(c-d)))*10**2+bd
        return result