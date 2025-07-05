class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = dict()
        for i in arr:
            if i in counter.keys():
                counter[i] += 1
            else:
                counter[i] = 1
        
        lucky = -1
        for key,value in counter.items():
            if key == value and key>lucky:
                lucky = key
        return lucky
