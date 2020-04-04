class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret=[]
        while(n!=0):
            n-=1
            ret.append(letters[n%26])
            n//=27
        s=""
        for i in ret[::-1]:
           s+=i
        return s

a=Solution()
print(a.convertToTitle(28))
