class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if(nums[i] in d.keys()):
                return [i,d[nums[i]]]
            d[target-nums[i]] = i
#         for i in range(len(nums)):
#             d[i] = nums[i] 
#         nums.sort()
        
#         left = 0
#         right = len(nums)-1
#         while(left<right):
#             if(nums[left]+nums[right]==target):
#                 return [left,right]
#             elif(nums[left]+nums[right]>target):
#                 right -= 1
#             else:
#                 left += 1
#         return [left,right]
        