class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        rec=[]
        n=len(s)
        if n<=1:
            return 0
        cnt=1
        for i in range(1,n):
            if s[i]!=s[i-1]:
                rec.append(cnt)
                cnt=1
            else:
                cnt+=1
        rec.append(cnt)
        ret=0
        for r in range(1,len(rec)):
            ret+=min(rec[r-1],rec[r])
        return ret

s="00110011"
a=Solution()
print(a.countBinarySubstrings(s))
