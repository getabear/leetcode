class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1==0:
            return 0
        s1cnt,index,s2cnt=0,0,0
        dic=dict()
        while True:
            s1cnt+=1
            for i in s1:
                if i==s2[index]:
                    index+=1
                    if index==len(s2):
                        s2cnt+=1
                        index=0
            if s1cnt==n1:
                return s2cnt//n2
            if index in dic:
                s1cnt_pre,s2cnt_pre=dic[index]
                loop=(s1cnt-s1cnt_pre,s2cnt-s2cnt_pre)
                break
            else:
                dic[index]=(s1cnt,s2cnt)
        ans=s2cnt_pre+(n1-s1cnt_pre)//loop[0]*loop[1]
        rest=(n1-s1cnt_pre)%loop[0]
        for i in range(rest):
            for s in s1:
                if s==s2[index]:
                    index+=1
                    if index==len(s2):
                        ans+=1
                        index=0
        return ans//n2




a=Solution()
s1="abdcdbce"
s2="adcbe"
print(a.getMaxRepetitions(s1,4,s2,2))
