class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # a,b,c = 0,0,0
        # if(len(set(nums))<3):
        #     return False
        # for i in range(len(nums)-2):
        #     while(i>0 and nums[i]>=nums[i-1]):
        #         i+=1
        #     a = nums[i]
        #     for j in range(i+1,len(nums)-1):
        #         while(j>i+1 and )
        #         b = nums[j]                
        #     while(i>0 and nums[i]>=nums[i-1]):
        #         i+=1
        #         for k in range(j+1,len(nums)):
        #             c = nums[k]
        #             if(a<c and c<b):
        #                 return True
        # return False
        
        stack = []
        num = float('-inf')
        for n in nums[::-1]:
            if n < num:
                return True
            while stack and stack[-1] < n:
                num = stack.pop()
            stack.append(n)
        return False
