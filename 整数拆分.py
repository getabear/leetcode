class Solution:
    dp=[0]*100
    dp2=[0]*100
    def find_max(self,num):    #暴力穷举   自顶向下    max被定义为整数时,max解释为整数而不是函数
        a=0
        temp=0
        if(num==0):    #如果为0 说明数字用完了,返回1
            return 1
        if(self.dp[num]!=0):
            return self.dp[num]
        for i in range(1,num+1):
            temp=max(temp,i*self.find_max(num-i))
            # if(temp>max):
            #     max=temp
        a=temp
        self.dp[num]=a
        return a

    def find_max3(self,num):   #动态规划   自底向上
        self.dp2[2]=1
        self.dp2[1]=1
        for i in range(3,num+1):
            for j in range(1,i):   #最大值可能为3种情况
                self.dp2[i]=max(self.dp2[i],j*self.dp2[i-j],j*(i-j))
        return self.dp2[num]

    def find_max2(self,num):   #贪心算法
        if(num<=3):
            return num-1
        else:
            times=num//3
            temp=num%3
            if(temp==0):
                return pow(3,times)
            elif(temp==1):
                return pow(3,times-1)*4
            elif(temp==2):
                return pow(3,times)*2


a=Solution()
print(a.find_max(10))
print(a.find_max3(10))