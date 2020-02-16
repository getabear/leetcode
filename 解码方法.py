class Solution:
    def numDecodings(self, s: str) -> int:
        #算法正确,超时了,看看怎么优化
        #重复子问题过多,下面咱们进行优化
        self.ret=0
        def fun(s):
            if not s:
                self.ret+=1
                return
            if int(s[:1])>0:
                fun(s[1:])
                if len(s)>=2 and int(s[:2])<=26:
                    fun(s[2:])
        fun(s)
        return self.ret
class Solution1:
    #此次目的,解决重复子问题,提交leetcode通过,但此解决方法用了额外的O(n)的空间
    def numDecodings(self, s: str) -> int:
        self.ret=0
        mem=[-1 for i in s]    #创建一个数组,用以记录
        length=len(s)
        def fun(i,s):   #i为字符串的下标索引
            if i==length:
                self.ret+=1
                return
            if mem[i]!=-1:   #如果有记录,则直接更新
                self.ret+=mem[i]
                return
            if mem[i]==-1:
                tp=self.ret
                if int(s[i:i+1])>0:
                    fun(i+1,s)
                    if i+1<length and int(s[i:i+2])<=26:
                        fun(i+2,s)
                mem[i]=self.ret-tp   #更新mem,记录增量
        fun(0,s)
        return self.ret


s="226"
a=Solution1()
print(a.numDecodings(s))
