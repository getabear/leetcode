from typing import List
class Solution1(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

    def generateParenthesis2(self,n):
        ret=[]
        def generate(s,n):
            if(n==0):
                if(valid(s)):
                    ret.append(s)
                return
            else:
                generate(s+"(",n-1)
                generate(s+")",n-1)
        def valid(s):
            num=0
            for i in s:
                if i=="(":
                    num+=1
                if i == ")":
                    num-=1
                if num<0:
                    return False
            return num==0
        generate("",2*n)
        return ret

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #本次咱们使用动态规划
        dp=[None for i in range(n+1)]
        dp[0]=[""]

        for i in range(1,n+1):
            tmp = []
            for j in range(i):
                left=dp[j]
                right=dp[i-j-1]
                for l in left:
                    for r in right:
                        tmp.append("("+l+")"+r)
                dp[i]=tmp

        return dp[n]



a=Solution()
ret=a.generateParenthesis(4)
print(ret)


