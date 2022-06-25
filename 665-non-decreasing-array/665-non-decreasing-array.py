class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        is_modified = False
        
        for i in range(1, len(nums)):
            
            if nums[i] - nums[i-1] < 0:
                if is_modified == True:
                    return False
                else:
                    is_modified = True
                    if i > 1 and nums[i] < nums[i-2]:
                        nums[i] = nums[i-1]
        
        return True
    