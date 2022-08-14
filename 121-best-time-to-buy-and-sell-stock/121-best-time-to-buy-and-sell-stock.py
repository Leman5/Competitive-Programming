class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==1):
            return 0
        m = prices[0]
        ma = 0
        for i in range(1,len(prices)):
            if(prices[i]>m):
                ma = max(ma,prices[i]-m)
            if(prices[i]<m):
                m = prices[i]
        return ma
                