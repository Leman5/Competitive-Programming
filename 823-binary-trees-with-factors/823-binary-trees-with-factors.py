class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        d = dict()
        for i in arr:
            d[i] = 1
        arr.sort()
        for i in range(len(arr)):
            count = 0
            for j in range(i):
                if(arr[i]%arr[j]==0):
                    if(arr[i]//arr[j] in d.keys()) :
                        count+=d[arr[j]]*d[arr[i]//arr[j]]
            d[arr[i]]+= count
        return sum(d.values())%(10**9+7)