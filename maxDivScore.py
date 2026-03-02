def maxDivScore(nums, divisors):
    
    lst = []
    
    for i in divisors:
        cnt = 0
        arr = []
        arr[:] = nums[:]
        for j in nums:
            if j % i == 0:
                cnt+=1
        lst.append(cnt)
        
    x = max(lst)
    res = []
    for i in range(len(lst)):
        if x == lst[i]:
            res.append(divisors[i])
    return min(res)
print(maxDivScore(nums = [2,9,15,50], divisors = [5,3,7,2]))
        
