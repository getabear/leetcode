from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        high=len(matrix)   #矩阵的高度
        if high==0:
            return []
        width=len(matrix[0])  #矩阵的宽度
        high-=1   #转换为矩阵的最大可访问下标
        width-=1
        s_w=0   #定义起始高度和宽度
        s_h=0
        ret=[]   #保存返回值
        while(True):
            w=s_w
            h=s_h
            #从左往右遍历
            while w<=width:
                ret.append(matrix[h][w])
                w+=1
            s_h+=1  #矩阵起始高度加1
            if s_h>high:
                break
            #从上到下遍历
            h=s_h
            while h<=high:
                ret.append(matrix[h][width])
                h+=1
            width-=1
            if s_w>width:
                break
            #从右到左遍历
            w=width
            while(w>=s_w):
                ret.append(matrix[high][w])
                w-=1
            high-=1
            if s_h>high:
                break
            #从下到上遍历
            h=high
            while(h>=s_h):
                ret.append(matrix[h][s_w])
                h-=1
            s_w+=1
            if s_w>width:
                break
        return ret

a=Solution()
matrix=[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(a.spiralOrder(matrix))




