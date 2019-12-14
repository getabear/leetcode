from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #size代表数字最后一位的下标
        def fun(digits,size):
            if digits[size]<9:
                digits[size]+=1
                return digits
            elif digits[size]==9:
                digits[size]=0
                if size-1>=0:  #下标只能大于等于0,否则需要加一个数组值
                    return fun(digits,size-1)
                else:
                    return [1]+digits
        size=len(digits)
        return fun(digits,size-1)

a=Solution()
digits=[9,9,9]
print(a.plusOne(digits))
