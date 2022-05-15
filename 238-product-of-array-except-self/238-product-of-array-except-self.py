class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #code here [10,11,0,2]
            #       [0,0,220,0]]
        n = len(nums)
        if(nums.count(0)>1):
            return [0]*n
        
        out = []
        contain_z = False
        product = 1
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
        