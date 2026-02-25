def sortByBits(arr):
    
    nums = []
    for num in arr:
        bn = bin(num)[2:]
        cnt = bn.count("1")
        nums.append((cnt,num))
        
    nums.sort()
    res = []
    
    for cnt, num in nums:
        res.append(num)
    return res
print(sortByBits(arr = [0,1,2,3,4,5,6,7,8]))