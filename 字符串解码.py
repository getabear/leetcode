class Solution:
    def decodeString(self, s: str) -> str:
        ret_s=""
        shu=[chr(i) for i in range(48,58)]
        # print(shu)
        def atoi(s):
            num = 0
            i=0
            while (s[i] != "["):
                num = num * 10 + int(s[i])
                i+=1
            return i,num
        def fun(s,num):
            index=0
            ch=""   #返回数据
            # count=0
            length=len(s)
            next_num=1
            while(index<length):
                if s[index] in shu:
                    temp,next_num=atoi(s[index:])
                    index+=temp
                    continue
                elif s[index]=="[":
                    count,ret=fun(s[index+1:],next_num)
                    ch+=ret
                    index+=count+1
                elif s[index]=="]":
                    return index,ch*num
                else:
                    ch+=s[index]
                index+=1
            return index,ch*num
        count,ret_s=fun(s,1)
        return ret_s

    def decodeString2(self, s: str) -> str:
        res=""
        mul=0
        stack=[]
        for i in s:
            if i>='0' and i<='9':
                mul=mul*10+int(i)
            elif i=="[":
                stack.append([res,mul])
                res=""
                mul=0
            elif i=="]":
                last_res,last_mul=stack.pop()
                res=last_res+res*last_mul
            else:
                res+=i
        return res



a=Solution()
s="2[leetcode3[a]]"
print(a.decodeString2(s))
