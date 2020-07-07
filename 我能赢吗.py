class Solution1:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        dp=dict()
        def fun(mem,val):
            key=tuple(mem)
            if key in dp:
                return dp[key]
            for i in range(1,maxChoosableInteger+1):
                if mem[i]==0:
                    mem[i]=1
                    if val+i>=desiredTotal or (not fun(mem[:],val+i)):
                        dp[key]=True
                        return True
                    mem[i]=0
            dp[key]=False
            return False
        tmp=sum([i for i in range(maxChoosableInteger+1)])
        if tmp<desiredTotal:
            return False
        if tmp==desiredTotal:
            if maxChoosableInteger&0x1==0:
                return False
            return True
        mem=[0 for i in range(maxChoosableInteger+1)]
        return fun(mem,0)

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        dp={}
        def fun(stat,val):
            if stat in dp:
                return dp[stat]
            for i in range(1,maxChoosableInteger+1):
                if (1<<i)&stat==0:
                    if val+i>=desiredTotal or not fun(stat|1<<i,val+i):
                        dp[stat]=True
                        return True
            dp[stat]=False
            return False
        tmp = sum([i for i in range(maxChoosableInteger + 1)])
        if tmp < desiredTotal:
            return False
        if tmp == desiredTotal:
            if maxChoosableInteger & 0x1 == 0:
                return False
            return True
        return fun(0,0)

a=Solution()
maxChoosableInteger=18
desiredTotal=79
print(a.canIWin(maxChoosableInteger,desiredTotal))