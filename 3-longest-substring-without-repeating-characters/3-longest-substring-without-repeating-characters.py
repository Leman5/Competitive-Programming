class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if(len(s)<=1):
            return len(s)
        
        out = 1
        visited = {
            s[0] : 0
        }
        start = 0
        end = 1
        while(start<len(s) and end<len(s)):
            if(s[end] in visited and (visited[s[end]]>=start and visited[s[end]]<end)):
                    start = visited[s[end]]+1                  
            else:
                out = max(out,end-start+1)
            visited[s[end]] = end
            end += 1
        return out