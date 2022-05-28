class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp = 0
        for i in range(len(nums)+1):
            exp+=i
        return exp-sum(nums)
        # expected = sum([expected+i for i in range(len(nums)+1)])
        
        