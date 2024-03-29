class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i+1)
            if len(s1) > len(s2):
                if len(res) < len(s1):
                    res = s1
            else:
                if len(res) < len(s2):
                    res = s2
        return res
    
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        