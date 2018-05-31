#the smallest number of coins and the correct combination of coins
def mininum(money,coins):
    minnumcoins=[0]
    for m in range(1,money+1):
        minnumcoins.append(10**6)
        for coini in coins:
            if m>=coini:
                if minnumcoins[m]>minnumcoins[m-coini]+1:
                    minnumcoins[m]=minnumcoins[m-coini]+1
    return minnumcoins


def dpchange(money,coins):
    minnumcoins=mininum(money,coins)
    print('Need %d coins'%(minnumcoins[-1]))
    while money>0:
        num=[]
        for coin in coins:
            num.append(minnumcoins[money-coin])
        n=num.index(min(num))
        money=money-coins[n]
        print(coins[n])

dpchange(15,[1,5,15])