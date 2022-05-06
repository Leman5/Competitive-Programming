#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, a, n, k):
		# code here
		for i in range(1,(n//k)+2):
            a[(i-1)*k:min(n,i*k)] = a[(i-1)*k:min(n,i*k)][::-1]
        # a = a[0:3:-1]
        # a = a[3:6:-1]
        # a = a[6:9:-1]
        # a = a[9:11:-1]
        return a

		    

#{ 
#  Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends