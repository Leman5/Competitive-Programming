class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2)
        n = len(word1)
        dp = [['#' for x in range(m+1)] for _ in range(n+1)]
        
        def long(i,j):
            if(i==0 or j==0):
                dp[i][j] = 0
                return 0
            if(dp[i][j]=='#'):
                # print(word1[:i+1],word2[:j+1])
                if(word1[i-1]==word2[j-1]):
                    dp[i][j] = long(i-1,j-1)+1
                else:
                    dp[i][j] = max(long(i-1,j),long(i,j-1))
            return dp[i][j]
        lcs = long(n,m)
        # print(lcs)
        # print(dp)
        out = m-lcs
        out += n-lcs
        return out