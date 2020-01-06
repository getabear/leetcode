from typing import List

class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        #本以为会超时,结果通过了...
        # 超越58%的用户
        def judge(s):  #用于判断字符串是否是回文串
            start=0
            end=len(s)-1
            while(start<end):
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True

        self.ret=[]
        def fun(s,tp):
            if len(s)==0:
                if tp not in self.ret:
                    self.ret.append(tp[:])
                return
            for i in range(1,len(s)+1):
                if judge(s[:i]):
                    fun(s[i:],tp+[s[:i]])
        fun(s,[])
        return self.ret

class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        #此方法明显速度提升了,超越了81%的用户
        rec={}   #加字典用于记录回文串
        def judge(s,start,end):  #用于判断字符串是否是回文串
            st=start
            ed=end
            if (st,ed) in rec:
                return rec[(st,ed)]
            while(start<end):
                if s[start]!=s[end]:
                    rec[(st,ed)]=False
                    return False
                start+=1
                end-=1
            rec[(st,ed)]=True
            return True

        self.ret=[]
        def fun(s,tp,start,end):
            if len(s)==start:
                if tp not in self.ret:
                    self.ret.append(tp[:])
                return
            for i in range(start,end):
                if judge(s,start,i):
                    fun(s,tp+[s[start:i+1]],i+1,end)
        fun(s,[],0,len(s))
        return self.ret
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #这次提交反而只超越了27%...   不应该啊..
        self.ret=[]
        #这次咱们用动态规划记录那些是回文,然后dfs
        dp=[[False for _ in s] for _ in s]
        #1.dp数组含义,dp[i][j]为从s[i]到s[j]是否为回文  False为否  True为是

        #2.转移方程:  dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
        #3.初始状态 dp[i][i]=True
        for i in range(len(s)):
            dp[i][i]=True
        for j in range(len(s)):   #这里的遍历顺序很关键,应该斜着遍历
            for i in range(j):
                if i+1<=j-1:
                    dp[i][j]=(s[i]==s[j]) and dp[i+1][j-1]
                else:
                    dp[i][j]= s[i]==s[j]
        def dfs(s,i,tp):
            if i==len(s):
                self.ret.append(tp[:])
                return
            for index in range(i,len(s)):
                if dp[i][index]:
                    dfs(s,index+1,tp+[s[i:index+1]])
        dfs(s,0,[])
        return self.ret

a=Solution()
s="abbab"
print(a.partition(s))
