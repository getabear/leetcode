from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        high=len(image)
        width=len(image[0])
        direct=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(y,x,oldColor):
            image[y][x]=newColor
            for dx,dy in direct:
                nx,ny=x+dx,y+dy
                if 0<=nx<width and 0<=ny<high and image[ny][nx]==oldColor:
                    dfs(ny,nx,oldColor)
            return
        oldColor=image[sr][sc]
        if oldColor==newColor:
            return image
        dfs(sr,sc,oldColor)
        return image

image=[[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
a=Solution()
print(a.floodFill(image,sr,sc,newColor))
