class Solution:
    def combination(self, k, n, result, start, output: List):
        if n == 0 and k == 0:
            output.append(result)
            return

        for i in range(start, 10):
            next_k = k - 1
            next_n = n - i
            if next_n < 0 or next_k < 0:
                continue

            self.combination(next_k, next_n, result + [i], i + 1, output)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        if k > n:
            return results

        self.combination(k=k, n=n, result=[], start=1, output=results)
        return results
    # def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         if (n * 9 < k):
#             return []
#         self.combinator(n,k,1)
#         return self.output
    
#     def combinator(self,n,k,last):
#         if(n==0 and k==0):
#             self.output.append(self.combination)
#             return
#         if(n<0 or k<0):
#             return 
#         for i in range(last,10):
#             if(not self.visited[i]):
#                 self.combination.append(i)
#                 self.visited[i] = True
#                 self.combinator(n-1,k-i,i+1)
#                 self.visited[i] = False
#                 self.combination.pop()
        
