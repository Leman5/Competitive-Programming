class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        j = len(nums) - 1
        
        
        while i<=j:
            if(nums[i]==val):
                nums[i],nums[j] = nums[j],nums[i]
                j -= 1
                k+=1
            else:
                i += 1

        
        return len(nums)-k