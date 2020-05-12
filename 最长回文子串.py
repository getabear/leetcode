class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        if length==0:
            return ""
        ret=1
        start=0
        # dp数组含义，dp[i][j]=True代表s[i:j+1]是回文
        dp=[[False]*length for _ in range(length)]
        #初始状态：长度为1的是回文
        for i in range(length):
            dp[i][i]=True
        #状态转移：dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
        for i in range(1,length):
            for j in range(0,i):
                if s[i]==s[j]:
                    if i-j<=2:
                        dp[j][i]=True
                    else:
                        dp[j][i]=dp[j+1][i-1]
                    if dp[j][i]:
                        if i-j+1>ret:
                            ret=i-j+1
                            start=j
        return s[start:start+ret]

a=Solution()
print(a.longestPalindrome("aaaa"))
