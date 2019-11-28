class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt=0
        num=0
        for i in s:
            if i=="L":
                num+=1
            else:
                num-=1
            if num==0:
                cnt+=1
        return cnt
a=Solution()
s="RLRRLLRLRL"
print(a.balancedStringSplit(s))