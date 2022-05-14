class Solution:
    visited = []
    maxo = -1
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dic = {}
        cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for l in times:
            if l[0] not in dic:
                dic[l[0]] = []
            dic[l[0]].append(l[1])
            cost[l[0]][l[1]] = l[2]
        for i in dic:
            if i != k:
                tf = True
                for j in dic:
                    if i in dic[j]:
                        tf = False
                        break
                if tf:
                    return -1
        store = {}
        def dfs(cur, time):
            if ((cur in store) and (time >= store[cur])) or ((cur == 0) and (time != 0)):
                return
            store[cur] = time
            if cur not in dic:
                return
            for dest in dic[cur]:
                dfs(dest, time + cost[cur][dest])
        
        dfs(k, 0)
        
        if len(store) != n:
            return -1
        
        ret = 0
        for i in store:
            ret = max(ret, store[i])
        return ret
        # graph = {}
        # Solution.visited = [False]*(n+1)
        # Solution.visited[0] = True
        # for i in range(1,n+1):
        #     graph[i] = {}
        # for i in times:
        #     graph[i[0]][i[1]] = i[2]
        # if(len(times)==1):
        #     return -1
        # def traverse(curr,graph):
        #     if(len(set(Solution.visited)) == 1 ):
        #         # print()
        #         return
        #     Solution.visited[curr] = True
        #     for i in graph[curr]:
        #         Solution.maxo += 1
        #         if(Solution.visited[i]==False):
        #             traverse(i,graph)
        # traverse(k,graph)
        # return Solution.maxo