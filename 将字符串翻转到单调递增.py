class Solution1:
    def minFlipsMonoIncr(self, S: str) -> int:
        #先写暴力解法,思路正确，超时是必然
        def judge(s):
            if len(s)<=1:
                return True
            slow,fast=0,1
            while fast<len(s):
                if s[slow]!=s[fast]:
                    if not (s[slow]=='0' and s[fast]=='1'):
                        return False
                slow+=1
                fast+=1
            return True

        self.ret=len(S)
        S=list(S)
        def fun(index,step):
            if judge(S) or step>=self.ret or index>=len(S):
                self.ret=min(self.ret,step)
                return
            if S[index]=='0':
                if judge(S[:index+1]):
                    fun(index+1,step)
                S[index]='1'
                if judge(S[:index+1]):
                    fun(index+1,step+1)
                S[index]='0'
            else:
                if judge(S[:index+1]):
                    fun(index+1,step)
                S[index]='0'
                if judge(S[:index+1]):
                    fun(index+1,step+1)
                S[index]='1'

        fun(0,0)
        return self.ret

class Solution2:
    def minFlipsMonoIncr(self, S: str) -> int:
        #以某个节点为分界，统计需要改变的数量，时间复杂度 平方级
        #超时，但是较递归方法速度更快
        def judge(s):
            if len(s) <= 1:
                return True
            slow, fast = 0, 1
            while fast < len(s):
                if s[slow] != s[fast]:
                    if not (s[slow] == '0' and s[fast] == '1'):
                        return False
                slow += 1
                fast += 1
            return True
        def count(s,index):
            ret=0
            for i in range(index):
                if s[i]=='1':
                    ret+=1
            for i in range(index+1,len(s)):
                if s[i]=='0':
                    ret+=1
            return ret

        if judge(S):
            return 0
        else:
            cnt=len(S)
            for i in range(len(S)):
                cnt=min(cnt,count(S,i))
            return cnt

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        #利用前面的结果，时间复杂度将为线性
        def judge(s):
            if len(s) <= 1:
                return True
            slow, fast = 0, 1
            while fast < len(s):
                if s[slow] != s[fast]:
                    if not (s[slow] == '0' and s[fast] == '1'):
                        return False
                slow += 1
                fast += 1
            return True
        def count(s,index):
            left,right=0,0
            for i in range(index):
                if s[i]=='1':
                    left+=1
            for i in range(index+1,len(s)):
                if s[i]=='0':
                    right+=1
            return (left,right)
        if judge(S):
            return 0
        else:
            left,right=count(S,0)
            ret=left+right
            for i in range(1,len(S)):
                if S[i]=='0':
                    right-=1
                if S[i-1]=='1':
                    left+=1
                ret=min(ret,left+right)
            return ret
a=Solution()
S="00011000"
print(a.minFlipsMonoIncr(S))