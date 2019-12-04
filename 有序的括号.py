# 给定一个只包括
# '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
import time

class Solution:
    def isValid(self, s: str) -> bool:  #方法一:栈
        zhan=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
               zhan.append(i)
            else:
                if i==')':
                    try:
                        if(zhan.pop()=='('):
                            continue
                        else:
                            return False
                    except:
                        return False
                elif i=='}':
                    try:
                        if(zhan.pop()=='{'):
                            continue
                        else:
                            return False
                    except:
                        return False

                elif i==']':
                    try:
                        if(zhan.pop()=='['):
                            continue
                        else:
                            return False
                    except:
                        return False
        return len(zhan)==0

a=Solution()
s='()[]{}'
print(a.isValid(s))
print(time.process_time())


