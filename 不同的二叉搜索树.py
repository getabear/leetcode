# 假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
# G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
# G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
#
# 当i为根节点时，其左子树节点个数为i - 1个，右子树节点为n - i，则
# f(i) = G(i - 1) * G(n - i)
# f(i) = G(i−1)∗G(n−i)
#
# 综合两个公式可以得到卡特兰数公式
# G(n) = G(0) * G(n - 1) + G(1) * (n - 2) + ... + G(n - 1) * G(0)
# G(n) = G(0)∗G(n−1)+G(1)∗G(n−2) + ... + G(n−1)∗G(0)

class Solution:
    def numTrees(self, n: int) -> int:
        #dp[i]为有i个节点的二叉排序树 即G(i)
        dp=[0 for i in range(n+1)]
        dp[0]=1
        dp[1]=1 #初始化条件dp[0]=1 dp[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]



a=Solution()
print(a.numTrees(3))