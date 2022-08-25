class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(int)
        for i in magazine:
            d[i] += 1
        for i in ransomNote:
            if(d[i]<=0):
                return False
            d[i] -=1
        return True