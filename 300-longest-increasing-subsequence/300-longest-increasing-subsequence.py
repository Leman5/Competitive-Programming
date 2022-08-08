class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            m_arr = [1]
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i]):
                    m_arr.append(1+dp[j])
            dp[i] = max(m_arr)
        # print(dp)
        return max(dp)