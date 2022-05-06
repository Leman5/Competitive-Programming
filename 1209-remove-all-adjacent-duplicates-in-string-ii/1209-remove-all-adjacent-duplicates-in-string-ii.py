class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, count]
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
                
            if stack[-1][1] == k:
                stack.pop()
        
        result = ""
        for char, count in stack:
            result += (char * count)
        
        return result
        # if(len(s) <k):
        #     return s
        # for i in range(len(s)-k+1):
        #     for j in range(i+k-1,i-1,-1):
        #         if(s[i]!=s[j] ):
        #             break
        #         if(j == i+k-1):
        #             print(s[:i]+s[i+k:],len(s[:i]+s[i+k:]))
        #             return self.removeDuplicates(s[:i]+s[i+k:], k)
        # return s