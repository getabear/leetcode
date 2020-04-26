class Solution1:
    def calculate(self, s: str) -> int:
        # 提交后通过了,但是代码冗余,看起来很难受
        def fun(s):
            index=0
            stack=[]
            sign=1
            tmp=0
            while index<len(s):
                if s[index]=='+':
                    stack.append(tmp*sign)
                    sign=1
                    index+=1
                    tmp=0
                    continue
                elif s[index]=='-':
                    stack.append(tmp * sign)
                    sign=-1
                    index+=1
                    tmp=0
                    continue
                elif s[index]==' ':
                    index+=1
                    continue
                elif s[index]=='(':
                    tmp,tmp2=fun(s[index+1:])
                    index+=tmp2+1
                    stack.append(tmp*sign)
                    index+=1
                    tmp=0
                    continue
                elif s[index]==')':
                    stack.append(tmp*sign)
                    return (sum(stack),index)
                ret=s[index]
                tmp = tmp * 10 + int(ret)
                index+=1
            stack.append(tmp*sign)
            return sum(stack)

        return fun(s)

class Solution:
    def calculate(self, s: str) -> int:
        def fun(s,index):
            stack=[]
            sign,tmp=1,0
            while index<len(s):
                if s[index]=='+':
                    stack.append(tmp*sign)
                    sign,tmp=1,0
                elif s[index]=='-':
                    stack.append(tmp*sign)
                    sign,tmp=-1,0
                elif s[index]=='(':
                    tmp,index=fun(s,index+1)
                elif s[index]==')':
                    stack.append(tmp*sign)
                    return (sum(stack),index)
                elif s[index].isdigit():
                    tmp=tmp*10+int(s[index])
                index+=1
            stack.append(tmp*sign)
            return (sum(stack),index)

        return fun(s,0)[0]




s="(1+(4+5+2)-3)+(6+8)"
a=Solution()
print(a.calculate(s))