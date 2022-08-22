class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if(num&num-1==0 and num%10 in (1,4,6)):
            return True
        return False