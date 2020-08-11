from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        high=len(board)
        if high==0:
            return
        width=len(board[0])
        if width==0:
            return
        direct=[(1,0),(0,1),(0,-1),(-1,0)]
        def dfs(x,y,ch):
            if board[y][x]=='O':
                board[y][x]=ch
            else:
                return
            for dx,dy in direct:
                if x+dx<width and x+dx>=0 and y+dy<high and y+dy>=0 and\
                    board[y+dy][x+dx]=='O':
                    dfs(x+dx,y+dy,ch)

        for i in range(high):
            if board[i][0]=='O':
                dfs(0,i,'.')
            if board[i][width-1]=='O':
                dfs(width-1,i,'.')
        for j in range(width):
            if board[0][j]=='O':
                dfs(j,0,'.')
            if board[high-1][j]=='O':
                dfs(j,high-1,'.')
        for i in range(high):
            for j in range(width):
                if board[i][j]=='O':
                    board[i][j]='X'
        for i in range(high):
            for j in range(width):
                if board[i][j]=='.':
                    board[i][j]='O'
        return

a=Solution()
board=[["O","X","O"],["X","O","X"],["O","X","O"]]
a.solve(board)
print(board)
