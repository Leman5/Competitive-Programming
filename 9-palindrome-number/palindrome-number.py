class Solution:
    def isPalindrome(self, num: int) -> bool:
        s_num = str(num)
        n = len(s_num)
        for i in range(n):
            if(s_num[i]!=s_num[n-i-1]):
                return False
        return True