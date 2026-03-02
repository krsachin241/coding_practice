# You are given a binary array nums (0-indexed).

# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
def prefixesDivBy5(nums):
    
    x = 0
    lst = []
    for i in range(len(nums)):
        x = (x * 2 + nums[i]) % 5
        lst.append(x)
    res = []
    for i in lst:
        if i == 0:
            res.append(True)
        else:
            res.append(False)
    return res
print(prefixesDivBy5(nums = [1,1,1]))
