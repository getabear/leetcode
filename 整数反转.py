class Solution:
    def reverse(self, x: int) -> int:
        ret=0
        flag=0
        if x<0:
            x=0-x
            flag=1
        while(x!=0):
            ret=10*ret+x%10
            x//=10
        if flag:
            if ret>(1<<31):
                return 0
            return -ret
        else:
            #注意此处(1<<31)要加括号,因为减号优先级高于<<
            if ret > ((1 << 31)-1):
                return 0
            return ret


a=Solution()
print(a.reverse(321))
print(1<<31)