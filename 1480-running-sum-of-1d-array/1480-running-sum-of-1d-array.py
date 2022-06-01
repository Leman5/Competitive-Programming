class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        rs = 0
        for i in range(len(nums)):
            rs += nums[i]
            out.append(rs)
        return out