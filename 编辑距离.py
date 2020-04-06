class Solution1:
    def miniDistance(self,word1,word2):
        len1=len(word1)
        len2=len(word2)
        if len1==0 or len2==0:
            if(len1>=len2):
                return len1-len2
            else :
                return len2-len1
        if(word1[0]==word2[0]):
            min=self.miniDistance(word1[1:],word2[1:])
        else:
            add=1+self.miniDistance(word1,word2[1:])
            replace=1+self.miniDistance(word1[1:],word2[1:])
            delete=1+self.miniDistance(word1[1:],word2)
            min=add
            if add>replace:
                min=replace
            if min>delete:
                min=delete
        return min

word1="horse"
word2="ros"

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 咱们尝试自底向上的动态规划

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

a=Solution()
print(a.minDistance(word1,word2))