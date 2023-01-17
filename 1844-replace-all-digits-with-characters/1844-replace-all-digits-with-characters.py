class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        def shift(c,digit):
            return chr(ord(c)+digit)
            
        for i in range(0,len(s)-1,2):
            s[i+1] = shift(s[i],int(s[i+1]))
            
        return ''.join(s)