class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        nums.sort()
        result, memo = 0, {}
        
        def dfs(remaining):
            
            if remaining == 0:
                return 1
            
            if remaining < 0: return 0
            
            if remaining in memo: return memo[remaining]
            
            memo[remaining] = 0
            
            for num in nums:
                if remaining - num < 0: break
                memo[remaining] += dfs(remaining-num)
            
            return memo[remaining]
        
        return dfs(target)
        