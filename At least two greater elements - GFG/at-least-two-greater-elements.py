#User function Template for python3

import heapq
class Solution:
    def findElements(self,a, n):
        # Your code goes here
        # a = a.sort()
        b = []
        # m1,m2 = -1000001,-1000001
        # a.sort()
        # return a[:-2]
        heapq.heapify(a)
        return heapq.nsmallest(n-2,a)
        # print(heapq.heappop(a))
        # print(heapq.heappop(a))
        # print(heapq.heappop(a))
        # return 
        # for x in range(len(a)):
        #     b.append(heapq.heappop(a))
        # return b
        # return sorted(a)
        

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n = int(input())
    	a = [int(x) for x in input().strip().split()]
    	ob=Solution()
    	print(*ob.findElements(a, n))
    	
    	T -= 1

if __name__ == "__main__":
    main()







# } Driver Code Ends