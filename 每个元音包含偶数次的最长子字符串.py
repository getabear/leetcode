class Solution1:
    def findTheLongestSubstring(self, s: str) -> int:
        # 超时了，需要优化
        yuan=['a','e','i','o','u']
        def fun(s,k):
            if len(s)<=k:
                return 0
            mem=dict()
            for index,i in enumerate(s):
                if i in yuan:
                    try:
                        mem[i].append(index)
                    except:
                        mem[i]=[]
                        mem[i].append(index)
            flag = 0
            self.ret = 0
            for i in mem.keys():
                #奇数个元音字母
                if len(mem[i])&0x1==1:
                    flag+=1
                    for j in mem[i]:
                        self.ret=max(self.ret,fun(s[0:j],self.ret),fun(s[j+1:],self.ret))
            if flag:
                return self.ret
            else:
                return len(s)
        return fun(s,0)

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bit_mask = eval('0b00000')
        state= {eval('0b00000'): -1}
        yuan = 'aeiou'
        res = 0
        for i in range(len(s)):
            for index,j in enumerate(yuan):
                if s[i]==j:
                    bit_mask^=eval('0b10000')>>index
            if bit_mask not in state:
                state[bit_mask] = i
            res = max(res, i - state[bit_mask])
        return res



a=Solution()
s="eleetminicoworoep"
print(a.findTheLongestSubstring(s))