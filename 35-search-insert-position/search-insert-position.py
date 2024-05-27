class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        # mid = (highlow)//2
        while(low <= high):
            mid = (high+low)//2
            if(nums[mid]==target):
                return mid
            if(target>nums[mid]):
                low = mid+1
            else:
                high = mid - 1
        
        # mid = (high+low)//2

        return low