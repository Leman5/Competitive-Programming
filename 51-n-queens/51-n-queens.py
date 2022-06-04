class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos = set()
        neg = set()
        
        out =[]
        board = [['.']*n for i in range(n)]
        
        def solve(r):
            if(r==n):
                copy = [''.join(row) for row in board]
                out.append(copy)
                return
            for c in range(n):
                if(c not in col and (r+c not in pos) and (r-c not in neg) ):
                    col.add(c)
                    pos.add(r+c)
                    neg.add(r-c)
                    board[r][c] = 'Q'
                    solve(r+1)
                    col.remove(c)
                    pos.remove(r+c)
                    neg.remove(r-c)
                    board[r][c] = '.'
        solve(0)
        return out
        