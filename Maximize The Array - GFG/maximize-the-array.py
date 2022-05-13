#User function Template for python3
from heapq import heapify, heappush, heappop
class Solution:
    def maximizeArray(self, arr1, arr2, n):
        heap = []
        heapify(heap)
        for i in range(n):
            heappush(heap, (-arr2[i],0,i))
            heappush(heap, (-arr1[i],1,i))
        i1 = []
        i2 = []
        used = set()
        k = 0
        while k<n and heap:
            ele, ar, ind = heappop(heap)
            if ar == 1 and ele not in used:
                i1.append(ind)
                used.add(ele)
                k+=1
            elif ar == 0 and ele not in used:
                i2.append(ind)
                used.add(ele)
                k+=1
                
        i1.sort()
        i2.sort()
        ans = []
        for i in i2:
            ans.append(arr2[i])
        for i in i1:
            ans.append(arr1[i])
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maximizeArray(arr1, arr2, n)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1

# } Driver Code Ends