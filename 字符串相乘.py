class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def fun(num1,num2):
            if num1=="0" or num2=="0":
                return "0"
            num2=num2[::-1]
            ret="0"
            for index,digit in enumerate(num2):
                tmp=mulstr(num1,int(digit))+"0"*index
                ret=plusstr(tmp,ret)
            return ret
        def mulstr(num,n):
            #num是字符串型
            #n 是整形
            #返回字符串 num*n
            s=num[::-1]  #把字符串翻转,方便
            ret=[]
            for i in s:
                temp=int(i)*n
                ret.append(temp)
            carry(ret)
            ret=ret[::-1]
            return "".join(str(x) for x in ret)


        def carry(nums):#处理进位
            # 举例：输入[15, 27, 12], 返回[5, 8, 4, 1]
            i=0
            jin=0
            size=len(nums)
            while(i<size):
                jin=nums[i]//10
                if i==size-1:  #防止访问越界
                    if jin:
                        nums.append(jin)
                else:
                    nums[i+1]+=jin
                nums[i]%=10
                i+=1

        def plusstr(s1,s2):
            size1=len(s1)
            size2=len(s2)
            if size1<size2:  #保证s1更长
                s1,s2=s2,s1
                size1,size2=size2,size1
            s1=[int(x) for x in s1]
            s2=[int(x) for x in s2]
            s1=s1[::-1]
            s2=s2[::-1]
            for index in range(len(s2)):
                s1[index]+=s2[index]
            carry(s1)
            s1=s1[::-1]
            return "".join(str(x) for x in s1)

        return fun(num1,num2)


a=Solution()
num1 = "123"
num2 = "456"
print(a.multiply(num1,num2))

