class Solution:
    def isMatch(self, s: str, p: str) -> bool:  #我写的,巨复杂
        lens=len(s)                           #陷入无尽的细节之中,推荐使用大佬解法
        lenp=len(p)
        if lens==0 or lenp==0:
            if lens==0:
                if lenp==0:
                    return True
                elif lenp>1 and p[1]=='*':
                    return self.isMatch(s,p[2:])
                else:
                    return False
            if lenp==0:
                if lens==0:
                    return True
                else:
                    return False
        ret=False
        if p[0]==s[0] or p[0]=='.':
            if lenp>1 and  p[1]=='*':
                ret=ret or self.isMatch(s[1:],p)
                ret=ret or self.isMatch(s,p[2:])
            else:
                ret=ret or self.isMatch(s[1:],p[1:])
        elif lenp>1 and p[1]=='*':
            ret=ret or self.isMatch(s,p[2:])
        return ret

    def isMatch2(self, s: str, p: str) -> bool:   #大佬写的
        if not p:                  #p 使用完后 ,s 还有剩余一定不匹配
            return not s
        first=bool(s) and p[0] in {s[0],'.'}   #bool(s)如果为真 则表明至少有s[0]
        if len(p)>=2 and p[1]=='*':
            return self.isMatch2(s,p[2:]) or first and self.isMatch2(s[1:],p)
        else:
            return first and self.isMatch2(s[1:],p[1:])

    def isMatch3(self, s: str, p: str) -> bool:    #动态规划,带备忘录的递归
        memo={}
        def fun(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j==len(p):
                ans=i==len(s)
                return ans
            first= i<len(s) and p[j] in {s[i],'.'}
            if len(p)-j>=2 and p[j+1]=='*':
                ans=fun(i,j+2) or first and fun(i+1,j)
            else:
                ans=first and fun(i+1,j+1)
            memo[(i,j)]=ans
            return ans
        return fun(0,0)

a=Solution()
s="ab"
p=".*c"
print(a.isMatch3(s,p))
