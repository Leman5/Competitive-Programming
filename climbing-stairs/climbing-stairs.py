class Solution:
    def climbStairs(self, n: int) -> int:
        
        if(n == 1):
            return 1
        elif(n==2):
            return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        l = [0]*(n+1)
        l[1],l[2] = 1,2        
        for i in range(3,n+1):
            l[i] = l[i-1]+l[i-2]
        return l[n]