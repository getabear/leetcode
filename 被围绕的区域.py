from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        size=len(board)
        if size<=2:    #如果高度小于等于2,一定不存在围起来的'o'
            return
        length=len(board[0])
        if length<=2:   #如果宽度小于等于2,一定不存在围起来的'o'
            return
        def dfs(i,j):
            if i>size-1 or j>length-1 or i<0 or j<0:
                return
            if board[i][j]=='O':
                board[i][j]='B'  # 将其标记为 B 方便以后将他更改回来
                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    dfs(i+x,j+y)
            return
        for i in range(length):   #第一行和最后一行的'O'处理
            if board[0][i]=='O':
                dfs(0,i)
            if board[size-1][i]=='O':
                dfs(size-1,i)
        for i in range(size):   #第一列和最后一列的'O'处理
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][length-1]=='O':
                dfs(i,length-1)
        for i in range(size):
            for j in range(length):
                if board[i][j]=='O':
                    board[i][j]='X'
        for i in range(size):
            for j in range(length):
                if board[i][j]=='B':
                    board[i][j]='O'
        return


board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
a=Solution()
a.solve(board)
print(board)