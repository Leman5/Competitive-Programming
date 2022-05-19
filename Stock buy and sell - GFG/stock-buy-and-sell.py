#User function template for Python

class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, A, n):
	    
 #code here
         ans=[]
         for i in range(1, n):
             if A[i]>A[i-1]:
                 ans.append([i-1, i])
         return ans
# 		#code here
# 		out = []
# 		b,s = 0,1
# 		maxp = -1
# 		while(s<n and b<n-1):
# 		    while(b<n-1 and A[b+1]<A[b]):
# 		        b+=1
# 		    l = [b]
# 		    s = b+1
# 		    while(s<n-1 and A[s]<A[s+1]):
# 		        s+=1
# 		    l.append(s)
# 		    out.append(l)
# 		    b = s+1
# 		  #  if(A[l]<A[r]):
# 		  #      maxp = max(maxp,A[r]-A[l])
# 		  #      r+=1
# 		  #  if()
		  
# 		return out

#{ 
#  Driver Code Starts
#Initial template for Python

def check(ans,A,p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]]-A[ans[i][0]]
    if(c==p):
        return 1 
    else:
        return 0

if __name__=='__main__':
	t = int(input())
	while(t>0):
		n = int(input())
		A = [int(x) for x in input().strip().split()]
		ob = Solution()
		ans = ob.stockBuySell(A,n)
		p=0
		for i in range(n-1):
		    p += max(0,A[i+1]-A[i])
		if(len(ans) == 0):
			print("No Profit",end="")
		else:
			print(check(ans,A,p),end="")
		print()
		t-=1
# } Driver Code Ends