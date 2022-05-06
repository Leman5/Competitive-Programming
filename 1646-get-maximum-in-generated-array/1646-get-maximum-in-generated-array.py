class Solution:
    
    def getMaximumGenerated(self, n: int) -> int:
        if(n<=1):
            return n
        arr = [0,1]
        for i in range(2,n+1):
            if(i%2==0):
                arr.append(arr[i//2])
            else:
                arr.append(arr[i//2]+arr[(i//2)+1])
            # print(arr)
        return max(arr)