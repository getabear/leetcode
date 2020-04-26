from typing import List
from collections import deque

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #通过了提交，击败5.05%。使用双端队列，击败15%
        def judge(high,width,n):
            if high+n>len(matrix) or width+n>len(matrix[0]):
                return False
            for i in range(high,high+n):
                if matrix[i][width+n-1]=='0':
                    return False
            for j in range(width,width+n):
                if matrix[high+n-1][j]=='0':
                    return False
            return True
        queue=deque()
        for high in range(len(matrix)):
            for width in range(len(matrix[0])):
                if matrix[high][width]=='1':
                    queue.append((high,width,1))
        self.n=0
        while queue:
            high,width,self.n=queue.popleft()
            if judge(high,width,self.n+1):
                queue.append((high,width,self.n+1))
        return self.n*self.n

matrix=[["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]
a=Solution()
ret=a.maximalSquare(matrix)
print(ret)



