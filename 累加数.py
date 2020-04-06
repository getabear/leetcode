class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        length=len(num)

        def fun(index,step,num1,num2):
            if index==length and step>2:
                return True
            if step>=2:
                for i in range(index+1,length+1):
                    # if(num[index])
                    tmp=int(num[index:i])
                    if(num[index]=='0' and tmp!=0):
                        break
                    if tmp==num1+num2:
                        if(fun(i,3,num2,tmp)):
                            return True
                return False
            else:
                for i in range(index+1,length+1):
                    tmp=int(num[index:i])
                    if(num[index]=='0' and tmp!=0):
                        break
                    if(fun(i,step+1,num2,tmp)):
                        return True
                return False


        return fun(0,0,0,0)

a=Solution()
num="112358"
print(a.isAdditiveNumber(num))



