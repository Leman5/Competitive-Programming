class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==1):
            return 0
        # dp = [[0]*len(prices)]*len(prices)
        # for i in range(len(prices)):
        #     for j in range(i):
        #         if(prices[j]<prices[i]):
        #             dp[i][j] = max(dp[i-1][j],prices[i]-prices[j])
        # return max(dp[-1])
        m = prices[0]
        dp = [0]*len(prices)
        for i in range(1,len(prices)):
            if(prices[i]>m):
                dp[i] = prices[i]-m
            if(prices[i]<m):
                m = prices[i]
        return max(dp)
                    
                