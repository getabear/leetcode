class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem=dict()
        def fun(idx1,idx2):
            if (idx1,idx2) in mem:
                return mem[(idx1,idx2)]
            if idx2==len(p):
                return idx1==len(s)
            if idx1==len(s):
                return p[idx2]=='*' and fun(idx1,idx2+1)
            flag=(s[idx1]==p[idx2] or p[idx2]=='?')
            if flag:
                mem[(idx1,idx2)]=fun(idx1+1,idx2+1)
                return mem[(idx1,idx2)]
            if p[idx2]!='*':
                mem[(idx1, idx2)]=False
                return False
            mem[(idx1, idx2)]= fun(idx1+1,idx2) or fun(idx1,idx2+1)
            return mem[(idx1,idx2)]
        return fun(0,0)

a=Solution()
s="aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab"
p="*ab***ba**b*b*aaab*b"
print(a.isMatch(s,p))
