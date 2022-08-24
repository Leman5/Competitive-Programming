class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0 ):
            return False
        if(n==1):
            return True
        # if(n%10 in (1,3,9,7)):
            
        return round((math.log(n)/math.log(3)),10).is_integer()