class Solution:
    def duplicates(self, arr, n): 
        duplicate={}
        val=[]
        for i in arr:
            if i not in duplicate:
                duplicate[i]='0'
            else:
                duplicate[i]='1'
        for i in duplicate:
            if  duplicate[i]=='1':
                val.append(i)
        if len(val) == 0:
            val.append(-1)
        val.sort()   
        return val
    # 	# code here
    # 	out = []
    # # 	    for j in range(i+1,n):
    # # 	        if(arr[i]==arr[j] and arr[i]>=0):
    # # 	            if(arr[i] not in out):
    # # 	                out.append(arr[i])
    # # 	                arr[j] = -1
    #     d = dict()
    #     for i in range(n):
    #         d[i] = False
        
    #     for i in range(n):
    #         if(d[arr[i]]):
    #             out.append(arr[i])
    #         else:
    #             d[arr[i]] = True
    # 	out.sort()
    #     return set(out) if(len(out)>0) else [-1]
    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends