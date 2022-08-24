class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0 ):
            return False
        # if(n==1):
        #     return True
        return round((math.log(n)/math.log(3)),10).is_integer()