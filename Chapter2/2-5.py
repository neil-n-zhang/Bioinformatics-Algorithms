#Fibonacci constant amount of storage
n=6

f=[1,1,0]
if n==1 or n==2:
    print(1)
else:
    for i in list(range(n-2)):
        f[2]=f[0]+f[1]
        f[0]=f[1]
        f[1]=f[2]
     print(f[2])