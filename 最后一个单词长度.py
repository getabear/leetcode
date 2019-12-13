
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size=len(s)
        if size==0:
            return 0
        index=size-1
        while(s[index]==' ' and index>=0):
            index-=1
        record=index
        while(index>=0):
            if s[index]==' ':
                return record-index
            index-=1
        return record+1

a=Solution()
s=" "
print(a.lengthOfLastWord(s))