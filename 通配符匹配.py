# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
import time
class Solution:
    def isMatch(self, s: str, p: str) -> bool:    #暴力递归,提交后超时了
        if len(p)==0:
            return len(s)==0
        if len(s)==0:
            return len(p)==0 or p[0]=='*' and self.isMatch(s,p[1:])
        first=p[0] in [s[0],'?','*']
        if p[0]=='*':
            return self.isMatch(s[1:],p) or self.isMatch(s,p[1:])
        else:
            return first and self.isMatch(s[1:],p[1:])

    def isMatch2(self, s: str, p: str) -> bool:  # 加备忘录的递归
        # if len(p) == 0:
        #     return len(s) == 0
        # if len(s) == 0:
        #     return len(p) == 0 or p[0] == '*' and self.isMatch(s, p[1:])
        # first = p[0] in [s[0], '?', '*']
        # if p[0] == '*':
        #     return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        # else:
        #     return first and self.isMatch(s[1:], p[1:])
        dp={}   ##dp[(i,j)] 代表从第i个字符到从第j 个字符是否匹配   很关键,提升上百倍
        def fun(s,p,i,j):
            if (i,j) in dp.keys():
                return dp[(i,j)]
            if(i==len(s)):
                res=j==len(p) or p[j]=='*' and fun(s,p,i,j+1)
                dp.setdefault((i,j),res)
                return res
            elif len(p)==j:
                res=len(s)==i
                dp.setdefault((i,j),res)
                return res
            first = p[j] in [s[i], '?', '*']
            if p[j]=='*':
                res=fun(s,p,i+1,j) or fun(s,p,i,j+1)
            else :
                res=first and fun(s,p,i+1,j+1)
            dp.setdefault((i,j),res)
            return res
        fun(s,p,0,0)
        return  dp[(0,0)]


s="aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab"
p="*ab***ba**b*b*aaab*b"
a=Solution()
start=time.process_time()
# process_time是cpu有效运行时间，空闲时间不算 返回CPU的占用时间
print(a.isMatch2(s,p))
end=time.process_time()
print("time",end-start)