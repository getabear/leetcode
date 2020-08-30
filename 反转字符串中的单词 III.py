class Solution:
    def reverseWords(self, s: str) -> str:
        list=s.split()
        return ' '.join(item[::-1] for item in list)

a=Solution()
s="Let's take LeetCode contest"
print(a.reverseWords(s))