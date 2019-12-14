class Solution:
    def addBinary(self, a: str, b: str) -> str:

        #这道题咱们用的异或加法
        def judge(a):
            for i in a:
                if i=='1':   #含有1 ,返回真
                    return True
            return False

        def fun(a, b):
            res = ""  # 异或后的结果
            tmp = "0"  # 异或后的进位标志
            sizea = len(a) - 1
            sizeb = len(b) - 1
            while (sizea >= 0 and sizeb >= 0):
                if a[sizea] == b[sizeb]:
                    res += '0'
                    if a[sizea] == '1':
                        tmp += '1'
                    else:
                        tmp += '0'
                else:
                    res+='1'
                    tmp+='0'
                sizea -= 1
                sizeb -= 1
            while (sizea >= 0):
                res += a[sizea]
                tmp += '0'
                sizea -= 1
            while (sizeb >= 0):
                res += b[sizeb]
                tmp += '0'
                sizeb -= 1
            res=res[::-1]
            tmp=tmp[::-1]
            if(judge(tmp)):  #如果tmp中含有1,则递归调用
                return fun(res,tmp)
            return res

        res=fun(a,b)
        def fun2(res):  #用于删除字符串前的'0'
            if res[0]=='0':
                return fun2(res[1:])
            else:
                return res
        if len(res)==1:
            return res
        return fun2(res)

t=Solution()
a='0'
b='0'
print(t.addBinary(a,b))



