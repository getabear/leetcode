from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        # dp[i][j]代表的含义为到triangle[i][j]所需要的最小路径
        dp = [[0 for _ in range(t + 1)] for t in range(h)]
        dp[0][0] = triangle[0][0]
        for i in range(1, h):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        res = min(dp[-1])
        return res


a = Solution()
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(a.minimumTotal(triangle))
