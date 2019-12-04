from typing import List
class Solution(object):
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

a=Solution()
ret1=a.generateParenthesis(4)
ret2=a.generateParenthesis2(4)
print(ret1==ret2)
print(ret2)