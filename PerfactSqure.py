import math
def isPerfectSquare(num):
        inte = int(math.sqrt(num))
        if inte*inte == num:
            return True
        else:
            return False
        
print(isPerfectSquare(num=25))