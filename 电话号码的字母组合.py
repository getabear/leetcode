from typing import List
class Solution:
    ret=[]
    num = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l']
        , '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    def letterCombinations(self, digits: str) -> List[str]:
        self.ret=[]
        if(digits==""):
            return self.ret
        self.fun("",digits)
        return self.ret
    def fun(self,before,digits):
        if digits=="":
            self.ret.append(before)
            return before
        else:
            for i in self.num[digits[0]]:
                self.fun(before+i,digits[1:])
            return
a=Solution()
print(a.letterCombinations("23"))
print(a.letterCombinations("3"))
print(a.letterCombinations(""))
