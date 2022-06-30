class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
		## SPACE COMPLEXITY : O(N) ##

        heapq.heapify(people)
        ans = [0] * len(people)
        while(people):
            person = heapq.heappop(people)
            count = 0
            for i in range(0,len(ans)):
                
                if( count == person[1] and ans[i] != 0):
                    continue
                
                if(count == person[1]):
                    ans[i] = person
                    
                if(ans[i] == 0 or ans[i][0] >= person[0]):  # 0 position will be filled by other bigger (or equal) height, so leave it and 
                    count += 1
                    continue
        return ans
    
        ## OPTIMIZED SOLUTION ##
        people.sort(key = lambda x: (-x[0], x[1]))
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
