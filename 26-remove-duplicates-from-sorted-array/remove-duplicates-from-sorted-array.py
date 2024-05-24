class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1,len(nums)):
            if(nums[i]!=nums[count-1]):
                nums[count],nums[i] = nums[i],nums[count]
                count += 1
        
        return count


        # from collections import Counter

        # d = Counter(nums)
        # count = len(d.keys())
        # ctr = 0
        # for i in d.keys():
        #     nums[ctr] = i
        #     ctr+=1
        
        # return count