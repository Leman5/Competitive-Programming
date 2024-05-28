# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # versions = [i for i in range(n)]
        low,high = 1,n
        while(low<=high):
            mid = (low+high)//2
            if(isBadVersion(mid)):
                if(isBadVersion(mid-1)):
                    high = mid-1
                else:
                    return mid
            else:
                low = mid+1
        