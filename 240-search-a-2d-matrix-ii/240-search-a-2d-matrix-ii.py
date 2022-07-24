class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
#         dp = [[0 for _ in range(n) ]for i in range(m)]
#         def traverse(i,j):
#             if(i>=m or j>=n):
#                 return False
#             if(dp[i][j]==0):
#                 val = matrix[i][j]
#                 if(val==target):
#                     dp[i][j] = True
#                 elif(val>target):
#                     dp[i][j] = False
#                 else:
#                     dp[i][j] = traverse(i+1,j) or traverse(i,j+1)
#             return dp[i][j]
#         return traverse(0,0)
        
        for i in range(len(matrix)):
            if matrix[i][0]<=target<=matrix[i][len(matrix[i])-1]:
                for j in range(len(matrix[i])):
                    if matrix[i][j]==target:
                        return True
        return False
        