class Solution:
    def calculate(self, s: str) -> int:
        s=s+'+'   #简化代码，不然后面老退出循环还需要入栈
        stack = []
        sign, tmp = '+', 0     #这里一定要牢记，这个sign是数字前面的符号！！！！重要！！！！
        for i in s:
            if i.isdigit():
                tmp = tmp * 10 + int(i)
            elif i == ' ':
                continue
            else:
                if sign == '+':
                    stack.append(tmp)
                elif sign == '-':
                    stack.append(-tmp)
                elif sign == '*':
                    pre = stack.pop(-1)
                    stack.append(pre * tmp)
                else:
                    pre = stack.pop(-1)
                    if pre < 0:
                        stack.append(-pre // tmp * (-1))
                    else:
                        stack.append(pre // tmp)
                tmp = 0
                sign = i
        return sum(stack)


a = Solution()
s = " 14-3/2 "
print(a.calculate(s))
