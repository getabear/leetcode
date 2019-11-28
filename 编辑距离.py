class Solution:
    def miniDistance(self,word1,word2):
        len1=len(word1)
        len2=len(word2)
        if len1==0 or len2==0:
            if(len1>=len2):
                return len1-len2
            else :
                return len2-len1
        if(word1[0]==word2[0]):
            min=self.miniDistance(word1[1:],word2[1:])
        else:
            add=1+self.miniDistance(word1,word2[1:])
            replace=1+self.miniDistance(word1[1:],word2[1:])
            delete=1+self.miniDistance(word1[1:],word2)
            min=add
            if add>replace:
                min=replace
            if min>delete:
                min=delete
        return min

word1="intention"
word2="execution"


a=Solution()
print(a.miniDistance(word1,word2))