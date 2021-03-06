from typing import List
import copy

# N皇后问题,所有皇后不能再同一列,同一行,同一斜线
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        l=[['.' for i in range(n)] for i in range(n)]
        ret=[]
        #想法,用回溯递归处理 这种方法很垃圾,建议第二种优化方案
        def fun(n,count):
            if count==n:
                if l not in ret:
                    ret.append(copy.deepcopy(l))
                return 0
            for i in range(n):
                for j in range(n):
                    if l[i][j]!='Q':
                        if(deal((i,j),n)): #有皇后
                            continue
                        l[i][j] = 'Q'
                        fun(n,count+1)
                        l[i][j]='.'

        #负责判断有无皇后
        #q为皇后的坐标(x,y)
        def deal(q,n):
            x=q[0]
            y=q[1]
            for i in range(n):
                if(l[x][i]=='Q'):
                    return 1
            for i in range(n):
                if(l[i][y]=='Q'):
                    return 1
            while(x<n and y<n):
                if l[x][y]=='Q':
                    return 1
                x+=1
                y+=1
            x = q[0]
            y = q[1]
            while(x>=0 and y>=0):
                if l[x][y]=='Q':
                    return 1
                x-=1
                y-=1
            x = q[0]
            y = q[1]
            while(x>=0 and y<n):
                if l[x][y]=='Q':
                    return 1
                x-=1
                y+=1
            x = q[0]
            y = q[1]
            while (x <n  and y >=0):
                if l[x][y] =='Q':
                    return 1
                x += 1
                y -= 1
            return 0
        fun(n,0)

        #以下代码转换格式使其能通过leedcode
        res=[]
        s=""
        tp=[]
        for i in ret:
            for j in i:
                for k in j:
                    s+=k
                tp.append(s)
                s=""
            res.append(tp)
            tp=[]
        return res

#第二种方案
class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:

        l = [['.' for i in range(n)] for i in range(n)]
        ret = []

        # 想法,用回溯递归处理,
        def fun(hang, count):
            if count == n:
                if l not in ret:
                    ret.append(copy.deepcopy(l))
                return 0
            if hang<n:
                for i in range(n):
                    if l[hang][i]!='Q':
                        if deal((hang,i),n):
                            continue
                        l[hang][i]='Q'
                        fun(hang+1,count+1)
                        l[hang][i]='.'


        # 负责判断有无皇后
        # q为皇后的坐标(x,y)
        def deal(q, n):
            x = q[0]
            y = q[1]
            for i in range(n):
                if (l[x][i] == 'Q'):
                    return 1
            for i in range(n):
                if (l[i][y] == 'Q'):
                    return 1
            while (x < n and y < n):
                if l[x][y] == 'Q':
                    return 1
                x += 1
                y += 1
            x = q[0]
            y = q[1]
            while (x >= 0 and y >= 0):
                if l[x][y] == 'Q':
                    return 1
                x -= 1
                y -= 1
            x = q[0]
            y = q[1]
            while (x >= 0 and y < n):
                if l[x][y] == 'Q':
                    return 1
                x -= 1
                y += 1
            x = q[0]
            y = q[1]
            while (x < n and y >= 0):
                if l[x][y] == 'Q':
                    return 1
                x += 1
                y -= 1
            return 0

        fun(0, 0)

        # 以下代码转换格式使其能通过leedcode
        res = []
        s = ""
        tp = []
        for i in ret:
            for j in i:
                for k in j:
                    s += k
                tp.append(s)
                s = ""
            res.append(tp)
            tp = []
        return res
import time
a=Solution()
print(time.process_time())
ret=a.solveNQueens(8)
# print(ret)
print(time.process_time())

