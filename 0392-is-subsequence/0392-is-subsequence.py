class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sn = len(s)
        tn = len(t)
        
        def check(i,j):
            if(i==0):
                return True
            if(i>j) :
                return False
            if(s[i-1] ==t[j-1] ):
                return check(i-1,j-1)
            else:
                return check(i,j-1)
        
        return check(sn,tn)