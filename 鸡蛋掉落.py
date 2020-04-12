class Solution1:
    def superEggDrop(self, K: int, N: int) -> int:
        mem={}   #虽然用来字典记录,但是时间复杂度依然很高
        def dp(K,N):
            if K==1:
                return N
            if N==0:
                return 0
            if (K,N) in mem:
                return mem[(K,N)]
            res=float("inf")
            for i in range(1,N+1):
                res=min(res,max(dp(K-1,i-1),dp(K,N-i))+1)
            mem[(K,N)]=res
            return res

        return dp(K,N)

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp=[[0 for i in range(N+1)] for j in range(K+1)]

        # dp数组的含义:               (大佬的解法,我感觉自己是个傻子,大佬们好厉害啊)
        # dp[k][m] = n
        # 当前有 k 个鸡蛋，可以尝试扔 m 次鸡蛋
        # 这个状态下，最坏情况下最多能确切测试一栋 n 层的楼
        # 比如说 dp[1][7] = 7 表示：
        # 现在有 1 个鸡蛋，允许你扔 7 次;
        # 这个状态下最多给你 7 层楼，
        # 使得你可以确定楼层 F 使得鸡蛋恰好摔不碎
        # （一层一层线性探查嘛）

        m=0
        while(dp[K][m]<N):
            m+=1
            for k in range(1,K+1):
                dp[k][m]=dp[k-1][m-1]+dp[k][m-1]+1
        return m


a=Solution()
print(a.superEggDrop(2,6))