from typing import List

class Solution1:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        #该方法时间复杂度过高,提交后会超时
        high=len(matrix)
        width=len(matrix[0])

        direct=[(1,0),(0,1),(-1,0),(0,-1)]   #方向数组

        def bfs(x,y):
            step=0
            queue = [(x,y,step)]
            visited = [[0 for i in range(width)] for j in range(high)]
            visited[x][y]=1
            while(queue):
                x,y,step=queue.pop(0)
                if matrix[x][y]!=0:
                    for dx,dy in direct:
                        if x+dx>=0 and x+dx<high and y+dy>=0 and\
                                y+dy<width and visited[x+dx][y+dy]!=1:
                            queue.append((x+dx,y+dy,step+1))
                            visited[x+dx][y+dy]=1
                    continue
                return step

        for i in range(high):
            for j in range(width):
                if matrix[i][j]==1:
                    step=bfs(i,j)
                    matrix[i][j]=step

        return matrix[:]

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        #利用超级0 的思想,先将所有的0加入队列
        high = len(matrix)
        width = len(matrix[0])
        direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 方向数组
        queue=[]
        visited=[[0 for i in range(width)] for j in range(high)]

        for i in range(high):
            for j in range(width):
                if matrix[i][j]==0:
                    queue.append((i,j,0))
                    visited[i][j]=1

        while(queue):
            x,y,step=queue.pop(0)
            for dx,dy in direct:
                if x + dx >= 0 and x + dx < high and y + dy >= 0 and \
                        y + dy < width and visited[x + dx][y + dy] != 1:
                    matrix[x+dx][y+dy]=step+1
                    visited[x+dx][y+dy]=1
                    queue.append((x+dx,y+dy,step+1))

        return matrix



matrix=[[0,0,0],[0,1,0],[1,1,1]]
a=Solution()
print(a.updateMatrix(matrix))



