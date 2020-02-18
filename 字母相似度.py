class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        s1=list(A)
        s2=list(B)
        length=len(s1)
        self.k=20
        def fun(s1,s2,i,times):
            if i==length:
                self.k=min(self.k,times)
                return
            if s1[i]==s2[i]:
                fun(s1,s2,i+1,times)
            else:
                tp=i+1
                while tp<length:
                    a=s2[i]
                    b=s2[tp]
                    if b==s1[i]:
                        s2[i],s2[tp]=b,a
                        fun(s1,s2,i+1,times+1)
                        s2[i],s2[tp]=a,b
                        if a == s1[tp]:
                            break
                    tp+=1

        fun(s1,s2,0,0)
        return self.k
#该版本未使用优化,所以对与较长的字符花费时间较久
a=Solution()
s1="aabc"
s2="abca"
print(a.kSimilarity(s1,s2))