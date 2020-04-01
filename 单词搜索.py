from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        high=len(board)
        width=len(board[0])
        length=len(word)

        #访问的记录
        visited=[[0 for i in range(width)] for j in range(high)]
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 方向数组

        def fun(visited,x,y,index):
            if(index==length):
                return True
            for dx,dy in direct:
                if(x+dx<high and y+dy<width and x+dx>=0 and y+dy>=0 and\
                        visited[x+dx][y+dy]==0 and word[index]==board[x+dx][y+dy]):
                    visited[x+dx][y+dy]=1
                    if(fun(visited,x+dx,y+dy,index+1)):
                        return True
                    visited[x + dx][y + dy] = 0
            return False

        for i in range(high):
            for j in range(width):
                if(board[i][j]==word[0]):
                    visited[i][j]=1
                    if(fun(visited,i,j,1)):
                        return True
                    visited[i][j]=0
        return False

a=Solution()
board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word="ABCB"
print(a.exist(board,word))