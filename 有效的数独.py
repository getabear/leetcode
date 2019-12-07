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
board=[[".",".",".",".",".",".","5",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       ["9","3",".",".","2",".","4",".","."],
       [".",".","7",".",".",".","3",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".","3","4",".",".",".","."],
       [".",".",".",".",".","3",".",".","."],
       [".",".",".",".",".","5","2",".","."]]

print(a.isValidSudoku(board))