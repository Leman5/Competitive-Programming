class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = len(s)
        j = len(t)
        # dp = [[False]*(tn+1)]*(sn+1)
        # def check(i,j):
        #     if(i==0):
        #         return True
        #     if(i>j) :
        #         return False
        #     if(dp[i][j]):
        #         return dp[i][j]
        #     if(s[i-1] ==t[j-1] ):
        #         dp[i][j] = check(i-1,j-1)
        #     else:
        #         dp[i][j] = check(i,j-1)
        #     return dp[i][j]
        # return check(sn,tn)
        while(i<=j):
            if(i==0):
                return True
            if(s[i-1]==t[j-1]):
                i -= 1
                j -= 1
            else:
                j -= 1
        if(i<=0):
            return True
        else:
            return False