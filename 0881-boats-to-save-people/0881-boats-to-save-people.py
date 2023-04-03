class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r =  len(people)-1
        count  = 0
        curr_limit = 0
        people.sort()
        curr_capacity = 0
        while(l<=r):
            
            if(curr_limit+people[r]<=limit and curr_capacity<2):
                curr_limit += people[r]
                r -= 1
                curr_capacity += 1
            elif(curr_limit+people[l]<=limit and curr_capacity<2):
                curr_limit += people[l]
                l += 1
                curr_capacity += 1
            else:
                count += 1
                curr_limit = 0
                curr_capacity = 0
                
        # if(l>=r):
        count += 1
        return count
        
            