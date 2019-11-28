# 多行注释 ctrl + /
#     f：function 函数
# 　　
# 　　p：parameter 参数
# 　　
# 　　m：method 方法
# 　　
# 　　c：class 类
# 　　
# 　　v：variable 变量
# class Solution:
def wordBreak(s,wordDict):
    length=len(s)
    if length==0:
        return True
    flag=False
    for i in range(length):
        if s[0:i+1] in wordDict:
            flag=wordBreak(s[i+1:length],wordDict)
        if(flag):
            return True
    return False

s="cat"
wordDict = ["cats", "dog", "sand", "and", "cat"]
if(wordBreak(s,wordDict)):
    print("yes")
else :
    print("no")



# test
# length=len(s)
# for i in range(length):
#     print(i)

# list={"nihao":0,"hello":2}
# str ="nihao"
# if list[str]:
#     print("yes")



# s="nihao123"
# list=["nihao","hello"]
# if s[:5] in list:
#     print("yes")
# else :
#     print("no")
