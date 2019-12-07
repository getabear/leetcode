from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map={}
        #检测列
        i=0
        j=0
        while i<9:
            while j<9:
                if board[i][j]=='.':
                    j+=1
                    continue
                if board[i][j] not in map:
                    map[board[i][j]]=1
                else:
                    return False
                j+=1
            j=0
            map={}
            i+=1
        #检测行
        i = 0
        j = 0
        while i < 9:
            while j < 9:
                if board[j][i] == '.':
                    j+=1
                    continue
                if board[j][i] not in map:
                    map[board[j][i]] = 1
                else:
                    return False
                j += 1
            j=0
            map = {}
            i += 1
        #检测九宫格
        def fun(start_x,start_y):  #start_x,start_y 为9宫格开始的位置
            i=start_x
            j=start_y
            map={}
            while i<start_x+3:
                while j<start_y+3:
                    if  board[i][j]=='.':
                        j+=1
                        continue
                    if board[i][j] not in map:
                        map[board[i][j]]=1
                    else:
                        return False
                    j+=1
                j=start_y
                i+=1
            return True
        i=0
        j=0
        while(i<=6):
            while(j<=6):
                if not fun(i,j):
                    return False
                j+=3
            j=0
            i+=3
        return True

a=Solution()
board=[
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]





print(a.isValidSudoku(board))