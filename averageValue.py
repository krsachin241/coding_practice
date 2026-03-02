# Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

# Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

 

# Example 1:

# Input: nums = [1,3,6,10,12,15]
# Output: 9
# Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9

def averageValue(nums = [1,3,6,10,12,15]):
    
    lst = []
    for i in nums:
        if i % 2 == 0 and i % 3 == 0:
            lst.append(i)
    n = len(lst)
    sm = sum(lst)
    
    if lst:
        return sm // n
    else:
        return 0
print(averageValue(nums = [1,2,4,7,10]))