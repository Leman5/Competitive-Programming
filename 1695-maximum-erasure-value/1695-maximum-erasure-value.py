class Solution:
    def maximumUniqueSubarray(self, s: List[int]) -> int:
        if(len(s)<=1):
            return sum(s)
        out = s[0]
        visited = {
            s[0] : 0
        }
        start = 0
        end = 1
        while(start<len(s) and end<len(s)):
            if(s[end] in visited and (visited[s[end]]>=start and visited[s[end]]<end)):
                    start = visited[s[end]]+1                  
            else:
                out = max(out,sum(s[start:end+1]))
            visited[s[end]] = end
            end += 1
        return out
        