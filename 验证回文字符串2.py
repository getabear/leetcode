class Solution1:
    def validPalindrome(self, s: str) -> bool:

        def judge(s):
            length=len(s)
            left,right=0,length-1
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        s1=s[::-1]
        length=len(s)
        for i in range(length):
            if s1[i]!=s[i]:
                if judge(s[0:i]+s[i+1:]) or judge(s1[:i]+s1[i+1:]):
                    return True
                else:
                    return False
        return True
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def judge(left,right):
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        length=len(s)
        right=length-1
        for i in range(length):
            if s[right-i]!=s[i]:
                if judge(i+1,length-i-1) or judge(i,length-i-2):
                    return True
                else:
                    return False
        return True