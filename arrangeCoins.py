def arrangeCoins(n):
    
    if n == 1:
        return 1
    cnt = 0
    for i in range(1, n+1):
        n-=i
        if n>=0:
            cnt+=1
        else:
            return cnt
print(arrangeCoins(n = 8))