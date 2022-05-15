#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here [10,11,0,2]
            #       [0,0,220,0]]
        if(nums.count(0)>1):
            return [0]*n
        
        out = []
        contain_z = False
        product = 1
        # print(10*3*5*6*2)
        for i in range(n):
            if(nums[i]!=0):
                product = product*nums[i]
            else:
                contain_z = True
                
        if(not contain_z):   
            for i in range(n):
                out.append(product//nums[i])
        else:
            for i in range(n):
                if(nums[i]==0):
                    out.append(product)
                else:
                    out.append(0)
        
        return out

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends