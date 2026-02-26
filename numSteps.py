# Example 1:

# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal representation.
# Step 1) 13 is odd, add 1 and obtain 14. 
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.  
# Step 5) 4 is even, divide by 2 and obtain 2. 
# Step 6) 2 is even, divide by 2 and obtain 1

def numstep(s):
    
    count = 0
    bn = int(s,2)
    while bn!=1:
        if bn % 2!=0:
            count+=1
            bn+=1
        else:
            count+=1
            bn//=2
            
        
    return count
print(numstep(s = '1101'))
    