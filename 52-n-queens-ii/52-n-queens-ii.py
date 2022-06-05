class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negD = set()
        posD = set()
        
        out = []
        board = [ ['.']*n for i in range(n)]
        
        def solve(r):
            if(r==n):
                out.append(1)
                # print(1)
                return
            for c in range(n):
                if(c not in col and (r+c not in posD) and (r-c not in negD)):
                    col.add(c)
                    negD.add(r-c)
                    posD.add(r+c)
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.'
                    col.remove(c)
                    negD.remove(r-c)
                    posD.remove(r+c)
        solve(0)
        return sum(out)