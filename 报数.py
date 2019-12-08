class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            ret=self.countAndSay(n-1)
            count=0
            s=""
            index=0
            now=ret[0]
            while(index<len(ret)):
                if ret[index]==now:
                    count+=1
                    if index+1<len(ret) and ret[index+1]!=now:
                        s+=str(count)+now
                        now=ret[index+1]
                        count=0
                index+=1
            if count!=0:
                s+=str(count)+now
            return s

a=Solution()
n=6
for i in range(1,n):
    print(a.countAndSay(i))