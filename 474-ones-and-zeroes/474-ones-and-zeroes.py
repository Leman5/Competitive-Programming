class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.h = {}
        def solve(arr,m,n,l):
            if(l == 0):
                return 0
            if(m == 0 and n == 0):
                return 0
            if((m,n,l) in self.h):
                return self.h[(m,n,l)]
            if(arr[l-1].count("0") <= m and arr[l-1].count("1")<=n):
                self.h[(m,n,l)] = max(1+solve(arr,m-arr[l-1].count("0"),n-arr[l-1].count("1"),l-1),solve(arr,m,n,l-1))
            else:
                self.h[(m,n,l)] = solve(arr,m,n,l-1)
            return self.h[(m,n,l)]
        return solve(strs,m,n,len(strs))
        # r0,r1 = m,n
        le = 0
        global matrix
        matrix = []
        # matrix = [[0 in range(n+1)] for x in range(m+1) ]
        for i in range(m+1):
            matrix.append([0]*(n+1))
        # print(len(matrix),len(matrix[0]))
        
        def func(strs,m,n,l):
            global matrix
            if(len(strs)==0 or (m<=0 and n<=0)):
                return matrix[m][n]
            if(m>strs[-1].count('0') and n>strs[-1].count('1')):
                return func(strs[:-1],m,n,l)
            if(matrix[m][n]>0):
                return matrix[m][n]
            else:
            # print(strs,m,n,l)
                a = func(strs[:-1],m-strs[-1].count('0'),n-strs[-1].count('1'),l+1)
                b = func(strs[:-1],m,n,l)
                matrix[m][n] = max(a,b)
                return max(a,b)
        return func(strs,m,n,le)