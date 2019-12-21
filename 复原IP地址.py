from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret=[]
        def fun(s,ip,n):
            if len(s)==0 and n==0:
                if ip[:-1] not in ret:
                    ret.append(ip[:-1])
                return
            if n==0:
                return
            if len(s)>=1:
                fun(s[1:],ip+s[0:1]+'.',n-1)
            if len(s)>=2 and s[0]!='0':
                fun(s[2:],ip+s[0:2]+'.',n-1)
            if len(s)>=3 and s[0]!='0' and int(s[:3]) <=255:
                fun(s[3:],ip+s[0:3]+'.',n-1)
        if len(s)>12:
            return []
        else:
            fun(s,"",4)
            return ret


a=Solution()
s="25525511135"
print(a.restoreIpAddresses(s))
