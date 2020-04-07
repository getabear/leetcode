from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        high=len(matrix)
        width=len(matrix[0])
        tmp=[[0 for i in range(width)] for j in range(high)]
        for i in range(high):
            for j in range(width):
                tmp[j][width-i-1]=matrix[i][j]
        matrix[:]=tmp