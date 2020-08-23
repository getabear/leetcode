from typing import List

class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        ss=S[1:-1]
        def judge1(s):
            if s[0]=='0' and len(s)>1:
                return False
            return True
        def judge2(s):
            return not (s[-1]=='0')

        temp=[]
        for idx in range(1,len(ss)):
            temp.append((ss[:idx],ss[idx:]))
        ret=[]
        for l,r in temp:
            if judge1(l):
                temp1=[l]
            else:
                temp1=[]
            for i in range(1,len(l)):
                if judge1(l[:i]) and judge2(l[i:]):
                    temp1.append(l[:i]+'.'+l[i:])
            if judge1(r):
                temp2=[r]
            else:
                temp2=[]
            for j in range(1,len(r)):
                if judge1(r[:j]) and judge2(r[j:]):
                    temp2.append(r[:j]+'.'+r[j:])
            for x in temp1:
                for y in temp2:
                    ret.append('('+x+', '+y+')')
        return ret

a=Solution()
S="(123)"
print(a.ambiguousCoordinates(S))
