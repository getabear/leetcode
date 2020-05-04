class Solution:
    def countDigitOne(self, n: int) -> int:
        if n<=0:
            return 0
        tmp=1
        res=0
        while tmp<=n:
            res+=(n//(10*tmp))*tmp+min(max(n%(10*tmp)-tmp+1,0),tmp)
            tmp=tmp*10
        return res