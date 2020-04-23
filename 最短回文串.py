class Solution1:
    def shortestPalindrome(self, s: str) -> str:
        def judge(left,right):
            while(left<right):
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        for i in range(len(s)-1,-1,-1):
            if judge(0,i):
                res=s[i+1:][::-1]+s
                return res
        return s[1::-1]+s

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def get_pmt(s):
            length=len(s)
            i=1
            j=0
            tab=[0]*length
            while(i<length):
                if s[i]==s[j]:
                    j+=1
                    tab[i]=j
                    i+=1
                else:
                    if j>0:
                        j=tab[j-1]
                    else:
                        i+=1
                        j=0
            return tab

        tab=get_pmt(s+"$"+s[::-1])
        return s[tab[-1]:][::-1]+s


a=Solution()
print(a.shortestPalindrome("abcd"))
