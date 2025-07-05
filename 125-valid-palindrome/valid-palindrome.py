class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr_1 = 0
        ptr_2 = len(s)-1
        s = s.lower()
        while(ptr_1<ptr_2):
            if(s[ptr_1].isalnum()):
                if(s[ptr_2].isalnum()):
                    if(s[ptr_1]==s[ptr_2]):
                        ptr_1 += 1
                        ptr_2 -= 1
                    else:
                        return False
                else:
                    ptr_2 -= 1
            else:
                ptr_1 += 1
        return True