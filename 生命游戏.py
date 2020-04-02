from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        #某个位置的方向数组
        direct = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        high=len(board)
        width=len(board[0])

        def fun(x,y):   #函数返回8个周围位置的1的个数(即活着的细胞数)
            count=0
            for dx,dy in direct:
                if(x+dx>=0 and x+dx<high and y+dy>=0 and y+dy<width):
                    if(board[x+dx][y+dy]==1):
                        count+=1
            return count

        #临时用来存储
        arr=[[0 for i in range(width)] for j in range(high)]

        for x in range(high):
            for y in range(width):
                tmp=fun(x,y)
                if(board[x][y]==1):  #活细胞
                    if(tmp==2 or tmp==3):  #仍然存活
                        arr[x][y]=1
                else:
                    if(tmp==3): #复活
                        arr[x][y]=1
        board[:]=arr

        return

board=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
a=Solution()
a.gameOfLife(board)
print(board)
