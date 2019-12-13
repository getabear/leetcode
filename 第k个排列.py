class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 方法一:列出所有情况,然后返回,猜想应该会提交超时
        # 但是不妨做一下,当做练习递归程序
        ret = []
        lis = [i for i in range(1, n + 1)]

        def fun(lis, s):
            if (len(lis) == 0):
                ret.append(s)
            for i in lis:
                temp = lis[:]
                temp.remove(i)
                fun(temp, s + str(i))
            return

        fun(lis, "")
        return ret[k - 1]


class Solution1:
    def getPermutation(self, n: int, k: int) -> str:
        # 方法二:咱们算出(n-1)!代表每个字符开头的个数
        # 调用咱们方法一所写的递归程序改进版
        # 这种方法勉强减掉了一部分递归,提交只超越了5%的人,效率还是低
        # 今天有点事,所以精进的算法先不看了
        ret = []
        lis = [i for i in range(1, n + 1)]

        def fun(lis, s, key):
            if (len(lis) == 0):
                ret.append(s)
            for i in lis:
                if len(ret) >= key:
                    break
                temp = lis[:]
                temp.remove(i)
                fun(temp, s + str(i), key)
            return

        def jie(n):  # 阶乘函数,返回n的阶乘
            ret = 1
            for i in range(1, n + 1):
                ret *= i
            return ret

        key = jie(n - 1)  # 每个数开头的个数
        count = 0
        tp = key
        count = k // key
        tp = k % key
        if tp == 0:
            tp2 = str(count)
            lis.remove(count)
            fun(lis, "", key)  # 最后一个
            return tp2 + ret[-1]
        else:
            tp2 = str(count + 1)
            lis.remove(count + 1)
            fun(lis, "", tp)
            return tp2 + ret[-1]


a = Solution1()
print(a.getPermutation(3, 2))
