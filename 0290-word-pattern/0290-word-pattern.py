class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ptw  = dict()
        wtp = dict()
        s = s.split()
        if(len(pattern)!= len(s)):
            return False
        for i in range(len(s)):
            if(pattern[i] in ptw.keys() ):
                if(ptw[pattern[i]] != s[i] ):
                    return False
            if(s[i] in wtp.keys()):
                if(wtp[s[i]] != pattern[i]):
                    return False
            ptw[pattern[i]] = s[i]
            wtp[s[i]] = pattern[i]
            
        return True
        