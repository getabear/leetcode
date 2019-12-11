from typing import List

class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        l = [['.' for i in range(n)] for i in range(n)]
        ret = []

        # 想法,用回溯递归处理
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
        res=len(ret)
        return res