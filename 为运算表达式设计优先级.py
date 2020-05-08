from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 未解决重复子问题
        length=len(input)
        if length==0:
            return []
        def fun(input:str):
            if input.isdigit():
                return [int(input)]
            res=[]
            for i,char in enumerate(input):
                if char in ['+','-','*']:
                    left=fun(input[:i])
                    right=fun(input[i+1:])
                    for l in left:
                        for r in right:
                            if char=='+':
                                res.append(l+r)
                            if char=='-':
                                res.append(l-r)
                            if char=='*':
                                res.append(l*r)
            return res
        return fun(input)

a=Solution()
input="2*3-4*5"
print(a.diffWaysToCompute(input))


