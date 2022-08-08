class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # for i in range(len(nums),-1,-1):
        #     for j in range(i+1,len(nums)):
        #         if()
        max_length = 1
        dp = [0 for i in range(len(nums))]
        dp[0] = 1 
        for curr_index in range(len(nums)):
            dp[curr_index] = 1
            for prev_index in range(curr_index):
                if nums[curr_index] > nums[prev_index] and dp[curr_index] <= dp[prev_index]:
                    dp[curr_index] = dp[prev_index] + 1
                    max_length = max(max_length, dp[curr_index])
        return max_length