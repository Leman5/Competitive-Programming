class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        out = []
        for i in range(len(tasks)):
            tasks[i].append(i)            
        tasks.sort(key = lambda x:x[0])
        timer = 0
        q = []
        
        # i = 0
        while(tasks):
            if(tasks[0][0]<=timer):
                heapq.heappush(q,[tasks[0][1],tasks[0][2]])
                tasks.pop(0)
            elif(not q):
                timer = tasks[0][0]
            else:
                # q.sort(key = lambda x : x[1])
                x,y = heapq.heappop(q)
                timer += x
                out.append(y)
        # q.sort(key = lambda x : x[1])
        while(q):
            x,y = heapq.heappop(q)
            out.append(y)
        return out
            
            
            
        
            
               
            
        
        
#         visited = 0
#         while(visited != len(tasks)):
#             timer += 1
#             if(q):
#                 q.sort(key = lambda x:x[1])
#                 in_hand = q.pop(0)
#                 timer += in_hand[1]
            
            
#         return out
            
            
            # if(q):
            #     q[0][1] 
                
            
        
            