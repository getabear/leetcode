class Solution:
    def titleToNumber(self, s: str) -> int:
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tab={}
        for index,letter in enumerate(letters):
            tab[letter]=index+1

        ret=0
        length=len(s)
        for i in s:
            ret+=tab[i]*pow(26,length-1)
            length-=1
        return ret



a=Solution()
print(a.titleToNumber("ZY"))