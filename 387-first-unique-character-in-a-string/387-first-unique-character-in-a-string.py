class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i in range(len(s)):
            if(s[i] in d):
                d[s[i]] = -1
            else:
                d[s[i]] = i
        for i in d.keys():
            if(d[i]!=-1):
                return d[i]
        return -1