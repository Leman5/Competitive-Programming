class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(0, len(nums)-1, 2):
        #     if(nums[i]!=nums[i+1]):
        #         return nums[i]
        # return nums[-1]

        # Solution 1:
        #     make a dict:
        #         if that number ka key not  present add it and value is false
        #         if that number ka key already present make the value as true
        #     find the false value in dict

        d = dict()
        for num in nums:
            if num in d.keys():
                d[num] = True
            else:
                d[num] = False
        for key,value in d.items():
            if value == False:
                return key
        


        # Solution 2: 
        #     sort
        #     for i in list, 2 increment
        #         if i != i+1
        #             return i
        #     return last element