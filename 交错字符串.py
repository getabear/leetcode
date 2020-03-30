class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #超时了,通过了99个测试用例
        def fun(index1,index2,index3):
            ret=False
            if index3==len(s3):
                return True
            if index1<len(s1) and s1[index1]==s3[index3]:
                ret=fun(index1+1,index2,index3+1)
                if ret:
                    return ret
            if index2 < len(s2) and s2[index2] == s3[index3]:
                ret = fun(index1, index2+1, index3 + 1)
            return ret

        if len(s1)+len(s2)!=len(s3):
            return False
        return fun(0,0,0)
class Solution2:
    # 提交后成功通过所有测试用例哈哈哈,击败71.59%
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        mem=[[-1 for i in s2+'1'] for j in s1+'1']
        def fun(index1,index2,index3):
            if index3==len(s3):
                return True
            if(index1<len(s1) and index2<len(s2) and mem[index1][index2]>=0):
                return True if mem[index1][index2] else False
            ans=False
            if(len(s1)>index1 and s1[index1]==s3[index3]):
                ans=fun(index1+1,index2,index3+1)
                if ans:
                    mem[index1][index2]=1
                    return ans
            if (len(s2) > index2 and s2[index2] == s3[index3]):
                ans = fun(index1, index2+1, index3 + 1)
                if ans:
                    mem[index1][index2] = 1
                    return ans
            mem[index1][index2]=0
            return ans
        if len(s1)+len(s2)!=len(s3):
            return False
        return fun(0,0,0)
class Solution:
    #动态规划,nice 击败57%的用户
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False for i in s2+' '] for j in s1+' ']
        #dp数组含义: dp[1][1]表示是s1和s2的第一个字符和s3匹配
        #递推关系   if dp[i-1][j] and s1[i-1]==s3[i+j-1] or dp[i][j-1] and s2[j-1]==s3[i+j-1]:
        #               dp[i][j]=True
        #初始化数据
        dp[0][0]=True
        for i in range(1,len(s1)+1):
            if dp[i-1][0] and s1[i-1]==s3[i-1]:
                dp[i][0]=True
        for j in range(1, len(s2) + 1):
            if dp[0][j-1] and s2[j-1]==s3[j-1]:
                dp[0][j]=True
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1]):
                    dp[i][j]=True

        return dp[-1][-1]

# s1="bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# s2="babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# s3="babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

a=Solution()
s1=""
s2=""
s3="aadbbbaccc"
print(a.isInterleave(s1,s2,s3))
