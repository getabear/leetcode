# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中
# 找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #这是暴力解法
        if needle == "":
            return 0
        len1=len(haystack)
        len2=len(needle)
        if len2>len1:
            return -1
        for i in range(len1-len2+1):
            if haystack[i:len2+i]==needle:
                return i
        return -1

class KMP:   #kmp解法,高端
    #大佬解题链接
    #https://leetcode-cn.com/problems/implement-strstr/solution/kmp-suan-fa-xiang-jie-by-labuladong/
    #不知道第一个想出这个方法的人是什么怪物
    def __init__(self,pat):   #只需要一个pat 即需要查找的字符串
        self.pat=pat
        length=len(self.pat)
        self.dp=[[0 for i in range(256)] for i in range(length)]   #初始化一个dp数组
        self.dp[0][ord(pat[0])]=1
        x=0            #影子状态
        for j in range(1,length):
            for i in range(256):
                if chr(i)==pat[j]:    #如果相等,则跟新状态为下一个位置
                    self.dp[j][i]=j+1
                else:
                    self.dp[j][i]=self.dp[x][i]
            x=self.dp[x][ord(pat[j])]     #更新影子状态
    def search(self,txt):
        lenpat=len(self.pat)
        lentxt=len(txt)
        j=0
        for index,i in enumerate(txt):
            j=self.dp[j][ord(i)]
            if j==lenpat:
                return index-lenpat+1
        return -1
a=Solution()
haystack= "ababc"
needle = "abc"
b=KMP(needle)
print(b.search(haystack))
print(a.strStr(haystack,needle))

