from typing import List
import  time
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        map=[[] for i in range(9)]   #建立9个数组,保存每个方格数字
        lie=[[] for i in range(9)]   #用于保存9列的数字
        hang=[[0 for i in range(9)] for i in range(9)]  #用于保存行数子

        #填充map的函数
        def map_fill(board):
            x=0
            y=0  #x,y代表起始宫格的坐标
            cnt=0   #代表记录到那个map
            x1=0
            y1=0
            while(x<=6):
                while(y<=6):
                    x1=x
                    y1=y
                    while x1<x+3:
                        while y1<y+3:
                            if board[x1][y1]!='.':
                                map[cnt].append(int(board[x1][y1]))
                            y1+=1
                        y1=y
                        x1+=1
                    cnt+=1
                    y+=3
                y=0
                x+=3
            return
        #填充lie的函数
        def lie_fill(board):
            cnt=0
            i=0
            j=0
            while i<9:
                while j<9:
                    if board[j][i]!='.':
                        lie[cnt].append(int(board[j][i]))
                    j+=1
                cnt+=1
                j=0
                i+=1
            return
        #填充行数字
        def hang_fill(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]!='.':
                        hang[i][j]=int(board[i][j])
        #检查 . 的数量,有点耽误时间用下面的函数count_lie
        # def count_num(board):
        #     ret=0
        #     for i in range(9):
        #         for j in range(9):
        #             if board[i][j]=='.':
        #                 ret+=1
        #     return ret
        def count_lie(lie):  #计算列长度
            ret=0
            for i in lie:
                ret+=len(i)
            return ret

        # 做选择的函数
        def choice():
            if count_lie(lie)==81:
                return 1
            for i in range(9):
                for j in range(9): #j代表列数
                    if board[i][j]=='.':    #代表找到了一个需要填充的位置
                        map_n=(i//3)*3+j//3   #确定在那个宫格中
                        board[i][j]='x'   #标记填了数字
                        for num in range(1,11): #num在1到10中
                            if num==10:  #说明一个满足条件的数都没找到
                                board[i][j] = '.'  # 恢复改掉的值
                                return 0
                            if num not in hang[i] and num not in lie[j] and num not in map[map_n]:
                                hang[i][j]=num   #行是带位置的,到时候直接填充到board中
                                lie[j].append(num)
                                map[map_n].append(num)
                                ret=choice()
                                if(ret==0):#递归调用,返回值为1代表不需要回溯,返回值为0代表需要回溯
                                    hang[i][j]=0   #回溯
                                    lie[j].remove(num)   #pop和remove,remove更快
                                    map[map_n].remove(num)
                                elif ret==1:  #返回1不需要回溯,直接返回
                                    return 1

        # 填充map和lie
        map_fill(board)
        lie_fill(board)
        hang_fill(board)
        choice()
        for i in range(9):
            for j in range(9):
                board[i][j]=str(hang[i][j])
        return

a=Solution()
# board=[
#   [".",".","7","2","5","8","3","6","."],
#   [".",".","8","3","6",".","4","7","1"],
#   ["3",".",".","4",".","1","5","8","2"],
#   ["4","7","1","5","8","2","6",".","3"],
#   ["5","8","2","6",".","3","7","1","4"],
#   ["6",".","3","7","1","4","8","2","5"],
#   ["7",".","4","8","2","5",".","3","6"],
#   ["8","2",".",".","3","6","1","4","7"],
#   [".","3","6","1","4","7",".","5","."]
# ]
board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
a.solveSudoku(board)
print(time.process_time())
for i in range(9):
    print(board[i])



