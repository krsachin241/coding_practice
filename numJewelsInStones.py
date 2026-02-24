def numJewelsInStones(jewels, stones):
    cnt = 0
    
    for stone in stones:
        if stone in jewels:
            cnt+=1
            
    return cnt
print(numJewelsInStones(jewels='aA',stones="aAaABbb"))