class Solution:
    def countVowelStrings(self, n: int) -> int:
        if(n==1):
            return 5
        # else:
        #     return (n*5)+self.countVowelStrings(n-1)
        # out = 0
        # for i in range(5,0,-1):
        #     out += (i*n)
        # return 
        # 5,15,35,70,126
        arr = [[],[1,1,1,1,1]]
        prev_sum = sum(arr[-1])
        for i in range(2,n+1):
            arr.append([0]*5)
            for j in range(5):
                # if(j==0):
                arr[i][j] = prev_sum
                prev_sum -= arr[i-1][j]
                 
            prev_sum = sum(arr[-1])
        return sum(arr[-1])
        