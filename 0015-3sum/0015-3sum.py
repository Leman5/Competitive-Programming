class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for x in range(len(nums)-2):
            if(nums[x]==nums[x-1] and x>0) :
                continue
            i = x+1
            j = len(nums)-1
            while(i<j):
                if(nums[i]+nums[j]+nums[x]==0):
                    output.append([nums[x],nums[i],nums[j]])
                    i+=1
                    while(i<j and nums[i]==nums[i-1]):
                        i+=1
                    # j-=1
                elif(nums[i]+nums[j]+nums[x]>0):
                    j -= 1
                else:
                    i+=1
            
        return output