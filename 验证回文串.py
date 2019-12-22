class Solution:
    def isPalindrome(self, s: str) -> bool:
        #双指针法
        start=0
        s=s.lower()
        end=len(s)-1
        while(start<end):
            if 'a'<=s[start]<='z' or '0'<=s[start]<='9':
                if 'a'<=s[end]<='z' or '0'<=s[end]<='9':
                    if s[start]==s[end]:
                        start+=1
                        end-=1
                    else:
                        return False
                else:
                    end-=1
            else:
                start+=1
        return True


a=Solution()
s="0P"
print(a.isPalindrome(s))