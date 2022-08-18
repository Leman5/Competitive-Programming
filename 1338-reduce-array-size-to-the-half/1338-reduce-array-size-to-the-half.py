class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = defaultdict(int)
        target = len(arr)//2
        for i in arr:
            d[i] +=1
        ctr = []
        for i in d.keys():
            ctr.append(d[i])
        ctr.sort(reverse=True)
        out = 0
        s = 0
        for i in ctr:
            out += 1
            s += i
            if(s>=target):
                return out
        
        