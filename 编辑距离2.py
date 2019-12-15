class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 咱们先用递归的方法实现,思路挺简单的,但是提交超时,还是老问题,重复子问题太多了
        def fun(word1: str, word2: str):
            # 如果word1的长度为0了,就添加word2的长度
            if len(word1) == 0:
                return len(word2)
            # 如果word2的长度为0了,就删除word1的长度
            if len(word2) == 0:
                return len(word1)
            else:
                # 这里有4种可能
                # 1.如果相等,则不改变,递归调用下去
                if word1[0] == word2[0]:
                    return fun(word1[1:], word2[1:])
                else:
                    # 这里包含3中可能,增加,删除,修改
                    return min(fun(word1[1:], word2),  # 删除
                               fun(word1[1:], word2[1:]),  # 替换
                               fun(word1, word2[1:])) + 1  # 增加

        return fun(word1, word2)


class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        # 加个备忘录,记录结果减少耗费的时间,提交直接通过
        dp = {}

        def fun(word1: str, word2: str, index1, index2):
            # 如果word1的长度为0了,就添加word2的长度
            if len(word1[index1:]) == 0:
                return len(word2[index2:])
            # 如果word2的长度为0了,就删除word1的长度
            if len(word2[index2:]) == 0:
                return len(word1[index1:])
            else:
                if (index1, index2) in dp:
                    return dp[(index1, index2)]
                if word1[index1] == word2[index2]:
                    dp[(index1, index2)] = fun(word1, word2, index1 + 1, index2 + 1)
                else:
                    dp[(index1, index2)] = min(fun(word1, word2, index1 + 1, index2),  # 删除
                                               fun(word1, word2, index1 + 1, index2 + 1),  # 替换
                                               fun(word1, word2, index1, index2 + 1)) + 1  # 增加
                return dp[(index1, index2)]

        return fun(word1, word2, 0, 0)


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        # 咱们尝试自底向上的动态规划,可能写得不够好,反而效率低了,痛苦的我,但是提交还是能勉强通过
        # 定义一个dp数组,dp[(i,j)]的含义为  word1[i]和word2[j]操作的最小次数
        dp = {}
        size1 = len(word1)
        size2 = len(word2)
        # 初始化环境
        tp=size1
        while tp>=0:
            dp[(tp,size2)]=size1-tp
            tp-=1
        tp=size2
        while tp>=0:
            dp[(size1,tp)]=size2-tp
            tp-=1

        index1 = size1 - 1
        index2 = size2 - 1
        while (index1 >= 0):
            while (index2 >= 0):
                if word1[index1] == word2[index2]:
                    dp[(index1, index2)] = dp[(index1 + 1, index2 + 1)]
                else:
                    dp[(index1, index2)] = min(dp[(index1 + 1, index2)],  # 删除
                                               dp[(index1 + 1, index2 + 1)],  # 替换
                                               dp[(index1, index2 + 1)]) + 1  # 增加
                index2 -= 1
            index2 = size2 - 1
            index1 -= 1
        return dp[(0, 0)]


a = Solution2()
word1 = ""
word2 = ""
print(a.minDistance(word1, word2))
