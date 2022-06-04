#User function Template for python3

class Solution:
    def nQueen(self, n):
        col = set()
        pos = set()
        neg = set()
        
        out =[]
        board = [['.']*n for i in range(n)]
        
        def solve(r):
            if(r==n):
                copy = []
                for i in board:
                    copy.append(i.index('Q')+1)
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
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends