class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        r = len(matrix)
        c = len(matrix[0])
        self.dp = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if(i == 0 and j == 0):
                    self.dp[i][j] = matrix[i][j]
                # elif(i == 0  and j>0):
                #     self.dp[i][j] = self.dp[i][j-1] + matrix[i][j]
                elif(i>0 and j==0):
                    self.dp[i][j] = matrix[i][j]
                else:
                    self.dp[i][j] = self.dp[i][j-1] + matrix[i][j]
                # else:
                #     self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] + matrix[i][j]
        # print(self.dp)      

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for i in range(row1,row2+1):
            if(col1>0):
                s += (self.dp[i][col2] - self.dp[i][col1 - 1])
            else:
                s += self.dp[i][col2]
        # return s
        # s = self.dp[row2][col2] - self.dp[row1][col1]
        return s
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)