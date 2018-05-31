def rechange(money, coins):
    if money==0:
        return 0
    minnumcoins=10^6
    for i in range(len(coins)):
        if money>=coins[i]:
            numcoins=rechange(money-coins[i],coins)
            if numcoins+1<minnumcoins:
                minnumcoins=numcoins+1
    return minnumcoins
